## 1. SBOM Overview  
Product: `sbom-gurobi-engine-v12.0.3rc0` (SPDX format), scanned 2025-07-11.  
Packages: 12 total / 3 affected.  
Unique CVEs: 62.  
CRA tiers (Art. 3):  
- EXPLOITABLE: 35  
- VULNERABILITY: 27  

---

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**  
No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
3 CVEs meet severe-incident criteria (CVSS≥9 + AV:N + CIA:H):  
- `CVE-2007-4559` (python@3.11.4): CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), EPSS 0.90582, fix: "Python directory traversal vulnerability in tarfile module"  
- `CVE-2025-15467` (openssl@3.0.16): CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), EPSS 0.00672, fix: "Upgrade OpenSSL 3.0.19 or newer"  
- `CVE-2025-4517` (python@3.11.4): CVSS 9.4 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L), EPSS 0.00071, fix: "Arbitrary writes via tarfile realpath overflow"  
Action: ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

---

## 3. Art. 3(41) Exploitability Assessment  
24 CVEs with PoC/exploits (8 GitHub, 10 PacketStorm, 6 HackerOne). Top 5 EXPLOITABLE CVEs:  
1. `CVE-2007-4559` (python): CVSS 9.8, EPSS 0.90582, 863 days public  
2. `CVE-2025-15467` (openssl): CVSS 9.8, EPSS 0.00672, 32 days public  
3. `CVE-2025-4517` (python): CVSS 9.4, EPSS 0.00071, 268 days public  
4. `CVE-2024-6232` (python): CVSS 7.5, EPSS 0.02874, 543 days public  
5. `CVE-2024-4032` (python): CVSS 7.5, EPSS 0.01127, 619 days public  

---

## 4. Critical & High Findings (Annex I Part II §2)  
Remaining CRITICAL/HIGH CVEs:  
- `CVE-2023-36632` (python): CVSS 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), EPSS 0.00112  
- `CVE-2023-41105` (python): CVSS 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N), EPSS 0.0037  
- `CVE-2024-8088` (python): CVSS 8.7 (AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/SC:N/VI:N/SI:N/VA:H), EPSS 0.00154  
...and 17 more across 3 packages.  

---

## 5. Risk Distribution & Age Risk  
Severity: CRITICAL (3), HIGH (23), MEDIUM (32), LOW (3).  
Top affected packages:  
1. python@3.11.4 (40 CVEs)  
2. openssl@3.0.16 (12 CVEs)  
3. curl@8.14.1 (10 CVEs)  

Oldest unpatched CRITICAL/HIGH:  
1. `CVE-2023-36632` (python): 979 days public  
2. `CVE-2023-41105` (python): 920 days public  
3. `CVE-2007-4559` (python): 863 days public  

---

## 6. CRA Defensible-Practice Actions  
1. **Immediate (Art. 14 + Annex I Part II §2)**: Patch Track 2 CVEs (`CVE-2007-4559`, `CVE-2025-15467`, `CVE-2025-4517`); submit ENISA notifications.  
2. **Urgent (Annex I Part II §2)**: Patch EXPLOITABLE CRITICAL/HIGH CVEs (e.g., `CVE-2024-6232` in python).  
3. **Planned**: Remediate HIGH/MEDIUM by age (prioritize `CVE-2023-36632`).  
4. **SBOM update (Annex I Part II §1)**: Refresh SPDX/CycloneDX SBOM post-remediation.  
5. **Public advisory (Annex I Part II §4)**: Publish patched versions and CVE details.  
6. **CVD hygiene (Annex I Part II §5–6)**: Verify disclosure policy and security contacts.