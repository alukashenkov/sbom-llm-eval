**Vulnerability Summary: OWASP Juice Shop Container (CycloneDX SBOM)**  
*Generated from scan dated 2026-02-24*

---

### 1. SBOM Overview  
The OWASP Juice Shop container image (sha256:75b03f3f…) contains 998 packages, of which 38 are affected by vulnerabilities. A total of 58 unique CVEs were identified, including 7 CRITICAL, 30 HIGH, and 21 MEDIUM severity issues.

---

### 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified. No CVEs were flagged as actively exploited or listed in CISA KEV.

---

### 3. Exploit Availability Assessment  
Public exploit evidence exists for 14 CVEs across GitHub (5), HackerOne (3), ExploitDB (2), PacketStorm (2), ZDT (2), and KitPloit (2). Top exploitable CVEs include:  
- **CVE-2023-32314** (vm2, CRITICAL, CVSS 9.8, EPSS 69.9%)  
- **CVE-2023-37466** (vm2, CRITICAL, CVSS 9.8, EPSS 5.0%)  
- **CVE-2023-37903** (vm2, CRITICAL, CVSS 9.8, EPSS 39.2%)  
- **CVE-2015-9235** (jsonwebtoken, CRITICAL, CVSS 9.8, EPSS 32.5%)  
- **CVE-2026-23745** (tar, HIGH, CVSS 8.2, EPSS 0.006%)  

---

### 4. Critical & High Findings  
Remaining high-impact vulnerabilities include:  
- **CVE-2022-23539** (jsonwebtoken, HIGH, CVSS 8.1, EPSS 0.07%)  
- **CVE-2022-23529** (jsonwebtoken, HIGH, CVSS 7.6, EPSS 0.04%)  
- **CVE-2026-23950** (tar, HIGH, CVSS 8.8, EPSS 0.006%)  
- **CVE-2026-24842** (tar, HIGH, CVSS 8.2, EPSS 0.012%)  
- **CVE-2023-46233** (crypto-js, CRITICAL, CVSS 9.1, EPSS 0.82%)  
- **CVE-2019-10744** (lodash, CRITICAL, CVSS 9.1, EPSS 2.44%)  
- **CVE-2024-29415** (ip, HIGH, CVSS 8.1, EPSS 86.5%)  
- **CVE-2021-23337** (lodash, HIGH, CVSS 7.2, EPSS 0.74%)  
...and 22 more HIGH findings across 12 packages.

---

### 5. Risk Distribution  
Top affected packages by CVE count:  
- `sanitize-html@1.4.2` (7 CVEs)  
- `jsonwebtoken@0.1.0/0.4.0` (5 each)  
- `tar@4.4.19` (5)  
- `vm2@3.9.17` (5)  

Severity distribution: 7 CRITICAL, 30 HIGH, 21 MEDIUM.

---

### 6. CRA Compliance Actions  
1. **Immediate Patching**: Upgrade `vm2` to ≥3.9.19 (fixes 4 CRITICAL RCEs).  
2. **Urgent Updates**: Replace `jsonwebtoken` v0.1.0/0.4.0 with ≥9.0.0 (critical algorithm bypass).  
3. **Dependency Refresh**: Update `tar` to ≥7.5.3 (multiple path traversal fixes).  
4. **Cryptographic Review**: Replace `crypto-js` with modern alternatives (weak PBKDF2).  
5. **SBOM Hygiene**: Remove unused packages like `notevil` (sandbox escape) and audit lodash usage.

*Prioritize fixes by exploitability (EPSS >30%) and CRITICAL CVSS scores.*  

---  
*Summary complies with EU CRA Article 14 reporting requirements. No mandatory triggers detected.*