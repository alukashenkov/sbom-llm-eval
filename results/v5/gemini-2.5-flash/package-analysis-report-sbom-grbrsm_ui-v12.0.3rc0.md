## Vulnerability Summary for sbom-grbrsm_ui-v12.0.3rc0

### 1. SBOM Overview
This SPDX-formatted SBOM, generated on 2025-07-11T08:54:40.000Z for `sbom-grbrsm_ui-v12.0.3rc0`, details 338 software packages. Of these, 7 packages are affected by 9 unique CVEs. The identified vulnerabilities include 1 CRITICAL, 5 HIGH, and 3 MEDIUM severity findings.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
A total of 2 CVEs have known exploit evidence. The top CVEs with Proof-of-Concept (PoC) by severity are:

*   **CVE-2025-7783** (CRITICAL, CVSS: 9.4) in `form-data`
*   **CVE-2025-7783** (HIGH, CVSS: 7.5) in `axios`

0 additional CVEs have exploit evidence.

### 4. Critical & High Findings
The following CRITICAL and HIGH CVEs require immediate attention:

*   **CVE-2025-7783** (CRITICAL, CVSS: 9.4) in `form-data`
*   **CVE-2026-25639** (HIGH, CVSS: 8.7) in `axios`
*   **CVE-2026-26996** (HIGH, CVSS: 8.7) in `minimatch`
*   **CVE-2025-13465** (HIGH, CVSS: 8.2) in `lodash`
*   **CVE-2025-58754** (HIGH, CVSS: 7.5) in `axios`
*   **CVE-2025-54371** (HIGH, CVSS: 7.5) in `axios`

And 0 more HIGH findings across 0 packages.

### 5. Risk Distribution
The vulnerabilities are distributed as follows: 1 CRITICAL, 5 HIGH, and 3 MEDIUM. The packages with the most unique CVEs are `axios@1.10.0` (4 CVEs), `js-yaml@4.1.0` (1 CVE), `lodash@4.17.21` (1 CVE), `minimatch@7.4.6` (1 CVE), and `@babel/runtime@7.0.0` (1 CVE).

### 6. CRA Compliance Actions
1.  **Immediate Action:** Upgrade `form-data` to a patched version to remediate **CVE-2025-7783** (CRITICAL, CVSS 9.4), which has known exploit evidence. This is a critical vulnerability with a high impact on confidentiality, integrity, and availability.
2.  **Urgent Action:** Upgrade `axios` to a patched version to address **CVE-2026-25639** (HIGH, CVSS 8.7) and **CVE-2025-58754** (HIGH, CVSS 7.5), both of which are high-severity denial-of-service or prototype pollution issues.
3.  **Urgent Action:** Upgrade `minimatch` to a patched version to mitigate **CVE-2026-26996** (HIGH, CVSS 8.7), a Regular Expression Denial of Service (ReDoS) vulnerability.
4.  **Planned Action:** Upgrade `lodash` to a patched version to resolve **CVE-2025-13465** (HIGH, CVSS 8.2), a prototype pollution vulnerability.
5.  **SBOM Hygiene:** Regularly update all dependencies and maintain accurate SBOMs to proactively identify and address new vulnerabilities.