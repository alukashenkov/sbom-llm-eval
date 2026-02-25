#!/usr/bin/env python3
"""
SBOM Vulnerability Summary — Prompt & Model Evaluation Workbench

Evaluates multiple LLM models against SBOM audit JSONs to find the optimal
prompt + model combination for CRA-aligned vulnerability summaries.

Usage:
    python summarize_sbom.py --evaluate --prompt prompts/v1.txt --data vulners_results/
    python summarize_sbom.py --summarize --model gemini-2.5-flash --prompt prompts/v1.txt --data vulners_results/
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

from preprocess import preprocess_file

load_dotenv()

# ---------------------------------------------------------------------------
# Model registry — OpenRouter model IDs
# ---------------------------------------------------------------------------
CANDIDATE_MODELS = {
    "gemini-3-flash": "google/gemini-3-flash-preview",
    "gpt-4.1-mini": "openai/gpt-4.1-mini",
    "deepseek-v3": "deepseek/deepseek-chat-v3-0324",
}

CONFIG = {"judge_model": "anthropic/claude-sonnet-4"}

# Pricing per million tokens (input, output) — for cost estimation
MODEL_PRICING = {
    "google/gemini-3-flash-preview": (0.50, 3.00),
    "openai/gpt-4.1-mini": (0.40, 1.60),
    "deepseek/deepseek-chat-v3-0324": (0.28, 0.40),
    "anthropic/claude-sonnet-4": (3.00, 15.00),
}


def get_prompt_version(prompt_path: str) -> str:
    """Extract prompt version from filename (e.g., 'v1' from 'prompts/v1.txt')."""
    stem = Path(prompt_path).stem
    if re.match(r"v\d+", stem):
        return stem
    return stem


def estimate_cost(model_id: str, usage: dict) -> float:
    """Estimate cost in USD from token usage."""
    if not usage:
        return 0.0
    pricing = MODEL_PRICING.get(model_id, (1.0, 1.0))
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)
    return (in_tok * pricing[0] + out_tok * pricing[1]) / 1_000_000


# ---------------------------------------------------------------------------
# OpenRouter API Client
# ---------------------------------------------------------------------------
def call_openrouter(
    model_id: str,
    system_prompt: str,
    user_content: str,
    max_tokens: int = 16384,
    temperature: float = 0.3,
) -> dict:
    """Call OpenRouter chat completions API."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set. Add it to .env file.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/ssa-sbom-eval",
        "X-Title": "SBOM Summary Evaluator",
    }

    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=300,
    )

    if resp.status_code != 200:
        return {
            "error": f"HTTP {resp.status_code}: {resp.text[:500]}",
            "content": None,
            "usage": None,
            "model": model_id,
        }

    data = resp.json()
    choice = data.get("choices", [{}])[0]
    return {
        "content": choice.get("message", {}).get("content", ""),
        "usage": data.get("usage"),
        "model": data.get("model", model_id),
        "error": None,
    }


# ---------------------------------------------------------------------------
# Evaluate Mode
# ---------------------------------------------------------------------------
JUDGE_PROMPT = """You are an expert evaluator of cybersecurity vulnerability summaries.
You will receive a CROSS-REFERENCED VULNERABILITY COMPARISON from two scan sources
and {n_models} candidate summaries produced by different LLM models.

GROUND TRUTH — source_comparison contains:
- **overview**: total CVEs per source, overlap percentage
- **packages**: which packages were found by each source vs both
- **cves_in_both**: CVEs confirmed by BOTH Vulners (weight 70%) and Grype (weight 30%),
  with side-by-side severity, CVSS, EPSS, and risk_score from each source
- **cves_vulners_only**: CVEs found only by Vulners (primary source, weight 70%)
- **cves_grype_only**: CVEs found only by Grype (cross-check, weight 30%)

Each CVE entry includes a computed risk_score (0-10) based on CVSS, EPSS, exploit
evidence, and fix availability.

EVALUATION RULES:
- A CVE in cves_in_both is CONFIRMED — penalise any summary that misses it or gets
  its severity/scores wrong.
- A CVE in cves_vulners_only is LEGITIMATE (70% weight) — do NOT penalise summaries
  that reference these.
- A CVE in cves_grype_only is LEGITIMATE (30% weight) — do NOT penalise, but summaries
  are not expected to include all of these.
- ONLY penalise CVEs found in NEITHER source (true hallucinations).
- Use risk_score values to assess whether summaries prioritise the right CVEs.

Score each summary on these criteria (1-10 scale):

| Criterion | Weight | Description |
|-----------|--------|-------------|
| CRA Alignment | 30% | Correctly flags exploited CVEs, mentions Article 14 deadlines (24h/72h/14d), surfaces CISA KEV entries |
| Accuracy | 25% | CVE IDs, counts, severity, CVSS/EPSS match source_comparison. Penalise true hallucinations heavily. |
| Completeness | 20% | All high-risk CVEs (risk_score >= 7) covered, fix versions mentioned where available |
| Conciseness | 15% | Under 600 words, no filler, no hallucinated CVEs |
| Actionability | 10% | Priority actions reference correct fix versions, ordered by risk_score then CRA obligation |

Output a JSON object with this structure:
{{
    "scores": {{
        "<model_name>": {{
            "cra_alignment": <1-10>,
            "accuracy": <1-10>,
            "completeness": <1-10>,
            "conciseness": <1-10>,
            "actionability": <1-10>,
            "weighted_total": <float>,
            "notes": "<brief justification>"
        }}
    }},
    "ranking": ["<best_model>", "<second>", ...],
    "winner": "<best_model>",
    "analysis": "<2-3 sentence overall analysis>"
}}

IMPORTANT: Return ONLY valid JSON, no markdown fencing."""


def find_comparison_file(comparisons_dir: Path, sample_fname: str):
    """Map a vulners_results filename to its comparison JSON.

    e.g. 'package-analysis-report-juice-shop' -> 'comparisons/juice-shop/comparison.json'
    """
    key = sample_fname
    prefix = "package-analysis-report-"
    if key.startswith(prefix):
        key = key[len(prefix) :]

    comp_path = comparisons_dir / key / "comparison.json"
    return comp_path if comp_path.exists() else None


def run_evaluation(
    data_dir: str,
    prompt_path: str,
    results_dir: str,
    comparisons_dir: str = "comparisons",
):
    """Run all candidate models on all files, then judge."""
    prompt_text = Path(prompt_path).read_text()
    prompt_version = get_prompt_version(prompt_path)
    json_files = sorted(Path(data_dir).glob("*.json"))

    if not json_files:
        print(f"No JSON files found in {data_dir}")
        sys.exit(1)

    print(f"Found {len(json_files)} files, {len(CANDIDATE_MODELS)} models")
    print(f"Prompt: {prompt_path} (version: {prompt_version})")
    print(
        f"Total calls: {len(json_files) * len(CANDIDATE_MODELS)} + {len(json_files)} judge calls\n"
    )

    # Metrics tracking: list of dicts per call
    run_metrics = []

    # Namespace results under prompt version
    versioned_dir = Path(results_dir) / prompt_version
    versioned_dir.mkdir(parents=True, exist_ok=True)

    # Phase 1: Generate summaries
    all_results = {}  # {filename: {model_name: {content, usage, ...}}}

    for jf in json_files:
        fname = jf.stem
        print(f"\n{'=' * 60}")
        print(f"Processing: {jf.name}")
        print(f"{'=' * 60}")

        preprocessed = preprocess_file(str(jf))
        user_content = json.dumps(preprocessed, indent=None, ensure_ascii=False)
        token_est = len(user_content) // 4
        print(f"  Preprocessed: {len(user_content) // 1024} KB (~{token_est} tokens)")

        all_results[fname] = {}

        for model_name, model_id in CANDIDATE_MODELS.items():
            model_dir = versioned_dir / model_name
            model_dir.mkdir(parents=True, exist_ok=True)
            output_path = model_dir / f"{fname}.md"

            # Skip if already generated
            if output_path.exists() and output_path.stat().st_size > 0:
                print(f"  [{model_name}] Skipping (cached)")
                all_results[fname][model_name] = {
                    "content": output_path.read_text(),
                    "cached": True,
                }
                run_metrics.append(
                    {
                        "file": jf.name,
                        "model": model_name,
                        "model_id": model_id,
                        "status": "cached",
                        "time_s": 0,
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "cost_usd": 0,
                        "prompt_version": prompt_version,
                    }
                )
                continue

            print(f"  [{model_name}] Calling {model_id}...", end=" ", flush=True)
            t0 = time.time()
            result = call_openrouter(model_id, prompt_text, user_content)
            elapsed = time.time() - t0

            usage = result.get("usage") or {}
            in_tok = usage.get("prompt_tokens", 0)
            out_tok = usage.get("completion_tokens", 0)
            cost = estimate_cost(model_id, usage)

            if result["error"]:
                print(f"ERROR ({elapsed:.1f}s): {result['error'][:100]}")
                all_results[fname][model_name] = result
                output_path.write_text(f"# ERROR\n\n{result['error']}")
                run_metrics.append(
                    {
                        "file": jf.name,
                        "model": model_name,
                        "model_id": model_id,
                        "status": "error",
                        "time_s": round(elapsed, 1),
                        "input_tokens": in_tok,
                        "output_tokens": out_tok,
                        "cost_usd": round(cost, 6),
                        "prompt_version": prompt_version,
                        "error": result["error"][:200],
                    }
                )
                # Write summary incrementally
                generate_run_summary(
                    run_metrics, versioned_dir, prompt_version, prompt_path
                )
            else:
                print(f"OK ({elapsed:.1f}s, {in_tok}/{out_tok} tokens, ${cost:.4f})")
                output_path.write_text(result["content"])
                all_results[fname][model_name] = result
                run_metrics.append(
                    {
                        "file": jf.name,
                        "model": model_name,
                        "model_id": model_id,
                        "status": "ok",
                        "time_s": round(elapsed, 1),
                        "input_tokens": in_tok,
                        "output_tokens": out_tok,
                        "cost_usd": round(cost, 6),
                        "prompt_version": prompt_version,
                    }
                )
                # Write summary incrementally
                generate_run_summary(
                    run_metrics, versioned_dir, prompt_version, prompt_path
                )

            # Rate limiting — be polite to OpenRouter
            time.sleep(1)

    # Phase 2: Judge evaluation
    print(f"\n{'=' * 60}")
    print("JUDGE EVALUATION")
    print(f"{'=' * 60}")

    judge_dir = versioned_dir / "judge"
    judge_dir.mkdir(parents=True, exist_ok=True)

    all_scores = {}

    for jf in json_files:
        fname = jf.stem
        scores_path = judge_dir / f"{fname}_scores.json"

        # Skip if already judged
        if scores_path.exists():
            print(f"\n  [{fname}] Skipping judge (cached)")
            with open(scores_path) as f:
                all_scores[fname] = json.load(f)
            continue

        print(f"\n  Judging: {fname}")

        # Load precomputed source comparison
        comp_path = find_comparison_file(Path(comparisons_dir), fname)
        if comp_path:
            with open(comp_path) as f:
                source_comparison = json.load(f)
            overview = source_comparison.get("overview", {})
            print(
                f"    Comparison: {overview.get('total_unique', '?')} CVEs "
                f"(overlap {overview.get('overlap_pct', '?')}%, "
                f"vulners {overview.get('vulners_cves', '?')}, "
                f"grype {overview.get('grype_cves', '?')})"
            )
        else:
            print(f"    WARNING: No comparison file for {fname}, skipping")
            continue

        # Build judge input
        model_outputs = {}
        for model_name in CANDIDATE_MODELS:
            result = all_results.get(fname, {}).get(model_name, {})
            content = result.get("content", "")
            if content and not content.startswith("# ERROR"):
                model_outputs[model_name] = content

        if len(model_outputs) < 2:
            print(f"    Skipping — only {len(model_outputs)} valid outputs")
            continue

        judge_user = json.dumps(
            {
                "source_comparison": source_comparison,
                "candidate_summaries": model_outputs,
            },
            indent=None,
            ensure_ascii=False,
        )

        judge_system = JUDGE_PROMPT.format(n_models=len(model_outputs))

        print(f"    Calling judge ({CONFIG['judge_model']})...", end=" ", flush=True)
        t0 = time.time()
        result = call_openrouter(
            CONFIG["judge_model"], judge_system, judge_user, max_tokens=2048
        )
        elapsed = time.time() - t0

        if result["error"]:
            print(f"ERROR ({elapsed:.1f}s): {result['error'][:100]}")
        else:
            print(f"OK ({elapsed:.1f}s)")
            # Parse judge JSON
            try:
                # Handle potential markdown fencing
                content = result["content"].strip()
                if content.startswith("```"):
                    content = content.split("\n", 1)[1].rsplit("```", 1)[0]
                scores = json.loads(content)
                all_scores[fname] = scores
                with open(scores_path, "w") as f:
                    json.dump(scores, f, indent=2)
            except (json.JSONDecodeError, IndexError) as e:
                print(f"    Judge output parse error: {e}")
                # Save raw output for debugging
                (judge_dir / f"{fname}_raw.txt").write_text(result["content"])

        time.sleep(1)

    # Phase 3: Aggregate rankings + final run summary
    generate_rankings(all_scores, judge_dir)
    generate_run_summary(run_metrics, versioned_dir, prompt_version, prompt_path)


def generate_rankings(all_scores: dict, judge_dir: Path):
    """Aggregate judge scores across all files and produce a rankings report."""
    if not all_scores:
        print("\nNo judge scores available.")
        return

    # Aggregate weighted totals per model
    model_totals = {}
    model_counts = {}

    for fname, scores_data in all_scores.items():
        for model_name, model_scores in scores_data.get("scores", {}).items():
            wt = model_scores.get("weighted_total", 0)
            model_totals[model_name] = model_totals.get(model_name, 0) + wt
            model_counts[model_name] = model_counts.get(model_name, 0) + 1

    model_avgs = {m: model_totals[m] / model_counts[m] for m in model_totals}
    ranked = sorted(model_avgs.items(), key=lambda x: x[1], reverse=True)

    # Generate markdown report
    lines = ["# Model Evaluation Rankings\n"]
    lines.append(f"Files evaluated: {len(all_scores)}\n")

    lines.append("## Overall Rankings\n")
    lines.append("| Rank | Model | Avg Score | Files |")
    lines.append("|------|-------|-----------|-------|")
    for i, (model, avg) in enumerate(ranked, 1):
        medal = ["🥇", "🥈", "🥉"][i - 1] if i <= 3 else f"{i}."
        lines.append(f"| {medal} | {model} | {avg:.2f} | {model_counts[model]} |")

    lines.append("\n## Per-File Scores\n")
    for fname, scores_data in sorted(all_scores.items()):
        lines.append(f"### {fname}\n")
        analysis = scores_data.get("analysis", "")
        if analysis:
            lines.append(f"> {analysis}\n")

        lines.append("| Model | CRA | Accuracy | Complete | Concise | Action | Total |")
        lines.append("|-------|-----|----------|----------|---------|--------|-------|")
        for model_name, ms in sorted(
            scores_data.get("scores", {}).items(),
            key=lambda x: x[1].get("weighted_total", 0),
            reverse=True,
        ):
            lines.append(
                f"| {model_name} "
                f"| {ms.get('cra_alignment', '-')} "
                f"| {ms.get('accuracy', '-')} "
                f"| {ms.get('completeness', '-')} "
                f"| {ms.get('conciseness', '-')} "
                f"| {ms.get('actionability', '-')} "
                f"| **{ms.get('weighted_total', '-')}** |"
            )
            notes = ms.get("notes", "")
            if notes:
                lines.append(f"  > {notes}\n")

    lines.append(f"\n---\n**Winner: {ranked[0][0]}** (avg score: {ranked[0][1]:.2f})\n")

    report = "\n".join(lines)
    rankings_path = judge_dir / "rankings.md"
    rankings_path.write_text(report)
    print(f"\n{'=' * 60}")
    print(f"Rankings written to: {rankings_path}")
    print(f"{'=' * 60}")
    print(report)


def generate_run_summary(
    metrics: list, results_dir: Path, prompt_version: str, prompt_path: str
):
    """Generate a run_summary.md with token counts, time, and cost per call."""
    results_dir.mkdir(parents=True, exist_ok=True)
    summary_path = results_dir / "run_summary.md"

    active = [m for m in metrics if m["status"] == "ok"]
    errors = [m for m in metrics if m["status"] == "error"]
    cached = [m for m in metrics if m["status"] == "cached"]

    total_cost = sum(m["cost_usd"] for m in metrics)
    total_in = sum(m["input_tokens"] for m in metrics)
    total_out = sum(m["output_tokens"] for m in metrics)
    total_time = sum(m["time_s"] for m in metrics)

    lines = [
        f"# Run Summary — Prompt {prompt_version}\n",
        f"- **Timestamp**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        f"- **Prompt file**: `{prompt_path}`",
        f"- **Calls**: {len(active)} ok, {len(errors)} errors, {len(cached)} cached",
        f"- **Total tokens**: {total_in:,} in / {total_out:,} out",
        f"- **Total time**: {total_time:.1f}s",
        f"- **Total cost**: ${total_cost:.4f}\n",
    ]

    # Per-model summary
    lines.append("## Per-Model Summary\n")
    lines.append("| Model | Calls | Avg Time | Total In | Total Out | Total Cost |")
    lines.append("|-------|-------|----------|----------|-----------|------------|")

    model_names = sorted(set(m["model"] for m in metrics))
    for mn in model_names:
        mm = [m for m in metrics if m["model"] == mn and m["status"] == "ok"]
        if not mm:
            err_count = len(
                [m for m in metrics if m["model"] == mn and m["status"] == "error"]
            )
            if err_count:
                lines.append(f"| {mn} | {err_count} errors | — | — | — | — |")
            continue
        avg_t = sum(m["time_s"] for m in mm) / len(mm)
        t_in = sum(m["input_tokens"] for m in mm)
        t_out = sum(m["output_tokens"] for m in mm)
        t_cost = sum(m["cost_usd"] for m in mm)
        lines.append(
            f"| {mn} | {len(mm)} | {avg_t:.1f}s | {t_in:,} | {t_out:,} | ${t_cost:.4f} |"
        )

    # Per-call detail
    lines.append("\n## Per-Call Detail\n")
    lines.append("| File | Model | Status | Time | In Tokens | Out Tokens | Cost |")
    lines.append("|------|-------|--------|------|-----------|------------|------|")
    for m in metrics:
        if m["status"] == "cached":
            lines.append(
                f"| {m['file'][:40]} | {m['model']} | cached | — | — | — | — |"
            )
        else:
            lines.append(
                f"| {m['file'][:40]} | {m['model']} | {m['status']} "
                f"| {m['time_s']}s | {m['input_tokens']:,} | {m['output_tokens']:,} "
                f"| ${m['cost_usd']:.4f} |"
            )

    report = "\n".join(lines)
    summary_path.write_text(report + "\n")

    # Also save raw metrics as JSON for programmatic access
    json_path = results_dir / "run_metrics.json"
    with open(json_path, "w") as f:
        json.dump({"prompt_version": prompt_version, "metrics": metrics}, f, indent=2)

    print(f"\nRun summary: {summary_path}")
    print(f"Raw metrics: {json_path}")


# ---------------------------------------------------------------------------
# Summarize Mode
# ---------------------------------------------------------------------------
def run_summarize(data_dir: str, prompt_path: str, model_name: str, results_dir: str):
    """Run a single model on all files to produce final summaries."""
    model_id = CANDIDATE_MODELS.get(model_name)
    if not model_id:
        print(f"Unknown model: {model_name}")
        print(f"Available: {', '.join(CANDIDATE_MODELS.keys())}")
        sys.exit(1)

    prompt_text = Path(prompt_path).read_text()
    json_files = sorted(Path(data_dir).glob("*.json"))

    print(f"Summarizing {len(json_files)} files with {model_name} ({model_id})")

    output_dir = Path(results_dir) / f"final-{model_name}"
    output_dir.mkdir(parents=True, exist_ok=True)

    for jf in json_files:
        output_path = output_dir / f"{jf.stem}.md"
        print(f"\n  {jf.name}...", end=" ", flush=True)

        preprocessed = preprocess_file(str(jf))
        user_content = json.dumps(preprocessed, indent=None, ensure_ascii=False)

        t0 = time.time()
        result = call_openrouter(model_id, prompt_text, user_content)
        elapsed = time.time() - t0

        if result["error"]:
            print(f"ERROR ({elapsed:.1f}s)")
            output_path.write_text(f"# ERROR\n\n{result['error']}")
        else:
            usage = result.get("usage", {})
            print(
                f"OK ({elapsed:.1f}s, {usage.get('completion_tokens', '?')} output tokens)"
            )
            output_path.write_text(result["content"])

        time.sleep(1)

    print(f"\nSummaries written to: {output_dir}/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="SBOM Vulnerability Summary — Prompt & Model Evaluation Workbench"
    )
    parser.add_argument(
        "--evaluate",
        action="store_true",
        help="Run all candidate models on all files + judge evaluation",
    )
    parser.add_argument(
        "--summarize",
        action="store_true",
        help="Run a single model on all files for final summaries",
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Path to prompt template file",
    )
    parser.add_argument(
        "--data",
        required=True,
        help="Directory containing SBOM audit JSON files",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model name for --summarize mode (e.g. gemini-2.5-flash)",
    )
    parser.add_argument(
        "--results",
        default="results",
        help="Directory to store results (default: results/)",
    )
    parser.add_argument(
        "--comparisons",
        default="comparisons",
        help="Directory with source comparison results (default: comparisons/)",
    )
    parser.add_argument(
        "--judge",
        default=CONFIG["judge_model"],
        help=f"Judge model ID (default: {CONFIG['judge_model']})",
    )

    args = parser.parse_args()

    if not args.evaluate and not args.summarize:
        parser.error("Must specify --evaluate or --summarize")

    if args.summarize and not args.model:
        parser.error("--summarize requires --model")

    CONFIG["judge_model"] = args.judge

    if args.evaluate:
        run_evaluation(args.data, args.prompt, args.results, args.comparisons)
    elif args.summarize:
        run_summarize(args.data, args.prompt, args.model, args.results)


if __name__ == "__main__":
    main()
