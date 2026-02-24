## 1. SBOM Overview
This CycloneDX SBOM for `bkimminich/juice-shop` (sha256:75b03f3f5336b39d1358d4280c09b8b265ae21e4cb215a9bf68e27f96ac76e3c), generated on 2026-02-24, identifies 998 total packages, with 38 affected by vulnerabilities. There are 3 Critical, 26 High, 16 Medium, and 1 Low unique CVEs.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
The following CVEs have publicly available exploit evidence:
*   **CVE-2023-37466** (vm2@3.9.17) - CVSS: 9.8 (CRITICAL), EPSS: 0.04997
*   **CVE-2023-37903** (vm2@3.9.17) - CVSS: 9.8 (CRITICAL), EPSS: 0.39234
*   **CVE-2022-24785** (moment@2.0.0) - CVSS: 7.5 (HIGH), EPSS: 0.01673
*   **CVE-2026-23745** (tar@4.4.19) - CVSS: 8.2 (HIGH), EPSS: 0.00006
*   **CVE-2026-23745** (tar@6.2.1) - CVSS: 8.2 (HIGH), EPSS: 0.00006

3 additional CVEs have exploit evidence.

## 4. Critical & High Findings
*   **CVE-2015-9235** (jsonwebtoken@0.1.0) - CVSS: 9.8 (CRITICAL), EPSS: 0.3247
*   **CVE-2023-32314** (vm2@3.9.17) - CVSS: 9.8 (CRITICAL), EPSS: 0.69875
*   **CVE-2019-10744** (lodash@2.4.2) - CVSS: 9.1 (CRITICAL), EPSS: 0.02441
*   **CVE-2023-46233** (crypto-js@3.3.0) - CVSS: 9.1 (CRITICAL), EPSS: 0.00823
*   **CVE-2026-22709** (vm2@3.9.17) - CVSS: 9.8 (CRITICAL), EPSS: 0.0003
*   **CVE-2026-23950** (tar@4.4.19) - CVSS: 8.8 (HIGH), EPSS: 0.00006
*   **CVE-2025-15284** (qs@6.14.0) - CVSS: 8.7 (HIGH), EPSS: 0.00085
*   **CVE-2026-26996** (minimatch@5.1.6) - CVSS: 8.7 (HIGH), EPSS: 0.0004
and 18 more HIGH findings across 11 packages.

## 5. Risk Distribution
*   **Critical:** 3 unique CVEs
*   **High:** 26 unique CVEs
*   **Medium:** 16 unique CVEs
*   **Low:** 1 unique CVE
*   **None:** 1 unique CVE

Top 3 most-affected packages:
1.  `sanitize-html`: 7 advisories
2.  `jsonwebtoken`: 5 advisories
3.  `tar`: 5 advisories

## 6. CRA Compliance Actions
1.  **Immediate Action:** Upgrade `vm2` to a version beyond 3.9.17 to remediate critical sandbox escapes (CVE-2023-32314, CVE-2023-37466, CVE-2023-37903, CVE-2026-22709) with known exploits.
2.  **Urgent Action:** Upgrade `jsonwebtoken` from 0.1.0 to address critical verification bypass (CVE-2015-9235).
3.  **Urgent Action:** Upgrade `crypto-js` from 3.3.0 to mitigate critical weak PBKDF2 implementation (CVE-2023-46233).
4.  **Planned Action:** Upgrade `lodash` from 2.4.2 to address critical prototype pollution (CVE-2019-10744).
5.  **SBOM Hygiene:** Review and update `base64url` from 0.0.6 as it allocates uninitialized buffers, which could lead to information disclosure on older Node.js versions.