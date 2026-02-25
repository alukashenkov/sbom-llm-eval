### 1. SBOM Overview  
- **Product**: sbom-gurobi-engine-v12.0.3rc0 (SPDX format)  
- **Scan date**: 2025-07-11  
- **Packages**: 12 total, 3 affected  
- **Unique CVEs**: 62 (CRITICAL: 3, HIGH: 23, MEDIUM: 32, LOW: 3, NONE: 1)  

### 2. CRA Mandatory Reporting (Article 14)  
- **No CRA Article 14 mandatory reporting triggers** (no wildExploited or CISA KEV entries).  

### 3. Exploit Assessment  
- **Top exploited CVEs**:  
  - `CVE-2025-4517` (CRITICAL, 9.4 CVSS, EPSS 0.00071) - Arbitrary writes via tarfile  
  - `CVE-2025-15467` (CRITICAL, 9.8 CVSS, EPSS 0.00672) - OpenSSL stack buffer overflow  
  - `CVE-2025-4138` (HIGH, 7.5 CVSS, EPSS 0.00077) - Symlink target bypass  
  - `CVE-2024-6232` (HIGH, 7.5 CVSS, EPSS 0.02874) - ReDoS in tarfile parsing  
  - `CVE-2025-4330` (HIGH, 7.5 CVSS, EPSS 0.00298) - Extraction filter bypass  
- **Additional CVEs with PoC**: 24 total (8 GitHub, 10 PacketStorm, 6 HackerOne).  

### 4. Critical & High Findings  
- `CVE-2025-4517` (CRITICAL, 9.4 CVSS, EPSS 0.00071) - python@3.11.4  
- `CVE-2025-15467` (CRITICAL, 9.8 CVSS, EPSS 0.00672) - openssl@3.0.16  
- `CVE-2024-8088` (HIGH, 8.7 CVSS, EPSS 0.00154) - python@3.11.4  
- `CVE-2024-4032` (HIGH, 7.5 CVSS, EPSS 0.01127) - python@3.11.4  
- `CVE-2024-9287` (HIGH, 7.8 CVSS, EPSS 0.00062) - python@3.11.4  
- `CVE-2025-9086` (HIGH, 7.5 CVSS, EPSS 0.00035) - curl@8.14.1  
- **And 17 more across 3 packages**.  

### 5. Risk Distribution  
- **Severity**: CRITICAL (3), HIGH (23), MEDIUM (32), LOW (3)  
- **Top affected packages**:  
  1. python@3.11.4 (40 CVEs)  
  2. openssl@3.0.16 (12 CVEs)  
  3. curl@8.14.1 (10 CVEs)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `CVE-2025-4517` (CRITICAL) and `CVE-2025-15467` (CRITICAL) per Article 11(3).  
2. **Urgent**: Address exploited HIGHs (`CVE-2025-4138`, `CVE-2024-6232`) with target versions.  
3. **Planned**: Remediate remaining HIGHs (e.g., `CVE-2024-9287`, `CVE-2025-9086`).  
4. **Hygiene**: Update SBOM for python@3.11.4 (40 CVEs) per Article 10(6).  
5. **Monitor**: Track EPSS >5% (`CVE-2024-6232` at 2.87%).