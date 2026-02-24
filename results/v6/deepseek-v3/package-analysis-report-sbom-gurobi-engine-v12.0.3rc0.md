### 1. SBOM Overview  
- **Product**: sbom-gurobi-engine-v12.0.3rc0 (SPDX format)  
- **Scan date**: 2025-07-11  
- **Packages**: 12 total, 3 affected  
- **Unique CVEs**: 62 (CRITICAL: 3, HIGH: 23, MEDIUM: 32, LOW: 3, NONE: 1)  

### 2. CRA Mandatory Reporting (Article 14)  
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).  

### 3. Exploit Assessment  
- **Top exploited CVEs**:  
  - `CVE-2025-4517` (CRITICAL, CVSS 9.4, EPSS 0.00071) - Arbitrary writes via tarfile realpath overflow (11 PoCs)  
  - `CVE-2025-4138` (HIGH, CVSS 7.5, EPSS 0.00066) - Extraction filter bypass (7 PoCs)  
  - `CVE-2025-4330` (HIGH, CVSS 7.5, EPSS 0.00253) - Extraction filter bypass (2 PoCs)  
  - `CVE-2024-6232` (HIGH, CVSS 7.5, EPSS 0.02874) - ReDoS in tarfile parsing (1 PoC)  
  - `CVE-2025-15467` (CRITICAL, CVSS 9.8, EPSS 0.00672) - OpenSSL stack buffer overflow (2 PoCs)  
- **Additional CVEs**: 19 more CVEs have PoC evidence (GitHub, PacketStorm, HackerOne).  

### 4. Critical & High Findings  
- `CVE-2025-4517` (CRITICAL, CVSS 9.4, EPSS 0.00071) - python@3.11.4  
- `CVE-2025-15467` (CRITICAL, CVSS 9.8, EPSS 0.00672) - openssl@3.0.16  
- `CVE-2025-4138` (HIGH, CVSS 7.5, EPSS 0.00066) - python@3.11.4  
- `CVE-2025-4330` (HIGH, CVSS 7.5, EPSS 0.00253) - python@3.11.4  
- `CVE-2024-6232` (HIGH, CVSS 7.5, EPSS 0.02874) - python@3.11.4  
- `CVE-2025-9086` (HIGH, CVSS 7.5, EPSS 0.00035) - curl@8.14.1  
- **And 17 more** across 3 packages.  

### 5. Risk Distribution  
- **Severity**: CRITICAL (3), HIGH (23), MEDIUM (32), LOW (3)  
- **Top affected packages**:  
  1. python@3.11.4 (40 CVEs)  
  2. openssl@3.0.16 (12 CVEs)  
  3. curl@8.14.1 (10 CVEs)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch `CVE-2025-4517` (CRITICAL, tarfile exploit) and `CVE-2025-15467` (CRITICAL, OpenSSL stack overflow).  
2. **Urgent**: Address exploited HIGH CVEs (`CVE-2025-4138`, `CVE-2025-4330`, `CVE-2024-6232`) in python@3.11.4.  
3. **Planned**: Remediate remaining HIGH CVEs (e.g., `CVE-2025-9086` in curl).  
4. **Hygiene**: Update SBOM per CRA Article 10(6) to track transitive dependencies.  
5. **Monitoring**: Track EPSS scores for MEDIUM CVEs with rising exploitability (e.g., `CVE-2024-6232`).