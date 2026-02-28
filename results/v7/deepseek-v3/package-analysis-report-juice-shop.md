## 1. SBOM Overview  
- **Product**: OWASP Juice Shop (container image) v19.1.1  
- **Scan date**: 2026-02-24  
- **Packages**: 998 total, 38 affected  
- **Unique CVEs**: 60 (CRITICAL: 7, HIGH: 32, MEDIUM: 20, NONE: 1)  
- **CRA Tiers**: EXPLOITABLE: 39, VULNERABILITY: 21  

---  

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2))**:  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

**Track 2 — Severe Incidents (Art. 14(3)–(5))**:  
- **CVE-2015-9235** (CRITICAL, 9.8 CVSS, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`): jsonwebtoken verification bypass. Fix: Upgrade jsonwebtoken.  
- **CVE-2023-32314** (CRITICAL, 9.8 CVSS, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`): vm2 sandbox escape (RCE). Fix: Upgrade vm2.  
- **CVE-2023-37466**/**CVE-2023-37903** (CRITICAL, 9.8 CVSS): vm2 sandbox escape via Node.js inspect. Fix: Upgrade vm2.  
- **CVE-2026-22709** (CRITICAL, 9.8 CVSS): vm2 sandbox escape via Promise handler. Fix: Upgrade vm2.  
- **CVE-2019-10744** (CRITICAL, 9.1 CVSS): lodash prototype pollution. Fix: Upgrade lodash.  
- **CVE-2023-46233** (CRITICAL, 9.1 CVSS): crypto-js PBKDF2 weakness. Fix: Upgrade crypto-js.  
**Action**: ≤24h early warning → ≤72h incident notification → ≤1 month final report (Art. 14(3)).  

---  

## 3. Art. 3(41) Exploitability Assessment  
- **Exploitable CVEs**: 39 (5 PoC sources: GitHub, ExploitDB, PacketStorm, ZDT, HackerOne)  
- Top 5 EXPLOITABLE CVEs:  
  1. **CVE-2023-32314** (vm2, 9.8 CVSS, EPSS 0.69875)  
  2. **CVE-2015-9235** (jsonwebtoken, 9.8 CVSS, EPSS 0.3247)  
  3. **CVE-2023-37466** (vm2, 9.8 CVSS, EPSS 0.04997)  
  4. **CVE-2026-22709** (vm2, 9.8 CVSS, EPSS 0.0003)  
  5. **CVE-2019-10744** (lodash, 9.1 CVSS, EPSS 0.02441)  
- **Note**: 9 CVEs have EPSS scores >90 days old — exploitability confidence reduced.  

---  

## 4. Critical & High Findings (Annex I Part II §2)  
- **CVE-2026-23745** (tar, 8.2 CVSS, `AV:L/AC:L/AT:N/PR:N/UI:A/VC:H/SC:H`): Arbitrary file overwrite. Fix: Upgrade tar.  
- **CVE-2026-23950** (tar, 8.8 CVSS, `AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:H/A:L`): macOS symlink poisoning. Fix: Upgrade tar.  
- **CVE-2025-9235** (jsonwebtoken, 9.8 CVSS): Verification bypass. Fix: Upgrade jsonwebtoken.  
- **And 5 more HIGH/CRITICAL CVEs across 4 packages**.  

---  

## 5. Risk Distribution & Age Risk  
- **Severity**: CRITICAL (7), HIGH (32), MEDIUM (20)  
- **Top affected packages**: sanitize-html (7 CVEs), jsonwebtoken (5 CVEs), tar (5 CVEs)  
- **Oldest unpatched CRITICAL/HIGH**:  
  1. **CVE-2016-4055** (moment, HIGH, 3049 days): ReDoS. Fix: Upgrade moment.  
  2. **CVE-2017-18214** (moment, HIGH, 2917 days): ReDoS. Fix: Upgrade moment.  
  3. **CVE-2015-9235** (jsonwebtoken, CRITICAL, 2699 days): Verification bypass.  

---  

## 6. CRA Defensible-Practice Actions  
1. **Immediate (Art. 14 + Annex I Part II §2)**: Patch all Track 2 CVEs (vm2, jsonwebtoken, lodash, crypto-js).  
2. **Urgent (Annex I Part II §2)**: Upgrade tar to mitigate symlink poisoning (CVE-2026-23950).  
3. **Planned**: Address oldest HIGHs (moment ReDoS, 3000+ days unpatched).  
4. **SBOM update (Annex I Part II §1)**: Refresh CycloneDX SBOM post-remediation.  
5. **Public advisory (Annex I Part II §4)**: Publish fixes for vm2, jsonwebtoken, tar.  
6. **CVD hygiene (Annex I Part II §5–6)**: Verify security contact at bjoern.kimminich@owasp.org is active.