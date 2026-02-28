#!/usr/bin/env python3
"""
SBOM Vulnerability Analysis — Single-file pipeline.

Preprocesses an SBOM audit JSON via preprocess.py, sends it to an LLM
via OpenRouter, and prints a CRA-aligned vulnerability summary to the console.

Usage:
    python3 analyze.py vulners_results/package-analysis-report-juice-shop.json
    python3 analyze.py report.json --model deepseek-v3 --prompt prompts/v7.txt
"""

import argparse
import json
import os
import sys
import time

import requests
from dotenv import load_dotenv

from preprocess import preprocess_file

load_dotenv()

# ---------------------------------------------------------------------------
# Model registry
# ---------------------------------------------------------------------------
MODELS = {
    "gemini-3-flash": "google/gemini-3-flash-preview",
    "gemini-2.5-flash": "google/gemini-2.5-flash",
    "gpt-4.1-mini": "openai/gpt-4.1-mini",
    "gpt-5-nano": "openai/gpt-5-nano",
    "deepseek-v3": "deepseek/deepseek-chat-v3-0324",
}

MODEL_PRICING = {
    "google/gemini-3-flash-preview": (0.50, 3.00),
    "google/gemini-2.5-flash": (0.30, 2.50),
    "openai/gpt-4.1-mini": (0.40, 1.60),
    "openai/gpt-5-nano": (0.05, 0.40),
    "deepseek/deepseek-chat-v3-0324": (0.28, 0.40),
}

DEFAULT_MODEL = "gemini-3-flash"
DEFAULT_PROMPT = os.path.join(os.path.dirname(__file__) or ".", "prompts", "v7.txt")


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
            "max_tokens": 16384,
            "temperature": 0.3,
        },
        timeout=300,
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

    # ------------------------------------------------------------------
    # Step 1: Preprocess (via preprocess.py)
    # ------------------------------------------------------------------
    print(f"{'=' * 60}")
    print(f"  File:   {args.file}")
    print(f"  Model:  {args.model} ({model_id})")
    print(f"  Prompt: {args.prompt}")
    print(f"{'=' * 60}")

    print("\n[1/3] Preprocessing...", end=" ", flush=True)
    t0 = time.time()
    preprocessed = preprocess_file(args.file)
    elapsed = time.time() - t0

    an = preprocessed["cveAnalytics"]
    user_content = json.dumps(preprocessed, indent=None, ensure_ascii=False)
    token_est = len(user_content) // 4

    print(f"done ({elapsed:.1f}s)")
    print(
        f"      Packages : {preprocessed['stats']['totalPackages']} total, "
        f"{preprocessed['stats']['affectedPackages']} affected"
    )
    print(f"      Advisories: {preprocessed['stats']['totalAdvisories']}")
    print(f"      Unique CVEs: {an['uniqueCVECount']}")

    # Severity distribution
    print("      Severity : ", end="")
    for sev in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
        count = an["severityDistribution"].get(sev, 0)
        if count:
            print(f"{sev}={count} ", end="")
    print()

    # CRA tier distribution
    tier_dist = an.get("craTierDistribution", {})
    if tier_dist:
        parts = []
        for tier in ("ACTIVELY_EXPLOITED", "EXPLOITABLE", "VULNERABILITY"):
            c = tier_dist.get(tier, 0)
            if c:
                parts.append(f"{tier}={c}")
        print(f"      CRA tiers: {', '.join(parts)}")

    # Art. 14 Track 1 — mandatory triggers
    triggers = an.get("craMandatoryTriggers")
    if triggers:
        print(
            f"      ⚠️  Art.14 Track1 TRIGGERS: {len(triggers)} — CSIRT/ENISA notification required"
        )
        for t in triggers:
            print(
                f"           {t['cve']}  CVSS={t['cvss']}  EPSS={t['epss']}  "
                f"wildExploited={t['wildExploited']}  KEV={t['cisa_kev']}"
            )
    else:
        print("      ✅ No Art. 14 Track 1 mandatory reporting triggers")

    # Art. 14 Track 2 — severe-incident candidates
    track2 = an.get("craTrack2Candidates")
    if track2:
        print(
            f"      ⚠️  Art.14 Track2 CANDIDATES: {len(track2)} possible severe-incident CVEs"
        )
        for t in track2[:3]:
            print(f"           {t['cve']}  CVSS={t['cvss']}  {t.get('cvssVector', '')}")
    else:
        print("      ✅ No Art. 14 Track 2 severe-incident candidates")

    # EPSS staleness
    stale = an.get("epssStaleCount", 0)
    if stale:
        print(
            f"      ℹ️  EPSS stale (>90d): {stale} CVEs — lower confidence in exploitability scores"
        )

    # Age risk
    age_risk = an.get("ageRisk")
    if age_risk:
        oldest = age_risk[0]
        print(
            f"      ⏱  Oldest unpatched: {oldest['cve']} ({oldest['severity']}) "
            f"— {oldest['daysPublic']} days public"
        )

    print(f"      Payload  : {len(user_content) // 1024} KB (~{token_est} tokens)")

    # ------------------------------------------------------------------
    # Step 2: Call LLM
    # ------------------------------------------------------------------
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
    print(f"      Cost:   ${cost:.4f}")

    # ------------------------------------------------------------------
    # Step 3: Output
    # ------------------------------------------------------------------
    print("\n[3/3] Summary")
    print("=" * 60 + "\n")
    print(result["content"])
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
