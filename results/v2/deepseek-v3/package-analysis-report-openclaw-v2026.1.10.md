# Vulnerability Summary for OpenClaw (EU Cyber Resilience Act Compliance)

## 1. SBOM Overview  
OpenClaw SPDX SBOM scanned on 2026-02-20. 21/1112 packages (1.9%) contain vulnerabilities. Unique CVEs by severity: 5 CRITICAL, 29 HIGH, 14 MEDIUM, 4 LOW.

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no CVEs with wildExploited=true or cisa_kev sources).

## 3. Exploit Availability Assessment  
Top 5 exploitable CVEs:  
- [CVE-2026-25253] Clawdbot@2026.1.10 — CVSS 8.8 (1-click RCE via gatewayUrl)  
- [CVE-2026-24763] Clawdbot@2026.1.10 — CVSS 8.8 (Docker command injection)  
- [CVE-2026-25157] Clawdbot@2026.1.10 — CVSS 7.7 (SSH command injection)  
- [CVE-2026-22610] @angular/core@21.0.3 — CVSS 8.5 (XSS via SVG)  
- [CVE-2025-65945] jws@4.0.0 — CVSS 7.5 (HMAC bypass)  
3 additional CVEs have exploit evidence.

## 4. Critical & High Findings  
- [CVE-2026-25593] openclaw@2026.1.10 — CVSS 8.4 (RCE via WebSocket)  
- [CVE-2026-26322] openclaw@2026.1.10 — CVSS 7.6 (gatewayUrl SSRF)  
- [CVE-2026-26324] openclaw@2026.1.10 — CVSS 7.5 (IPv6 SSRF bypass)  
- [CVE-2026-26321] openclaw@2026.1.10 — CVSS 7.5 (local file read)  
and 25 more HIGH findings across 8 packages.

## 5. Risk Distribution  
Severity counts: CRITICAL (5), HIGH (29), MEDIUM (14), LOW (4).  
Most affected packages:  
1. openclaw (38 advisories)  
2. clawdbot (12 advisories)  
3. fast-xml-parser (5 advisories)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch openclaw to ≥2026.2.15 (CRITICAL CVE-2026-25593 RCE)  
2. **Immediate**: Update clawdbot (CVE-2026-25253 1-click RCE)  
3. **Urgent**: Replace fast-xml-parser@4.5.3 (CRITICAL XXE CVE-2026-25896)  
4. **Urgent**: Upgrade @angular/core (XSS CVE-2026-22610)  
5. **Planned**: Audit all webhook handlers for SSRF protections  

Prioritize based on CRA Article 14 obligations (exploitability first).