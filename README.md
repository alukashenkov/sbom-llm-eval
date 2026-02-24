# SBOM Summary — LLM Prompt & Model Evaluation

## Winner: Gemini 3 Flash + v6 prompt

| | |
|---|---|
| **Model** | `google/gemini-3-flash-preview` via OpenRouter |
| **Prompt** | `prompts/v6.txt` |
| **Score** | 8.16 / 10 (judged by Claude Sonnet 4) |
| **Speed** | ~9s per file |
| **Cost** | ~$0.024 per file |

Best balance of quality, speed, and cost for CRA-aligned SBOM vulnerability summaries. Produces accurate, concise reports with proper EU CRA Article citations and correct mandatory reporting triggers.

For maximum quality at the expense of speed, use **DeepSeek V3** (8.47 avg, ~40s/file).

## Evaluation Summary (6 rounds, 6 test files)

| Model | Best Score | Speed | Why not winner |
|-------|-----------|-------|----------------|
| **Gemini 3 Flash** | **8.16** (v6) | **9s** | ✅ **Winner** |
| DeepSeek V3 | 8.47 (v6) | 40s | Too slow for real-time use (~5x slower) |
| Gemini 2.5 Flash | 7.88 (v6) | 7s | Persistent verbosity — exceeds word limits |
| GLM 4.7 | 7.53 (v1) | 64s | Slow, expensive, only scored 4/6 files in v2 |
| Kimi K2.5 | — | 200s | Replaced after v0 — 200s/call unusable |
| Qwen Turbo | 6.07 (v1) | 37s | Collapsed on largest file (score 2.45) |
| Claude 3 Haiku | 5.91 (v1) | 15s | Falsely triggered CRA Article 14 reporting |

## Key Optimizations

1. **Pre-computed CVE analytics** (v5) — Python deduplicates CVEs before sending to LLM. Eliminated counting errors that plagued all models.
2. **Inline CRA article citations** (v6) — Baking "Article 10/11/14" into prompt section headers drove CRA alignment scores from ~7 to ~8.5.
3. **Bullet points over prose** (v6) — Reduced verbosity by ~30% for Gemini models.
4. **Anti-hallucination rule** (v6) — "ONLY reference CVEs in the input data" reduced fabricated entries.

## Project Structure

```
SSA/
├── sample_data/           # SBOM audit JSON files
├── prompts/               # Prompt versions (v1–v6)
│   └── v6.txt             # Best prompt
├── results/               # Versioned evaluation results
│   └── v6/                # Latest: rankings, judge scores, metrics
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

Runs the full pipeline on one SBOM JSON file: preprocess → call LLM → print summary to console.

```bash
# Default: Gemini 3 Flash + v6 prompt
python3 analyze.py sample_data/package-analysis-report-juice-shop.json

# Custom model and prompt
python3 analyze.py sample_data/package-analysis-report-juice-shop.json --model deepseek-v3 --prompt prompts/v4.txt
```

### `summarize_sbom.py` — Evaluation workbench

Runs all candidate models on all files, then uses a judge model (Claude Sonnet 4) to score and rank outputs.

```bash
# Full evaluation
python3 summarize_sbom.py --evaluate --prompt prompts/v6.txt --data sample_data/

# Single model, all files (no judging)
python3 summarize_sbom.py --summarize --model gemini-3-flash --prompt prompts/v6.txt --data sample_data/
```
