### 1. SBOM Overview  
The SBOM for **sbom-grbrsm_ui-v12.0.3rc0** (SPDX format, generated 2025-07-11) includes 338 packages, of which **7 are affected by vulnerabilities**. Deduplicated CVE counts reveal **5 HIGH** and **1 CRITICAL** severity issues, with no mandatory reporting triggers under CRA Article 14.  

### 2. CRA Mandatory Reporting Triggers  
**No CRA mandatory reporting triggers identified** (no advisories with `wildExploited=true` or `cisa_kev` in `pocSources`).  

### 3. Exploit Availability Assessment  
1. **[CVE-2025-7783]** form-data@4.0.3 — CVSS 9.4 (CRITICAL) — EPSS 0.00177 — Unsafe random boundary selection (PoC on GitHub).  
2. **[CVE-2025-54371]** axios@1.10.0 — CVSS 7.5 (HIGH) — EPSS N/A — Transitive form-data vulnerability (PoC on GitHub).  
**Total:** 2 CVEs with exploit evidence.  

### 4. Critical & High Findings  
- **[CVE-2026-25639]** axios@1.10.0 — CVSS 8.7 (HIGH) — EPSS 0.00033 — Prototype Pollution.  
- **[CVE-2025-13465]** lodash@4.17.21 — CVSS 8.2 (HIGH) — EPSS 0.00025 — Prototype Pollution.  
- **[CVE-2026-26996]** minimatch@7.4.6 — CVSS 8.7 (HIGH) — EPSS 0.0004 — ReDoS.  
**And 2 more HIGH findings across 2 packages.**  

### 5. Risk Distribution  
**Unique CVEs:** 1 CRITICAL, 5 HIGH, 3 MEDIUM.  
**Top affected packages:**  
1. **axios** (4 advisories, 3 CVEs)  
2. **lodash** (2 advisories, 1 CVE)  
3. **form-data** (1 advisory, 1 CRITICAL CVE).  

### 6. CRA Compliance Actions  
1. **Immediate:** Patch `form-data` to ≥4.0.4 (CVE-2025-7783, CRITICAL).  
2. **Urgent:** Update `axios` to ≥1.10.1 (multiple HIGH CVEs).  
3. **Planned:** Upgrade `lodash` to ≥4.17.23 (prototype pollution).  
4. **SBOM Hygiene:** Rebuild SBOM post-patching to verify fixes.  
5. **Monitor:** Track EPSS for CVE-2026-26996 (minimatch ReDoS).  

**Priority Order:** CRITICAL → Exploitable HIGH → Non-exploitable HIGH.