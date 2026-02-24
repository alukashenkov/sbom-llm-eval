# Vulnerability Summary for sbom-grbrsm_ui-v12.0.3rc0 (SPDX, scanned 2025-07-11)  

## 1. SBOM Overview  
Analysis covers 338 packages with 7 affected (2.1% vulnerable). Unique CVEs: 1 CRITICAL (CVE-2025-7783), 5 HIGH, and 3 MEDIUM severity.  

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no CVEs with wildExploited=true or CISA KEV entries).  

## 3. Exploit Availability Assessment  
2 CVEs have exploit evidence:  
- [CVE-2025-7783] form-data@4.0.3 (CRITICAL, CVSS 9.4) - Unsafe random boundary selection  
- [CVE-2025-54371] axios@1.10.0 (HIGH, CVSS 7.5) - Transitive form-data vulnerability  

## 4. Critical & High Findings  
- [CVE-2025-7783] form-data@4.0.3 (CRITICAL, CVSS 9.4, EPSS 0.00177)  
- [CVE-2026-25639] axios@1.10.0 (HIGH, CVSS 8.7) - Prototype pollution  
- [CVE-2026-26996] minimatch@7.4.6 (HIGH, CVSS 8.7) - ReDoS  
- [CVE-2025-13465] lodash@4.17.21 (HIGH, CVSS 8.2) - Prototype pollution  
and 2 more HIGH findings across 3 packages.  

## 5. Risk Distribution  
Severity: 1 CRITICAL, 5 HIGH, 3 MEDIUM. Top affected:  
- axios@1.10.0 (4 advisories, 3 CVEs)  
- form-data@4.0.3 (1 CRITICAL CVE)  
- minimatch@7.4.6 (2 advisories, 1 HIGH CVE)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch form-data@4.0.3 (CRITICAL CVE-2025-7783)  
2. **Urgent**: Update axios@1.10.0 (3 HIGH CVEs including exploitable CVE-2025-54371)  
3. **Planned**: Replace minimatch@7.4.6 (ReDoS vulnerability)  
4. **SBOM Hygiene**: Review transitive dependency form-data usage in axios  
5. **Monitor**: lodash@4.17.21 (prototype pollution) for exploit developments  

Prioritize by: CRITICAL → exploit evidence → CVSS ≥8.0.