### 1. SBOM Overview  
Product `sbom-grbrsm_ui-v12.0.3rc0` (SPDX format) scanned on 2025-07-11 includes 338 packages, with 7 affected by 13 advisories. Unique CVEs: **1 CRITICAL**, **6 HIGH**, **3 MEDIUM**.  

### 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified.  

### 3. Exploit Availability Assessment  
- [CVE-2025-7783] form-data@4.0.3 — CVSS 9.4 (CRITICAL) — EPSS 0.00177 — GitHub exploit PoC for unsafe random boundary generation.  
- [CVE-2025-54371] axios@1.10.0 — CVSS 7.5 (HIGH) — EPSS N/A — GitHub exploit PoC (withdrawn advisory).  
1 additional CVE has exploit evidence.  

### 4. Critical & High Findings  
- [CVE-2025-7783] form-data@4.0.3 — CVSS 9.4 (CRITICAL) — EPSS 0.00177  
- [CVE-2026-25639] axios@1.10.0 — CVSS 8.7 (HIGH) — EPSS 0.00033  
- [CVE-2026-26996] minimatch@7.4.6 — CVSS 8.7 (HIGH) — EPSS 0.0004  
- [CVE-2025-13465] lodash@4.17.21 — CVSS 8.2 (HIGH) — EPSS 0.00025  
and 2 more HIGH findings across 2 packages.  

### 5. Risk Distribution  
Severity (unique CVEs): **1 CRITICAL**, **6 HIGH**, **3 MEDIUM**.  
Top affected packages:  
- axios (4 advisories)  
- lodash (2 advisories)  
- minimatch (2 advisories)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `form-data` to ≥4.0.4 (CVE-2025-7783, CRITICAL, exploit PoC).  
2. **Urgent**: Update `axios` to ≥1.10.1 (CVE-2026-25639, HIGH, prototype pollution).  
3. **Planned**: Upgrade `minimatch` (CVE-2026-26996, HIGH, ReDoS).  
4. **SBOM Hygiene**: Re-audit transitive dependency `form-data` via axios.  
5. **Monitor**: Track EPSS for CVE-2025-13465 (lodash, HIGH).