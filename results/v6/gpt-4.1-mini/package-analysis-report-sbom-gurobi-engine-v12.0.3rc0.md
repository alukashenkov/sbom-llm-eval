1. SBOM Overview
- Product: sbom-gurobi-engine-v12.0.3rc0
- Format: SPDX
- Scan Date: 2025-07-11T08:53:07Z
- Total Packages: 12
- Affected Packages: 3
- Unique CVEs: 62 total
  - CRITICAL: 3
  - HIGH: 23
  - MEDIUM: 32
  - LOW: 3
  - NONE: 1

2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3. Exploit Assessment
- PoC Summary: 24 total (GitHub: 8, PacketStorm: 10, HackerOne: 6)
- Top 5 exploited CVEs by severity:
  - CVE-2025-4517 (python@3.11.4) - CVSS 9.4 (CRITICAL), PoC on GitHub (11)
  - CVE-2025-15467 (openssl@3.0.16) - CVSS 9.8 (CRITICAL), PoC on GitHub (2), PacketStorm (2)
  - CVE-2023-36632 (python@3.11.4) - CVSS 7.5 (HIGH), Exploit on NVD
  - CVE-2025-4138 (python@3.11.4) - CVSS 7.5 (HIGH), PoC on GitHub (7), PacketStorm (1)
  - CVE-2025-4330 (python@3.11.4) - CVSS 7.5 (HIGH), PoC on GitHub (2)
- 19 additional CVEs have PoC evidence.

4. Critical & High Findings (excluding above exploited CVEs)
- CVE-2023-41105 (python@3.11.4) - CVSS 7.5, EPSS 0.0037
- CVE-2024-6232 (python@3.11.4) - CVSS 7.5, EPSS 0.02874
- CVE-2024-7592 (python@3.11.4) - CVSS 7.5, EPSS 0.00796
- CVE-2024-8088 (python@3.11.4) - CVSS 7.5, EPSS 0.00154
- CVE-2024-4032 (python@3.11.4) - CVSS 7.5, EPSS 0.01127
- CVE-2024-9287 (python@3.11.4) - CVSS 7.8, EPSS 0.00062
- CVE-2023-6597 (python@3.11.4) - CVSS 7.8, EPSS 0.00071
- CVE-2025-8194 (python@3.11.4) - CVSS 7.5, EPSS 0.00162
- And 15 more across 2 packages.

5. Risk Distribution
- Severity counts:
  - CRITICAL: 3
  - HIGH: 23
  - MEDIUM: 32
  - LOW: 3
  - NONE: 1
- Top affected packages by unique CVEs:
  - python@3.11.4: 40 CVEs
  - openssl@3.0.16: 12 CVEs
  - curl@8.14.1: 10 CVEs

6. CRA Compliance Actions
- Immediate:
  - Patch CRITICAL CVEs with PoC: CVE-2025-4517 (python), CVE-2025-15467 (openssl)
- Urgent:
  - Patch HIGH severity CVEs with PoC: CVE-2023-36632, CVE-2025-4138, CVE-2025-4330 (python)
- Planned:
  - Patch remaining HIGH severity CVEs including CVE-2023-41105, CVE-2024-6232, CVE-2024-7592, CVE-2024-8088, CVE-2024-4032, CVE-2024-9287, CVE-2023-6597, CVE-2025-8194
- Hygiene:
  - Maintain and update SBOM regularly per CRA Article 10(6) to ensure accurate vulnerability tracking and compliance.