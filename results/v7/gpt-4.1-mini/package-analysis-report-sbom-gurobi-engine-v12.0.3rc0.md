## 1. SBOM Overview
- Product: sbom-gurobi-engine-v12.0.3rc0, SPDX format, scanned 2025-07-11
- Total packages: 12; Affected packages: 3
- Unique CVEs: 62
- CRA Tier distribution (Art. 3(40/41/42)): EXPLOITABLE 35, VULNERABILITY 27
- Severity distribution: CRITICAL 3, HIGH 23, MEDIUM 32, LOW 3, NONE 1

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
- CVE-2007-4559 (python@3.11.4): CVSS 9.8, Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.90582, 863 days public, fix: "Python directory traversal vulnerability in tarfile modul"  
- CVE-2025-15467 (openssl@3.0.16): CVSS 9.8, Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00672, 32 days public, fix: "Stack based buffer overflow in OpenSSL when parsing AuthEnvelopedData; upgrade OpenSSL 3.0.19 or newer."  
- CVE-2025-4517 (python@3.11.4): CVSS 9.4, Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L, EPSS 0.00071, 268 days public, fix: "BELL-CVE-2025-4517 bulletin lacks description for software security vulnerability details"  
- Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h vulnerability notification → ≤1 month final report (Art. 14(3)–(5)).

## 3. Art. 3(41) Exploitability Assessment
- PoC sources: githubexploit 8, packetstorm 10, hackerone 6
- EXPLOITABLE CVEs: 35
- Top 5 EXPLOITABLE CVEs by CVSS score:
  1. CVE-2007-4559 (python@3.11.4): 9.8, EPSS 0.90582, 863 days public, fix: "Python directory traversal vulnerability in tarfile modul"
  2. CVE-2025-4517 (python@3.11.4): 9.4, EPSS 0.00071, 268 days public, fix: "BELL-CVE-2025-4517 bulletin lacks description for software security vulnerability details"
  3. CVE-2025-15467 (openssl@3.0.16): 9.8, EPSS 0.00672, 32 days public, fix: "Stack based buffer overflow in OpenSSL when parsing AuthEnvelopedData; upgrade OpenSSL 3.0.19 or newer."
  4. CVE-2024-8088 (python@3.11.4): 8.7, EPSS 0.00154, 320 days public, fix: "High severity vulnerability in CPython \"zipfile\" modul"
  5. CVE-2024-4032 (python@3.11.4): 7.5, EPSS 0.01127, 619 days public, fix: "The ipaddress module in CPython 3.12.4 had incorrect information about IPv4 and IPv6 addresses, impacting is_private and is_global properties"
- EPSS stale count: 0 — exploitability confidence not reduced.

## 4. Critical & High Findings (Annex I Part II §2 — Remediate Without Delay)
- CVE-2024-0397 (python@3.11.4): 7.4, CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:H, EPSS 0.00384, VULNERABILITY, fix: "A memory race condition in Python \"ssl\" module with \"cert_store_stats()\" and \"get_ca_certs()\" methods could be triggered during TLS handshake"
- CVE-2023-6597 (python@3.11.4): 7.8, CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N, EPSS 0.00071, VULNERABILITY, fix: "An issue found in CPython TemporaryDirectory affecting versions 3.12.1, 3.11.7, 3.10.13, 3.9.18, and 3.8.1"
- CVE-2023-41105 (python@3.11.4): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N, EPSS 0.0037, EXPLOITABLE, fix: "An issue in Python 3.11 through 3.11.4 truncates paths containing '\\0' bytes passed to os.path.normpath("
- CVE-2023-36632 (python@3.11.4): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H, EPSS 0.00112, EXPLOITABLE, fix: "Legacy Python email.utils.parseaddr function allows attackers to trigger a \"RecursionError\" via crafted input"
- CVE-2023-5363 (openssl@3.0.16): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N, EPSS 0.0439, EXPLOITABLE, fix: "openssl vulnerability allows altering key and initialization vector lengths after setup, causing truncation or overruns."
- CVE-2025-4330 (python@3.11.4): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N, EPSS 0.00298, EXPLOITABLE, fix: "Extraction filter bypass allows symlink targets outside directory for untrusted tar archives."
- CVE-2025-4435 (python@3.11.4): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N, EPSS 0.00123, EXPLOITABLE, fix: "TarFile extracts filtered members despite errorlevel=0, contrary to documented behavior."
- CVE-2025-4138 (python@3.11.4): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N, EPSS 0.00077, EXPLOITABLE, fix: "Vulnerability in tarfile module allows symlink creation outside extraction directory, affecting Python 3.12+."
- And 15 more across 2 packages.

## 5. Risk Distribution & Age Risk
- Severity counts: CRITICAL 3, HIGH 23, MEDIUM 32, LOW 3, NONE 1
- Top affected packages by unique CVEs: python@3.11.4 (40), openssl@3.0.16 (12), curl@8.14.1 (10)
- Top 3 longest-unpatched CRITICAL/HIGH CVEs by days public:
  1. CVE-2023-36632 (python@3.11.4): 979 days, fix: "Legacy Python email.utils.parseaddr function allows attackers to trigger \"RecursionError: maximum recursion depth exceeded while calling a Python obje"
  2. CVE-2023-41105 (python@3.11.4): 920 days, fix: "python vulnerability due to _Py_normpath functio"
  3. CVE-2007-4559 (python@3.11.4): 863 days, fix: "Python directory traversal vulnerability in tarfile modul"
- These represent potential Annex I Part II §2 "without delay" remediation signals.

## 6. CRA Defensible-Practice Actions
1. **Immediate — Art. 14 + Annex I Part II §2**:  
   - Patch and mitigate Track 2 CVEs: CVE-2007-4559, CVE-2025-15467, CVE-2025-4517. Use provided fix hints and upgrade OpenSSL to 3.0.19+ and Python tarfile module patches.
   - Submit Art. 14 notifications per CRA requirements.
2. **Urgent — Annex I Part II §2**:  
   - Patch EXPLOITABLE CRITICAL/HIGH CVEs in python@3.11.4 and openssl@3.0.16, including CVE-2023-41105, CVE-2023-36632, CVE-2023-6597, CVE-2023-5363, CVE-2025-4330, CVE-2025-4435, CVE-2025-4138.
   - Follow fix hints for upgrade paths and mitigations.
3. **Planned — Annex I Part II §2**:  
   - Remediate remaining HIGH and MEDIUM severity CVEs, prioritizing oldest first.
4. **SBOM update — Annex I Part II §1**:  
   - Update SBOM to reflect current component states, ensuring top-level dependencies are machine-readable (SPDX).
5. **Public advisory — Annex I Part II §4**:  
   - Publish advisories with CVE IDs, severity, vectors, affected versions, and remediation steps after patches are available.
6. **CVD hygiene — Annex I Part II §5–6**:  
   - Verify coordinated vulnerability disclosure policy and security contact info are published and current.