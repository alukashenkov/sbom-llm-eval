1) SBOM Overview
- Product: vulners-mcp
- Format: CycloneDX
- Scan date: 2026-02-24
- Packages: total 560; affected 20
- Unique CVEs from cveAnalytics.severityDistribution: 188

2) CRA Mandatory Reporting (Article 14)
- Trigger: CVE-2025-48384
  - CVE: CVE-2025-48384
  - Package: git (version 2.47.3-0+deb13u1)
  - CVSS: 8.0 HIGH
  - EPSS: 0.00456
  - WildExploited: true; CISA KEV present
  - CRA Article 14(2) note: 24h early warning → 72h assessment → 14-day final report

3) Exploit Assessment
- Top exploited CVEs by severity (with PoC evidence)
  - CVE-2025-53014, package tar, CVSS 9.8, EPSS 0.00031
  - CVE-2025-53101, package tar, CVSS 9.8, EPSS 0.00069
  - CVE-2024-40896, package libxml2, CVSS 9.1, EPSS 0.00553
  - CVE-2025-48385, package git, CVSS 8.6, EPSS 0.00039
  - CVE-2025-53015, package tar, CVSS 7.5, EPSS 0.00039
- PoC evidence overview: 33 total PoC entries across sources (packetstorm, githubexploit, hackerone, cisa_kev, gitee, nuclei, kitploit)

4) Critical & High Findings
- Remaining CRITICAL/HIGH CVEs not in §2-3 (selected 8, max allowed)
  - CVE-2025-53014, tar, CVSS 9.8, EPSS 0.00031
  - CVE-2025-53101, tar, CVSS 9.8, EPSS 0.00069
  - CVE-2024-40896, libxml2, CVSS 9.1, EPSS 0.00553
  - CVE-2025-55154, imagemagick, CVSS 8.8, EPSS 0.00047
  - CVE-2025-55212, imagemagick, CVSS 7.5, EPSS 0.00038
  - CVE-2025-5244, binutils, CVSS 7.8, EPSS 0.0003
  - CVE-2025-5245, binutils, CVSS 7.8, EPSS 0.00031
  - CVE-2025-68618, imagemagick, CVSS 7.5, EPSS 0.00096
- and 83 more across multiple packages (not listed here)

5) Risk Distribution
- Severity distribution: HIGH 76, MEDIUM 87, CRITICAL 12, LOW 12, NONE 1
- Top affected packages: imagemagick (77 CVEs), binutils (32 CVEs), libxml2 (17 CVEs)

6) CRA Compliance Actions (Article 10 & 11)
- Immediate: patch CVE-2025-48384 in git to mitigate current exploitation (Article 10)
- Urgent: patch exploited CRITICAL/HIGH fixes with target versions:
  - CVE-2025-53014 (tar) → fixed tar release
  - CVE-2024-40896 (libxml2) → fixed libxml2 release
  - CVE-2025-55154 (imagemagick) → fixed imagemagick release
- Planned: complete remediation for remaining HIGH fixes (e.g., CVE-2025-68618, CVE-2025-55212, CVE-2025-5244, CVE-2025-5245) and verify no new disclosures
- Hygiene: SBOM maintenance per Article 10(6) — refresh and publish updated SBOM, ensure logsupply of CVEs/EPSS/CVSS, and align with CRA Article 11 vulnerability handling processes