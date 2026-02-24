## 1. SBOM Overview

This SBOM for `sbom-gurobi-engine-v12.0.3rc0`, generated on 2025-07-11T08:53:07.000Z, details the software components within the product. Out of 12 total packages, 3 are affected by vulnerabilities. The scan identified a total of 62 unique CVEs, comprising 3 Critical, 23 High, 32 Medium, 3 Low, and 1 None severity vulnerabilities.

## 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment

A total of 24 CVEs have known exploit evidence from various sources (8 GitHub exploits, 10 PacketStorm exploits, 6 HackerOne reports). The top 5 CVEs with Proof-of-Concept (PoC) by severity are:

*   **CVE-2007-4559** (CRITICAL, CVSS: 9.8, EPSS: 0.90582) affecting `python`
*   **CVE-2025-15467** (CRITICAL, CVSS: 9.8, EPSS: 0.00672) affecting `https://openssl.org|openssl`
*   **CVE-2025-4517** (CRITICAL, CVSS: 9.4, EPSS: 0.00071) affecting `python`
*   **CVE-2024-6232** (HIGH, CVSS: 7.5, EPSS: 0.02874) affecting `python`
*   **CVE-2024-4032** (HIGH, CVSS: 7.5, EPSS: 0.01127) affecting `python`

19 additional CVEs have exploit evidence.

## 4. Critical & High Findings

The following Critical and High severity CVEs, not covered above, require immediate attention:

*   **CVE-2023-41105** (HIGH, CVSS: 7.5, EPSS: 0.0037) affecting `python`
*   **CVE-2023-36632** (HIGH, CVSS: 7.5, EPSS: 0.00112) affecting `python`
*   **CVE-2025-4138** (HIGH, CVSS: 7.5, EPSS: 0.00066) affecting `python`
*   **CVE-2025-4330** (HIGH, CVSS: 7.5, EPSS: 0.00253) affecting `python`
*   **CVE-2025-4435** (HIGH, CVSS: 7.5, EPSS: 0.00123) affecting `python`
*   **CVE-2025-8194** (HIGH, CVSS: 7.5, EPSS: 0.00162) affecting `python`
*   **CVE-2024-8088** (HIGH, CVSS: 8.7, EPSS: 0.00154) affecting `python`
*   **CVE-2025-13836** (HIGH, CVSS: 7.5, EPSS: 0.00152) affecting `python`

and 15 more HIGH findings across 3 packages.

## 5. Risk Distribution

The vulnerabilities are distributed as follows: 3 Critical, 23 High, 32 Medium, 3 Low, and 1 None. The packages most affected by unique CVEs are `python@3.11.4` (40 CVEs), `https://openssl.org|openssl@3.0.16` (12 CVEs), and `https://curl.se|curl@8.14.1` (10 CVEs).

## 6. CRA Compliance Actions

1.  **Immediate Action:** Address CVE-2007-4559 (CRITICAL, CVSS 9.8) in `python@3.11.4` due to its critical severity and confirmed exploit. Upgrade `python` to a patched version immediately.
2.  **Urgent Patching:** Prioritize patching `https://openssl.org|openssl@3.0.16` to mitigate CVE-2025-15467 (CRITICAL, CVSS 9.8) and `python@3.11.4` for CVE-2025-4517 (CRITICAL, CVSS 9.4), both having critical severity and exploit availability.
3.  **High Priority Remediation:** Address all remaining High severity CVEs in `python@3.11.4`, `https://openssl.org|openssl@3.0.16`, and `https://curl.se|curl@8.14.1` to reduce attack surface.
4.  **Regular Updates:** Implement a schedule for regular updates of `python`, `openssl`, and `curl` to ensure all known vulnerabilities are addressed promptly.
5.  **SBOM Hygiene:** Maintain accurate and up-to-date SBOMs for all software products to facilitate continuous vulnerability monitoring and compliance with CRA requirements.