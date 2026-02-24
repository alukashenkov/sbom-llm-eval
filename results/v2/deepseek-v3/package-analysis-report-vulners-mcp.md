## 1. SBOM Overview  
CycloneDX SBOM for container image `vulners-mcp` (sha256:1cb7222c...) scanned on 2026-02-24. Total packages: 560 (20 affected). Unique CVEs: 9 CRITICAL, 22 HIGH, 34 MEDIUM, 4 LOW severity.

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no wildExploited=true or cisa_kev entries).

## 3. Exploit Availability Assessment  
Top 5 exploitable CVEs:  
- [CVE-2025-48384] git@2.4.7 — CVSS 8.0 — EPSS 0.46% — RCE via malformed config (9 PoCs)  
- [CVE-2025-15467] openssl@3.5.4 — CVSS 9.8 — EPSS 0.67% — Stack overflow in CMS parsing (4 PoCs)  
- [CVE-2025-68973] gnupg@2.4.7 — CVSS 7.8 — EPSS 0.02% — Armor filter OOB write  
- [CVE-2025-53014] imagemagick@7.1.1 — CVSS 9.8 — EPSS 0.03% — Heap buffer overflow  
- [CVE-2025-5244] binutils@2.44 — CVSS 7.8 — EPSS 0.03% — elflink.c buffer overflow  
15 additional CVEs have exploit evidence.

## 4. Critical & High Findings  
- [CVE-2025-48385] git@2.4.7 — CVSS 8.6 — EPSS 0.04% — Bundle URI injection  
- [CVE-2025-66628] imagemagick@7.1.1 — CVSS 7.5 — EPSS 0.05% — TIM image integer overflow  
- [CVE-2025-69420] openssl@3.5.4 — CVSS 8.2 — EPSS 0.07% — Type confusion in TS verification  
- [CVE-2025-53014] imagemagick@7.1.1 — CVSS 9.8 — EPSS 0.03% — Heap buffer overflow  
and 18 more HIGH findings across 6 packages.

## 5. Risk Distribution  
Severity: CRITICAL (9), HIGH (22), MEDIUM (34), LOW (4).  
Top affected:  
1. openssl (11 advisories)  
2. imagemagick (9 advisories)  
3. binutils (6 advisories)

## 6. CRA Compliance Actions  
1. **Immediate**: Patch git to ≥2.4.9 (CVE-2025-48384 RCE)  
2. **Urgent**: Upgrade openssl to ≥3.5.5 (CVE-2025-15467 CRITICAL)  
3. **Urgent**: Update imagemagick to ≥7.1.2-15 (multiple heap overflows)  
4. **Planned**: Replace vulnerable binutils@2.44  
5. **SBOM hygiene**: Remove unused packages (20/560 have advisories)  

Prioritize git/openssl patches within 72h per CRA Article 14 exploitability requirements.