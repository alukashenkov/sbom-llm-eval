# Vulners SBOM Audit Summary — LLM Prompt & Model Evaluation

LLM-powered summarization of [Vulners SBOM Audit](https://vulners.com/sbom-audit) results into CRA-aligned vulnerability reports under **Regulation (EU) 2024/2847** (Cyber Resilience Act). Audit results can be obtained via [UI](https://vulners.com/sbom-audit) or [API](https://docs.vulners.com/docs/api/audit/#sbom-audit).

## Winner: Gemini 3 Flash + v7 prompt *(speed-weighted)*

| | |
| --- | --- |
| **Model** | `google/gemini-3-flash-preview` via OpenRouter |
| **Prompt** | `prompts/v7.txt` |
| **Quality score** | 7.77 / 10 (judged by Claude Sonnet 4) |
| **Speed** | **~11s per file** (2× faster than GPT-4.1-mini, 4× faster than DeepSeek) |
| **Cost** | ~$0.032 per file |
| **Composite (50% quality + 50% speed)** | **7.69** |

For highest output quality (CRA alignment, accuracy, completeness) without hard latency constraints, use **GPT-4.1-mini** (composite 6.79, quality 8.52, ~23s/file).

## v7 Evaluation Summary — Speed-Weighted Composite (50/50)

| Rank | Model | Quality | Avg time | Speed score | **Composite** |
|---|---|---|---|---|---|
| 🥇 | **gemini-3-flash** | 7.77 | **11.4s** | 7.61 | **7.69** |
| 🥈 | gpt-4.1-mini | **8.52** | 23.4s | 5.07 | 6.79 |
| 🥉 | deepseek-v3 | 8.08 | 47.5s | 0.00 | 4.04 |

> DeepSeek disqualifies itself under ≥50% speed weight — tail latency of 84.7s on large files (openclaw) makes it unsuitable for production with SLA requirements, despite being the cheapest ($0.085 total) and most concise.

### Per-Criterion Quality Scores (v7)

| Criterion | Weight | gemini-3-flash | gpt-4.1-mini | deepseek-v3 |
|---|---|---|---|---|
| CRA Alignment | 30% | 8.33 | **9.00** | 8.17 |
| Accuracy | 25% | 7.17 | **8.50** | 8.00 |
| Completeness | 20% | 8.17 | **9.00** | 7.33 |
| Conciseness | 15% | 6.50 | 7.00 | **9.17** |
| Actionability | 10% | 8.33 | **8.83** | 7.80 |

### Per-File Response Times (v7)

| File | gemini-3-flash | gpt-4.1-mini | deepseek-v3 |
|---|---|---|---|
| juice-shop | 13.6s | 26.9s | 31.1s |
| la-vulners-mcp | 9.2s | 19.1s | 34.9s |
| openclaw | 14.0s | 23.6s | ⚠️ 84.7s |
| grbrsm_ui | 7.6s | 23.2s | 20.2s |
| gurobi-engine | 12.6s | 29.9s | 38.0s |
| vulners-mcp | 11.2s | 17.8s | ⚠️ 76.2s |

## Ground Truth: Dual-Source Comparison

Evaluation uses cross-referenced findings from **Vulners** (70% weight) and **Grype** (30% weight). The `compare_sources.py` script normalises vulnerability IDs (including non-CVE advisories like GHSA), computes per-CVE risk scores, and generates structured comparison data for the judge.

Judge receives a `source_comparison` with CVEs categorised as:

- **In both sources** — confirmed findings, penalises summaries that miss them
- **Vulners-only** — legitimate (primary source), no penalty for including
- **Grype-only** — legitimate (cross-check), not mandatory to include
- **In neither** — true hallucinations, penalised heavily

## CRA Alignment

Summaries are produced under the three-tier vulnerability taxonomy of Regulation (EU) 2024/2847:

| Tier | CRA Article | Definition | Action |
|---|---|---|---|
| `ACTIVELY_EXPLOITED` | Art. 3(42) | Reliable evidence of in-the-wild malicious exploitation | Art. 14 Track 1: 24h → 72h → 14-day report to ENISA/CSIRT |
| `EXPLOITABLE` | Art. 3(41) | Potential to be effectively used under practical operational conditions | Pre-market gate (Annex I §2); remediate without delay (Annex I Part II §2) |
| `VULNERABILITY` | Art. 3(40) | Weakness that can be exploited | Track, document, manage throughout lifecycle |

## Key Optimisations

1. **CRA-accurate article references** (v7) — corrected from Article 10/11 to **Art. 3, 13, 14, Annex I** per final Regulation (EU) 2024/2847 text.
2. **Three-tier taxonomy pre-classification** (v7) — `preprocess.py` computes `craTier` per CVE before sending to the LLM, eliminating exploitability inference errors.
3. **Art. 14 dual-track reporting** (v7) — Track 1 (actively exploited: 24h/72h/14d) and Track 2 (severe incident: 24h/72h/1mo) are surfaced as separate pre-computed `craMandatoryTriggers` / `craTrack2Candidates` fields.
4. **Rich CVSS fields** (v7) — `cvssVector`, `cvssVersion`, `cvssSource` extracted; model can reason about network reachability and attack complexity for Art. 3(41) exploitability assessment.
5. **EPSS percentile + staleness** (v7) — `epssPercentile` and `epssDate` extracted; stale scores (>90 days) flagged so the model can express appropriate uncertainty.
6. **Fix hints from Vulners AI** (v7) — `enchantments.short_description` ("upgrade to X.Y.Z") and `aiDescription` extracted as `fixHint` and `description`; drives concrete remediation actions in Annex I Part II §2.
7. **Age risk signal** (v7) — `daysPublic` computed per CVE; top unpatched CRITICAL/HIGH CVEs surfaced as `ageRisk` — long-unpatched issues are flagged as potential "without delay" violations (Annex I Part II §2).
8. **EPSS merge bug fixed** (v7) — EPSS score now correctly keeps the *highest* value when a CVE appears across multiple advisories (previously took first seen).
9. **Pre-computed CVE analytics** (v5) — Python deduplicates CVEs before sending to LLM. Eliminated counting errors across all models.
10. **Dual-source judge** (v5) — Cross-referenced Vulners + Grype findings with per-CVE risk scores give the judge structured, verifiable ground truth.

## Project Structure

```
SSA/
├── vulners_results/       # Vulners SBOM audit JSON files
├── grype_results/         # Grype vulnerability scan outputs
├── comparisons/           # Cross-source comparison reports per SBOM
│   └── {sbom-name}/
│       ├── comparison.md  # Human-readable report
│       └── comparison.json # Structured data for judge
├── prompts/               # Prompt versions (v1–v7)
│   └── v7.txt             # Current best prompt (CRA-aligned)
├── results/               # Versioned evaluation results
│   └── v7/                # Latest: rankings, judge scores, run metrics
├── compare_sources.py     # Grype vs Vulners comparison script
├── preprocess.py          # Data preprocessing — CRA-tier classification,
│                          #   CVSS/EPSS/fixHint/ageRisk extraction
├── summarize_sbom.py      # Evaluation workbench (multi-model + judge)
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

Preprocesses one Vulners SBOM audit JSON, calls the LLM, and prints a CRA-aligned summary to the console.

```bash
# Default: Gemini 3 Flash + v7 prompt
python3 analyze.py vulners_results/package-analysis-report-juice-shop.json

# Custom model and prompt
python3 analyze.py vulners_results/package-analysis-report-juice-shop.json \
  --model gpt-4.1-mini --prompt prompts/v7.txt
```

Available models: `gemini-3-flash`, `gemini-2.5-flash`, `gpt-4.1-mini`, `gpt-5-nano`, `deepseek-v3`

### `compare_sources.py` — Grype vs Vulners comparison

Cross-references Grype and Vulners findings per SBOM. Normalises vulnerability IDs (CVE + GHSA), computes risk scores, and generates comparison reports used by the judge.

```bash
python3 compare_sources.py
# Custom paths:
python3 compare_sources.py --vulners vulners_results/ --grype grype_results/ --output comparisons/
```

### `summarize_sbom.py` — Evaluation workbench

Runs all candidate models on all files, then scores and ranks outputs using Claude Sonnet 4 as judge with cross-source ground truth.

```bash
# Full evaluation (run compare_sources.py first)
python3 summarize_sbom.py --evaluate --prompt prompts/v7.txt --data vulners_results/

# Single model, all files (no judging)
python3 summarize_sbom.py --summarize --model gemini-3-flash --prompt prompts/v7.txt --data vulners_results/
```
