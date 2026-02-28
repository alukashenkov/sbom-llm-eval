## 1. SBOM Overview
- Product: sbom-grbrsm_ui-v12.0.3rc0  
- Format: SPDX  
- Scan date: 2025-07-11  
- Total packages: 338 / Affected packages: 7  
- Unique CVEs: 9  
- CRA tier distribution (Art. 3(40/41/42)):  
  • EXPLOITABLE: 7  
  • VULNERABILITY: 2  
  • ACTIVELY_EXPLOITED: 0  

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
- CVE-2025-7783 (axios@1.10.0, form-data@4.0.3)  
  • CVSS 9.4 (CVSS:4.0/AV:N/AC:H/AT:N/UI:N/VC:H/SC:H/VI:H)  
  • EPSS 0.00177 (not stale)  
  • Days public: 222  
  • Fix hint: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
- Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h incident notification → ≤1 month final report.

## 3. Art. 3(41) Exploitability Assessment
- PoC sources: 2 GitHub exploits reported.  
- EXPLOITABLE CVEs: 7 total.  
- Top 5 EXPLOITABLE CVEs by CVSS score:  
  1. CVE-2025-7783 (axios@1.10.0, form-data@4.0.3)  
     • CVSS 9.4, EPSS 0.00177 (not stale), 222 days public  
     • Fix: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
  2. CVE-2026-25639 (axios@1.10.0)  
     • CVSS 8.7, EPSS 0.00033 (not stale), 19 days public  
     • Fix: Prototype pollution in axios via mergeConfig allows __proto__ to crash or cause code execution.  
  3. CVE-2026-26996 (minimatch@7.4.6)  
     • CVSS 8.7, EPSS 0.0004 (not stale), 10 days public  
     • Fix: Minimatch AST has a regular expression denial of service vulnerability caused by catastrophic backtracking with many asterisks.  
  4. CVE-2025-13465 (lodash@4.17.21)  
     • CVSS 7.9, EPSS 0.00025 (not stale), 38 days public  
     • Fix: Lodash prototype pollution in unset and omit affects versions 4.0.0 through 4.17.22; patch is 4.17.23.  
  5. CVE-2025-54371 (axios@1.10.0)  
     • CVSS 7.5, EPSS 0.00177 (not stale), 220 days public  
     • Fix: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
- EPSS stale count: 0 — exploitability confidence not reduced.

## 4. Critical & High Findings (Annex I Part II §2 — Remediate Without Delay)
- CVE-2025-54371 (axios@1.10.0)  
  • CVSS 7.5, AV:N/AC:L/PR:N/UI:N, EPSS 0.00177, EXPLOITABLE  
  • Fix: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
- CVE-2025-58754 (axios@1.10.0)  
  • CVSS 7.5, AV:N/AC:L/PR:N/UI:N, EPSS 0.00102, EXPLOITABLE  
  • Fix: Axios on Node decodes data: URIs into memory, ignoring size limits, enabling DoS with large payloads.  
- CVE-2025-13465 (lodash@4.17.21)  
  • CVSS 7.9, AV:N/AC:L/PR:N/UI:N, EPSS 0.00025, EXPLOITABLE  
  • Fix: Lodash prototype pollution in unset and omit affects versions 4.0.0 through 4.17.22; patch is 4.17.23.  
- CVE-2026-25639 (axios@1.10.0)  
  • CVSS 8.7, AV:N/AC:L/PR:N/UI:N, EPSS 0.00033, EXPLOITABLE  
  • Fix: Prototype pollution in axios via mergeConfig allows __proto__ to crash or cause code execution.  
- CVE-2026-26996 (minimatch@7.4.6)  
  • CVSS 8.7, AV:N/AC:L/PR:N/UI:N, EPSS 0.0004, EXPLOITABLE  
  • Fix: Minimatch AST has a regular expression denial of service vulnerability caused by catastrophic backtracking with many asterisks.  
- And 1 more HIGH CVE across 1 package.

## 5. Risk Distribution & Age Risk
- Severity distribution: HIGH 5, CRITICAL 1, MEDIUM 3  
- Top affected packages:  
  1. axios@1.10.0 (4 CVEs)  
  2. js-yaml@4.1.0 (1 CVE)  
  3. lodash@4.17.21 (1 CVE)  
- Top 3 longest-unpatched CRITICAL/HIGH CVEs:  
  1. CVE-2025-7783 (CRITICAL, 222 days)  
     • Fix: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
  2. CVE-2025-54371 (HIGH, 220 days)  
     • Fix: Critical vulnerability in axios form-data allowing predictable boundary values for attacks.  
  3. CVE-2025-58754 (HIGH, 170 days)  
     • Fix: Axios on Node decodes data: URIs into memory, ignoring size limits, enabling DoS with large payloads.

## 6. CRA Defensible-Practice Actions
1. **Immediate — Art. 14 + Annex I Part II §2:**  
   - Patch CVE-2025-7783 in axios@1.10.0 and form-data@4.0.3 per fix hint. Submit Art. 14 Track 2 notifications.  
2. **Urgent — Annex I Part II §2:**  
   - Patch EXPLOITABLE HIGH CVEs in axios (CVE-2025-54371, CVE-2025-58754, CVE-2026-25639), lodash (CVE-2025-13465), minimatch (CVE-2026-26996) using provided fix hints.  
3. **Planned — Annex I Part II §2:**  
   - Remediate remaining MEDIUM severity vulnerabilities in js-yaml@4.1.0 and @babel/runtime@7.0.0, prioritizing by age.  
4. **SBOM update — Annex I Part II §1:**  
   - Update SBOM to reflect current patched component versions in SPDX format.  
5. **Public advisory — Annex I Part II §4:**  
   - Publish advisories listing CVEs, severity, vectors, affected versions, and remediation steps once patches are available.  
6. **CVD hygiene — Annex I Part II §5–6:**  
   - Verify coordinated vulnerability disclosure policy and security contact details are current and publicly accessible.