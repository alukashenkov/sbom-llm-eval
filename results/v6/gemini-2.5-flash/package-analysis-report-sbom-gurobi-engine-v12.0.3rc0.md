## 1. SBOM Overview
This SBOM, generated on 2025-07-11T08:53:07.000Z, is for `sbom-gurobi-engine-v12.0.3rc0` in SPDX format.
- Total packages: 12
- Affected packages: 3
- Unique CVEs: 62 (3 Critical, 23 High, 32 Medium, 3 Low, 1 None)

## 2. CRA Mandatory Reporting (Article 14)
No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
- CVE-2007-4559 (python): CVSS 9.8, EPSS 0.90582 (githubexploit: 1)
- CVE-2025-4517 (python): CVSS 9.4, EPSS 0.00071 (githubexploit: 11)
- CVE-2025-15467 (https://openssl.org|openssl): CVSS 9.8, EPSS 0.00672 (githubexploit: 2, packetstorm: 2)
- CVE-2024-6232 (python): CVSS 7.5, EPSS 0.02874 (githubexploit: 1)
- CVE-2025-4138 (python): CVSS 7.5, EPSS 0.00066 (githubexploit: 7, packetstorm: 1)
- 24 additional CVEs have PoC evidence.

## 4. Critical & High Findings
- CVE-2023-41105 (python): CVSS 7.5, EPSS 0.0037
- CVE-2023-36632 (python): CVSS 7.5, EPSS 0.00112
- CVE-2025-4330 (python): CVSS 7.5, EPSS 0.00253
- CVE-2025-4435 (python): CVSS 7.5, EPSS 0.00123
- CVE-2025-8194 (python): CVSS 7.5, EPSS 0.00162
- CVE-2024-8088 (python): CVSS 8.7, EPSS 0.00154
- CVE-2024-4032 (python): CVSS 7.5, EPSS 0.01127
- CVE-2024-7592 (python): CVSS 7.5, EPSS 0.00796
- and 15 more across 3 packages.

## 5. Risk Distribution
- CRITICAL: 3
- HIGH: 23
- MEDIUM: 32
- LOW: 3
- NONE: 1
- Top 3 affected packages:
    - python@3.11.4: 40 unique CVEs
    - https://openssl.org|openssl@3.0.16: 12 unique CVEs
    - https://curl.se|curl@8.14.1: 10 unique CVEs

## 6. CRA Compliance Actions
1. **Immediate Action (CRA Article 11(1))**: Patch `python` to address CVE-2007-4559 (CVSS 9.8) due to its high EPSS score (0.90582) and `CVE-2025-4517` (CVSS 9.4) due to arbitrary write vulnerability.
2. **Urgent Action (CRA Article 10(1), 11(1))**: Update `https://openssl.org|openssl` to address CVE-2025-15467 (CVSS 9.8) to prevent stack buffer overflow.
3. **Planned Action (CRA Article 10(1))**: Address all remaining HIGH severity CVEs in `python`, `https://openssl.org|openssl`, and `https://curl.se|curl` to mitigate potential risks.
4. **Hygiene (CRA Article 10(6))**: Implement regular security updates for all software components to ensure ongoing vulnerability management.
5. **Documentation (CRA Article 10(1))**: Maintain detailed records of all identified vulnerabilities and the remediation actions taken.