## Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0

### 1. SBOM Overview
This SPDX-formatted SBOM for `sbom-gurobi-engine-v12.0.3rc0`, scanned on 2025-07-11, identifies 12 total packages, with 3 affected by vulnerabilities. A total of 39 unique CVEs were found, comprising 2 Critical, 19 High, 17 Medium, and 1 Low severity vulnerabilities.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following 5 most critical CVEs have known exploit evidence:
- CVE-2007-4559 (CRITICAL, CVSS: 9.8, EPSS: 0.90582) in python@3.11.4
- CVE-2025-15467 (CRITICAL, CVSS: 9.8, EPSS: 0.00672) in https://openssl.org|openssl@3.0.16
- CVE-2025-4517 (CRITICAL, CVSS: 9.4, EPSS: 0.00071) in python@3.11.4
- CVE-2024-8088 (HIGH, CVSS: 8.7, EPSS: 0.00154) in python@3.11.4
- CVE-2024-9287 (HIGH, CVSS: 7.8, EPSS: 0.00062) in python@3.11.4
11 additional CVEs have exploit evidence.

### 4. Critical & High Findings
- CVE-2023-41105 (HIGH, CVSS: 7.5, EPSS: 0.0037) in python@3.11.4
- CVE-2023-36632 (HIGH, CVSS: 7.5, EPSS: 0.00112) in python@3.11.4
- CVE-2025-4138 (HIGH, CVSS: 7.5, EPSS: 0.00066) in python@3.11.4
- CVE-2025-4330 (HIGH, CVSS: 7.5, EPSS: 0.00253) in python@3.11.4
- CVE-2025-4435 (HIGH, CVSS: 7.5, EPSS: 0.00123) in python@3.11.4
- CVE-2025-8194 (HIGH, CVSS: 7.5, EPSS: 0.00162) in python@3.11.4
- CVE-2024-6232 (HIGH, CVSS: 7.5, EPSS: 0.02874) in python@3.11.4
- CVE-2024-7592 (HIGH, CVSS: 7.5, EPSS: 0.00796) in python@3.11.4
and 8 more HIGH findings across 3 packages.

### 5. Risk Distribution
- **CRITICAL:** 2 unique CVEs
- **HIGH:** 19 unique CVEs
- **MEDIUM:** 17 unique CVEs
- **LOW:** 1 unique CVEs
- **NONE:** 0 unique CVEs

Top 3 most-affected packages:
1. `python` (31 advisories)
2. `https://openssl.org|openssl` (12 advisories)
3. `https://curl.se|curl` (10 advisories)

### 6. CRA Compliance Actions
1. **Immediate Action:** Upgrade `python` to a version that remediates CVE-2007-4559 (CRITICAL, Directory Traversal) and CVE-2025-4517 (CRITICAL, Arbitrary Writes).
2. **Urgent Action:** Upgrade `https://openssl.org|openssl` to a version that remediates CVE-2025-15467 (CRITICAL, Stack-based Buffer Overflow).
3. **Urgent Action:** Upgrade `python` to a version that remediates CVE-2024-8088 (HIGH, Infinite Loop) and CVE-2024-9287 (HIGH, Command Injection).
4. **Planned Action:** Review and remediate all remaining High severity vulnerabilities in `python`, `https://openssl.org|openssl`, and `https://curl.se|curl`.
5. **SBOM Hygiene:** Implement automated vulnerability scanning and dependency management to maintain up-to-date SBOMs and proactively address new vulnerabilities.