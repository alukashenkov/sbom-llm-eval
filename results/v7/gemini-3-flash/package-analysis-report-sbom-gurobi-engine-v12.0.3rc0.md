## 1. SBOM Overview
*   **Product:** sbom-gurobi-engine-v12.0.3rc0
*   **Format:** SPDX | **Scan Date:** 2025-07-11
*   **Packages:** 12 total / 3 affected
*   **Unique CVEs:** 62
*   **CRA Tier Distribution (Art. 3):** 35 EXPLOITABLE / 27 VULNERABILITY / 0 ACTIVELY_EXPLOITED.

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
*   No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
*   **CVE-2007-4559** | python@3.11.4 | CVSS: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Fix: Python directory traversal vulnerability in tarfile modul
*   **CVE-2025-15467** | openssl@3.0.16 | CVSS: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Fix: upgrade OpenSSL 3.0.19 or newer.
*   **CVE-2025-4517** | python@3.11.4 | CVSS: 9.4 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L) | Fix: BELL-CVE-2025-4517 bulletin lacks description
*   **State:** ≤24h early warning → ≤72h incident notification → ≤1 month final report.

## 3. Art. 3(41) Exploitability Assessment
*   **Total PoC/Exploits:** 24 (8 GitHub, 10 Packetstorm, 6 HackerOne).
*   **Exploitable Count:** 35 CVEs.
*   **Top 5 EXPLOITABLE CVEs:**
    1.  **CVE-2007-4559** | python@3.11.4 | CVSS: 9.8 | EPSS: 0.90582 (99th%) | 863 days public | Fix: Python directory traversal vulnerability in tarfile modul
    2.  **CVE-2025-15467** | openssl@3.0.16 | CVSS: 9.8 | EPSS: 0.00672 (70th%) | 32 days public | Fix: upgrade OpenSSL 3.0.19 or newer.
    3.  **CVE-2025-4517** | python@3.11.4 | CVSS: 9.4 | EPSS: 0.00071 (21st%) | 268 days public | Fix: BELL-CVE-2025-4517 bulletin lacks description
    4.  **CVE-2024-8088** | python@3.11.4 | CVSS: 8.7 | EPSS: 0.00154 (36th%) | 320 days public | Fix: High severity vulnerability in CPython "zipfile" modul
    5.  **CVE-2024-9287** | python@3.11.4 | CVSS: 7.8 | EPSS: 0.00062 (19th%) | 494 days public | Fix: command injection in virtual environment activation script

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2024-6232** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.02874 | Tier: EXPLOITABLE | Fix: CPython vulnerability in tarfile header parsin
*   **CVE-2024-7592** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.00796 | Tier: EXPLOITABLE | Fix: inefficient parsing of cookies with backslashes
*   **CVE-2023-5363** | openssl@3.0.16 | CVSS: 7.5 | AV: Network | EPSS: 0.04390 | Tier: EXPLOITABLE | Fix: altering key and initialization vector lengths
*   **CVE-2025-9086** | curl@8.14.1 | CVSS: 7.5 | AV: Network | EPSS: 0.00035 | Tier: EXPLOITABLE | Fix: Out-of-bounds read in cookie path handling
*   **CVE-2025-13836** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.00152 | Tier: EXPLOITABLE | Fix: Default Content-Length reads enable memory exhaustion
*   **CVE-2024-4032** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.01127 | Tier: EXPLOITABLE | Fix: ipaddress module incorrect info
*   **CVE-2023-41105** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.00370 | Tier: EXPLOITABLE | Fix: _Py_normpath function path truncation
*   **CVE-2023-36632** | python@3.11.4 | CVSS: 7.5 | AV: Network | EPSS: 0.00112 | Tier: EXPLOITABLE | Fix: Legacy email.utils.parseaddr RecursionError
*   *And 18 more across 3 packages.*

## 5. Risk Distribution & Age Risk
*   **Distribution:** 3 CRITICAL, 23 HIGH, 32 MEDIUM, 3 LOW.
*   **Top Affected:** python@3.11.4 (40), openssl@3.0.16 (12), curl@8.14.1 (10).
*   **Oldest Unpatched (Annex I Part II §2 Violation Risk):**
    1.  **CVE-2023-36632** | 979 days | Fix: Use email.pa
    2.  **CVE-2023-41105** | 920 days | Fix: python vulnerability due to _Py_normpath functio
    3.  **CVE-2007-4559** | 863 days | Fix: Python directory traversal vulnerability in tarfile modul

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2:** Submit Track 2 notifications for CVE-2007-4559 and CVE-2025-15467 within 24h.
2.  **Urgent — Annex I Part II §2:** Patch OpenSSL to v3.0.19+ and Python to v3.11.5+ to remediate CRITICAL/HIGH exploitable flaws.
3.  **Planned — Annex I Part II §2:** Remediate 900+ day old vulnerabilities in Python email and path modules to maintain "security by default."
4.  **SBOM update — Annex I Part II §1:** Regenerate SPDX SBOM following package upgrades to reflect current compliance state.
5.  **Public advisory — Annex I Part II §4:** Publish security advisory for CVE-2025-15467 and CVE-2025-4517 detailing remediation steps.
6.  **CVD hygiene — Annex I Part II §5–6:** Ensure security contact for Gurobi Engine is accessible for coordinated disclosure.