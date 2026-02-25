## 1. SBOM Overview  
- **Product**: vulners-mcp (container)  
- **Format**: CycloneDX  
- **Scan Date**: 2026-02-24  
- **Packages**: 560 total, 20 affected  
- **Unique CVEs**: 188 (CRITICAL: 14, HIGH: 82, MEDIUM: 79, LOW: 12, NONE: 1)  

## 2. CRA Mandatory Reporting (Article 14)  
- **CVE-2025-48384** (git@1:2.47.3-0+deb13u1): CVSS 8, EPSS 0.00456  
  - Wild-exploited + CISA KEV listed  
  - **Action**: Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.  

## 3. Exploit Assessment  
- **Top 5 Exploited CVEs**:  
  1. **CVE-2025-48384** (git): 9 GitHub PoCs, CISA KEV  
  2. **CVE-2025-15467** (openssl): 2 GitHub PoCs, 2 PacketStorm  
  3. **CVE-2024-41817** (imagemagick): 2 GitHub PoCs  
  4. **CVE-2025-11187** (openssl): 1 PacketStorm PoC  
  5. **CVE-2025-5399** (curl): 1 HackerOne PoC  
- **Additional**: 28 more CVEs have PoC evidence (GitHub/PacketStorm/HackerOne).  

## 4. Critical & High Findings  
1. **CVE-2026-25897** (imagemagick): CVSS 9.8, EPSS 0.00038  
2. **CVE-2026-26284** (imagemagick): CVSS 9.1, EPSS 0.00037  
3. **CVE-2025-53101** (imagemagick): CVSS 9.8, EPSS 0.00069  
4. **CVE-2025-15467** (openssl): CVSS 9.8, EPSS 0.00672  
5. **CVE-2025-48385** (git): CVSS 8.6, EPSS 0.00039  
6. **CVE-2025-55298** (imagemagick): CVSS 8.8, EPSS 0.0043  
7. **CVE-2025-57803** (imagemagick): CVSS 8.8, EPSS 0.00075  
8. **CVE-2025-53014** (imagemagick): CVSS 9.8, EPSS 0.00031  
- **And 74 more** across 15 packages.  

## 5. Risk Distribution  
- **Severity**: CRITICAL (14), HIGH (82), MEDIUM (79), LOW (12)  
- **Top Affected Packages**:  
  1. imagemagick (77 CVEs)  
  2. binutils (32 CVEs)  
  3. libxml2 (17 CVEs)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch CVE-2025-48384 (git) per Article 14(2).  
2. **Urgent**: Update openssl to mitigate CVE-2025-15467 (CRITICAL, exploited).  
3. **Planned**: Upgrade imagemagick to address 9.8/8.8 CVEs (CVE-2026-25897, CVE-2025-55298).  
4. **Hygiene**: Refresh SBOM post-patching per Article 10(6).  
5. **Monitor**: Track exploit activity on CVE-2024-41817 (ImageMagick).