# Vulnerability Summary for OpenClaw (EU Cyber Resilience Act Compliance)

## 1. SBOM Overview
- **Product**: OpenClaw (SPDX format)
- **Scan Date**: 2026-02-20
- **Total Packages**: 1,112
- **Affected Packages**: 21 (1.9%)
- **Vulnerabilities**: 125 total advisories
  - CRITICAL: 4
  - HIGH: 32
  - MEDIUM: 19
  - LOW: 6

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified (no wild exploitation or CISA KEV entries).

## 3. Exploit Availability Assessment
**Public PoCs Available**:
- [CVE-2026-25253] Clawdbot@2026.1.10 - CVSS 8.8 (EPSS 0.00049) - 1-click RCE via gatewayUrl token exfiltration (3 GitHub exploits)
- [CVE-2026-24763] Clawdbot@2026.1.10 - CVSS 8.8 (EPSS 0.00083) - Authenticated command injection via PATH (1 GitHub exploit)
- [CVE-2026-25157] Clawdbot@2026.1.10 - CVSS 7.7 (EPSS 0.00006) - OS command injection via SSH root path (1 GitHub exploit)
- [CVE-2026-22610] @angular/core@21.0.3 - CVSS 8.5 (EPSS 0.00021) - XSS via SVG script attributes (1 GitHub exploit)
- [CVE-2025-65945] jws@4.0.0 - CVSS 7.5 (EPSS 0.00009) - HMAC signature verification flaw (1 GitHub exploit)

## 4. Critical & High Findings
**Critical**:
- GHSA-4RJ2-GPMH-QQ5X - Voice-call auth bypass (CVSS 9.4)
- GHSA-RV39-79C4-7459 - Gateway device identity check bypass (CVSS 9.3)
- GHSA-M7X8-2W3W-PR42 - Command injection in maintainer script (CVSS 8.6)
- GHSA-2QJ5-GWG2-XWC4 - Unsanitized CWD path injection (CVSS 8.6)

**High**:
- GHSA-G55J-C2V4-PJCG - Unauthenticated RCE via WebSocket (CVSS 8.4)
- GHSA-X22M-J5QQ-J49M - Dual SSRF in Feishu extension (CVSS 8.6)
- GHSA-R5FQ-947M-XM57 - Path traversal in apply_patch (CVSS 8.8)
- GHSA-JQPQ-MGVM-F9R6 - Command hijacking via PATH (CVSS 8.8)

## 5. Risk Distribution
- **Severity**: CRITICAL (4), HIGH (32), MEDIUM (19), LOW (6)
- **Top Affected Packages**: 
  1. OpenClaw (62 vulnerabilities)
  2. Clawdbot (12 vulnerabilities)
  3. fast-xml-parser (5 vulnerabilities)
- **Exploitability**: 5 vulnerabilities with public PoCs, 0 actively exploited

## 6. CRA Compliance Actions
1. **Immediate**: Patch critical RCE vulnerabilities (GHSA-G55J-C2V4-PJCG, GHSA-M7X8-2W3W-PR42)
2. **Urgent**: Update dependencies with public PoCs (Angular, jws, Clawdbot)
3. **Planned**: Implement CRA-compliant vulnerability monitoring for all components
4. **SBOM Hygiene**: Establish automated SBOM generation with vulnerability scanning
5. **Documentation**: Create CRA-required security documentation for product lifecycle

**Priority Rationale**: Focused on critical RCEs first, then exploit-published vulnerabilities, followed by CRA procedural requirements. All critical/high issues should be addressed within CRA's 14-day final reporting window.