### 1. SBOM Overview  
**Product:** openclaw  
**Format:** SPDX  
**Scan Date:** 2026-02-20  
**Total Packages:** 1112  
**Affected Packages:** 21  
**Total Advisories:** 125  

**Vulnerability Distribution by Severity:**  
- **CRITICAL:** 5  
- **HIGH:** 44  
- **MEDIUM:** 49  
- **LOW:** 27  

---

### 2. CRA Mandatory Reporting Triggers (Article 14)  
**No CRA mandatory reporting triggers identified.**  
None of the advisories have `wildExploited=true` or `cisa_kev` status.  

---

### 3. Exploit Availability Assessment  
**Public PoC available (githubexploit/exploitdb):**  
- **CVE-2026-25253 (GHSA-G8P2-7WF7-98MQ):** 3 GitHub PoCs  
- **CVE-2026-24763 (GHSA-MC68-Q9JW-2H3V):** 1 GitHub PoC  
- **CVE-2026-25157 (GHSA-Q284-4PVR-M585):** 1 GitHub PoC  
- **CVE-2026-22610 (GHSA-JRMJ-C5CX-3CW6):** 1 GitHub PoC  

**Exploit Framework Integration (nuclei/packetstorm):**  
- None identified.  

**Bug Bounty Disclosed (hackerone):**  
- None identified.  

---

### 4. Critical & High Findings  
- **CVE-2026-25593 (OpenClaw):** High (CVSS 8.4), EPSS 0.00023, No fix available  
- **CVE-2026-26328 (OpenClaw):** Medium (CVSS 6.5), EPSS 0.00025, No fix available  
- **CVE-2026-25253 (Clawdbot):** High (CVSS 8.8), EPSS 0.00049, No fix available  
- **CVE-2026-24763 (Clawdbot):** High (CVSS 8.8), EPSS 0.00083, No fix available  
- **CVE-2026-22610 (Angular):** High (CVSS 8.5), EPSS 0.00021, No fix available  

---

### 5. Risk Distribution  
**Severity Counts:**  
- **CRITICAL:** 5  
- **HIGH:** 44  
- **MEDIUM:** 49  
- **LOW:** 27  

**Top 3 Most-Affected Packages:**  
1. **openclaw (15 advisories)**  
2. **clawdbot (8 advisories)**  
3. **fast-xml-parser (5 advisories)**  

**Exploitation Landscape:**  
- 5 advisories with public PoC (githubexploit/exploitdb)  
- 1 advisory with GitHub PoC (CVE-2026-22610)  
- No known exploit framework integrations  

---

### 6. CRA Compliance Actions (Priority-Ordered)  
1. **Immediate:** Address **CVE-2026-25253** (Clawdbot) and **CVE-2026-24763** (Clawdbot) due to high exploitability and public PoC.  
2. **Urgent:** Patch **CVE-2026-22610** (Angular) and **CVE-2026-25593** (OpenClaw) to mitigate high-risk vulnerabilities.  
3. **Planned:** Review and address **CVE-2026-26328** (OpenClaw) and **CVE-2026-25157** (OpenClaw) for authorization bypass and command injection.  
4. **SBOM Hygiene:** Ensure all advisories are properly documented and updated in SBOM for traceability.  
5. **Monitoring:** Continuously monitor for new exploit activity (e.g., GitHub, ExploitDB) for high-severity advisories.