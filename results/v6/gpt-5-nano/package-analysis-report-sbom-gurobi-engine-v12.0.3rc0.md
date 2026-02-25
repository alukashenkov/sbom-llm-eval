1) SBOM Overview
- Product: sbom-gurobi-engine-v12.0.3rc0
- Format: SPDX
- Scan date: 2025-07-11
- Packages: total 12 / affected 3
- Unique CVEs (cveAnalytics.severityDistribution.uniqueCVECount): 62
- Severity distribution: HIGH 23, MEDIUM 32, CRITICAL 3, LOW 3, NONE 1

2) CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3) Exploit Assessment
- Top exploited CVEs by severity (with package and PoC evidence)
  - CVE-2025-15467 — OpenSSL (SNYK:CONAN-OPENSSL-15124519) — CVSS 9.8 CRITICAL (3.1); EPSS 0.00672; PoC sources: GitHub, PacketStorm
  - CVE-2025-4517 — OpenSSL / Python context (BIT-PYTHON-2025-4517) — CVSS 9.4 CRITICAL (3.1); EPSS 0.00071; PoC sources: GitHub, PacketStorm
  - CVE-2025-4138 — Python (BIT-PYTHON-2025-4138) — CVSS 7.5 HIGH (3.1); EPSS 0.00066; PoC sources: GitHubexploit, PacketStorm
  - CVE-2025-4330 — Python (BIT-PYTHON-2025-4330) — CVSS 7.5 HIGH (3.1); EPSS 0.00253; PoC sources: GitHubexploit
  - CVE-2025-4435 — Python (BIT-PYTHON-2025-4435) — CVSS 7.5 HIGH (3.1); EPSS 0.00123; PoC sources: GitHubexploit
- N additional CVEs have PoC evidence: 1

4) Critical & High Findings
- Remaining CRITICAL/HIGH CVEs not in §2-3 (max 8)
  - CVE-2024-6232 — Python (BIT-PYTHON-2024-6232) — HIGH; CVSS 7.5; EPSS 0.02874; p ocSources: GitHubexploit
  - CVE-2024-4032 — Python/BELL context (BELL-CVE-2024-4032) — HIGH; CVSS 7.5; EPSS 0.01127
  - CVE-2024-8088 — Python (BIT-PYTHON-2024-8088) — HIGH; CVSS 7.5; EPSS 0.00154
  - CVE-2023-6597 — Python (BIT-PYTHON-2023-6597) — HIGH; CVSS 7.8; EPSS 0.00071
  - CVE-2023-41105 — Python (OSV/BELL/OSV-PYTHON context) — HIGH; CVSS 7.5; EPSS 0.0037
  - CVE-2024-7592 — Python (OSV/BIT-PYTHON-2024-7592) — HIGH; CVSS 7.5; EPSS 0.00796
- Note: all entries above exist in input data and represent CRITICAL/HIGH findings not included in §3.

5) Risk Distribution
- Severity counts (cveAnalytics.severityDistribution): HIGH 23, MEDIUM 32, CRITICAL 3, LOW 3, NONE 1
- Top affected packages (cveAnalytics.topAffectedPackages):
  - python@3.11.4 — 40 unique CVEs
  - https://openssl.org|openssl@3.0.16 — 12 unique CVEs
  - https://curl.se|curl@8.14.1 — 10 unique CVEs

6) CRA Compliance Actions (max 5)
- Immediate (Article 10): Patch CRITICAL CVEs CVE-2025-15467 and CVE-2025-4517; coordinate with PSIRT/affected vendors.
- Urgent (Article 11): Patch HIGH CVEs with PoC and active impact (CVE-2025-4138, CVE-2025-4330, CVE-2025-4435) with target fixed versions as released.
- Planned (Article 11): Schedule fixes for additional HIGH CVEs not yet deployed (e.g., CVE-2024-6232, CVE-2024-4032, CVE-2024-8088, CVE-2023-6597, CVE-2024-7592, CVE-2023-41105).
- Hygiene (Article 10(6)): Maintain SBOM accuracy and update per new advisories; ensure dependency mapping and CVE links are current.
- Governance: Document patch status and remediation SLAs; align with CRA Article 10/11 processes and CRA Article 14 readiness if triggered.