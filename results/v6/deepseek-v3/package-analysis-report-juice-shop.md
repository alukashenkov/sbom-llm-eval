### 1. SBOM Overview  
- **Product**: OWASP Juice Shop (container) v19.1.1  
- **Format**: CycloneDX  
- **Scan date**: 2026-02-24  
- **Packages**: 998 total, 38 affected  
- **Unique CVEs**: 60 (CRITICAL: 7, HIGH: 32, MEDIUM: 20, NONE: 1)  

---

### 2. CRA Mandatory Reporting (Article 14)  
**No CRA Article 14 mandatory reporting triggers** (no `wildExploited` or CISA KEV entries).  

---

### 3. Exploit Assessment  
- **14 CVEs** have PoC evidence (GitHub: 5, ExploitDB: 2, PacketStorm: 2, ZDT: 2, HackerOne: 3, KitPloit: 2).  
- **Top exploited CVEs**:  
  - `CVE-2023-32314` (vm2, CRITICAL, CVSS 9.8, EPSS 0.70)  
  - `CVE-2023-37466` (vm2, CRITICAL, CVSS 9.8, EPSS 0.05)  
  - `CVE-2023-37903` (vm2, CRITICAL, CVSS 9.8, EPSS 0.39)  
  - `CVE-2015-9235` (jsonwebtoken, CRITICAL, CVSS 9.8, EPSS 0.32)  
  - `CVE-2026-23745` (tar, HIGH, CVSS 8.2, EPSS 0.00006)  

---

### 4. Critical & High Findings  
- `CVE-2022-23539` (jsonwebtoken, HIGH, CVSS 8.1, EPSS 0.0007)  
- `CVE-2026-23950` (tar, HIGH, CVSS 8.8, EPSS 0.00006)  
- `CVE-2026-24842` (tar, HIGH, CVSS 8.2, EPSS 0.00012)  
- `CVE-2022-25887` (sanitize-html, HIGH, CVSS 7.5, EPSS 0.0045)  
- **And 28 more** across 15 packages.  

---

### 5. Risk Distribution  
- **Severity**: CRITICAL (7), HIGH (32), MEDIUM (20)  
- **Top affected packages**:  
  1. `sanitize-html@1.4.2` (7 CVEs)  
  2. `jsonwebtoken@0.1.0` / `0.4.0` (5 CVEs each)  
  3. `tar@4.4.19` / `vm2@3.9.17` (5 CVEs each)  

---

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `vm2` (CVE-2023-32314, CVE-2023-37466, CVE-2023-37903) – critical sandbox escapes.  
2. **Urgent**: Update `jsonwebtoken` (CVE-2015-9235, CVE-2022-23539) – token validation bypasses.  
3. **Planned**: Address `tar` path traversal (CVE-2026-23745, CVE-2026-23950).  
4. **Hygiene**: Rebuild SBOM post-patching per CRA Article 10(6).  
5. **Monitor**: Track EPSS ≥0.1 (e.g., `CVE-2024-29415` in `ip@2.0.1`, EPSS 0.87).  

*Note: Prioritize fixes per CRA Articles 10 (security requirements) and 11 (vulnerability handling).*