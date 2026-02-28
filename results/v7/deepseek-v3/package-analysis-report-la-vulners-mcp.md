## 1. SBOM Overview  
Product: `la-vulners-mcp` (CycloneDX, scanned 2026-02-24).  
Packages: 97 total / 3 affected.  
Unique CVEs: 7.  
CRA tiers:  
- EXPLOITABLE: 3  
- VULNERABILITY: 4  

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**  
No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
- `CVE-2023-45853` (zlib@1.3.1-r2): CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H). Fix: Upgrade to zlib ≥1.3.1.  
- `CVE-2026-22184` (zlib@1.3.1-r2): CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H). Fix: Upgrade to zlib ≥1.3.1.2.  
Action: Submit ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

## 3. Art. 3(41) Exploitability Assessment  
Top EXPLOITABLE CVEs:  
1. `CVE-2023-45853` (zlib@1.3.1-r2): CVSS 9.8, EPSS 1.4% (868 days public). Fix: Upgrade zlib.  
2. `CVE-2026-22184` (zlib@1.3.1-r2): CVSS 9.8, EPSS 0.04% (52 days public). Fix: Upgrade zlib.  
3. `CVE-2025-60876` (busybox@1.37.0-r30): CVSS 6.5, EPSS 0.05% (110 days public). Fix: Patch BusyBox wget.  

## 4. Critical & High Findings (Annex I Part II §2)  
- `CVE-2025-26519` (musl@1.2.5-r21): CVSS 8.1 (AV:L/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:L). Fix: Upgrade musl libc.  
- And 1 more HIGH/MEDIUM across 2 packages.  

## 5. Risk Distribution & Age Risk  
Severity: CRITICAL (2), HIGH (1), MEDIUM (2), LOW (2).  
Top affected: zlib@1.3.1-r2 (3 CVEs), busybox@1.37.0-r30 (3 CVEs).  
Oldest unpatched:  
1. `CVE-2023-45853` (868 days).  
2. `CVE-2025-26519` (379 days).  
3. `CVE-2026-22184` (52 days).  

## 6. CRA Defensible-Practice Actions  
1. **Immediate (Art. 14 + Annex I Part II §2)**: Patch `CVE-2023-45853` and `CVE-2026-22184` in zlib; submit Track 2 notifications.  
2. **Urgent (Annex I Part II §2)**: Upgrade musl libc to fix `CVE-2025-26519`.  
3. **Planned**: Address BusyBox `CVE-2025-60876` (header injection).  
4. **SBOM update (Annex I Part II §1)**: Refresh CycloneDX SBOM post-patching.  
5. **Public advisory (Annex I Part II §4)**: Publish remediation steps for zlib/musl CVEs.  
6. **CVD hygiene (Annex I Part II §5–6)**: Verify security contact details are current.