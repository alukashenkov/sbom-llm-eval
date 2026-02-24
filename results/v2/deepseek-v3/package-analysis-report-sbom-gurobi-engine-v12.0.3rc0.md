# Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0 (SPDX, 2025-07-11)

## 1. SBOM Overview  
Scanned 12 packages, with 3 affected (25%). Found 154 advisories referencing **42 unique CVEs**:  
- CRITICAL: 2  
- HIGH: 17  
- MEDIUM: 20  
- LOW: 3  

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no CVEs with wildExploited=true or cisa_kev sources).  

## 3. Exploit Availability Assessment  
Top 5 CVEs with PoC evidence:  
1. [CVE-2025-4517] CRITICAL (CVSS 9.4) - Arbitrary filesystem writes via tarfile (11 GitHub PoCs)  
2. [CVE-2025-15467] CRITICAL (CVSS 9.8) - OpenSSL stack buffer overflow (2 GitHub/PacketStorm PoCs)  
3. [CVE-2025-4138] HIGH (CVSS 7.5) - Symlink target bypass (7 GitHub/PacketStorm PoCs)  
4. [CVE-2024-6232] HIGH (CVSS 7.5) - Python tarfile ReDoS (GitHub PoC)  
5. [CVE-2025-4330] HIGH (CVSS 7.5) - Extraction filter bypass (2 GitHub PoCs)  
*7 additional CVEs have exploit evidence.*

## 4. Critical & High Findings  
Remaining critical/high CVEs:  
- [CVE-2024-9287] HIGH (CVSS 7.8) - Python venv path injection  
- [CVE-2024-4032] HIGH (CVSS 7.5) - Python IP address misclassification  
- [CVE-2025-69419] HIGH (CVSS 7.4) - OpenSSL PKCS#12 out-of-bounds write  
- [CVE-2025-69420] HIGH (CVSS 7.5) - OpenSSL type confusion  
*and 13 more HIGH findings across Python/OpenSSL/curl.*

## 5. Risk Distribution  
Top affected packages:  
1. **python@3.11.4**: 28 advisories (7 HIGH)  
2. **openssl@3.0.16**: 12 advisories (2 CRITICAL)  
3. **curl@8.14.1**: 8 advisories (1 HIGH)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch OpenSSL to ≥3.0.17 (CVE-2025-15467 CRITICAL RCE)  
2. **Urgent**: Upgrade Python to ≥3.11.5 (CVE-2025-4517 CRITICAL file write)  
3. **Planned**: Update curl to ≥8.15.0 (CVE-2025-9086 HIGH cookie leak)  
4. **SBOM Hygiene**: Remove duplicate advisories for python@3.11.4  
5. **Monitor**: Track exploit development for CVE-2024-6232 (tarfile ReDoS)  

*Prioritize fixes by: CRA obligations > exploit availability > CVSS severity.*