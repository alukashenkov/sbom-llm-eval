## 1. SBOM Overview
*   **Product:** sbom-grbrsm_ui-v12.0.3rc0 (SPDX)
*   **Scan Date:** 2025-07-11
*   **Packages:** 338 total / 7 affected
*   **Unique CVEs:** 9
*   **CRA Tier Breakdown:** 0 ACTIVELY_EXPLOITED / 7 EXPLOITABLE / 2 VULNERABILITY

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
*   No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
*   **CVE-2025-7783** | `axios@1.10.0`, `form-data@4.0.3` | CVSS: 9.4 | CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/SC:H/VI:H/SI:H/VA:N/SA:N | **Fix:** Critical vulnerability in axios form-data allowing predictable boundary values for attacks.
*   **State:** ≤24h early warning → ≤72h incident notification → ≤1 month final report via ENISA Single Reporting Platform.

## 3. Art. 3(41) Exploitability Assessment
*   **Total Exploitability:** 7 CVEs classified as EXPLOITABLE; 2 PoC sources identified.
*   **CVE-2025-7783** | `form-data@4.0.3` | CVSS: 9.4 | EPSS: 0.17% | 222 days public | **Fix:** form-data uses unsafe Math.random() for boundary selection.
*   **CVE-2026-26996** | `minimatch@7.4.6` | CVSS: 8.7 | EPSS: 0.04% | 10 days public | **Fix:** minimatch ReDoS: many consecutive wildcards cause exponential backtracking.
*   **CVE-2026-25639** | `axios@1.10.0` | CVSS: 8.7 | EPSS: 0.03% | 19 days public | **Fix:** Prototype pollution in axios via mergeConfig allows __proto__ to crash or cause code execution.
*   **CVE-2025-13465** | `lodash@4.17.21` | CVSS: 8.2 | EPSS: 0.02% | 38 days public | **Fix:** Prototype pollution in lodash lets delete prototype methods via _.unset and _.omit.
*   **CVE-2025-54371** | `axios@1.10.0` | CVSS: 7.5 | EPSS: 0.17% | 220 days public | **Fix:** Critical vulnerability in axios form-data allowing predictable boundary values for attacks.

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2025-58754** | `axios@1.10.0` | CVSS: 7.5 | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H | EPSS: 0.10% | EXPLOITABLE | **Fix:** Axios on Node decodes data: URIs into memory, ignoring size limits, enabling DoS.
*   And 0 more across 0 packages.

## 5. Risk Distribution & Age Risk
*   **Severity:** 1 CRITICAL, 5 HIGH, 3 MEDIUM.
*   **Top Affected:** `axios@1.10.0` (4), `js-yaml@4.1.0` (1), `lodash@4.17.21` (1).
*   **Age Risk (Annex I Part II §2 violations):**
    1.  **CVE-2025-7783** (CRITICAL): 222 days public. **Fix:** Update `form-data`.
    2.  **CVE-2025-54371** (HIGH): 220 days public. **Fix:** Update `axios` dependencies.
    3.  **CVE-2025-58754** (HIGH): 170 days public. **Fix:** Patch `axios` Node adapter.

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2:** Submit Art. 14(3) notification for CVE-2025-7783; patch `form-data` and `axios` immediately.
2.  **Urgent — Annex I Part II §2:** Remediate EXPLOITABLE HIGH CVEs in `minimatch` (CVE-2026-26996) and `lodash` (CVE-2025-13465) using `fixHint` paths.
3.  **Planned — Annex I Part II §2:** Address remaining MEDIUM vulnerabilities in `js-yaml` and `prismjs` (CVE-2024-53382).
4.  **SBOM Update — Annex I Part II §1:** Regenerate SBOM to verify removal of `axios@1.10.0` and `lodash@4.17.21`.
5.  **Public Advisory — Annex I Part II §4:** Publish security advisory detailing the `form-data` boundary selection risk and remediation.
6.  **CVD Hygiene — Annex I Part II §5–6:** Ensure the security contact for `grbrsm_ui` is reachable for reporting future incidents.