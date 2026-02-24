## 1. SBOM Overview  
The SBOM for **openclaw** (SPDX format, scanned 2026-02-20) covers 1,112 total packages, with 21 affected packages containing vulnerabilities. Deduplicated CVE counts by severity:  
- **CRITICAL**: 5  
- **HIGH**: 32  
- **MEDIUM**: 18  
- **LOW**: 6  

## 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified (no advisories with `wildExploited=true` or `cisa_kev` in `pocSources`).  

## 3. Exploit Availability Assessment  
Top 5 CVEs with PoC evidence:  
- **[CVE-2026-25253]** `clawdbot@2026.1.10` (CVSS 8.8, EPSS 0.00049) – 1-Click RCE via gatewayUrl token exfiltration  
- **[CVE-2026-24763]** `clawdbot@2026.1.10` (CVSS 8.8, EPSS 0.00083) – Docker command injection via PATH  
- **[CVE-2026-22610]** `@angular/core@21.0.3` (CVSS 8.5, EPSS 0.00021) – XSS via SVG script attributes  
- **[CVE-2025-65945]** `jws@4.0.0` (CVSS 7.5, EPSS 0.00009) – HMAC signature verification bypass  
- **[CVE-2026-25157]** `clawdbot@2026.1.10` (CVSS 7.7, EPSS 0.00006) – SSH command injection  
*5 additional CVEs have exploit evidence.*  

## 4. Critical & High Findings  
Remaining critical/high CVEs:  
- **[CVE-2026-25593]** `openclaw@2026.1.10` (CVSS 8.4, EPSS 0.00023) – Unauthenticated RCE via WebSocket  
- **[CVE-2026-27002]** `openclaw@2026.1.10` (CVSS 7.7, EPSS 0.00045) – Docker container escape  
- **[CVE-2026-26324]** `openclaw@2026.1.10` (CVSS 7.5, EPSS 0.00011) – SSRF bypass via IPv6  
*and 29 more HIGH findings across 12 packages.*  

## 5. Risk Distribution  
Unique CVE counts: CRITICAL (5), HIGH (32), MEDIUM (18), LOW (6).  
Top affected packages:  
1. `openclaw` – 41 advisories  
2. `clawdbot` – 12 advisories  
3. `hono` – 7 advisories  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch `openclaw` to ≥2026.2.15 (fixes CRITICAL CVE-2026-27002 container escape).  
2. **Urgent**: Update `clawdbot` (fixes exploitable RCEs CVE-2026-25253/CVE-2026-24763).  
3. **Planned**: Replace vulnerable `jws@4.0.0` (HMAC bypass) with maintained alternatives.  
4. **SBOM Hygiene**: Remove unused packages (`@isaacs/brace-expansion`, `qs`).  
5. **Monitoring**: Track EPSS for HIGH CVEs with PoCs (e.g., CVE-2026-22610).  

*Prioritized by exploitability, CVSS, and CRA Article 14 obligations.*