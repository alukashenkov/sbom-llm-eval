# Vulnerability Summary for sbom-gurobi-engine-v12.0.3rc0 (SPDX, 2025-07-11)

## 1. SBOM Overview  
The SBOM for sbom-gurobi-engine-v12.0.3rc0 (SPDX format, scanned 2025-07-11) includes 12 total packages, with 3 affected by vulnerabilities. After deduplication, there are:  
- **1 CRITICAL** (CVE-2025-4517)  
- **12 HIGH** (including CVE-2025-15467, CVE-2024-8088)  
- **15 MEDIUM** (including CVE-2025-9230, CVE-2025-13836)  
- **2 LOW** severity CVEs.

## 2. CRA Mandatory Reporting Triggers  
**No CRA mandatory reporting triggers identified** (no advisories with `wildExploited=true` or `cisa_kev` in pocSources).

## 3. Exploit Availability Assessment  
Top 5 CVEs with PoC evidence:  
1. [CVE-2025-4517] Python@3.11.4 — CVSS 9.4 (CRITICAL) — EPSS 0.00071 — Arbitrary filesystem writes via tarfile (11 GitHub exploits)  
2. [CVE-2025-15467] OpenSSL@3.0.16 — CVSS 9.8 (CRITICAL) — EPSS 0.00672 — Stack buffer overflow in CMS parsing (2 GitHub, 2 PacketStorm)  
3. [CVE-2025-4138] Python@3.11.4 — CVSS 7.5 (HIGH) — EPSS 0.00066 — Symlink target bypass (7 GitHub, 1 PacketStorm)  
4. [CVE-2024-6232] Python@3.11.4 — CVSS 7.5 (HIGH) — EPSS 0.02874 — ReDoS in tarfile parsing (1 GitHub exploit)  
5. [CVE-2025-4330] Python@3.11.4 — CVSS 7.5 (HIGH) — EPSS 0.00253 — Extraction filter bypass (2 GitHub exploits)  
**7 additional CVEs have exploit evidence** (e.g., CVE-2025-69419, CVE-2025-14524).

## 4. Critical & High Findings  
Remaining HIGH+CVEs without PoCs:  
- [CVE-2024-8088] Python@3.11.4 — CVSS 8.7 — EPSS 0.00154 — Infinite loop in zipfile.Path  
- [CVE-2025-13836] Python@3.11.4 — CVSS 7.5 — EPSS 0.00152 — HTTP client DoS  
- [CVE-2025-9230] OpenSSL@3.0.16 — CVSS 7.5 — EPSS 0.00031 — CMS decryption OOB read  
**and 9 more HIGH findings across 3 packages**.

## 5. Risk Distribution  
Unique CVEs by severity: CRITICAL (1), HIGH (12), MEDIUM (15), LOW (2).  
Top affected packages:  
1. **Python@3.11.4**: 25 advisories (8 HIGH)  
2. **OpenSSL@3.0.16**: 16 advisories (1 CRITICAL, 3 HIGH)  
3. **curl@8.14.1**: 8 advisories (1 HIGH)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch Python to ≥3.11.5 (fixes CVE-2025-4517 CRITICAL tarfile RCE).  
2. **Urgent**: Upgrade OpenSSL to ≥3.0.17 (fixes CVE-2025-15467 CRITICAL stack overflow).  
3. **Planned**: Update curl to ≥8.14.2 (fixes CVE-2025-9086 HIGH cookie security bypass).  
4. **SBOM Hygiene**: Rebuild SBOM after patching to reflect fixed versions.  
5. **Monitoring**: Track exploit development for CVE-2025-15467 (high EPSS percentile).  

Priority rationale: CRITICAL RCE → exploit-tagged HIGH → other HIGH → medium EPSS.