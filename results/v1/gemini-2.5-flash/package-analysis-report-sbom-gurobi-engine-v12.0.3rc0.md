## Vulnerability Summary for `sbom-gurobi-engine-v12.0.3rc0`

**SBOM Overview**

This SBOM, `sbom-gurobi-engine-v12.0.3rc0`, was created on 2025-07-11T08:53:07.000Z. It lists 12 total packages, with 3 packages identified as affected by vulnerabilities.

**Vulnerability Counts by Severity:**

*   **CRITICAL:** 2
*   **HIGH:** 23
*   **MEDIUM:** 26
*   **LOW:** 3
*   **NONE:** 1

**CRA Mandatory Reporting Triggers (Article 14)**

No CRA mandatory reporting triggers identified.

**Exploit Availability Assessment**

*   **Public PoC available:**
    *   CVE-2025-4517 (CRITICAL) in `python@3.11.4` (11 GitHub exploits)
    *   CVE-2025-4138 (HIGH) in `python@3.11.4` (7 GitHub exploits)
    *   CVE-2025-4330 (HIGH) in `python@3.11.4` (2 GitHub exploits)
    *   CVE-2025-15467 (CRITICAL) in `https://openssl.org|openssl@3.0.16` (2 GitHub exploits)
    *   CVE-2024-12718 (MEDIUM) in `python@3.11.4` (1 GitHub exploit)
    *   CVE-2025-4435 (HIGH) in `python@3.11.4` (1 GitHub exploit)
    *   CVE-2007-4559 (CRITICAL) in `python@3.11.4` (1 GitHub exploit)
    *   CVE-2024-6232 (HIGH) in `python@3.11.4` (1 GitHub exploit)
*   **Exploit framework integration:**
    *   CVE-2025-4138 (HIGH) in `python@3.11.4` (1 Packetstorm exploit)
    *   CVE-2025-15467 (CRITICAL) in `https://openssl.org|openssl@3.0.16` (2 Packetstorm exploits)
    *   CVE-2025-68160 (MEDIUM) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2025-69418 (MEDIUM) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2025-69419 (HIGH) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2025-69420 (HIGH) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2025-69421 (HIGH) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2026-22795 (MEDIUM) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
    *   CVE-2026-22796 (MEDIUM) in `https://openssl.org|openssl@3.0.16` (1 Packetstorm exploit)
*   **Bug bounty disclosed:**
    *   CVE-2025-14524 (MEDIUM) in `https://curl.se|curl@8.14.1` (2 HackerOne reports)
    *   CVE-2025-15079 (MEDIUM) in `https://curl.se|curl@8.14.1` (1 HackerOne report)
    *   CVE-2025-15224 (LOW) in `https://curl.se|curl@8.14.1` (1 HackerOne report)
    *   CVE-2025-10966 (MEDIUM) in `https://curl.se|curl@8.14.1` (1 HackerOne report)
    *   CVE-2025-9086 (HIGH) in `https://curl.se|curl@8.14.1` (1 HackerOne report)
    *   CVE-2025-10148 (MEDIUM) in `https://curl.se|curl@8.14.1` (1 HackerOne report)

**Critical & High Findings**

*   CVE-2023-41105 python@3.11.4 - CVSS:7.5 EPSS:0.0037 - Fix available.
*   CVE-2023-36632 python@3.11.4 - CVSS:7.5 EPSS:0.00112 - Fix available.
*   CVE-2024-4032 python@3.11.4 - CVSS:7.5 EPSS:0.01127 - Fix available.
*   CVE-2024-8088 python@3.11.4 - CVSS:8.7 EPSS:0.00154 - Fix available.
*   CVE-2024-0397 python@3.11.4 - CVSS:7.4 EPSS:0.00384 - Fix available.
*   CVE-2025-13836 python@3.11.4 - CVSS:7.5 EPSS:0.00152 - Fix available.
*   CVE-2023-6597 python@3.11.4 - CVSS:7.8 EPSS:0.00071 - Fix available.
*   CVE-2024-9287 python@3.11.4 - CVSS:7.8 EPSS:0.00062 - Fix available.
*   CVE-2024-4030 python@3.11.4 - CVSS:7.1 EPSS:0.00025 - Fix available.
*   CVE-2025-9230 https://openssl.org|openssl@3.0.16 - CVSS:7.5 EPSS:0.00031 - Fix available.

**Risk Distribution**

*   **CRITICAL:** 2 (3.7%)
*   **HIGH:** 23 (42.6%)
*   **MEDIUM:** 26 (48.1%)
*   **LOW:** 3 (5.6%)
*   **NONE:** 1 (1.9%)

**Top 3 Most-Affected Packages:**

1.  `python@3.11.4`: 47 advisories (1 CRITICAL, 20 HIGH, 23 MEDIUM, 3 LOW)
2.  `https://openssl.org|openssl@3.0.16`: 19 advisories (1 CRITICAL, 6 HIGH, 12 MEDIUM)
3.  `https://curl.se|curl@8.14.1`: 12 advisories (0 CRITICAL, 2 HIGH, 9 MEDIUM, 1 LOW)

**Exploitation Landscape Stats:**

*   **Total CVEs with PoC:** 12
*   **Total CVEs with Exploit Framework Integration:** 9
*   **Total CVEs with Bug Bounty Disclosures:** 6

**CRA Compliance Actions**

1.  **Immediate Action: Address Critical Vulnerabilities with Public Exploits:** Prioritize patching `CVE-2025-4517` in `python@3.11.4` and `CVE-2025-15467` in `https://openssl.org|openssl@3.0.16` due to their critical severity and confirmed public exploit availability. This is crucial for maintaining product security and avoiding potential CRA Article 14 reporting obligations if these are actively exploited.
2.  **Urgent Action: Patch High Vulnerabilities with Public Exploits:** Address `CVE-2025-4138`, `CVE-2025-4330`, `CVE-2025-4435`, `CVE-2007-4559`, and `CVE-2024-6232` in `python@3.11.4` immediately. The presence of public exploits significantly increases the risk of exploitation.
3.  **Planned Action: Update `python` to a patched version:** The `python@3.11.4` package has a high number of vulnerabilities across all severities. Plan an upgrade to a version that addresses the identified issues, especially those with available fixes.
4.  **Planned Action: Update `openssl` to a patched version:** The `https://openssl.org|openssl@3.0.16` package contains critical and high vulnerabilities with exploit framework integration. Schedule an update to a secure version to mitigate these risks.
5.  **SBOM Hygiene: Enhance Exploit Source Monitoring:** Implement continuous monitoring for new exploit availability, particularly for vulnerabilities in core components like `python`, `openssl`, and `curl`, to proactively identify and respond to emerging threats as per CRA Article 11 requirements.