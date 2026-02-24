## 1. SBOM Overview
- Product: openclaw, SPDX format
- Scan Date: 2026-02-20T17:16:42.000Z
- Total Packages: 1112
- Affected Packages: 21
- Unique CVEs: 57 (2 CRITICAL, 34 HIGH, 19 MEDIUM, 2 LOW)

## 2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
- CVE-2026-25253 (clawdbot): CVSS 8.8, EPSS 0.00049
- CVE-2026-24763 (clawdbot): CVSS 8.8, EPSS 0.00083
- CVE-2026-25157 (clawdbot): CVSS 7.7, EPSS 0.00006
- CVE-2026-22610 (@angular/compiler): CVSS 8.5, EPSS 0.00021
- CVE-2026-22610 (@angular/core): CVSS 8.5, EPSS 0.00021
- 6 additional CVEs have PoC evidence.

## 4. Critical & High Findings
- CVE-2023-34104 (fast-xml-parser): CVSS 9.3, EPSS 0.00273
- CVE-2026-25896 (fast-xml-parser): CVSS 9.3, EPSS 0.00029
- GHSA-FHVM-J76F-QMJV (openclaw): CVSS 9.1, EPSS N/A
- GHSA-4RJ2-GPMH-QQ5X (openclaw): CVSS 9.4, EPSS N/A
- GHSA-RV39-79C4-7459 (openclaw): CVSS 9.3, EPSS N/A
- GHSA-JQPQ-MGVM-F9R6 (openclaw): CVSS 8.8, EPSS N/A
- GHSA-R5FQ-947M-XM57 (openclaw): CVSS 8.8, EPSS N/A
- CVE-2026-25593 (openclaw): CVSS 8.4, EPSS 0.00023
- and 25 more across 10 packages.

## 5. Risk Distribution
- CRITICAL: 2
- HIGH: 34
- MEDIUM: 19
- LOW: 2
- Top 3 Affected Packages:
    - openclaw@2026.1.10: 29 unique CVEs
    - hono@4.11.3: 6 unique CVEs
    - clawdbot@2026.1.10: 5 unique CVEs

## 6. CRA Compliance Actions
- **Immediate (CRA Article 10, 11)**:
    - Patch CVE-2026-25253 in `clawdbot` to prevent 1-Click RCE.
    - Patch CVE-2026-24763 in `clawdbot` to address authenticated command injection.
    - Patch CVE-2026-25157 in `clawdbot` to fix OS command injection.
    - Patch CVE-2026-22610 in `@angular/compiler` and `@angular/core` to mitigate XSS.
    - Patch CVE-2025-69873 in `ajv` to prevent ReDoS.
    - Patch CVE-2025-65945 in `jws` to fix improper HMAC signature verification.
- **Urgent (CRA Article 10, 11)**:
    - Update `fast-xml-parser` to address CRITICAL vulnerabilities CVE-2023-34104 and CVE-2026-25896 (entity encoding bypass).
    - Address CRITICAL vulnerabilities in `openclaw` (GHSA-FHVM-J76F-QMJV, GHSA-4RJ2-GPMH-QQ5X, GHSA-RV39-79C4-7459) related to authorization bypass and identity checks.
    - Update `node-forge` to fix HIGH severity ASN.1 vulnerabilities CVE-2025-66031 and CVE-2025-12816.
- **Planned (CRA Article 10, 11)**:
    - Review and update `openclaw` to address remaining HIGH severity issues including RCE, SSRF, and path traversal vulnerabilities.
    - Update `hono` to fix HIGH severity JWT algorithm confusion vulnerabilities CVE-2026-22818 and CVE-2026-22817.
    - Update `qs` to mitigate HIGH severity DoS vulnerabilities CVE-2025-15284 and CVE-2026-2391.
    - Update `minimatch` to fix HIGH severity ReDoS vulnerability CVE-2026-26996.
- **Hygiene (CRA Article 10(6))**:
    - Regularly review and update all dependencies to ensure known vulnerabilities are addressed promptly.
    - Implement automated vulnerability scanning in CI/CD pipelines.