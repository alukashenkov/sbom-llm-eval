1. SBOM Overview  
- Product: openclaw  
- Format: SPDX  
- Scan date: 2026-02-20  
- Total packages: 1112  
- Affected packages: 21  
- Unique CVEs: 96  
- CRA tier distribution (Art. 3):  
  • ACTIVELY_EXPLOITED: 0  
  • EXPLOITABLE: 41  
  • VULNERABILITY: 55  

2. CRA Art. 14 — Mandatory Reporting  

Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

Track 2 — Severe Incidents (Art. 14(3)–(5)):  
- OSV:GHSA-4RJ2-GPMH-QQ5X (openclaw@2026.1.10)  
  • CVSS 9.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L)  
  • Fix: fixed in 2026.2.2 (voice-call extension bypasses inbound allowlist)  
- OSV:GHSA-RV39-79C4-7459 (openclaw@2026.1.10)  
  • CVSS 9.3 (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N)  
  • Fix: gateway connect skips identity checks; no validated auth.token  
- CVE-2023-34104 (fast-xml-parser@4.5.3)  
  • CVSS 9.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N)  
  • Fix: DOCTYPE entity regex injection enabling XSS  
- CVE-2026-25896 (fast-xml-parser@4.5.3)  
  • CVSS 9.3 (same vector as above)  
  • Fix: same as above  
- OSV:GHSA-FHVM-J76F-QMJV (openclaw@2026.1.10)  
  • CVSS 9.1 (CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N)  
  • Fix: accepts unauthenticated Telegram webhooks without secret  
- Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

3. Art. 3(41) Exploitability Assessment  
- PoC sources: 6 GitHub exploits reported  
- EXPLOITABLE CVEs: 41 total  
- Top 5 EXPLOITABLE CVEs by CVSS score:  
  • OSV:GHSA-4RJ2-GPMH-QQ5X (openclaw@2026.1.10) - 9.4, no EPSS, 11 days public, fix in 2026.2.2  
  • OSV:GHSA-RV39-79C4-7459 (openclaw@2026.1.10) - 9.3, no EPSS, 11 days public, fix available  
  • CVE-2023-34104 (fast-xml-parser@4.5.3) - 9.3, EPSS 0.00273 (50.4 percentile), 8 days public, fix available  
  • CVE-2026-25896 (fast-xml-parser@4.5.3) - 9.3, EPSS 0.00273 (50.4 percentile), 8 days public, fix available  
  • OSV:GHSA-FHVM-J76F-QMJV (openclaw@2026.1.10) - 9.1, no EPSS, 11 days public, fix available  
- EPSS stale count: 0 — exploitability confidence is high.  

4. Critical & High Findings (Annex I Part II §2 — Remediate Without Delay)  
- Remaining CRITICAL/HIGH CVEs not in Art. 14:  
  • OSV:GHSA-RV39-79C4-7459 openclaw@2026.1.10, CVSS 9.3, AV:N (network), EPSS N/A, EXPLOITABLE, fix: skip identity checks on auth.token presence  
  • CVE-2026-24763 clawdbot@2026.1.10, CVSS 8.8, AV:N, fix: authenticated command injection via PATH env  
  • CVE-2026-25253 openclaw@2026.1.10, CVSS 8.8, AV:N, fix: exfiltration of gateway token via unvalidated gatewayUrl  
  • OSV:GHSA-R5FQ-947M-XM57 openclaw@2026.2.13, CVSS 8.8, AV:N, fix: path traversal in apply_patch writes outside workspace  
  • OSV:GHSA-X22M-J5QQ-J49M openclaw@2026.2.14, CVSS 8.6, AV:N, fix: Feishu extension SSRF paths patched  
  • OSV:GHSA-M7X8-2W3W-PR42 openclaw@source, CVSS 8.6, AV:N, fix: command injection in maintainer clawtributors updater  
  • CVE-2025-66031 node-forge@1.3.1, CVSS 8.7, AV:N, fix: unbounded recursion in ASN.1 parser causes DoS  
  • CVE-2025-12816 node-forge@1.3.1, CVSS 8.7, AV:N, fix: ASN.1 validation desynchronization bypass  
- And 44 more across 15 packages.  

5. Risk Distribution & Age Risk  
- Severity distribution: HIGH 52, MEDIUM 33, CRITICAL 5, LOW 6  
- Top affected packages:  
  • openclaw@2026.1.10: 67 CVEs  
  • clawdbot@2026.1.10: 11 CVEs  
  • hono@4.11.3: 7 CVEs  
- Top 3 oldest CRITICAL/HIGH CVEs by days public:  
  • CVE-2026-2327 (markdown-it@14.1.0) - 238 days, CVSS 7.5, fix: upgrade to 14.1.1+  
  • CVE-2025-66031 (node-forge@1.3.1) - 94 days, CVSS 8.7, fix: patch ASN.1 recursion  
  • CVE-2025-12816 (node-forge@1.3.1) - 94 days, CVSS 8.7, fix: desync ASN.1 validation bypass  

6. CRA Defensible-Practice Actions  
- Immediate — Art. 14 + Annex I Part II §2:  
  • Patch all Track 1 & Track 2 CVEs immediately; submit Art. 14 notifications for OSV:GHSA-4RJ2-GPMH-QQ5X, OSV:GHSA-RV39-79C4-7459, CVE-2023-34104, CVE-2026-25896, OSV:GHSA-FHVM-J76F-QMJV. Use fixes in 2026.2.2+ and fast-xml-parser 5.3.4+.  
- Urgent — Annex I Part II §2:  
  • Patch EXPLOITABLE CRITICAL/HIGH CVEs including openclaw gateway identity bypass, clawdbot Docker PATH injection, openclaw token exfiltration, apply_patch path traversal, Feishu SSRF, maintainer script command injection, node-forge ASN.1 flaws.  
- Planned — Annex I Part II §2:  
  • Remediate remaining HIGH/MEDIUM CVEs prioritizing oldest first (e.g., markdown-it ReDoS, qs DoS, Hono JWT forgery).  
- SBOM update — Annex I Part II §1:  
  • Update SBOM to reflect current component versions including patched releases (e.g., openclaw 2026.2.14+, fast-xml-parser 5.3.5+).  
- Public advisory — Annex I Part II §4:  
  • Publish advisories with CVE IDs, severity, vectors, affected versions, and remediation steps once patches are available.  
- CVD hygiene — Annex I Part II §5–6:  
  • Verify coordinated vulnerability disclosure policy and security contact address are published and current.