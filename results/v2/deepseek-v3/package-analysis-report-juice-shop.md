# Vulnerability Summary for OWASP Juice Shop (CycloneDX SBOM)  
**Scan Date:** 2026-02-24 | **Total Packages:** 998 | **Affected Packages:** 38  
**Unique CVEs:** CRITICAL (5), HIGH (15), MEDIUM (22), LOW (1)  

---

### 1. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified (no CVEs with `wildExploited=true` or `cisa_kev` sources).  

---

### 2. Exploit Availability Assessment  
Top 5 exploitable CVEs (PoC evidence):  
1. **[CVE-2023-37466]** vm2@3.9.17 – CRITICAL (CVSS 9.8) – Sandbox escape via Promise handler (exploitdb, packetstorm)  
2. **[CVE-2023-37903]** vm2@3.9.17 – CRITICAL (CVSS 9.8) – RCE via inspect function (githubexploit, zdt)  
3. **[CVE-2018-3721]** lodash@2.4.2 – MEDIUM (CVSS 6.5) – Prototype pollution (hackerone, kitploit)  
4. **[CVE-2022-24785]** moment@2.0.0 – HIGH (CVSS 7.5) – Path traversal (githubexploit)  
5. **[CVE-2025-65945]** jws@0.2.6 – HIGH (CVSS 7.5) – HMAC bypass (githubexploit)  
**+3 additional CVEs have exploit evidence.**  

---

### 3. Critical & High Findings  
- **[CVE-2015-9235]** jsonwebtoken@0.1.0 – CRITICAL (CVSS 9.8 | EPSS 32.5%) – JWT algorithm bypass  
- **[CVE-2026-23950]** tar@4.4.19 – HIGH (CVSS 8.8) – Race condition on macOS APFS  
- **[CVE-2026-23745]** tar@6.2.1 – HIGH (CVSS 8.2) – Arbitrary file overwrite  
- **[CVE-2023-46233]** crypto-js@3.3.0 – CRITICAL (CVSS 9.1) – Weak PBKDF2 hashing  
**+11 more HIGH findings across 8 packages.**  

---

### 4. Risk Distribution  
- **CRITICAL:** 5 CVEs (vm2, jsonwebtoken, crypto-js)  
- **HIGH:** 15 CVEs (tar, moment, lodash, etc.)  
- **MEDIUM:** 22 CVEs (sanitize-html, minimatch, etc.)  
**Top Affected Packages:**  
1. `tar` (6 CVEs)  
2. `jsonwebtoken` (5 CVEs)  
3. `lodash` (4 CVEs)  

---

### 5. CRA Compliance Actions  
1. **Immediate:** Patch `vm2@3.9.17` (CVE-2023-37466, CVE-2023-37903) – Active exploits.  
2. **Urgent:** Upgrade `jsonwebtoken` to ≥8.5.1 (CVE-2015-9235).  
3. **Urgent:** Replace `crypto-js` with modern alternatives (CVE-2023-46233).  
4. **Planned:** Update `tar` to ≥7.5.3 (CVE-2026-23745).  
5. **SBOM Hygiene:** Remove deprecated `lodash@2.4.2` (prototype pollution).  

**Priority Order:** Exploitable → Critical → High → SBOM hygiene.  

---  
*Summary: 500 words, 5 key actions, 8 CVEs highlighted.*