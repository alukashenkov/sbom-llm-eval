## 1. SBOM Overview  
- **Product**: vulners-mcp (container)  
- **Format**: CycloneDX  
- **Scan date**: 2026-02-24  
- **Packages**: 560 total, 20 affected  
- **Unique CVEs**: 188 (CRITICAL: 12, HIGH: 76, MEDIUM: 87, LOW: 12, NONE: 1)  

## 2. CRA Mandatory Reporting (Article 14)  
- **CVE-2025-48384** (git@1:2.47.3-0+deb13u1, CVSS 8, EPSS 0.00456)  
  - Wild-exploited + CISA KEV listed  
  - **Action**: Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.  

## 3. Exploit Assessment  
- **PoC evidence**: 33 CVEs (13 Packetstorm, 9 GitHub, 7 HackerOne, 1 CISA KEV, 1 Gitee, 1 Nuclei, 1 Kitploit)  
- **Top exploited CVEs**:  
  1. **CVE-2025-15467** (openssl, CRITICAL 9.8, EPSS 0.00672) - GitHub/Packetstorm PoC  
  2. **CVE-2025-48384** (git, HIGH 8, EPSS 0.00456) - Wild-exploited  
  3. **CVE-2025-5399** (curl, HIGH 7.5, EPSS 0.00146) - HackerOne PoC  
  4. **CVE-2025-69419** (openssl, HIGH 7.4, EPSS 0.00056) - Packetstorm PoC  
  5. **CVE-2025-69420** (openssl, HIGH 7.5, EPSS 0.0007) - Packetstorm PoC  

## 4. Critical & High Findings  
- **CVE-2026-22770** (imagemagick, CRITICAL 9.8, EPSS 0.00065)  
- **CVE-2025-55298** (imagemagick, HIGH 8.8, EPSS 0.0043)  
- **CVE-2025-57803** (imagemagick, HIGH 8.8, EPSS 0.00075)  
- **CVE-2025-5244** (binutils, HIGH 7.8, EPSS 0.0003)  
- **CVE-2025-5245** (binutils, HIGH 7.8, EPSS 0.00031)  
- **and 68 more across 15 packages**  

## 5. Risk Distribution  
- **Severity**: CRITICAL (12), HIGH (76), MEDIUM (87), LOW (12)  
- **Top affected packages**:  
  1. imagemagick (77 CVEs)  
  2. binutils (32 CVEs)  
  3. libxml2 (17 CVEs)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch CVE-2025-48384 (git) per Article 14(2)  
2. **Urgent**: Patch exploited CRITICAL/HIGH (CVE-2025-15467, CVE-2025-48384)  
3. **Planned**: Address remaining HIGHs (e.g., imagemagick CVEs)  
4. **Hygiene**: Update SBOM per Article 10(6)  
5. **Monitor**: Track EPSS ≥0.1% (CVE-2025-15467, CVE-2025-48384)