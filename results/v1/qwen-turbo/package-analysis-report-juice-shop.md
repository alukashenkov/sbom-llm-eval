### 1. SBOM Overview  
**Product:** `bkimminich/juice-shop` (Docker image)  
**Format:** CycloneDX  
**Scan Date:** 2026-02-24  
**Total Packages:** 998  
**Affected Packages:** 38  
**Total Advisories:** 82  

**Vulnerability Distribution:**  
- **CRITICAL:** 3  
- **HIGH:** 17  
- **MEDIUM:** 62  

---

### 2. CRA Mandatory Reporting Triggers (Article 14)  
**No CRA mandatory reporting triggers identified.**  
No vulnerabilities have `wildExploited=true` or are listed in CISA KEV.  

---

### 3. Exploit Availability Assessment  
**Public PoC available (githubexploit/exploitdb):**  
- `vm2` (CVE-2023-37466, CVE-2023-37903)  
- `tar` (CVE-2026-23745)  

**Exploit framework integration (nuclei/packetstorm):**  
- `vm2` (CVE-2023-37466)  
- `tar` (CVE-2026-23745)  

**Bug bounty disclosed (hackerone):**  
- `lodash` (CVE-2018-3721, CVE-2018-16487)  
- `jsonwebtoken` (CVE-2015-9235)  

---

### 4. Critical & High Findings  
- **jsonwebtoken@0.1.0 (CVE-2015-9235):** CRITICAL, CVSS 9.8, EPSS 0.3247, No fix available  
- **vm2@3.9.17 (CVE-2023-32314):** CRITICAL, CVSS 9.8, EPSS 0.69875, No fix available  
- **vm2@3.9.17 (CVE-2023-37466):** CRITICAL, CVSS 9.8, EPSS 0.04997, No fix available  
- **jsonwebtoken@0.4.0 (CVE-2022-23540):** HIGH, CVSS 6.4, EPSS 0.00017, No fix available  
- **jsonwebtoken@0.1.0 (CVE-2022-23529):** HIGH, CVSS 7.6, EPSS 0.00044, No fix available  

---

### 5. Risk Distribution  
**Severity Counts:**  
- **CRITICAL:** 3  
- **HIGH:** 17  
- **MEDIUM:** 62  

**Top 3 Most Affected Packages:**  
1. `jsonwebtoken` (5 advisories)  
2. `vm2` (5 advisories)  
3. `sanitize-html` (6 advisories)  

**Exploitation Landscape:**  
- 11 advisories have public PoC or exploit sources.  
- 3 critical vulnerabilities with high EPSS scores (≥0.3).  

---

### 6. CRA Compliance Actions  
1. **Immediate:** Patch `jsonwebtoken` (CVE-2015-9235) and `vm2` (CVE-2023-32314) to mitigate critical risks.  
2. **Urgent:** Address high-severity issues in `sanitize-html` and `tar` with public exploit sources.  
3. **Planned:** Review and update all packages with high EPSS scores (≥0.1).  
4. **SBOM Hygiene:** Ensure all dependencies are tracked and updated regularly.  
5. **Monitoring:** Continuously monitor for new advisories and exploit activity.