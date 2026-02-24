## Vulnerability Summary for bkimminich/juice-shop

### 1. SBOM Overview

This SBOM for `bkimminich/juice-shop` (version `sha256:75b03f3f5336b39d1358d4280c09b8b265ae21e4cb215a9bf68e27f96ac76e3c`), generated on 2026-02-24T14:44:13.000Z, identifies a total of 998 packages. Out of these, 38 packages are affected by known vulnerabilities. The identified vulnerabilities include 7 Critical, 30 High, and 21 Medium severity findings.

### 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers (CVEs with `wildExploited=true` or CISA KEV entries) were identified in this SBOM.

### 3. Exploit Availability Assessment

A total of 14 CVEs have publicly available Proof-of-Concept (PoC) exploits. The top 5 CVEs with PoC by severity are:

*   **CVE-2023-37903** (vm2): CRITICAL, CVSS: 9.8, EPSS: 0.39234 (exploitdb, githubexploit, packetstorm, zdt)
*   **CVE-2023-37466** (vm2): CRITICAL, CVSS: 9.8, EPSS: 0.04997 (exploitdb, githubexploit, packetstorm, zdt)
*   **CVE-2023-32314** (vm2): CRITICAL, CVSS: 9.8, EPSS: 0.69875
*   **CVE-2015-9235** (jsonwebtoken): CRITICAL, CVSS: 9.8, EPSS: 0.3247
*   **CVE-2023-46233** (crypto-js): CRITICAL, CVSS: 9.1, EPSS: 0.00823

9 additional CVEs have exploit evidence.

### 4. Critical & High Findings

The following critical and high severity CVEs were identified:

*   **CVE-2026-22709** (vm2): CRITICAL, CVSS: 9.8, EPSS: 0.0003
*   **CVE-2019-10744** (lodash): CRITICAL, CVSS: 9.1, EPSS: 0.02441
*   **CVE-2024-37890** (ws): HIGH, CVSS: 8.7, EPSS: 0.00541
*   **CVE-2025-15284** (qs): HIGH, CVSS: 8.7, EPSS: 0.00085
*   **CVE-2026-26996** (minimatch): HIGH, CVSS: 8.7, EPSS: 0.0004
*   **CVE-2025-48997** (multer): HIGH, CVSS: 8.7, EPSS: 0.00081
*   **CVE-2016-1000223** (jws): HIGH, CVSS: 8.7, EPSS: 0
*   **CVE-2026-23950** (tar): HIGH, CVSS: 8.8, EPSS: 0.00006

and 22 more HIGH findings across 15 packages.

### 5. Risk Distribution

The product contains 58 unique CVEs, distributed as follows: 7 Critical, 30 High, and 21 Medium. The packages with the highest number of unique CVEs are `sanitize-html@1.4.2` (7 CVEs), `jsonwebtoken@0.1.0` (5 CVEs), `jsonwebtoken@0.4.0` (5 CVEs), `tar@4.4.19` (5 CVEs), and `vm2@3.9.17` (5 CVEs).

### 6. CRA Compliance Actions

1.  **Immediate Action (CRA Obligation - Exploitable Criticals):** Upgrade `vm2` to a version past `3.9.17` to remediate CVE-2023-32314, CVE-2023-37466, CVE-2023-37903, and CVE-2026-22709, which are Critical severity with known exploits.
2.  **Urgent Action (Exploitable Criticals):** Upgrade `jsonwebtoken` to address CVE-2015-9235 (CRITICAL, CVSS 9.8), which has known exploit availability.
3.  **Urgent Action (Exploitable Criticals):** Upgrade `crypto-js` to a version past `3.3.0` to remediate CVE-2023-46233 (CRITICAL, CVSS 9.1), which has known exploit availability.
4.  **Planned Action (High Severity with PoC):** Address the multiple High severity vulnerabilities with PoC in `tar` (CVE-2026-23745, CVE-2026-23950, CVE-2026-24842, CVE-2026-26960) by upgrading to the latest secure version.
5.  **SBOM Hygiene:** Implement continuous monitoring for new vulnerabilities, especially for packages like `sanitize-html`, `lodash`, and `multer`, which show a recurring pattern of security issues. Maintain up-to-date SBOMs for all software components.