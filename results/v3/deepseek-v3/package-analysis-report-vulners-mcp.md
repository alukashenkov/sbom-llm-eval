## 1. SBOM Overview  
Container image `vulners-mcp` (CycloneDX, scanned 2026-02-24) contains 560 packages with 20 affected (3.6%). Found 369 advisories covering 112 unique CVEs: CRITICAL (9), HIGH (27), MEDIUM (63), LOW (13).  

## 2. CRA Mandatory Reporting Triggers (Article 14)  
**[CVE-2025-48384]** git@1:2.47.3-0+deb13u1 — CVSS 8.0 — EPSS 0.46% — Arbitrary code execution via malformed Git config (CISA KEV-listed, 9 PoCs on GitHub).  
**⚠️ Immediate ENISA notification required** (24h deadline).  

## 3. Exploit Availability Assessment  
1. [CVE-2025-15467] openssl@3.5.4 — CVSS 9.8 — Stack buffer overflow (2 GitHub PoCs)  
2. [CVE-2025-48384] git@2.47.3 — CVSS 8.0 — Config injection (9 PoCs)  
3. [CVE-2026-22770] imagemagick@7.1.1 — CVSS 9.8 — Heap overflow  
4. [CVE-2025-5244] binutils@2.44 — CVSS 7.8 — Buffer overflow  
5. [CVE-2025-68973] gnupg@2.4.7 — CVSS 7.8 — OOB write  
*15 additional CVEs have exploit evidence.*  

## 4. Critical & High Findings  
- [CVE-2025-53014] imagemagick@7.1.1 — CVSS 9.8 — Heap buffer overflow  
- [CVE-2025-53101] imagemagick@7.1.1 — CVSS 9.8 — Path traversal  
- [CVE-2025-55298] imagemagick@7.1.1 — CVSS 8.8 — Format string bug  
- [CVE-2025-5245] binutils@2.44 — CVSS 7.8 — Debug.c overflow  
*4 more HIGH in openssl, 3 in libxml2.*  

## 5. Risk Distribution  
Severity: CRITICAL (9), HIGH (27), MEDIUM (63), LOW (13).  
Top affected:  
1. openssl (32 advisories)  
2. imagemagick (29 advisories)  
3. binutils (15 advisories)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch git to 2.47.4 (CVE-2025-48384, CISA KEV)  
2. **Urgent**: Upgrade openssl to 3.5.5 (CVE-2025-15467)  
3. **Urgent**: Update imagemagick to 7.1.2-15 (6 CRITICAL/HIGH CVEs)  
4. **Planned**: Replace binutils 2.44 with patched version  
5. **SBOM hygiene**: Remove unused imagemagick coders (webp, emf)  

*Prioritize git/openssl patches within 72h per CRA Article 14.*