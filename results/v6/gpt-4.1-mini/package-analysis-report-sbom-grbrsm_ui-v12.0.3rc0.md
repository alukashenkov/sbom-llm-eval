1. SBOM Overview  
- Product: sbom-grbrsm_ui-v12.0.3rc0  
- Format: SPDX  
- Scan date: 2025-07-11  
- Total packages: 338  
- Affected packages: 7  
- Unique CVEs: 9 (Severity distribution: 1 CRITICAL, 5 HIGH, 3 MEDIUM)  

2. CRA Mandatory Reporting (Article 14)  
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).  

3. Exploit Assessment  
- PoC evidence summary: 2 CVEs with GitHub exploits  
- Top 5 exploited CVEs by severity (from advisory data):  
  • CVE-2025-7783 (form-data / axios) – CVSS 9.4 CRITICAL, EPSS 0.00177  
  • CVE-2026-25639 (axios) – CVSS 8.7 HIGH, EPSS 0.00033  
  • CVE-2026-26996 (minimatch) – CVSS 8.7 HIGH, EPSS 0.0004  
  • CVE-2025-13465 (lodash) – CVSS 8.2 HIGH, EPSS 0.00025  
  • CVE-2025-58754 (axios) – CVSS 7.5 HIGH, EPSS 0.00102  
- 4 additional CVEs have PoC evidence (including CVE-2025-54371, CVE-2025-64718, CVE-2025-27789, CVE-2024-53382)  

4. Critical & High Findings (excluding §2-3)  
- CVE-2025-54371 (axios) – CVSS 7.5 HIGH, EPSS not listed  
- CVE-2025-64718 (js-yaml) – CVSS 6.9 MEDIUM, EPSS 0.0002  
- CVE-2025-27789 (@babel/runtime) – CVSS 6.2 MEDIUM, EPSS 0.00139  
- CVE-2024-53382 (prismjs) – CVSS 4.9 MEDIUM, EPSS 0.00083  
- and 0 more across 3 packages (all remaining CVEs are MEDIUM severity)  

5. Risk Distribution  
- Severity counts: CRITICAL 1, HIGH 5, MEDIUM 3  
- Top 3 affected packages by unique CVEs:  
  • axios@1.10.0 (4 CVEs)  
  • js-yaml@4.1.0 (1 CVE)  
  • lodash@4.17.21 (1 CVE)  

6. CRA Compliance Actions  
- **Immediate**: Patch form-data for CVE-2025-7783 (CRITICAL) per CRA Article 10(1)  
- **Urgent**: Patch axios for CVE-2026-25639, CVE-2025-58754; lodash for CVE-2025-13465; minimatch for CVE-2026-26996 (HIGH severity with PoC) per Article 11(1)  
- **Planned**: Address remaining HIGH severity CVEs in axios (CVE-2025-54371) and js-yaml (CVE-2025-64718)  
- **Hygiene**: Maintain SBOM accuracy and update per CRA Article 10(6) to ensure ongoing vulnerability tracking and reporting compliance