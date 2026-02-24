# Vulnerability Summary for vulners-mcp (CycloneDX SBOM, 2026-02-24)

## 1. SBOM Overview  
The container image `vulners-mcp` (sha256:1cb7222c81317af65f1a4fb535ccbd3627926d1ab84f583f3358fc841b94ddd9) contains 560 packages, with 20 affected by vulnerabilities. Unique CVE counts by severity:  
- **CRITICAL**: 4  
- **HIGH**: 12  
- **MEDIUM**: 28  
- **LOW**: 6  

## 2. CRA Mandatory Reporting Triggers  
**[CVE-2025-48384] git@1:2.47.3-0+deb13u1** — CVSS 8.0 (EPSS 0.46%)  
Active exploitation (CISA KEV listed) with public PoCs allowing arbitrary code execution via config injection.  

## 3. Exploit Availability Assessment  
Top 5 CVEs with exploit evidence:  
1. **[CVE-2025-15467] openssl@3.5.4** — CVSS 9.8 (githubexploit, packetstorm)  
2. **[CVE-2025-48384] git@1:2.47.3** — CVSS 8.0 (10+ PoCs)  
3. **[CVE-2025-11187] openssl@3.5.4** — CVSS 7.5 (packetstorm)  
4. **[CVE-2025-69420] openssl@3.5.4** — CVSS 8.2 (packetstorm)  
5. **[CVE-2025-68973] gnupg@2.4.7** — CVSS 7.8 (githubexploit)  
*7 additional CVEs have exploit evidence.*  

## 4. Critical & High Findings  
- **[CVE-2026-22770] imagemagick@8:7.1.1.43** — CVSS 9.8 (EPSS 0.065%)  
- **[CVE-2025-5244] binutils@2.44-3** — CVSS 7.8 (EPSS 0.03%)  
- **[CVE-2025-55298] imagemagick@8:7.1.1.43** — CVSS 8.8 (EPSS 0.43%)  
- **[CVE-2025-48385] git@1:2.47.3** — CVSS 8.6 (EPSS 0.039%)  
*and 8 more HIGH findings across 5 packages.*  

## 5. Risk Distribution  
**Severity Distribution**:  
- CRITICAL: 4  
- HIGH: 12  
- MEDIUM: 28  
- LOW: 6  

**Top Affected Packages**:  
1. openssl (16 advisories)  
2. imagemagick (14 advisories)  
3. git (3 advisories)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch git to ≥2.47.3-0+deb13u2 (CVE-2025-48384)  
2. **Urgent**: Upgrade openssl to ≥3.5.4-1~deb13u3 (CVE-2025-15467)  
3. **Urgent**: Update imagemagick to ≥8:7.1.1.43+dfsg1-1+deb13u6 (CVE-2026-22770)  
4. **Planned**: Replace binutils with patched version (CVE-2025-5244)  
5. **SBOM Hygiene**: Rebuild container with updated base image  

Prioritization based on CRA obligations, exploit availability, and CVSS scores.