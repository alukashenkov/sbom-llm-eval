1. SBOM Overview
- Product: bkimminich/juice-shop
- Format: CycloneDX container
- Scan Date: 2026-02-24
- Total Packages: 998
- Affected Packages: 38
- Unique CVEs: 60 (Critical: 7, High: 32, Medium: 20, None: 1)

2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3. Exploit Assessment
- PoC Evidence Summary: githubexploit (5), exploitdb (2), packetstorm (2), zdt (2), hackerone (3), kitploit (2)
- Top 5 exploited CVEs by severity:
  - CVE-2023-37466 (vm2, CRITICAL, CVSS 9.8, EPSs 0.04997)
  - CVE-2023-37903 (vm2, CRITICAL, CVSS 9.8, EPSs 0.39234)
  - CVE-2023-32314 (vm2, CRITICAL, CVSS 9.8, EPSs 0.69875)
  - CVE-2015-9235 (jsonwebtoken, CRITICAL, CVSS 9.8, EPSs 0.3247)
  - CVE-2026-23745 (tar, HIGH, CVSS 8.2, EPSs 6e-05)
- Additional 12 CVEs have PoC evidence.

4. Critical & High Findings (excluding above)
- CVE-2026-22709 (vm2, CRITICAL, CVSS 9.8, EPSs 0.0003)
- CVE-2019-10744 (lodash@2.4.2, CRITICAL, CVSS 9.1, EPSs 0.02441)
- CVE-2023-46233 (crypto-js, CRITICAL, CVSS 9.1, EPSs 0.00823)
- CVE-2025-13465 (lodash@4.17.21, HIGH, CVSS 7.9, EPSs 0.00025)
- CVE-2025-47935 (multer, HIGH, CVSS 7.5, EPSs 0.00048)
- CVE-2025-47944 (multer, HIGH, CVSS 7.5, EPSs 0.00011)
- CVE-2025-48997 (multer, HIGH, CVSS 8.7, EPSs 0.00081)
- CVE-2024-4068 (braces, HIGH, CVSS 7.5, EPSs 0.00225)
- and 17 more across 11 packages.

5. Risk Distribution
- Severity counts: CRITICAL 7, HIGH 32, MEDIUM 20, NONE 1
- Top affected packages by unique CVEs:
  - sanitize-html@1.4.2 (7 CVEs)
  - jsonwebtoken@0.1.0 (5 CVEs)
  - jsonwebtoken@0.4.0 (5 CVEs)

6. CRA Compliance Actions
- Immediate: Patch vm2 for critical sandbox escape CVEs (CVE-2023-37466, CVE-2023-37903, CVE-2023-32314), jsonwebtoken critical verification bypass (CVE-2015-9235).
- Urgent: Patch tar for arbitrary file overwrite (CVE-2026-23745) and other high severity CVEs with known PoCs.
- Planned: Address remaining high severity CVEs in multer, lodash, braces, and other packages.
- Hygiene: Maintain and update SBOM regularly per CRA Article 10(6) to ensure ongoing vulnerability tracking and compliance.
- Vulnerability handling per CRA Article 11: Prioritize patching based on CVSS, EPSs, and PoC evidence, with timely assessment and remediation.

Summary: The SBOM contains 60 unique CVEs with 7 critical and 32 high severity. No mandatory CRA Article 14 reporting triggers were found. Multiple critical vulnerabilities with PoC exist in vm2 and jsonwebtoken, requiring immediate patching. High severity issues in tar, multer, lodash, and other packages also require urgent and planned remediation. Regular SBOM maintenance and vulnerability management per CRA Articles 10 and 11 are essential.