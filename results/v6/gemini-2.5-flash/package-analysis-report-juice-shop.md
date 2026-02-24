## 1. SBOM Overview
- **Product:** bkimminich/juice-shop (CycloneDX)
- **Scan Date:** 2026-02-24T14:44:13.000Z
- **Packages:** 998 total, 38 affected
- **Unique CVEs:** 58
  - CRITICAL: 7
  - HIGH: 30
  - MEDIUM: 21

## 2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
- **Top 5 Exploited CVEs by Severity:**
    - CVE-2023-37903 (vm2@3.9.17): CRITICAL, EPSS: 0.39234
    - CVE-2015-9235 (jsonwebtoken@0.1.0): CRITICAL, EPSS: 0.3247
    - CVE-2023-32314 (vm2@3.9.17): CRITICAL, EPSS: 0.69875
    - CVE-2023-37466 (vm2@3.9.17): CRITICAL, EPSS: 0.04997
    - CVE-2026-23745 (tar@4.4.19): HIGH, EPSS: 0.00006
- 10 additional CVEs have PoC evidence.

## 4. Critical & High Findings
- CVE-2023-46233 (crypto-js@3.3.0): CRITICAL, CVSS: 9.1, EPSS: 0.00823
- CVE-2019-10744 (lodash@2.4.2): CRITICAL, CVSS: 9.1, EPSS: 0.02441
- CVE-2026-22709 (vm2@3.9.17): CRITICAL, CVSS: 9.8, EPSS: 0.0003
- CVE-2026-23950 (tar@4.4.19): HIGH, CVSS: 8.8, EPSS: 0.00006
- CVE-2025-15284 (qs@6.14.0): HIGH, CVSS: 8.7, EPSS: 0.00085
- CVE-2026-26996 (minimatch@5.1.6): HIGH, CVSS: 8.7, EPSS: 0.0004
- CVE-2025-48997 (multer@1.4.5-lts.2): HIGH, CVSS: 8.7, EPSS: 0.00081
- CVE-2024-37890 (ws@7.4.6): HIGH, CVSS: 8.7, EPSS: 0.00541
- and 22 more across 17 packages.

## 5. Risk Distribution
- **Severity Counts:**
    - CRITICAL: 7
    - HIGH: 30
    - MEDIUM: 21
- **Top 3 Affected Packages:**
    - sanitize-html@1.4.2: 7 unique CVEs
    - jsonwebtoken@0.1.0: 5 unique CVEs
    - jsonwebtoken@0.4.0: 5 unique CVEs

## 6. CRA Compliance Actions
1. **Immediate Action (CRA Article 11):** Address CVEs with PoC evidence and CRITICAL severity, especially CVE-2023-37903, CVE-2015-9235, CVE-2023-32314, CVE-2023-37466, and CVE-2026-23745.
2. **Urgent Action (CRA Article 10, 11):** Patch `vm2` to a version beyond 3.9.17 to mitigate multiple CRITICAL sandbox escapes. Patch `jsonwebtoken` to address CRITICAL verification bypass (CVE-2015-9235).
3. **Planned Action (CRA Article 10, 11):** Prioritize patching all remaining HIGH severity vulnerabilities, focusing on those with higher EPSS scores, such as CVE-2023-46233 in `crypto-js` and CVE-2019-10744 in `lodash`.
4. **Hygiene (CRA Article 10(6)):** Maintain up-to-date SBOMs and regularly scan for new vulnerabilities to ensure continuous compliance.