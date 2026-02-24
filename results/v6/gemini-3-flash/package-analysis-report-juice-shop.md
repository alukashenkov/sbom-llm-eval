## 1. SBOM Overview
*   **Product**: bkimminich/juice-shop (sha256:75b03f3f...)
*   **Format**: CycloneDX (Container)
*   **Scan Date**: 2026-02-24
*   **Packages**: 998 total / 38 affected
*   **Unique CVEs**: 58 (7 CRITICAL, 30 HIGH, 21 MEDIUM)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **CVE-2023-37903** | vm2 | CVSS 9.8 | EPSS 0.39234 (Exploit-DB, GitHub, PacketStorm, ZDT)
*   **CVE-2023-37466** | vm2 | CVSS 9.8 | EPSS 0.04997 (Exploit-DB, PacketStorm, ZDT)
*   **CVE-2026-23745** | tar | CVSS 8.2 | EPSS 0.00006 (GitHub)
*   **CVE-2022-24785** | moment | CVSS 7.5 | EPSS 0.01673 (GitHub)
*   **CVE-2025-65945** | jws | CVSS 7.5 | EPSS 0.00009 (GitHub)
*   11 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2015-9235** | jsonwebtoken | CVSS 9.8 | EPSS 0.32470
*   **CVE-2023-32314** | vm2 | CVSS 9.8 | EPSS 0.69875
*   **CVE-2026-22709** | vm2 | CVSS 9.8 | EPSS 0.00030
*   **CVE-2019-10744** | lodash | CVSS 9.1 | EPSS 0.02441
*   **CVE-2023-46233** | crypto-js | CVSS 9.1 | EPSS 0.00823
*   **CVE-2026-23950** | tar | CVSS 8.8 | EPSS 0.00006
*   **CVE-2025-48997** | multer | CVSS 8.7 | EPSS 0.00081
*   **CVE-2026-26996** | minimatch | CVSS 8.7 | EPSS 0.00040
*   and 21 more across 12 packages.

## 5. Risk Distribution
*   **Severity**: 7 CRITICAL, 30 HIGH, 21 MEDIUM.
*   **Top Affected Packages**: 
    1. `sanitize-html@1.4.2` (7 CVEs)
    2. `jsonwebtoken@0.1.0` (5 CVEs)
    3. `jsonwebtoken@0.4.0` (5 CVEs)

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `vm2` to version >3.9.19 or migrate (project is deprecated) to resolve CRITICAL sandbox escapes (CVE-2023-37903, CVE-2023-37466) per Article 10(1).
2.  **Urgent**: Update `jsonwebtoken` to >8.5.1 to remediate CRITICAL signature bypass (CVE-2015-9235).
3.  **Planned**: Update `tar` to >7.5.2 and `multer` to >2.0.2 to address HIGH severity path traversals and DoS triggers.
4.  **Planned**: Upgrade `lodash` to >4.17.21 and `crypto-js` to >4.2.0 to resolve Article 10 security requirement gaps.
5.  **Hygiene**: Implement automated SBOM lifecycle management and vulnerability monitoring to comply with Article 10(6) and Article 11.