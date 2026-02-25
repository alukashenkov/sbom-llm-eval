1. SBOM Overview
- Product: vulners-mcp container
- Format: CycloneDX
- Scan date: 2026-02-24T14:35:34Z
- Total packages: 560
- Affected packages: 20
- Unique CVEs: 188 total
  - Critical: 12
  - High: 76
  - Medium: 87
  - Low: 12
  - None: 1

2. CRA Mandatory Reporting (Article 14)
- CVE-2025-48384 (git@1:2.47.3-0+deb13u1)
  - CVSS: 8.0 (High)
  - EPSS: 0.00456
  - Wild exploited and on CISA KEV list
- Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.

3. Exploit Assessment
- PoC evidence summary: 13 Packetstorm, 9 GitHub exploits, 7 HackerOne, 1 CISA KEV, 1 Gitee, 1 Nuclei, 1 Kitploit
- Top 5 exploited CVEs by severity (from advisory data):
  - CVE-2025-48384 (git) - CVSS 8.0, EPSS 0.00456
  - CVE-2025-15467 (openssl) - CVSS 9.8 (Critical), EPSS 0.00672
  - CVE-2025-55298 (imagemagick) - CVSS 8.8 (High), EPSS 0.0043
  - CVE-2025-57803 (imagemagick) - CVSS 8.8 (High), EPSS 0.00075
  - CVE-2025-11082 (binutils) - CVSS 7.8 (High), EPSS 0.00017
- Additional 17 CVEs have PoC evidence.

4. Critical & High Findings (excluding §2-3)
- CVE-2026-23876 (imagemagick) - CVSS 9.8 (Critical), EPSS 0.00062
- CVE-2026-22770 (imagemagick) - CVSS 9.8 (Critical), EPSS 0.00065
- CVE-2024-40896 (libxml2) - CVSS 9.1 (Critical), EPSS 0.00553
- CVE-2025-49794 (libxml2) - CVSS 9.1 (Critical), EPSS 0.00078
- CVE-2025-49796 (libxml2) - CVSS 9.1 (Critical), EPSS 0.0055
- CVE-2025-53014 (imagemagick) - CVSS 9.8 (Critical), EPSS 0.00031
- CVE-2025-53101 (imagemagick) - CVSS 9.8 (Critical), EPSS 0.00069
- CVE-2025-55212 (imagemagick) - CVSS 7.5 (High), EPSS 0.0026
- and 68 more across 14 packages.

5. Risk Distribution
- Severity counts:
  - Critical: 12
  - High: 76
  - Medium: 87
  - Low: 12
  - None: 1
- Top affected packages:
  - imagemagick@8:7.1.1.43+dfsg1-1+deb13u5: 77 CVEs
  - binutils@2.44-3: 32 CVEs
  - libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2: 17 CVEs

6. CRA Compliance Actions
- Immediate (CRA Article 14 triggers):
  - Patch git@1:2.47.3-0+deb13u1 for CVE-2025-48384 (wild exploited, CISA KEV)
- Urgent:
  - Patch openssl@3.5.4-1~deb13u2 for CVE-2025-15467 (Critical, PoC)
  - Patch imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 for CVE-2025-55298, CVE-2025-57803 (High, PoC)
  - Patch binutils@2.44-3 for CVE-2025-11082 (High)
- Planned:
  - Patch remaining High severity CVEs in imagemagick, libxml2, curl, and other affected packages
- Hygiene:
  - Maintain and update SBOM regularly per CRA Article 10(6) to ensure timely vulnerability tracking and compliance