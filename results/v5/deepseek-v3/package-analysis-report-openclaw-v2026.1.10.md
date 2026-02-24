# Vulnerability Summary for OpenClaw (EU Cyber Resilience Act Compliance)

## 1. SBOM Overview  
The OpenClaw software (SPDX format, scanned 2026-02-20) contains 1,112 packages with 21 affected components. Analysis revealed 57 unique CVEs: 2 CRITICAL, 34 HIGH, 19 MEDIUM, and 2 LOW severity vulnerabilities.

## 2. CRA Mandatory Reporting Triggers (Article 14)  
No CRA mandatory reporting triggers identified (no CVEs with active exploitation or CISA KEV listing). Had triggers existed, ENISA/CSIRT notification deadlines would apply: 24h initial → 72h detailed → 14d final report.

## 3. Exploit Availability Assessment  
6 CVEs have publicly available PoCs (all via GitHub). Top exploitable vulnerabilities:  
- CVE-2026-25253 (Clawdbot RCE via gatewayUrl, CVSS 8.8, EPSS 0.00049)  
- CVE-2026-24763 (Clawdbot Docker cmd injection, CVSS 8.8, EPSS 0.00083)  
- CVE-2026-25157 (SSH cmd injection, CVSS 7.7, EPSS 0.00006)  

## 4. Critical & High Findings  
Priority vulnerabilities not covered above:  
- CVE-2026-25593 (OpenClaw RCE via WebSocket, CVSS 8.4, EPSS 0.00023)  
- CVE-2026-25474 (Telegram auth bypass, CVSS 7.5, EPSS 0.00015)  
- CVE-2026-26316 (BlueBubbles auth bypass, CVSS 7.5, EPSS 0.00061)  
- CVE-2026-26322 (Gateway URL hijack, CVSS 7.6, EPSS 0.00013)  
...and 30 more HIGH findings across 8 packages.

## 5. Risk Distribution  
Top affected packages:  
1. openclaw@2026.1.10 (29 CVEs)  
2. hono@4.11.3 (6 CVEs)  
3. clawdbot@2026.1.10 (5 CVEs)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch openclaw to ≥2026.2.15 (fixes 9 CRITICAL/HIGH CVEs including CVE-2026-25593)  
2. **Urgent**: Update clawdbot to eliminate RCE vectors (CVE-2026-25253/24763)  
3. **Planned**: Replace vulnerable fast-xml-parser@4.5.3 (CRITICAL XXE)  
4. **SBOM Hygiene**: Remove unused packages (hono, qs) with high-severity issues  
5. **Monitoring**: Track EPSS scores >0.1% for CVE-2026-26316/26322  

*Prioritized by CRA obligations → exploitability → CVSS severity*