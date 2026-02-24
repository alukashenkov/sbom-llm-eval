## 1. SBOM Overview
*   **Product**: sbom-grbrsm_ui-v12.0.3rc0
*   **Format**: SPDX
*   **Scan Date**: 2025-07-11
*   **Packages**: 338 total / 7 affected
*   **Unique CVEs**: 9 (1 CRITICAL, 5 HIGH, 3 MEDIUM)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **CVE-2025-7783** | form-data | CVSS 9.4 | EPSS 0.00177 (PoC available)
*   **CVE-2025-7783** | axios | CVSS 7.5 | EPSS 0.00177 (PoC available)
*   1 additional CVE has PoC evidence.

## 4. Critical & High Findings
*   **CVE-2026-26996** | minimatch | CVSS 8.7 | EPSS 0.00040
*   **CVE-2026-25639** | axios | CVSS 8.7 | EPSS 0.00033
*   **CVE-2025-13465** | lodash | CVSS 8.2 | EPSS 0.00025
*   **CVE-2025-58754** | axios | CVSS 7.5 | EPSS 0.00102
*   **CVE-2025-54371** | axios | CVSS 7.5 | EPSS N/A
*   and 0 more across 0 packages.

## 5. Risk Distribution
*   **Severity**: 1 CRITICAL, 5 HIGH, 3 MEDIUM.
*   **Top Affected Packages**:
    1. axios@1.10.0 (4 unique CVEs)
    2. js-yaml@4.1.0 (1 unique CVE)
    3. lodash@4.17.21 (1 unique CVE)

## 6. CRA Compliance Actions
1.  **Immediate**: Patch `form-data` to resolve **CVE-2025-7783** (CRITICAL) to meet Article 10 security-by-default requirements.
2.  **Urgent**: Update `axios` to latest stable version to mitigate multiple HIGH severity vulnerabilities including **CVE-2026-25639** and **CVE-2025-58754**.
3.  **Planned**: Remediate `minimatch` (**CVE-2026-26996**) and `lodash` (**CVE-2025-13465**) through dependency updates to address Article 11 vulnerability handling obligations.
4.  **Hygiene**: Review and maintain the SBOM per Article 10(6) to ensure accurate tracking of transitive dependencies like `form-data`.