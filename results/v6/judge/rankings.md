# Model Evaluation Rankings

Files evaluated: 6

## Overall Rankings

| Rank | Model | Avg Score | Files |
|------|-------|-----------|-------|
| 🥇 | deepseek-v3 | 8.47 | 6 |
| 🥈 | gemini-3-flash | 8.16 | 6 |
| 🥉 | gemini-2.5-flash | 7.88 | 6 |

## Per-File Scores

### package-analysis-report-juice-shop

> Gemini-3-flash provides the best balance of comprehensive CRA compliance coverage with specific Article references, accurate technical details, and actionable recommendations with version targets. While deepseek-v3 excels in conciseness, gemini-3-flash's superior actionability and CRA alignment outweigh the length consideration.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| gemini-3-flash | 9 | 9 | 9 | 9 | 9 | **8.85** |
  > Excellent CRA alignment with specific Article references. Accurate data presentation and comprehensive exploit assessment. Well-structured actionable recommendations with specific version targets.

| deepseek-v3 | 8 | 9 | 8 | 10 | 8 | **8.45** |
  > Good CRA compliance coverage with clean formatting. Accurate statistics and proper exploit identification. Excellent conciseness at 450 words while maintaining essential information.

| gemini-2.5-flash | 8 | 9 | 9 | 6 | 8 | **8.15** |
  > Strong CRA compliance focus with correct Article 14 assessment. Accurate CVE counts and severity distribution. Comprehensive coverage but exceeds word limit significantly.

### package-analysis-report-la-vulners-mcp

> DeepSeek-v3 delivers the most effective summary with superior conciseness while maintaining complete coverage of critical findings. It correctly identifies PoC evidence and provides clear, CRA-aligned action priorities with specific Article references. The other models are solid but more verbose with less precise exploit assessment.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 9 | 9 | 9 | 9 | 9 | **9.0** |
  > Excellent conciseness while maintaining completeness. Correctly identifies PoC evidence for specific CVEs. Clear CRA-aligned action priorities with specific Article references.

| gemini-2.5-flash | 8 | 9 | 8 | 7 | 8 | **8.05** |
  > Strong CRA alignment with correct Article 14 assessment. Accurate CVE counts and EPSS values. Well-structured but slightly verbose.

| gemini-3-flash | 8 | 8 | 9 | 6 | 9 | **8.05** |
  > Good CRA compliance focus with specific version recommendations. Mentions PoC evidence discrepancy. Slightly verbose with redundant phrasing.

### package-analysis-report-openclaw-v2026.1.10

> Gemini-3-flash achieves the best balance of CRA compliance, accuracy, and actionability while maintaining reasonable length. Gemini-2.5-flash provides comprehensive detail but is too verbose, while deepseek-v3 excels in conciseness but has some accuracy issues and less detailed CRA guidance.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| gemini-3-flash | 8 | 9 | 8 | 8 | 9 | **8.4** |
  > Excellent CRA compliance focus with proper Article references. Accurate data representation and good balance of detail vs brevity. Strong actionable recommendations with clear prioritization.

| gemini-2.5-flash | 8 | 9 | 9 | 6 | 8 | **8.05** |
  > Strong CRA alignment with correct Article 14 assessment and detailed compliance actions. Accurate CVE counts and severity distribution. Comprehensive coverage but exceeds word limit significantly.

| deepseek-v3 | 7 | 8 | 7 | 10 | 7 | **7.65** |
  > Good CRA awareness but less detailed Article references. Accurate core data but some CVE attribution issues (CVE-2026-25253 listed under openclaw vs clawdbot). Excellent conciseness at 450 words.

### package-analysis-report-sbom-grbrsm_ui-v12.0.3rc0

> DeepSeek-v3 provides the most accurate and actionable summary with proper CRA Article citations, correct CVE details, and clear exploit evidence presentation. While all models correctly identify no mandatory reporting triggers, DeepSeek-v3 excels in accuracy and conciseness without sacrificing completeness.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 9 | 8 | 9 | 9 | 9 | **8.7** |
  > Excellent overall performance with accurate CVE details, proper CRA Article references, clear exploit evidence, and specific actionable recommendations. Most concise while maintaining completeness.

| gemini-2.5-flash | 8 | 6 | 8 | 7 | 8 | **7.35** |
  > Good CRA compliance structure but contains inaccuracies in CVE counts and EPSS values. Some hallucinated details like 'and 0 more across 0 packages'.

| gemini-3-flash | 8 | 5 | 7 | 8 | 8 | **7.15** |
  > Strong CRA alignment and actionable recommendations, but significant accuracy issues including duplicate CVE-2025-7783 entries and incorrect package associations.

### package-analysis-report-sbom-gurobi-engine-v12.0.3rc0

> DeepSeek-v3 wins with superior conciseness and actionability while maintaining strong CRA alignment and accuracy. All models correctly identified no Article 14 triggers and provided good exploit assessments, but DeepSeek-v3 delivered the most focused and actionable summary. Gemini-3-Flash was close second with good structure, while Gemini-2.5-Flash was too verbose despite good technical content.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 8 | 8 | 8 | 9 | 9 | **8.3** |
  > Excellent conciseness while maintaining completeness. Strong CRA alignment and very actionable recommendations with clear priority ordering. Good accuracy on technical details.

| gemini-3-flash | 8 | 8 | 9 | 8 | 8 | **8.1** |
  > Strong CRA compliance focus with proper Article 14 assessment. Good accuracy on CVE details and EPSS scores. Well-structured with clear exploit assessment and actionable recommendations.

| gemini-2.5-flash | 8 | 7 | 8 | 6 | 7 | **7.35** |
  > Good CRA alignment with Article 14 check and compliance actions. Some accuracy issues with CVE counts and EPSS values. Comprehensive but verbose at ~600 words.

### package-analysis-report-vulners-mcp

> All models correctly identified the critical CRA Article 14 requirement for CVE-2025-48384. DeepSeek-v3 wins with superior conciseness and accuracy while maintaining comprehensive coverage. Gemini-3-flash provides strong actionability but is slightly less precise, while Gemini-2.5-flash is comprehensive but more verbose.

| Model | CRA | Accuracy | Complete | Concise | Action | Total |
|-------|-----|----------|----------|---------|--------|-------|
| deepseek-v3 | 9 | 9 | 8 | 9 | 9 | **8.7** |
  > Excellent accuracy and conciseness. Perfect CRA compliance identification. Clear, actionable recommendations with proper prioritization. Most efficient presentation.

| gemini-3-flash | 9 | 8 | 8 | 8 | 9 | **8.4** |
  > Strong CRA alignment and actionable recommendations. Good balance of completeness and conciseness. Clear priority ordering and specific actions.

| gemini-2.5-flash | 9 | 8 | 9 | 7 | 8 | **8.35** |
  > Excellent CRA compliance with correct Article 14 identification and timeline. Comprehensive coverage but slightly verbose. Minor accuracy issues with some CVE details.


---
**Winner: deepseek-v3** (avg score: 8.47)
