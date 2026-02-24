#!/usr/bin/env python3
"""
SBOM Vulnerability Analysis — Single-file pipeline.

Preprocesses an SBOM audit JSON, sends it to an LLM via OpenRouter,
and prints a CRA-aligned vulnerability summary to the console.

Usage:
    python3 analyze.py sample_data/package-analysis-report-juice-shop.json
    python3 analyze.py report.json --model deepseek-v3 --prompt prompts/v4.txt
"""

import argparse
import json
import os
import sys
import time

import requests
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Model registry
# ---------------------------------------------------------------------------
MODELS = {
    "gemini-3-flash": "google/gemini-3-flash-preview",
    "gemini-2.5-flash": "google/gemini-2.5-flash",
    "deepseek-v3": "deepseek/deepseek-chat-v3-0324",
}

MODEL_PRICING = {
    "google/gemini-3-flash-preview": (0.50, 3.00),
    "google/gemini-2.5-flash": (0.30, 2.50),
    "deepseek/deepseek-chat-v3-0324": (0.28, 0.40),
}

DEFAULT_MODEL = "gemini-3-flash"
DEFAULT_PROMPT = os.path.join(os.path.dirname(__file__) or ".", "prompts", "v6.txt")

# ---------------------------------------------------------------------------
# Reference types indicating PoC / exploit availability
# ---------------------------------------------------------------------------
POC_REFERENCE_TYPES = {
    "githubexploit",
    "packetstorm",
    "exploitdb",
    "hackerone",
    "nuclei",
    "zdt",
    "kitploit",
    "cisa_kev",
    "gitee",
}


# ---------------------------------------------------------------------------
# Preprocessing (self-contained — no external imports needed)
# ---------------------------------------------------------------------------
def preprocess_advisory(adv: dict) -> dict:
    """Strip an advisory to CRA-relevant fields + PoC extraction."""
    poc_sources = {}
    enchantments = adv.get("enchantments", {})
    deps = enchantments.get("dependencies", {})
    for ref in deps.get("references", []):
        rtype = ref.get("type", "")
        if rtype in POC_REFERENCE_TYPES:
            poc_sources[rtype] = len(ref.get("idList", []))

    desc = adv.get("description", "")
    return {
        "id": adv.get("id"),
        "title": adv.get("title"),
        "cvelist": adv.get("cvelist", []),
        "description": desc[:200] + ("..." if len(desc) > 200 else ""),
        "metrics": adv.get("metrics"),
        "epss": adv.get("epss"),
        "aiScore": adv.get("aiScore"),
        "exploitation": adv.get("exploitation"),
        "exploits": [
            {"type": e.get("type"), "href": e.get("href")}
            for e in adv.get("exploits", [])
        ]
        or None,
        "pocSources": poc_sources or None,
    }


def compute_cve_analytics(processed_data: list) -> dict:
    """Pre-compute CVE-level analytics for LLM accuracy."""
    cve_map = {}
    cra_triggers = []
    poc_by_type = {}
    pkg_cve_counts = {}

    for pkg in processed_data:
        pkg_name = f"{pkg['package']}@{pkg['version']}"
        pkg_cves = set()

        for adv in pkg["advisories"]:
            cve_ids = adv.get("cvelist", [])
            poc = adv.get("pocSources") or {}
            exploitation = adv.get("exploitation") or {}
            metrics = adv.get("metrics") or {}
            epss_data = adv.get("epss") or []
            epss_score = epss_data[0].get("epss") if epss_data else None

            cvss_score = None
            severity = None
            cvss = metrics.get("cvss")
            if cvss:
                cvss_score = cvss.get("score")
                severity = (cvss.get("severity") or "").upper()

            is_wild = exploitation.get("wildExploited", False)
            has_kev = "cisa_kev" in poc

            for cve_id in cve_ids:
                pkg_cves.add(cve_id)
                if cve_id not in cve_map:
                    cve_map[cve_id] = {
                        "severity": severity,
                        "cvss": cvss_score,
                        "epss": epss_score,
                        "packages": set(),
                        "wildExploited": False,
                        "cisa_kev": False,
                    }
                entry = cve_map[cve_id]
                entry["packages"].add(pkg_name)
                if is_wild:
                    entry["wildExploited"] = True
                if has_kev:
                    entry["cisa_kev"] = True
                sev_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
                if sev_order.get(severity, 0) > sev_order.get(entry["severity"], 0):
                    entry["severity"] = severity
                    entry["cvss"] = cvss_score

            for src_type in poc:
                if src_type not in poc_by_type:
                    poc_by_type[src_type] = set()
                for cve_id in cve_ids:
                    poc_by_type[src_type].add(cve_id)

        pkg_cve_counts[pkg_name] = len(pkg_cves)

    severity_dist = {}
    for info in cve_map.values():
        sev = info["severity"] or "UNKNOWN"
        severity_dist[sev] = severity_dist.get(sev, 0) + 1

    for cve_id, info in cve_map.items():
        if info["wildExploited"] or info["cisa_kev"]:
            cra_triggers.append(
                {
                    "cve": cve_id,
                    "cvss": info["cvss"],
                    "epss": info["epss"],
                    "packages": sorted(info["packages"]),
                    "wildExploited": info["wildExploited"],
                    "cisa_kev": info["cisa_kev"],
                }
            )

    top_packages = sorted(pkg_cve_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        "uniqueCVECount": len(cve_map),
        "severityDistribution": severity_dist,
        "craMandatoryTriggers": cra_triggers or None,
        "pocSummary": {k: len(v) for k, v in poc_by_type.items()},
        "topAffectedPackages": [
            {"package": p, "uniqueCVEs": c} for p, c in top_packages[:5]
        ],
    }


def preprocess_file(filepath: str) -> dict:
    """Load a JSON report and strip to CRA-relevant data with analytics."""
    with open(filepath) as f:
        raw = json.load(f)

    meta = raw.get("meta", {})
    packages = raw.get("data", [])
    processed_data = []
    total_packages = len(packages)

    for pkg in packages:
        advisories = pkg.get("applicableAdvisories", [])
        if not advisories:
            continue
        processed_data.append(
            {
                "package": pkg.get("package"),
                "version": pkg.get("version"),
                "advisories": [preprocess_advisory(a) for a in advisories],
            }
        )

    analytics = compute_cve_analytics(processed_data)

    return {
        "meta": meta,
        "stats": {
            "totalPackages": total_packages,
            "affectedPackages": len(processed_data),
            "totalAdvisories": sum(len(p["advisories"]) for p in processed_data),
        },
        "cveAnalytics": analytics,
        "data": processed_data,
    }


# ---------------------------------------------------------------------------
# OpenRouter API
# ---------------------------------------------------------------------------
def call_openrouter(model_id: str, system_prompt: str, user_content: str) -> dict:
    """Call OpenRouter and return response."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: OPENROUTER_API_KEY not set. Add it to .env file.")
        sys.exit(1)

    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ssa-sbom-eval",
            "X-Title": "SBOM Summary Analyzer",
        },
        json={
            "model": model_id,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            "max_tokens": 4096,
            "temperature": 0.3,
        },
        timeout=120,
    )

    if resp.status_code != 200:
        return {
            "error": f"HTTP {resp.status_code}: {resp.text[:500]}",
            "content": None,
            "usage": None,
        }

    data = resp.json()
    choice = data.get("choices", [{}])[0]
    return {
        "content": choice.get("message", {}).get("content", ""),
        "usage": data.get("usage"),
        "error": None,
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Analyze a single SBOM audit JSON and print a CRA-aligned vulnerability summary."
    )
    parser.add_argument("file", help="Path to SBOM audit JSON file")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        choices=list(MODELS.keys()),
        help=f"Model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help=f"Path to prompt file (default: {DEFAULT_PROMPT})",
    )
    args = parser.parse_args()

    model_id = MODELS[args.model]
    prompt_text = open(args.prompt).read()

    # Step 1: Preprocess
    print(f"{'=' * 60}")
    print(f"  File:   {args.file}")
    print(f"  Model:  {args.model} ({model_id})")
    print(f"  Prompt: {args.prompt}")
    print(f"{'=' * 60}")

    print("\n[1/3] Preprocessing...", end=" ", flush=True)
    t0 = time.time()
    preprocessed = preprocess_file(args.file)
    elapsed = time.time() - t0

    analytics = preprocessed["cveAnalytics"]
    user_content = json.dumps(preprocessed, indent=None, ensure_ascii=False)
    token_est = len(user_content) // 4

    print(f"done ({elapsed:.1f}s)")
    print(
        f"      Packages: {preprocessed['stats']['totalPackages']} total, "
        f"{preprocessed['stats']['affectedPackages']} affected"
    )
    print(f"      Advisories: {preprocessed['stats']['totalAdvisories']}")
    print(f"      Unique CVEs: {analytics['uniqueCVECount']}")
    print(f"      Severity: ", end="")
    for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
        count = analytics["severityDistribution"].get(sev, 0)
        if count:
            print(f"{sev}={count} ", end="")
    print()
    triggers = analytics.get("craMandatoryTriggers")
    if triggers:
        print(f"      ⚠️  CRA TRIGGERS: {len(triggers)} mandatory reporting entries")
    else:
        print(f"      ✅ No CRA mandatory reporting triggers")
    print(f"      Payload: {len(user_content) // 1024} KB (~{token_est} tokens)")

    # Step 2: Call LLM
    print(f"\n[2/3] Calling {args.model}...", end=" ", flush=True)
    t0 = time.time()
    result = call_openrouter(model_id, prompt_text, user_content)
    elapsed = time.time() - t0

    if result["error"]:
        print(f"ERROR ({elapsed:.1f}s)")
        print(f"      {result['error']}")
        sys.exit(1)

    usage = result.get("usage") or {}
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)
    pricing = MODEL_PRICING.get(model_id, (1.0, 1.0))
    cost = (in_tok * pricing[0] + out_tok * pricing[1]) / 1_000_000

    print(f"done ({elapsed:.1f}s)")
    print(f"      Tokens: {in_tok:,} in / {out_tok:,} out")
    print(f"      Cost: ${cost:.4f}")

    # Step 3: Output
    print(f"\n[3/3] Summary")
    print(f"{'=' * 60}\n")
    print(result["content"])
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
