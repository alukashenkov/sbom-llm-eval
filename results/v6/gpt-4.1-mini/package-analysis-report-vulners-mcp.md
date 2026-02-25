1. SBOM Overview
- Product: vulners-mcp
- Format: CycloneDX container
- Scan date: 2026-02-24T14:35:34Z
- Total packages: 560
- Affected packages: 20
- Unique CVEs: 188 total
  - Critical: 14
  - High: 82
  - Medium: 79
  - Low: 12
  - None: 1

2. CRA Mandatory Reporting (Article 14)
- CVE-2025-48384 (git@1:2.47.3-0+deb13u1)
  - CVSS: 8.0 (High)
  - EPSS: 0.00456
  - Wild exploited and listed in CISA KEV
- Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.

3. Exploit Assessment
- Total PoC evidence CVEs: 33 (githubexploit: 9, packetstorm: 13, hackerone: 7, cisa_kev: 1, gitee: 1, nuclei: 1, kitploit: 1)
- Top 5 exploited CVEs by severity from advisory data:
  1. CVE-2025-48384 (git) - CVSS 8.0, EPSS 0.00456, wild exploited
  2. CVE-2025-15467 (openssl) - CVSS 9.8 (Critical), EPSS 0.00672, PoC on github & packetstorm
  3. CVE-2024-40896 (libxml2) - CVSS 9.1 (Critical), EPSS 0.00553
  4. CVE-2025-55298 (imagemagick) - CVSS 8.8 (High), EPSS 0.0043
  5. CVE-2021-32804 (tar) - CVSS 8.2 (High), EPSS 0.84982, github PoC
- 28 additional CVEs have PoC evidence.

4. Critical & High Findings (excluding §2-3)
- CVE-2026-22770 (imagemagick) - CVSS 9.8, EPSS 0.00065
- CVE-2026-23876 (imagemagick) - CVSS 9.8, EPSS 0.00062
- CVE-2025-53014 (imagemagick) - CVSS 9.8, EPSS 0.00031
- CVE-2025-53101 (imagemagick) - CVSS 9.8, EPSS 0.00069
- CVE-2026-25897 (imagemagick) - CVSS 9.8, EPSS 0.00038
- CVE-2026-26284 (imagemagick) - CVSS 9.1, EPSS 0.00037
- CVE-2025-5244 (binutils) - CVSS 7.8, EPSS 0.0003
- CVE-2025-11082 (binutils) - CVSS 7.8, EPSS 0.00016
- and 74 more across 17 packages.

5. Risk Distribution
- Severity counts:
  - Critical: 14
  - High: 82
  - Medium: 79
  - Low: 12
  - None: 1
- Top 3 affected packages by unique CVEs:
  1. imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 (77 CVEs)
  2. binutils@2.44-3 (32 CVEs)
  3. libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 (17 CVEs)

6. CRA Compliance Actions
- Immediate:
  - Patch git@1:2.47.3-0+deb13u1 for CVE-2025-48384 (wild exploited, CRA Article 14 trigger)
- Urgent:
  - Patch critical/high exploited CVEs with PoC:
    - CVE-2025-15467 (openssl 3.5.4-1~deb13u2)
    - CVE-2024-40896 (libxml2 2.12.7+dfsg+really2.9.14-2.1+deb13u2)
    - CVE-2025-55298 (imagemagick 8:7.1.1.43+dfsg1-1+deb13u5)
    - CVE-2021-32804 (tar 1.35+dfsg-3.1)
- Planned:
  - Patch remaining High severity CVEs in imagemagick, binutils, openssl, curl, and others.
- Hygiene:
  - Maintain SBOM accuracy and update per CRA Article 10(6) requirements.

Summary:
- 188 unique CVEs found, 14 critical, 82 high severity.
- One CRA Article 14 mandatory report: CVE-2025-48384 in git (wild exploited).
- 33 CVEs with PoC evidence; top exploited include CVE-2025-48384, CVE-2025-15467, CVE-2024-40896.
- Immediate patching required for git CVE-2025-48384.
- Urgent patching for critical/high CVEs with PoC in openssl, libxml2, imagemagick, tar.
- Planned patching for remaining high severity CVEs.
- SBOM maintenance ongoing per CRA compliance.