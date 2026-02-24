## 1. SBOM Overview
**Product:** bkimminich/juice-shop (Container)  
**Format:** CycloneDX | **Scan Date:** Feb 24, 2026  
The analysis identified **58 unique CVEs** across **38 affected packages** out of a total of 998. The vulnerability density is high, with a severity distribution of **7 Critical, 30 High, and 21 Medium** findings.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities in the current dataset are confirmed as actively exploited in the wild or listed in the CISA KEV catalog.

## 3. Exploit Availability Assessment
There are **16 unique exploit references** identified across the SBOM (5 GitHub, 2 ExploitDB, 2 PacketStorm, 2 ZDT, 3 HackerOne, 2 KitPloit).

**Top 5 CVEs with Proof-of-Concept (PoC):**
1. **CVE-2023-37466** (vm2): CVSS 9.8 (CRITICAL). Sandbox escape leading to RCE.
2. **CVE-2023-37903** (vm2): CVSS 9.8 (CRITICAL). Sandbox escape leading to RCE.
3. **CVE-2026-23745** (tar): CVSS 8.2 (HIGH). Arbitrary file overwrite.
4. **CVE-2022-24785** (moment): CVSS 7.5 (HIGH). Path Traversal.
5. **CVE-2018-3721** (lodash): CVSS 6.5 (MEDIUM). Prototype Pollution.

11 additional CVEs have exploit evidence.

## 4. Critical & High Findings
The following critical risks require immediate attention:
*   **CVE-2015-9235** (jsonwebtoken): CVSS 9.8, EPSS 0.32. Verification bypass.
*   **CVE-2023-32314** (vm2): CVSS 9.8, EPSS 0.69. Sandbox escape.
*   **CVE-2026-22709** (vm2): CVSS 9.8, EPSS 0.00. Sandbox escape.
*   **CVE-2019-10744** (lodash): CVSS 9.1, EPSS 0.02. Prototype pollution.
*   **CVE-2023-46233** (crypto-js): CVSS 9.1, EPSS 0.00. Weak PBKDF2 iteration count.
*   **CVE-2026-23950** (tar): CVSS 8.8, EPSS 0.00. Race condition/Path traversal.
*   **CVE-2025-48997** (multer): CVSS 8.7, EPSS 0.00. Denial of Service.
*   **CVE-2026-26996** (minimatch): CVSS 8.7, EPSS 0.00. ReDoS.

And **22 more HIGH findings** across **12 packages**.

## 5. Risk Distribution
The risk is heavily concentrated in core utility libraries. The **top affected packages** by unique CVE count are:
1.  **sanitize-html@1.4.2**: 7 CVEs
2.  **vm2@3.9.17**: 5 CVEs (High RCE risk)
3.  **tar@4.4.19**: 5 CVEs
4.  **jsonwebtoken@0.1.0/0.4.0**: 5 CVEs (Auth bypass risk)

## 6. CRA Compliance Actions
1.  **Immediate (24h-72h):** Replace or remove **vm2**. The library is deprecated and contains multiple unpatchable Critical sandbox escapes (CVE-2023-37466, CVE-2023-37903).
2.  **Urgent:** Update **jsonwebtoken** to version >9.0.0 to resolve critical verification bypasses (CVE-2015-9235).
3.  **Urgent:** Update **lodash** to >=4.17.21 and **sanitize-html** to >=2.12.1 to mitigate prototype pollution and XSS.
4.  **Planned:** Update **tar** to >=9.0.0 to resolve multiple high-severity path traversal and file overwrite vulnerabilities.
5.  **Hygiene:** Consolidate duplicate package versions (e.g., `tar`, `minimatch`, `lodash`) to reduce the attack surface and simplify compliance tracking.