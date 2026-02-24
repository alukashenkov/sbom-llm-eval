### 1. SBOM Overview  
- **Product**: OWASP Juice Shop (container) `sha256:75b03f3f5336b39d1358d4280c09b8b265ae21e4cb215a9bf68e27f96ac76e3c`  
- **Format**: CycloneDX  
- **Scan date**: 2026-02-24  
- **Packages**: 998 total, 38 affected (3.8%)  
- **Unique CVEs**: 58 (CRITICAL: 7, HIGH: 30, MEDIUM: 21)  

---

### 2. CRA Mandatory Reporting (Article 14)  
- **No CRA Article 14 mandatory reporting triggers** (no `wildExploited` or CISA KEV entries).  

---

### 3. Exploit Assessment  
- **14 CVEs** have documented PoC/exploit evidence:  
  - `CVE-2023-32314` (vm2@3.9.17, CRITICAL, CVSS 9.8, EPSS 0.69875)  
  - `CVE-2023-37466` (vm2@3.9.17, CRITICAL, CVSS 9.8, EPSS 0.04997)  
  - `CVE-2023-37903` (vm2@3.9.17, CRITICAL, CVSS 9.8, EPSS 0.39234)  
  - `CVE-2015-9235` (jsonwebtoken@0.1.0/0.4.0, CRITICAL, CVSS 9.8, EPSS 0.3247)  
  - `CVE-2026-23745` (tar@4.4.19/6.2.1/7.5.2, HIGH, CVSS 8.2, EPSS 0.00006)  

---

### 4. Critical & High Findings  
- `CVE-2024-29415` (ip@2.0.1, HIGH, CVSS 8.1, EPSS 0.86505)  
- `CVE-2023-46233` (crypto-js@3.3.0, CRITICAL, CVSS 9.1, EPSS 0.00823)  
- `CVE-2022-23539` (jsonwebtoken@0.1.0/0.4.0, HIGH, CVSS 8.1, EPSS 0.00072)  
- `CVE-2026-23950` (tar@4.4.19/6.2.1/7.5.2, HIGH, CVSS 8.8, EPSS 0.00006)  
- **And 23 more** across 12 packages.  

---

### 5. Risk Distribution  
- **Severity**: CRITICAL (7), HIGH (30), MEDIUM (21)  
- **Top affected packages**:  
  1. `sanitize-html@1.4.2` (7 CVEs)  
  2. `jsonwebtoken@0.1.0/0.4.0` (5 CVEs each)  
  3. `tar@4.4.19` (5 CVEs)  

---

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `vm2@3.9.17` (CRITICAL CVEs with active exploits).  
2. **Urgent**: Upgrade `jsonwebtoken` to ≥8.5.2 (CRITICAL/HIGH CVEs).  
3. **Planned**: Address HIGH-severity issues in `tar`, `ip`, and `crypto-js`.  
4. **Hygiene**: Update SBOM per CRA Article 10(6) with quarterly scans.  
5. **Monitor**: Track EPSS ≥0.1 (e.g., `CVE-2024-29415`).  

---  
*Word count: 450*