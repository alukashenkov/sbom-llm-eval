## 1. SBOM Overview
*   **Product**: bkimminich/juice-shop (Container)
*   **Format**: CycloneDX
*   **Scan Date**: 2026-02-24
*   **Packages**: 998 total, 38 affected
*   **Unique CVEs**: 60 (7 CRITICAL, 32 HIGH, 20 MEDIUM, 1 NONE)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **PoC Summary**: 16 unique CVEs have public exploit evidence (5 GitHub, 2 Exploit-DB, 2 PacketStorm, 2 ZDT, 3 HackerOne, 2 KitPloit).
*   **Top Exploited CVEs**:
    *   **CVE-2023-37903** (vm2, CVSS 9.8, EPSS 0.39234): CRITICAL sandbox escape.
    *   **CVE-2023-37466** (vm2, CVSS 9.8, EPSS 0.04997): CRITICAL sandbox escape.
    *   **CVE-2026-23745** (tar, CVSS 8.2, EPSS 0.00006): HIGH arbitrary file overwrite.
    *   **CVE-2022-24785** (moment, CVSS 7.5, EPSS 0.01673): HIGH path traversal.
    *   **CVE-2018-3721** (lodash, CVSS 6.5, EPSS 0.00252): MEDIUM prototype pollution.
*   11 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2015-9235** (jsonwebtoken, CVSS 9.8, EPSS 0.32470)
*   **CVE-2023-32314** (vm2, CVSS 9.8, EPSS 0.69875)
*   **CVE-2026-22709** (vm2, CVSS 9.8, EPSS 0.00030)
*   **CVE-2019-10744** (lodash, CVSS 9.1, EPSS 0.02441)
*   **CVE-2023-46233** (crypto-js, CVSS 9.1, EPSS 0.00823)
*   **CVE-2026-23950** (tar, CVSS 8.8, EPSS 0.00006)
*   **CVE-2025-48997** (multer, CVSS 8.7, EPSS 0.00081)
*   **CVE-2026-26996** (minimatch, CVSS 8.7, EPSS 0.00040)
*   And 24 more across 12 packages.

## 5. Risk Distribution
*   **Severity**: 7 CRITICAL, 32 HIGH, 20 MEDIUM.
*   **Top Affected Packages**:
    1.  `sanitize-html@1.4.2` (7 CVEs)
    2.  `jsonwebtoken@0.1.0` (5 CVEs)
    3.  `tar@4.4.19` (5 CVEs)

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `vm2` to >3.9.19 and `jsonwebtoken` to >8.5.1 to address CRITICAL sandbox escapes and verification bypasses (Article 10).
2.  **Urgent**: Update `tar` to >7.5.2 to remediate HIGH severity arbitrary file overwrites with known PoCs (Article 11).
3.  **Planned**: Update `lodash` to >4.17.21 and `multer` to >2.0.2 to resolve HIGH risk prototype pollution and DoS vulnerabilities.
4.  **Hygiene**: Replace `sanitize-html@1.4.2` (legacy version) to reduce the attack surface of 7 unique CVEs (Article 10(6)).
5.  **Hygiene**: Establish a vulnerability handling policy to meet Article 11 requirements for the 60 identified unique vulnerabilities.