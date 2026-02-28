## 1. SBOM Overview
- Product: bkimminich/juice-shop (container image, CycloneDX format)
- Scan date: 2026-02-24
- Total packages: 998; Affected packages: 38
- Unique CVEs: 60
- CRA tiers (Art. 3): ACTIVELY_EXPLOITED: 0; EXPLOITABLE: 39; VULNERABILITY: 21

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
- CVE-2015-9235 (jsonwebtoken@0.1.0, 0.4.0): CVSS 9.8, CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fix: update jsonwebtoken >4.2.1  
- CVE-2023-32314 (vm2@3.9.17): CVSS 9.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fix: upgrade vm2 beyond 3.9.17  
- CVE-2023-37466, CVE-2023-37903 (vm2@3.9.17): CVSS 9.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fix: upgrade vm2 beyond 3.9.19  
- CVE-2026-22709 (vm2@3.9.17): CVSS 9.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fix: upgrade vm2 to 3.10.0  
- CVE-2019-10744 (lodash@2.4.2): CVSS 9.1, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H, fix: upgrade lodash >4.17.1  
- CVE-2023-46233 (crypto-js@3.3.0): CVSS 9.1, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N, fix: upgrade crypto-js to secure PBKDF2 implementation  
- Notify per Art. 14: ≤24h early warning → ≤72h incident notification → ≤1 month final report.

## 3. Art. 3(41) Exploitability Assessment
- PoC sources: githubexploit (5), exploitdb (2), packetstorm (2), zdt (2), hackerone (3), kitploit (2)
- EXPLOITABLE CVEs: 39
- EPSS stale count: 9 CVEs with EPSS scores >90 days old — exploitability confidence reduced.
- Top 5 EXPLOITABLE CVEs by CVSS score:  
  • CVE-2015-9235 (jsonwebtoken@0.1.0, 0.4.0): 9.8, EPSS 0.3247 (not stale), 2699 days public, fix: update >4.2.1  
  • CVE-2023-32314 (vm2@3.9.17): 9.8, EPSS 0.69875 (not stale), 1020 days public, fix: upgrade >3.9.17  
  • CVE-2023-37466 (vm2@3.9.17): 9.8, EPSS 0.04997 (not stale), 961 days public, fix: upgrade >3.9.19  
  • CVE-2023-37903 (vm2@3.9.17): 9.8, EPSS 0.04997 (not stale), 961 days public, fix: upgrade >3.9.19  
  • CVE-2026-22709 (vm2@3.9.17): 9.8, EPSS 0.0003 (not stale), 33 days public, fix: upgrade to 3.10.0

## 4. Critical & High Findings (Annex I Part II §2)
- CVE-2026-23745 (tar@4.4.19, 6.2.1, 7.5.2): 8.2, CVSS:4.0/AV:L/AC:L/PR:N/UI:A/VC:H/SC:H/VI:L/SI:L/VA:N/SA:N, EPSS 6e-05, EXPLOITABLE, fix: upgrade tar >7.5.2  
- CVE-2026-23950 (tar@4.4.19, 6.2.1, 7.5.2): 8.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:H/A:L, EPSS 6e-05, VULNERABILITY, fix: upgrade tar >7.5.3  
- CVE-2026-24842 (tar@4.4.19, 6.2.1, 7.5.2): 8.2, CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N, EPSS 0.00012, VULNERABILITY, fix: upgrade tar >7.5.2  
- CVE-2025-47944 (multer@1.4.5-lts.2): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H, EPSS 0.00011, EXPLOITABLE, fix: upgrade multer to 2.0.0  
- CVE-2025-47935 (multer@1.4.5-lts.2): 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H, EPSS 0.00048, EXPLOITABLE, fix: upgrade multer <2.0.0  
- CVE-2025-48997 (multer@1.4.5-lts.2): 8.7, CVSS:4.0/AV:N/AC:L/PR:N/UI:N/VC:N/SC:N/VI:N/SI:N/VA:H/SA:N, EPSS 0.00081, EXPLOITABLE, fix: upgrade multer to 2.0.1  
- CVE-2026-26996 (minimatch@3.0.5, 3.0.8, 3.1.2, 5.1.6, 9.0.5): 8.7, CVSS:4.0/AV:N/AC:L/PR:N/UI:N/VC:N/SC:N/VI:N/SI:N/VA:H/SA:N, EPSS N/A, EXPLOITABLE, fix: upgrade minimatch >9.0.5  
- CVE-2025-13465 (lodash@4.17.21): 7.9, CVSS:4.0/AV:N/AC:L/PR:N/UI:N/VC:N/SC:H/VI:L/SI:H/VA:L/SA:H/E:P, EPSS 0.00025, EXPLOITABLE, fix: upgrade lodash to 4.17.23  
- And 24 more across 31 packages.

## 5. Risk Distribution & Age Risk
- Severity counts: MEDIUM 20, HIGH 32, CRITICAL 7, NONE 1
- Top affected packages: sanitize-html@1.4.2 (7 CVEs), jsonwebtoken@0.1.0 (5 CVEs), jsonwebtoken@0.4.0 (5 CVEs)
- Top 3 oldest CRITICAL/HIGH CVEs:  
  • CVE-2016-4055 (moment@2.0.0): HIGH, CVSS 7.8, 3049 days, fix: upgrade moment >2.11  
  • CVE-2017-18214 (moment@2.0.0): HIGH, CVSS 7.5, 2917 days, fix: upgrade moment >2.19.3  
  • CVE-2015-9235 (jsonwebtoken@0.1.0, 0.4.0): CRITICAL, CVSS 9.8, 2699 days, fix: upgrade jsonwebtoken >4.2.1

## 6. CRA Defensible-Practice Actions
- Immediate — Art. 14 + Annex I Part II §2: Patch jsonwebtoken (CVE-2015-9235), vm2 (CVE-2023-32314, CVE-2023-37466, CVE-2023-37903, CVE-2026-22709), lodash (CVE-2019-10744), crypto-js (CVE-2023-46233). Submit Art. 14 notifications for Track 2 CVEs.  
- Urgent — Annex I Part II §2: Patch EXPLOITABLE HIGH CVEs in tar (CVE-2026-23745, CVE-2026-23950, CVE-2026-24842), multer (CVE-2025-47944, CVE-2025-47935, CVE-2025-48997), minimatch (CVE-2026-26996), lodash (CVE-2025-13465).  
- Planned — Annex I Part II §2: Remediate remaining HIGH/MEDIUM CVEs prioritizing oldest first (e.g., moment CVEs CVE-2016-4055, CVE-2017-18214).  
- SBOM update — Annex I Part II §1: Maintain up-to-date CycloneDX SBOM reflecting current component versions and fixes.  
- Public advisory — Annex I Part II §4: Publish advisories with CVE IDs, severity, vectors, affected versions, and remediation steps after patching.  
- CVD hygiene — Annex I Part II §5–6: Ensure coordinated vulnerability disclosure policy and security contact info are published and current.