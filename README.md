# Vulners SBOM Audit Summary — LLM Prompt & Model Evaluation

LLM-powered summarization of [Vulners SBOM Audit](https://vulners.com/sbom-audit) results into CRA-aligned vulnerability reports. Audit results can be obtained via [UI](https://vulners.com/sbom-audit) or [API](https://docs.vulners.com/docs/api/audit/#sbom-audit).

## Winner: DeepSeek V3 + v6 prompt

| | |
| --- | --- |
| **Model** | `deepseek/deepseek-chat-v3-0324` via OpenRouter |
| **Prompt** | `prompts/v6.txt` |
| **Score** | 8.01 / 10 (judged by Claude Sonnet 4) |
| **Speed** | ~44s per file |
| **Cost** | ~$0.012 per file |

Best balance of quality and cost for CRA-aligned vulnerability summaries from Vulners SBOM audit JSON. Consistently wins on conciseness and accuracy, with strong CRA article citations.

Fastest option: **Gemini 3 Flash** (7.66 avg, ~8s/file).
Most consistent: **GPT-4.1-mini** (7.81 avg, ~14s/file).

## Ground Truth: Dual-Source Comparison

Evaluation uses cross-referenced findings from **Vulners** (70% weight) and **Grype** (30% weight). The `compare_sources.py` script normalizes vulnerability IDs (including non-CVE advisories like GHSA), computes per-CVE risk scores, and generates structured comparison data for the judge.

Judge receives a `source_comparison` with CVEs categorized as:

- **In both sources** — confirmed findings, penalises summaries that miss them
- **Vulners-only** — legitimate (primary source), no penalty for including
- **Grype-only** — legitimate (cross-check), not mandatory to include
- **In neither** — true hallucinations, penalised heavily

## Evaluation Summary (9 models tested, 6 prompt iterations, 6 test files)

| Model | Score (v6) | Speed | Status |
|-------|-----------|-------|--------|
| **DeepSeek V3** | **8.01** | 44s | ✅ **Winner** — best quality-to-cost ratio, wins 4/6 files |
| GPT-4.1-mini | 7.81 | 14s | Most consistent — narrowest score range, wins openclaw |
| Gemini 3 Flash | 7.66 | 8s | Fastest — best for bulk processing, wins la-vulners-mcp |
| Gemini 2.5 Flash | 7.88 (prev) | 7s | Persistent verbosity — exceeds word limits |
| GPT-5 Nano | 7.67 (prev) | 120s | All tokens consumed by internal reasoning; needs 16K max_tokens |
| GLM 4.7 | 7.53 (v1) | 64s | Slow, expensive, only scored 4/6 files in v2 |
| Kimi K2.5 | — | 200s | Replaced after v0 — 200s/call unusable |
| Qwen Turbo | 6.07 (v1) | 37s | Collapsed on largest file (score 2.45) |
| Claude 3 Haiku | 5.91 (v1) | 15s | Falsely triggered CRA Article 14 reporting |

### Per-File Breakdown (v6)

| File | DeepSeek V3 | GPT-4.1-mini | Gemini 3 Flash |
|------|-------------|-------------|----------------|
| openclaw (96 vulns) | 8.20 | **8.60** | 7.60 |
| vulners-mcp (374 vulns) | **8.50** | 8.40 | 7.60 |
| gurobi-engine (62 vulns) | **8.40** | 7.90 | 7.60 |
| juice-shop (87 vulns) | **8.20** | 7.50 | 7.65 |
| la-vulners-mcp (15 vulns) | 6.85 | 7.65 | **8.35** |
| grbrsm_ui (9 vulns) | **7.90** | 6.25 | 7.15 |

## Key Optimizations

1. **Pre-computed CVE analytics** (v5) — Python deduplicates CVEs before sending to LLM. Eliminated counting errors that plagued all models.
2. **Non-CVE advisory support** — GHSA and other non-CVE advisories are included via advisory ID fallback when `cvelist` is empty. Increased openclaw from 57 to 96 matched vulnerabilities.
3. **Dual-source comparison judge** — Cross-referenced Vulners + Grype findings with per-CVE risk scores give the judge structured, verifiable ground truth.
4. **Inline CRA article citations** (v6) — Baking "Article 10/11/14" into prompt section headers drove CRA alignment scores from ~7 to ~8.5.
5. **Anti-hallucination rule** (v6) — "ONLY reference CVEs in the input data" reduced fabricated entries. Judge penalises only CVEs found in neither source.

## Project Structure

```
SSA/
├── vulners_results/           # Vulners SBOM audit JSON files
├── grype_results/         # Grype vulnerability scan outputs
├── comparisons/           # Cross-source comparison reports per SBOM
│   └── {sbom-name}/
│       ├── comparison.md  # Human-readable report
│       └── comparison.json # Structured data for judge
├── prompts/               # Prompt versions (v1–v6)
│   └── v6.txt             # Best prompt
├── results/               # Versioned evaluation results
│   └── v6/                # Latest: rankings, judge scores, metrics
├── compare_sources.py     # Grype vs Vulners comparison script
├── preprocess.py          # Data preprocessing module
├── summarize_sbom.py      # Evaluation workbench (multi-model, judge)
├── analyze.py             # Single-file analysis script
├── requirements.txt       # Python dependencies
└── .env                   # OPENROUTER_API_KEY (not committed)
```

## Setup

```bash
pip3 install -r requirements.txt
echo 'OPENROUTER_API_KEY=sk-or-v1-your-key' > .env
```

## Scripts

### `analyze.py` — Single-file analysis

Runs the full pipeline on one Vulners SBOM audit JSON file: preprocess → call LLM → print summary to console.

```bash
# Default: Gemini 3 Flash + v6 prompt
python3 analyze.py vulners_results/package-analysis-report-juice-shop.json

# Custom model and prompt
python3 analyze.py vulners_results/package-analysis-report-juice-shop.json --model deepseek-v3 --prompt prompts/v4.txt
```

### `compare_sources.py` — Grype vs Vulners comparison

Cross-references Grype and Vulners findings per SBOM. Normalizes vulnerability IDs (CVE + GHSA), computes risk scores, and generates comparison reports.

```bash
# Default directories
python3 compare_sources.py

# Custom paths
python3 compare_sources.py --vulners vulners_results/ --grype grype_results/ --output comparisons/
```

### `summarize_sbom.py` — Evaluation workbench

Runs all candidate models on all files, then uses a judge model (Claude Sonnet 4) to score and rank outputs using cross-source comparison data.

```bash
# Full evaluation (requires comparison data — run compare_sources.py first)
python3 summarize_sbom.py --evaluate --prompt prompts/v6.txt --data vulners_results/ --comparisons comparisons/

# Single model, all files (no judging)
python3 summarize_sbom.py --summarize --model gemini-3-flash --prompt prompts/v6.txt --data vulners_results/
```
