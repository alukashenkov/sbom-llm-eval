## Vulnerability Summary for sbom-grbrsm_ui-v12.0.3rc0

### 1. SBOM Overview
This report summarizes vulnerabilities identified in `sbom-grbrsm_ui-v12.0.3rc0`, an SPDX-formatted SBOM generated on 2025-07-11. Out of 338 total packages, 7 are affected by vulnerabilities. A total of 8 unique CVEs were identified, comprising 1 Critical, 5 High, and 2 Medium severity findings.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of exploit availability:
*   **CVE-2025-7783** (form-data@4.0.3) — CVSS 9.4 (CRITICAL) — EPSS 0.00177 — Unsafe random function for boundary selection.
*   **CVE-2025-54371** (axios@1.10.0) — CVSS 7.5 (HIGH) — EPSS N/A — Transitive vulnerability via form-data.
*   **CVE-2026-25639** (axios@1.10.0) — CVSS 8.7 (HIGH) — EPSS 0.00033 — Prototype Pollution.
*   **CVE-2025-13465** (lodash@4.17.21) — CVSS 7.9 (HIGH) — EPSS 0.00025 — Prototype Pollution in `_.unset` and `_.omit`.
*   **CVE-2026-26996** (minimatch@7.4.6) — CVSS 8.7 (HIGH) — EPSS 0.0004 — Regular Expression Denial of Service (ReDoS).

### 4. Critical & High Findings
*   **CVE-2025-7783** (form-data@4.0.3) — CVSS 9.4 — EPSS 0.00177
*   **CVE-2025-54371** (axios@1.10.0) — CVSS 7.5 — EPSS N/A
*   **CVE-2025-58754** (axios@1.10.0) — CVSS 7.5 — EPSS 0.00102
*   **CVE-2026-25639** (axios@1.10.0) — CVSS 8.7 — EPSS 0.00033
*   **CVE-2025-13465** (lodash@4.17.21) — CVSS 7.9 — EPSS 0.00025
*   **CVE-2026-26996** (minimatch@7.4.6) — CVSS 8.7 — EPSS 0.0004

### 5. Risk Distribution
*   **Critical:** 1 CVE
*   **High:** 5 CVEs
*   **Medium:** 2 CVEs
The most affected packages are: axios (4 advisories), js-yaml (2 advisories), and lodash (2 advisories).

### 6. CRA Compliance Actions
1.  **Immediate Action:** Upgrade `form-data` to a patched version to mitigate **CVE-2025-7783** (CRITICAL, exploit available) which uses an unsafe random function for boundary selection.
2.  **Urgent Action:** Upgrade `axios` to address **CVE-2026-25639** (HIGH, exploit available) and **CVE-2025-58754** (HIGH) to prevent Prototype Pollution and DoS.
3.  **Urgent Action:** Upgrade `lodash` to mitigate **CVE-2025-13465** (HIGH, exploit available) to prevent Prototype Pollution.
4.  **Urgent Action:** Upgrade `minimatch` to address **CVE-2026-26996** (HIGH, exploit available) to prevent Regular Expression Denial of Service (ReDoS).
5.  **Planned Action:** Review and upgrade `js-yaml` and `@babel/runtime` to address identified Medium severity vulnerabilities.