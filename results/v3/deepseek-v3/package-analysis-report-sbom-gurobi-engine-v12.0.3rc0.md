# Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0 (SPDX, 2025-07-11)

## 1. SBOM Overview  
Scanned 12 packages with 3 affected (25%). Found 38 unique CVEs: 1 CRITICAL, 14 HIGH, 19 MEDIUM, 4 LOW.  

## 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified (no wildExploited=true or cisa_kev entries found).  

## 3. Exploit Availability Assessment  
Top PoC-bearing CVEs:  
- [CVE-2025-15467] openssl@3.0.16 — CRITICAL 9.4 (EPSS 0.67%) — Stack overflow in CMS AuthEnvelopedData (githubexploit, packetstorm)  
- [CVE-2025-4517] python@3.11.4 — CRITICAL 9.4 (EPSS 0.07%) — Arbitrary filesystem writes via tarfile (githubexploit)  
- [CVE-2025-4138] python@3.11.4 — HIGH 7.5 (EPSS 0.07%) — Symlink target bypass (githubexploit, packetstorm)  
- [CVE-2025-4330] python@3.11.4 — HIGH 7.5 (EPSS 0.25%) — Extraction filter bypass (githubexploit)  
- [CVE-2024-6232] python@3.11.4 — HIGH 7.5 (EPSS 2.87%) — ReDoS in tarfile parsing (githubexploit)  
5 additional CVEs have exploit evidence.  

## 4. Critical & High Findings  
- [CVE-2007-4559] python@3.11.4 — CRITICAL 9.8 (EPSS 90.6%) — Directory traversal in tarfile  
- [CVE-2024-9287] python@3.11.4 — HIGH 7.8 (EPSS 0.06%) — venv path injection  
- [CVE-2024-8088] python@3.11.4 — HIGH 8.7 (EPSS 0.15%) — zipfile infinite loop  
- [CVE-2024-4032] python@3.11.4 — HIGH 7.5 (EPSS 1.13%) — Incorrect IPv4/IPv6 range checks  
and 6 more HIGH findings across 3 packages.  

## 5. Risk Distribution  
Severity (unique CVEs): CRITICAL 2, HIGH 12, MEDIUM 19, LOW 5.  
Most affected packages:  
1. python@3.11.4 — 32 advisories  
2. openssl@3.0.16 — 5 advisories  
3. curl@8.14.1 — 1 advisory  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch python to ≥3.11.5 (fixes CVE-2007-4559 critical dir traversal)  
2. **Urgent**: Upgrade openssl to ≥3.0.17 (mitigates CVE-2025-15467 critical stack overflow)  
3. **Planned**: Replace vulnerable tarfile usage with secure alternatives  
4. **SBOM Hygiene**: Consolidate duplicate python advisories (154 → 38 unique CVEs)  
5. **Monitoring**: Track CVE-2025-15467 exploit development (active PoCs)  

Priority rationale: Critical tarfile vulnerability (EPSS 90.6%) poses imminent risk, followed by OpenSSL stack overflow with public exploits. Python dominates the risk profile with 84% of findings.