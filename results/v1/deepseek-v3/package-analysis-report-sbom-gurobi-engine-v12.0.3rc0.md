# Vulnerability Summary Report - EU Cyber Resilience Act (CRA) Compliance  

**Product:** sbom-gurobi-engine-v12.0.3rc0  
**Format:** SPDX  
**Scan Date:** 2025-07-11  
**Total Packages:** 12  
**Affected Packages:** 3 (25%)  
**Total Advisories:** 154  

## Severity Distribution  
- **CRITICAL:** 2  
- **HIGH:** 18  
- **MEDIUM:** 28  
- **LOW:** 2  

---

## 1. CRA Mandatory Reporting Triggers (Article 14)  
*Vulnerabilities actively exploited (wildExploited=true) or listed in CISA KEV require notification within 24h → 72h → 14d*  

**No CRA mandatory reporting triggers identified.**  

---

## 2. Exploit Availability Assessment  
### Public Proof-of-Concept Available (githubexploit/exploitdb)  
- **[CVE-2025-4517]** CRITICAL (CVSS 9.4) - Python tarfile arbitrary filesystem writes (11 GitHub PoCs)  
- **[CVE-2025-4138]** HIGH (CVSS 7.5) - Python tarfile symlink bypass (7 GitHub PoCs + PacketStorm)  
- **[CVE-2025-15467]** CRITICAL (CVSS 9.8) - OpenSSL stack buffer overflow (2 GitHub PoCs + 2 PacketStorm)  

### Exploit Framework Integration  
- **[CVE-2024-6232]** HIGH (CVSS 7.5) - Python tarfile ReDoS (GitHub exploit)  

### Bug Bounty Disclosed (hackerone)  
- **[CVE-2025-15079]** MEDIUM (CVSS 5.3) - curl SSH host verification bypass  
- **[CVE-2025-9086]** HIGH (CVSS 7.5) - curl secure cookie leakage  

---

## 3. Critical & High Findings  
*Remaining HIGH+ CVEs without active exploitation evidence*  

- **[CVE-2024-8088]** HIGH (CVSS 8.7) - Python zipfile infinite loop  
- **[CVE-2024-4032]** HIGH (CVSS 7.5) - Python ipaddress incorrect private range detection  
- **[CVE-2025-69420]** HIGH (CVSS 7.5) - OpenSSL timestamp verification flaw  
- **[CVE-2007-4559]** CRITICAL (CVSS 9.8) - Python tarfile directory traversal (EPSS 90.5%)  

---

## 4. Risk Distribution  
**Top Affected Packages:**  
1. Python (3.11.4) - 142 advisories  
2. OpenSSL (3.0.16) - 22 advisories  
3. curl (8.14.1) - 16 advisories  

**Exploitation Landscape:**  
- 15 vulnerabilities with public PoCs  
- 6 vulnerabilities with HackerOne disclosures  
- 5 vulnerabilities with PacketStorm integration  

---

## 5. CRA Compliance Actions  
1. **Immediate Patching**  
   - Upgrade Python to ≥3.11.5 (fixes CVE-2025-4517 critical tarfile flaw)  
   - Update OpenSSL to ≥3.0.17 (fixes CVE-2025-15467 stack overflow)  

2. **Exploit Mitigation**  
   - Disable Python tarfile module if unused  
   - Implement network segmentation for systems using vulnerable OpenSSL versions  

3. **Notification Procedures**  
   - Establish 24/7 contact protocol with ENISA/CSIRT for future KEV-listed vulnerabilities  

4. **SBOM Hygiene**  
   - Implement automated vulnerability scanning for all dependency updates  

5. **Compensating Controls**  
   - Deploy WAF rules to block malicious tar/zip file uploads  
   - Monitor for anomalous filesystem writes  

*Prioritize remediation based on CRA obligations > exploitability > CVSS score.*  

---  
**Word Count:** 598