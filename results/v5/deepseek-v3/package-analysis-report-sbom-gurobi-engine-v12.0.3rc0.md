# Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0 (SPDX SBOM, scanned 2025-07-11)

## 1. SBOM Overview  
The SBOM contains 12 total packages, with 3 affected packages (25%) containing vulnerabilities. Analysis revealed 62 unique CVEs: 3 CRITICAL, 23 HIGH, 32 MEDIUM, 3 LOW, and 1 NONE severity findings.

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no CVEs with active exploitation or CISA KEV listing).

## 3. Exploit Availability Assessment  
24 CVEs have published PoCs (8 GitHub exploits, 10 Packet Storm, 6 HackerOne). Top exploitable CVEs:  
- CVE-2025-4517 (CRITICAL, CVSS 9.4) - Arbitrary writes via tarfile overflow  
- CVE-2025-15467 (CRITICAL, CVSS 9.8) - OpenSSL stack buffer overflow  
- CVE-2024-6232 (HIGH, CVSS 7.5) - Python tarfile ReDoS  
- CVE-2025-4138 (HIGH, CVSS 7.5) - Python symlink extraction bypass  
- CVE-2025-9086 (HIGH, CVSS 7.5) - curl cookie security bypass  

## 4. Critical & High Findings  
Remaining HIGH+ severity vulnerabilities:  
- CVE-2024-9287 (HIGH, CVSS 7.8) - Python venv path injection  
- CVE-2025-4330 (HIGH, CVSS 7.5) - Python tarfile filter bypass  
- CVE-2025-13836 (HIGH, CVSS 7.5) - Python HTTP client DoS  
- CVE-2025-69420 (HIGH, CVSS 7.5) - OpenSSL type confusion  
...and 16 more HIGH findings across 3 packages.

## 5. Risk Distribution  
Top affected packages:  
- python@3.11.4 (40 CVEs)  
- openssl@3.0.16 (12 CVEs)  
- curl@8.14.1 (10 CVEs)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch python@3.11.4 → 3.11.5+ (CVE-2025-4517 critical RCE)  
2. **Urgent**: Upgrade openssl@3.0.16 → 3.0.17+ (CVE-2025-15467 critical overflow)  
3. **Planned**: Update curl@8.14.1 → 8.14.2+ (multiple protocol security bypasses)  
4. **SBOM Hygiene**: Remove unused python tarfile/zipfile module dependencies  
5. **Monitoring**: Track CVE-2025-15467 exploit development (active PoCs)  

Prioritization based on CRA obligations > exploitability > CVSS severity.