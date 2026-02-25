1. SBOM Overview
- Product: sbom-gurobi-engine-v12.0.3rc0
- Format: SPDX
- Scan Date: 2025-07-11
- Total Packages: 12
- Affected Packages: 3
- Unique CVEs: 62 total
  - Critical: 3
  - High: 23
  - Medium: 32
  - Low: 3
  - None: 1

2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3. Exploit Assessment
- PoC evidence summary: 24 total (GitHub: 8, PacketStorm: 10, HackerOne: 6)
- Top 5 exploited CVEs by severity (from advisory data):
  1. CVE-2025-4517 (python) - CVSS 9.4 (Critical), EPSS 0.00071, PoC on GitHub (11)
  2. CVE-2025-15467 (openssl) - CVSS 9.8 (Critical), EPSS 0.00672, PoC on GitHub (2), PacketStorm (2)
  3. CVE-2023-36632 (python) - CVSS 7.5 (High), EPSS 0.00112, Exploit reported (NVD)
  4. CVE-2025-4138 (python) - CVSS 7.5 (High), EPSS 0.00077, PoC on GitHub (7), PacketStorm (1)
  5. CVE-2025-4330 (python) - CVSS 7.5 (High), EPSS 0.00298, PoC on GitHub (2)
- Additional 19 CVEs have PoC evidence.

4. Critical & High Findings (excluding above)
- CVE-2007-4559 (python) - CVSS 9.8 (Critical), EPSS 0.90582, PoC GitHub (1)
- CVE-2024-8088 (python) - CVSS 7.5 (High), EPSS 0.00154
- CVE-2024-6232 (python) - CVSS 7.5 (High), EPSS 0.02874, PoC GitHub (1)
- CVE-2024-4032 (python) - CVSS 7.5 (High), EPSS 0.01127
- CVE-2023-6597 (python) - CVSS 7.8 (High), EPSS 0.00071
- CVE-2024-9287 (python) - CVSS 7.8 (High), EPSS 0.00062
- CVE-2025-8194 (python) - CVSS 7.5 (High), EPSS 0.00162
- CVE-2025-9086 (curl) - CVSS 7.5 (High), EPSS 0.00035
- And 15 more across 2 packages.

5. Risk Distribution
- Severity counts:
  - Critical: 3
  - High: 23
  - Medium: 32
  - Low: 3
  - None: 1
- Top affected packages:
  1. python@3.11.4 (40 CVEs)
  2. openssl@3.0.16 (12 CVEs)
  3. curl@8.14.1 (10 CVEs)

6. CRA Compliance Actions
- Immediate: Patch CRITICAL CVEs with PoC, e.g., CVE-2025-4517 (python 3.11.x < 3.11.5), CVE-2025-15467 (openssl 3.0.16)
- Urgent: Patch exploited HIGH CVEs with PoC, e.g., CVE-2023-36632, CVE-2025-4138, CVE-2025-4330 (python), CVE-2025-9086 (curl)
- Planned: Address remaining HIGH severity CVEs without PoC, e.g., CVE-2024-8088, CVE-2024-4032, CVE-2024-9287 (python)
- Hygiene: Maintain SBOM accuracy and update per CRA Article 10(6)
- Vulnerability handling per CRA Article 11: Monitor for new exploits, timely patching, and reporting as required.

Summary:
- No mandatory CRA Article 14 notifications required.
- Multiple critical and high vulnerabilities with PoC exist, especially in python and openssl packages.
- Prioritize patching critical and exploited high vulnerabilities immediately.
- Maintain ongoing vulnerability management and SBOM updates per CRA compliance.