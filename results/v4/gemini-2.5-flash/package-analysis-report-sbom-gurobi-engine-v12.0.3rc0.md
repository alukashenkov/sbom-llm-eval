## Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0

### 1. SBOM Overview
This SBOM, generated in SPDX format on 2025-07-11, details the components of the gurobi-engine-v12.0.3rc0 product. Out of 12 total packages, 3 are affected by vulnerabilities. There are 2 Critical, 15 High, 18 Medium, 2 Low, and 1 None unique CVEs identified.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of exploit availability:
- CVE-2007-4559: python@3.11.4 — CVSS 9.8 — EPSS 0.90582 — Critical directory traversal.
- CVE-2025-15467: https://openssl.org|openssl@3.0.16 — CVSS 9.8 — EPSS 0.00672 — Critical stack-based buffer overflow.
- CVE-2025-4517: python@3.11.4 — CVSS 9.4 — EPSS 0.00071 — Critical arbitrary filesystem writes.
- CVE-2024-6232: python@3.11.4 — CVSS 7.5 — EPSS 0.02874 — High regular-expression DoS.
- CVE-2025-4138: python@3.11.4 — CVSS 7.5 — EPSS 0.00066 — High extraction filter bypass for symlinks.
10 additional CVEs have exploit evidence.

### 4. Critical & High Findings
- CVE-2024-9287: python@3.11.4 — CVSS 7.8 — EPSS 0.00062
- CVE-2023-6597: python@3.11.4 — CVSS 7.8 — EPSS 0.00071
- CVE-2023-41105: python@3.11.4 — CVSS 7.5 — EPSS 0.0037
- CVE-2023-36632: python@3.11.4 — CVSS 7.5 — EPSS 0.00112
- CVE-2024-4032: python@3.11.4 — CVSS 7.5 — EPSS 0.01127
- CVE-2025-13836: python@3.11.4 — CVSS 7.5 — EPSS 0.00152
- CVE-2025-9230: https://openssl.org|openssl@3.0.16 — CVSS 7.5 — EPSS 0.00031
- CVE-2025-69420: https://openssl.org|openssl@3.0.16 — CVSS 7.5 — EPSS 0.0007
and 7 more HIGH findings across 2 packages.

### 5. Risk Distribution
- **Critical:** 2
- **High:** 15
- **Medium:** 18
- **Low:** 2
- **None:** 1

Top 3 most-affected packages:
1. python: 36 advisories
2. https://openssl.org|openssl: 18 advisories
3. https://curl.se|curl: 13 advisories

### 6. CRA Compliance Actions
1. **Immediate Action (Patch Critical Vulnerabilities):** Upgrade `python` to a version that remediates CVE-2007-4559 and CVE-2025-4517. Upgrade `https://openssl.org|openssl` to a version that remediates CVE-2025-15467. These are critical and have exploit evidence.
2. **Urgent Action (Address High Severity with Exploit Evidence):** Upgrade `python` to a version that remediates CVE-2024-6232 and CVE-2025-4138.
3. **Planned Action (Address Remaining High Vulnerabilities):** Prioritize upgrades for `python` to address CVE-2024-9287, CVE-2023-6597, CVE-2023-41105, CVE-2023-36632, CVE-2024-4032, CVE-2025-13836. Similarly, upgrade `https://openssl.org|openssl` to address CVE-2025-9230 and CVE-2025-69420.
4. **SBOM Hygiene:** Ensure all future SBOMs include `cisa_kev` and `wildExploited` fields for accurate CRA reporting.