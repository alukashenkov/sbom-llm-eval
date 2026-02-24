# Vulnerability Summary for sbom-grbrsm_ui-v12.0.3rc0  

## 1. SBOM Overview  
The SPDX-formatted SBOM for sbom-grbrsm_ui-v12.0.3rc0 (scanned 2025-07-11) contains 338 packages, with 7 affected by vulnerabilities. Analysis reveals 9 unique CVEs: 1 CRITICAL, 5 HIGH, and 3 MEDIUM severity findings.  

## 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified (no CVEs with wild exploitation or CISA KEV entries).  

## 3. Exploit Availability Assessment  
2 CVEs have GitHub-hosted PoCs:  
- **CVE-2025-7783** (CRITICAL, 9.4 CVSS, form-data@4.0.3)  
- **CVE-2025-54371** (HIGH, 7.5 CVSS, axios@1.10.0)  

## 4. Critical & High Findings  
**Critical**:  
- CVE-2025-7783 (form-data@4.0.3, EPSS 0.00177)  

**High**:  
- CVE-2025-58754 (axios@1.10.0, 7.5 CVSS, EPSS 0.00102)  
- CVE-2026-25639 (axios@1.10.0, 8.7 CVSS, EPSS 0.00033)  
- CVE-2025-13465 (lodash@4.17.21, 8.2 CVSS, EPSS 0.00025)  
- CVE-2026-26996 (minimatch@7.4.6, 8.7 CVSS, EPSS 0.0004)  

*and 1 more HIGH finding across 1 package.*  

## 5. Risk Distribution  
Top affected packages:  
1. **axios@1.10.0** (4 CVEs)  
2. js-yaml@4.1.0, lodash@4.17.21, minimatch@7.4.6, @babel/runtime@7.0.0 (1 CVE each)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch form-data to ≥4.0.4 (CVE-2025-7783 CRITICAL)  
2. **Urgent**: Upgrade axios to ≥1.10.1 (4 HIGH CVEs)  
3. **Planned**: Update lodash (CVE-2025-13465) and minimatch (CVE-2026-26996)  
4. **SBOM Hygiene**: Refresh transitive dependencies via @babel/runtime update  
5. **Monitoring**: Track EPSS trends for CVE-2026-25639 (HIGH, rising exploitability)  

*Prioritization aligns with CRA Article 10 obligations and exploitability evidence.*