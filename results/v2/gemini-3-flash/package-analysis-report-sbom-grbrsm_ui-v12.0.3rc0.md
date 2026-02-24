## 1. SBOM Overview
The product **sbom-grbrsm_ui-v12.0.3rc0** (SPDX format) was scanned on 2025-07-11. Out of 338 total packages, 7 are affected by vulnerabilities. The scan identified **8 unique CVEs**: 1 Critical, 5 High, and 2 Medium.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities are currently flagged as exploited in the wild or listed in the CISA KEV.

## 3. Exploit Availability Assessment
One unique CVE has documented proof-of-concept (PoC) evidence:
*   **[CVE-2025-7783]** form-data@4.0.3 — CVSS 9.4 — EPSS 0.00177 — Weak boundary generation via Math.random().
0 additional CVEs have exploit evidence.

## 4. Critical & High Findings
The following high-impact vulnerabilities require immediate attention:
*   **[CVE-2025-7783]** form-data@4.0.3 — CVSS 9.4 (Critical) — EPSS 0.00177
*   **[CVE-2026-26996]** minimatch@7.4.6 — CVSS 8.7 (High) — EPSS 0.00040
*   **[CVE-2026-25639]** axios@1.10.0 — CVSS 8.7 (High) — EPSS 0.00033
*   **[CVE-2025-13465]** lodash@4.17.21 — CVSS 8.2 (High) — EPSS 0.00025
*   **[CVE-2025-58754]** axios@1.10.0 — CVSS 7.5 (High) — EPSS 0.00102
*   **[CVE-2025-54371]** axios@1.10.0 — CVSS 7.5 (High) — EPSS 0.00177
and 0 more HIGH findings across 0 packages.

## 5. Risk Distribution
*   **Critical:** 1
*   **High:** 5
*   **Medium:** 2
*   **Low:** 0

**Top 3 Most-Affected Packages:**
1.  **axios:** 4 advisories (3 unique CVEs)
2.  **js-yaml:** 2 advisories (1 unique CVE)
3.  **lodash:** 2 advisories (1 unique CVE)

## 6. CRA Compliance Actions
1.  **Immediate:** Update `form-data` to a version using cryptographically secure random values to remediate CVE-2025-7783.
2.  **Urgent:** Patch `axios` to v1.10.1+ or equivalent to resolve Prototype Pollution (CVE-2026-25639) and DoS (CVE-2025-58754).
3.  **Urgent:** Update `minimatch` to remediate ReDoS (CVE-2026-26996).
4.  **Planned:** Update `lodash` to v4.17.22+ to address Prototype Pollution in `_.unset` and `_.omit` (CVE-2025-13465).
5.  **Planned:** Update `js-yaml` and `@babel/runtime` to address remaining Medium severity risks.