# Vulnerability Summary Report  
**Product:** sbom-grbrsm_ui-v12.0.3rc0  
**Format:** SPDX | **Scan Date:** 2025-07-11  
**Total Packages:** 338 | **Affected Packages:** 7 | **Advisories:** 13  

---

### 1. CRA Mandatory Reporting Triggers (Article 14)  
**No CRA mandatory reporting triggers identified.**  
*(No vulnerabilities with `wildExploited=true` or `cisa_kev` entries found.)*  

---

### 2. Exploit Availability Assessment  
**Public PoC Available:**  
- [CVE-2025-7783] form-data@4.0.3 — CVSS 9.4 (CRITICAL) — EPSS 0.00177  
  *Insecure random boundary selection in multipart forms (GitHub exploit available).*  

*(No exploit framework integrations or bug bounty disclosures detected.)*  

---

### 3. Critical & High Findings  
- [CVE-2025-7783] form-data@4.0.3 — CVSS 9.4 (CRITICAL) — EPSS 0.00177  
- [CVE-2026-25639] axios@1.10.0 — CVSS 8.7 (HIGH) — EPSS 0.00033  
- [CVE-2025-13465] lodash@4.17.21 — CVSS 8.2 (HIGH) — EPSS 0.00025  
- [CVE-2026-26996] minimatch@7.4.6 — CVSS 8.7 (HIGH) — EPSS 0.0004  

---

### 4. Risk Distribution  
**Severity:** CRITICAL (1), HIGH (6), MEDIUM (5), LOW (1)  
**Top Affected Packages:**  
1. `axios` (4 advisories)  
2. `lodash` (2 advisories)  
3. `form-data` (1 CRITICAL advisory)  

**Exploitation Landscape:**  
- 1 vulnerability with public PoC (7.7% of total)  
- Low EPSS scores (<0.002) for all high/critical CVEs  

---

### 5. CRA Compliance Actions  
1. **Immediate:** Patch `form-data@4.0.3` (CVE-2025-7783) due to CRITICAL severity and public PoC.  
2. **Urgent:** Upgrade `axios` to address prototype pollution (CVE-2026-25639).  
3. **Planned:** Replace `lodash` with modern alternatives to mitigate persistent prototype pollution risks.  
4. **SBOM Hygiene:** Enforce version pinning for transitive dependencies like `form-data`.  
5. **Monitoring:** Subscribe to CISA KEV updates for emerging exploitation trends.  

*(Report generated in compliance with EU CRA Article 14 notification timelines.)*