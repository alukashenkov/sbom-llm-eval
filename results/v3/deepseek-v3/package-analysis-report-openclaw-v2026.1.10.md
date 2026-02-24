# Vulnerability Summary for OpenClaw (EU Cyber Resilience Act Compliance)

## 1. SBOM Overview  
OpenClaw (SPDX format, scanned 2026-02-20) contains 1,112 packages with 21 affected packages and 125 advisories. Found 42 unique CVEs: 5 CRITICAL, 18 HIGH, 12 MEDIUM, 7 LOW severity.

## 2. CRA Mandatory Reporting Triggers (Article 14)  
**No CRA mandatory reporting triggers identified** after scanning all advisories for wildExploited=true and "cisa_kev" in pocSources.  

## 3. Exploit Availability Assessment  
Top 5 CVEs with PoC evidence:  
- [CVE-2026-25253] clawdbot@2026.1.10 — CVSS 8.8 HIGH — EPSS 0.00049 — 1-Click RCE via gatewayUrl token exfiltration (3 GitHub exploits)  
- [CVE-2026-24763] clawdbot@2026.1.10 — CVSS 8.8 HIGH — EPSS 0.00083 — Docker PATH injection RCE (1 GitHub exploit)  
- [CVE-2026-25157] clawdbot@2026.1.10 — CVSS 7.7 HIGH — EPSS 0.00006 — SSH command injection (1 GitHub exploit)  
- [CVE-2026-22610] @angular/core@21.0.3 — CVSS 8.5 HIGH — EPSS 0.00021 — SVG XSS (1 GitHub exploit)  
- [CVE-2025-65945] jws@4.0.0 — CVSS 7.5 HIGH — EPSS 0.00009 — JWT HMAC bypass (1 GitHub exploit)  
*3 additional CVEs have exploit evidence.*

## 4. Critical & High Findings  
- [CVE-2026-27487] openclaw@2026.1.10 — CVSS 9.4 CRITICAL — Voice-call auth bypass  
- [CVE-2026-26324] openclaw@2026.1.10 — CVSS 7.5 HIGH — SSRF via IPv6 bypass  
- [CVE-2026-26321] openclaw@2026.1.10 — CVSS 7.5 HIGH — Local file read via Feishu  
- [CVE-2026-25593] openclaw@2026.1.10 — CVSS 8.4 HIGH — WebSocket RCE  
*and 14 more HIGH findings across 8 packages*  

## 5. Risk Distribution  
Severity (unique CVEs): CRITICAL (5), HIGH (18), MEDIUM (12), LOW (7).  
Top affected packages: openclaw (32 advisories), clawdbot (12), fast-xml-parser (5).  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch clawdbot to ≥2026.2.15 (CVE-2026-25253 RCE)  
2. **Urgent**: Update openclaw to fixed version addressing 9 CRITICAL/HIGH CVEs  
3. **Planned**: Replace vulnerable fast-xml-parser (CRITICAL XML parsing flaws)  
4. **SBOM hygiene**: Remove unused packages (jws, qs, minimatch with HIGH flaws)  
5. **Monitoring**: Watch for CISA KEV updates on Angular XSS (CVE-2026-22610)  

Prioritize remediation by exploitability (PoC available) → CRITICAL severity → CRA Article 14 triggers.