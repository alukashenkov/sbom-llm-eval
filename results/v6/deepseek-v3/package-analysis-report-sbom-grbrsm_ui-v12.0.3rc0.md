### 1. SBOM Overview  
- **Product**: `sbom-grbrsm_ui-v12.0.3rc0` (SPDX)  
- **Scan date**: 2025-07-11  
- **Packages**: 338 total, 7 affected  
- **Unique CVEs**: 9 (1 CRITICAL, 5 HIGH, 3 MEDIUM)  

### 2. CRA Mandatory Reporting (Article 14)  
- No CRA Article 14 mandatory reporting triggers (no `wildExploited` or CISA KEV entries).  

### 3. Exploit Assessment  
- **Exploited CVEs**:  
  - `CVE-2025-7783` (CRITICAL, 9.4 CVSS, form-data@4.0.3) - GitHub PoC  
  - `CVE-2025-54371` (HIGH, 7.5 CVSS, axios@1.10.0) - GitHub PoC  
- 2 additional CVEs have PoC evidence.  

### 4. Critical & High Findings  
- `CVE-2026-25639` (HIGH, 8.7 CVSS, axios@1.10.0, EPSS 0.033%)  
- `CVE-2025-58754` (HIGH, 7.5 CVSS, axios@1.10.0, EPSS 0.102%)  
- `CVE-2025-13465` (HIGH, 8.2 CVSS, lodash@4.17.21, EPSS 0.025%)  
- `CVE-2026-26996` (HIGH, 8.7 CVSS, minimatch@7.4.6, EPSS 0.040%)  
- And 1 more HIGH across 1 package.  

### 5. Risk Distribution  
- **Severity**: CRITICAL (1), HIGH (5), MEDIUM (3)  
- **Top affected packages**:  
  - `axios@1.10.0` (4 CVEs)  
  - `js-yaml@4.1.0` (1 CVE)  
  - `lodash@4.17.21` (1 CVE)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `form-data@4.0.3` (CVE-2025-7783) per Article 10(3) critical risk mitigation.  
2. **Urgent**: Update `axios@1.10.0` (CVE-2025-54371, CVE-2025-58754) with PoC evidence.  
3. **Planned**: Address remaining HIGH risks in `lodash` and `minimatch`.  
4. **Hygiene**: Maintain SBOM integrity per Article 10(6) for future audits.  
5. **Monitor**: Track EPSS for `CVE-2026-25639` (HIGH, axios) due to rising exploit likelihood.