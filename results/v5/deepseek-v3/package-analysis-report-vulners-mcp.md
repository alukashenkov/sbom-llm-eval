# Vulnerability Summary for vulners-mcp (CycloneDX SBOM)  
**Scan Date:** 2026-02-24  
**Total Packages:** 560 (20 affected)  
**Unique CVEs:** 188 (12 CRITICAL, 76 HIGH, 87 MEDIUM)  

## 1. CRA Mandatory Reporting Triggers (Article 14)  
**CVE-2025-48384** (git@1:2.47.3-0+deb13u1)  
- **CVSS:** 8.0 (HIGH) | **EPSS:** 0.46%  
- **Trigger:** Wild exploitation + CISA KEV listing  
- **Deadlines:** Initial ENISA/CSIRT notification within 24h, detailed report within 72h, final patch within 14 days  

## 2. Exploit Availability Assessment  
33 CVEs have Proof-of-Concept (PoC) evidence:  
- **Top 5 Exploitable CVEs:**  
  1. CVE-2025-15467 (CRITICAL 9.8, openssl) - GitHub/PacketStorm PoCs  
  2. CVE-2025-48384 (HIGH 8.0, git) - Multiple GitHub exploits  
  3. CVE-2026-22770 (CRITICAL 9.8, imagemagick)  
  4. CVE-2025-5244 (HIGH 7.8, binutils)  
  5. CVE-2025-6021 (HIGH 7.5, libxml2)  

## 3. Critical & High Findings  
**Remaining Critical/High CVEs:**  
- CVE-2025-53014 (CRITICAL 9.8, imagemagick)  
- CVE-2025-53101 (CRITICAL 9.8, imagemagick)  
- CVE-2025-55298 (HIGH 8.8, imagemagick)  
- CVE-2025-57803 (HIGH 8.8, imagemagick)  
- CVE-2025-66628 (HIGH 7.5, imagemagick)  
- CVE-2025-9240 (HIGH 7.5, openssl)  
- CVE-2025-69420 (HIGH 7.5, openssl)  
*(and 4 more HIGH findings across 3 packages)*  

## 4. Risk Distribution  
**Top Affected Packages:**  
1. imagemagick (77 CVEs)  
2. binutils (32 CVEs)  
3. libxml2 (17 CVEs)  
4. openssl (16 CVEs)  
5. curl (11 CVEs)  

## 5. CRA Compliance Actions  
1. **Immediate:** Patch git@1:2.47.3-0+deb13u1 → 2.47.4+ (CVE-2025-48384)  
2. **Urgent:** Upgrade imagemagick to 7.1.2-15+ (6 CRITICAL/HIGH fixes)  
3. **Planned:** Update openssl to 3.5.5+ (4 HIGH severity CVEs)  
4. **SBOM Hygiene:** Remove deprecated tar@1.35+dfsg-3.1 (7 HIGH vulns)  
5. **Monitoring:** Track exploit development for CVE-2025-15467  

*Prioritized by CRA obligations → exploitability → CVSS severity*