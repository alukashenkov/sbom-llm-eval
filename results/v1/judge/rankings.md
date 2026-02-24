# Model Evaluation Rankings

Files evaluated: 6

## Overall Rankings

| Rank | Model | Avg Score | Files |
|------|-------|-----------|-------|
| 🥇 | deepseek-v3 | 8.18 | 6 |
| 🥈 | glm-4.7 | 7.53 | 5 |
| 🥉 | gemini-2.5-flash | 6.99 | 6 |
| 4. | qwen-turbo | 6.07 | 6 |
| 5. | claude-3-haiku | 5.91 | 6 |

## Per-File Scores

### package-analysis-report-juice-shop

> Deepseek-v3 provides the most accurate and CRA-compliant summary with correct vulnerability counts, proper exploit source identification, and actionable recommendations within word limits. Claude-3-haiku significantly underperforms due to major accuracy issues, incorrectly classifying critical vulnerabilities as medium severity.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 9 | 9 | 8 | 9 | 9 | **8.8** |
  > Excellent CRA compliance awareness, accurate counts, well-structured and actionable within word limits

| qwen-turbo | 8 | 7 | 7 | 8 | 7 | **7.4** |
  > Good CRA structure and conciseness, but has some severity count discrepancies and missing some critical details

| gemini-2.5-flash | 8 | 6 | 9 | 4 | 8 | **7.1** |
  > Strong CRA compliance focus and comprehensive coverage, but contains severity count inaccuracies and exceeds word limit significantly

| glm-4.7 | 7 | 5 | 3 | 8 | 6 | **5.8** |
  > Good CRA structure and conciseness but appears truncated, missing critical vulnerabilities and has accuracy issues

| claude-3-haiku | 6 | 4 | 5 | 7 | 6 | **5.4** |
  > Major accuracy issues with severity classifications, missing critical vulnerabilities, though well-structured

### package-analysis-report-la-vulners-mcp

> GLM-4.7 wins with superior accuracy (correctly identifying 6 unique CVEs vs inflated counts by others) and excellent CRA compliance structure with clear immediate/urgent/planned action prioritization. DeepSeek-v3 follows closely with strong completeness and specific PoC documentation, while other models suffered from significant accuracy issues in vulnerability counting.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| glm-4.7 | 9 | 8 | 8 | 9 | 9 | **8.5** |
  > Excellent CRA compliance focus, accurate CVE counts (6 unique), concise format. Strong actionability with immediate/urgent/planned prioritization.

| deepseek-v3 | 9 | 7 | 9 | 8 | 9 | **8.4** |
  > Strong CRA alignment and structure. Good completeness with specific PoC links. Minor accuracy issues with severity distribution but excellent actionability.

| gemini-2.5-flash | 8 | 6 | 9 | 7 | 8 | **7.45** |
  > Good CRA structure and completeness, but inaccurate severity counts (claims 4 CRITICAL vs actual 13 total advisories). Strong actionability with specific patching guidance.

| claude-3-haiku | 8 | 7 | 8 | 6 | 7 | **7.3** |
  > Solid CRA structure and good completeness. Some accuracy issues with package counts and version formatting. Less concise than others but actionable.

| qwen-turbo | 8 | 5 | 7 | 9 | 7 | **7.0** |
  > Good CRA compliance structure but major accuracy issues (claims 10 CRITICAL vs source data). Very concise but lacks detail on exploit sources.

### package-analysis-report-openclaw-v2026.1.10

> GLM-4.7 provides the best balance of CRA compliance awareness, accuracy, and actionability while maintaining conciseness. Claude-3-Haiku fails significantly by incorrectly triggering CRA reporting requirements, while Gemini-2.5-Flash is too verbose despite good technical detail.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| glm-4.7 | 8 | 7 | 8 | 9 | 8 | **7.95** |
  > Excellent CRA compliance focus with proper Article 14 analysis. Concise format under 600 words. Good accuracy on vulnerability counts and severity distribution. Clear actionable priorities.

| deepseek-v3 | 7 | 6 | 7 | 8 | 8 | **7.05** |
  > Good CRA structure and compliance focus. Some inaccuracies in vulnerability counts (lists 4 critical vs source showing different numbers). Well-organized and actionable recommendations.

| gemini-2.5-flash | 3 | 8 | 9 | 4 | 7 | **6.25** |
  > Correctly identifies no CRA triggers but provides comprehensive vulnerability details. Very verbose (exceeds 600 words) and includes many GHSA entries not in source data. Good accuracy on CVE counts and EPSS values.

| qwen-turbo | 6 | 5 | 6 | 8 | 7 | **6.25** |
  > Mentions CRA Article 14 but lacks depth. Significant inaccuracies in severity counts (5 critical, 44 high vs actual data). Good structure but missing key vulnerability details.

| claude-3-haiku | 2 | 4 | 5 | 9 | 6 | **4.65** |
  > Major CRA misalignment - incorrectly claims CVEs require ENISA/CSIRT notification without wildExploited=true. Significant undercount of vulnerabilities (only 25 total vs 125). Concise but inaccurate.

### package-analysis-report-sbom-grbrsm_ui-v12.0.3rc0

> Deepseek-v3 wins with the strongest CRA compliance focus, accurate vulnerability data, and excellent conciseness while maintaining comprehensive coverage. Claude-3-haiku performs poorly due to fundamental misunderstanding of CRA triggers, incorrectly flagging normal CVEs for mandatory reporting.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 6 | 8 | 8 | 9 | 8 | **7.7** |
  > Strong CRA compliance focus, accurate vulnerability data, comprehensive critical findings coverage, very concise presentation, and well-structured actionable steps.

| glm-4.7 | 5 | 7 | 8 | 8 | 8 | **7.0** |
  > Good CRA alignment, mostly accurate counts (1 Critical, 5 High matches), comprehensive coverage of key CVEs, concise format, and actionable recommendations with proper prioritization.

| qwen-turbo | 5 | 7 | 7 | 9 | 7 | **6.8** |
  > Good CRA awareness, mostly accurate data with some EPSS formatting inconsistencies, covers key vulnerabilities, very concise, and provides clear action items.

| gemini-2.5-flash | 4 | 6 | 7 | 6 | 7 | **5.85** |
  > Correctly identifies no CRA triggers but has inaccurate vulnerability counts (claims 1 CRITICAL, 8 HIGH vs actual 1 CRITICAL, 5 HIGH). Good completeness but verbose at ~600 words.

| claude-3-haiku | 3 | 5 | 6 | 5 | 6 | **4.85** |
  > Misunderstands CRA triggers (incorrectly flags CVEs for ENISA notification), has accuracy issues with severity counts, and provides less precise actionability despite good structure.

### package-analysis-report-sbom-gurobi-engine-v12.0.3rc0

> Deepseek-v3 excels with perfect CRA alignment including proper Article 14 deadline references, highly accurate vulnerability counts, and exceptional actionability with specific remediation steps. GLM-4.7 provides strong technical accuracy and good CRA compliance but lacks the detailed regulatory framework references that make Deepseek-v3 superior for EU CRA compliance scenarios.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 10 | 9 | 9 | 9 | 10 | **9.4** |
  > Outstanding CRA alignment with proper Article 14 references, highly accurate data, and excellent actionable guidance within word limit

| glm-4.7 | 9 | 8 | 8 | 8 | 9 | **8.4** |
  > Excellent CRA compliance focus with accurate severity counts and actionable recommendations, well-structured and concise

| gemini-2.5-flash | 8 | 7 | 9 | 6 | 8 | **7.65** |
  > Strong CRA awareness and comprehensive exploit analysis, but exceeds word limit and has some accuracy issues with CVE counts

| claude-3-haiku | 7 | 5 | 6 | 9 | 7 | **6.55** |
  > Good conciseness and CRA awareness but major accuracy issues with severely undercounted vulnerabilities (18 total vs 154 advisories)

| qwen-turbo | 6 | 6 | 7 | 7 | 7 | **6.5** |
  > Basic CRA awareness but significant accuracy issues with inflated HIGH count (35 vs actual ~23) and some duplicate CVE listings

### package-analysis-report-vulners-mcp

> DeepSeek-v3 wins with the best balance of CRA compliance, accuracy, and conciseness, properly identifying CISA KEV status and maintaining readability. Gemini-2.5-flash shows strong CRA understanding but suffers from significant accuracy issues with inflated vulnerability counts. Qwen-turbo fails completely due to massive repetitive content and missing critical CRA triggers.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 8 | 7 | 7 | 9 | 8 | **7.7** |
  > Good CRA compliance focus with CISA KEV mention. More accurate severity counts but some completeness gaps. Excellent conciseness at 598 words.

| gemini-2.5-flash | 9 | 6 | 8 | 7 | 9 | **7.65** |
  > Excellent CRA alignment with proper Article 14 deadlines and wild exploitation flag. However, significant accuracy issues with inflated CVE counts and severity mismatches.

| claude-3-haiku | 6 | 8 | 5 | 8 | 7 | **6.7** |
  > Good accuracy and conciseness but missed critical CRA requirement of wild exploitation flag. Limited completeness with only 20 CVEs covered.

| qwen-turbo | 2 | 3 | 4 | 1 | 3 | **2.45** |
  > Major failures: missed wild exploitation flag, massive repetitive content making it unusable, severe accuracy issues with wrong severity counts.


---
**Winner: deepseek-v3** (avg score: 8.18)
