1. SBOM Overview  
- Product: sbom-grbrsm_ui-v12.0.3rc0  
- Format: SPDX  
- Scan Date: 2025-07-11  
- Total Packages: 338  
- Affected Packages: 7  
- Unique CVEs: 9 (Severity distribution: HIGH 5, CRITICAL 1, MEDIUM 3)  

2. CRA Mandatory Reporting (Article 14)  
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).  

3. Exploit Assessment  
- PoC evidence summary: 2 CVEs with GitHub exploits.  
- Top 5 exploited CVEs by severity:  
  • CVE-2025-7783 (form-data/axios) – CVSS 9.4 (Critical), EPSS 0.00177  
  • CVE-2026-25639 (axios) – CVSS 8.7 (High), EPSS 0.00033  
  • CVE-2026-26996 (minimatch) – CVSS 8.7 (High), EPSS 0.0004  
  • CVE-2025-13465 (lodash) – CVSS 8.2 (High), EPSS 0.00025  
  • CVE-2025-58754 (axios) – CVSS 7.5 (High), EPSS 0.00102  
- 4 additional CVEs have PoC evidence.  

4. Critical & High Findings (excluding above exploited CVEs)  
- CVE-2025-54371 (axios) – CVSS 7.5 (High), no EPSS data  
- CVE-2025-64718 (js-yaml) – CVSS 6.9 (Medium), EPSS 0.0002 (included here due to severity)  
- CVE-2025-27789 (@babel/runtime) – CVSS 6.2 (Medium), EPSS 0.00139  
- CVE-2024-53382 (prismjs) – CVSS 4.9 (Medium), EPSS 0.00083  
- and 1 more CVE across 1 package.  

5. Risk Distribution  
- Severity counts: HIGH 5, CRITICAL 1, MEDIUM 3  
- Top affected packages:  
  • axios@1.10.0 (4 unique CVEs)  
  • js-yaml@4.1.0 (1 unique CVE)  
  • lodash@4.17.21 (1 unique CVE)  

6. CRA Compliance Actions  
- **Immediate**: Patch form-data@4.0.3 for CVE-2025-7783 (Critical, CVSS 9.4) per CRA Article 10(1) and 11(1).  
- **Urgent**: Patch axios@1.10.0 for CVE-2026-25639 and CVE-2025-58754 (High severity with PoC).  
- **Planned**: Patch lodash@4.17.21 for CVE-2025-13465 and minimatch@7.4.6 for CVE-2026-26996 (High severity).  
- **Hygiene**: Maintain SBOM updates and vulnerability scanning per CRA Article 10(6).