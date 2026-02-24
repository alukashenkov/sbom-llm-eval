**Vulnerability Summary (CRA Compliance)**  
*SBOM: sbom-grbrsm_ui-v12.0.3rc0 (SPDX) – Scan Date: 2025-07-11*  
**Total Packages:** 338 | **Affected:** 7 | **Total Advisories:** 13  

---

### **1. CRA Mandatory Reporting Triggers (Article 14)**  
**No CRA mandatory reporting triggers identified.**  
None of the advisories have `wildExploited=true` or `cisa_kev` status.

---

### **2. Exploit Availability Assessment**  
- **Public PoC available:**  
  - `CVE-2025-7783` (axios, form-data) – GitHub PoC (1)  
- **Exploit framework integration:** None  
- **Bug bounty disclosed:** None  

---

### **3. Critical & High Findings**  
- `CVE-2025-7783` (form-data@4.0.3) – CVSS 9.4 (CRITICAL) – EPSS 0.177% – Fix: Patched in form-data 4.0.4  
- `CVE-2026-25639` (axios@1.10.0) – CVSS 8.7 (HIGH) – EPSS 0.033% – Fix: Patched in axios 1.10.1  
- `CVE-2025-58754` (axios@1.10.0) – CVSS 7.5 (HIGH) – EPSS 0.102% – Fix: Patched in axios 1.10.1  
- `CVE-2025-13465` (lodash@4.17.21) – CVSS 8.2 (HIGH) – EPSS 0.025% – Fix: Patched in lodash 4.17.22  
- `CVE-2026-26996` (minimatch@7.4.6) – CVSS 8.7 (HIGH) – EPSS 0.040% – Fix: Patched in minimatch 7.4.7  

---

### **4. Risk Distribution**  
- **Severity:** 1 CRITICAL, 7 HIGH, 5 MEDIUM  
- **Top 3 Affected Packages:** axios (4 advisories), lodash (1), minimatch (2)  
- **Exploitation Landscape:** 1 advisory with public PoC, 12 with low EPSS scores (<1%).

---

### **5. CRA Compliance Actions**  
1. **Immediate:** Patch `form-data@4.0.3` (CVE-2025-7783) – CRITICAL risk.  
2. **Urgent:** Update `axios@1.10.0` to 1.10.1 (CVE-2025-7783, CVE-2025-58754).  
3. **Planned:** Address `lodash@4.17.21` (CVE-2025-13465) – HIGH risk.  
4. **Planned:** Update `minimatch@7.4.6` (CVE-2026-26996) – HIGH risk.  
5. **SBOM Hygiene:** Validate and update SBOM to reflect patched versions.