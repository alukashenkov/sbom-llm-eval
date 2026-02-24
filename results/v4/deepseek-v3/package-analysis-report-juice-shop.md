# Vulnerability Summary for OWASP Juice Shop (CycloneDX SBOM, 2026-02-24)

## 1. SBOM Overview  
The OWASP Juice Shop container image (sha256:75b03f3f5336) contains 998 packages, with 38 affected by vulnerabilities. Analysis revealed 82 advisories impacting these packages, yielding **32 unique CVEs**: 4 CRITICAL, 12 HIGH, 15 MEDIUM, and 1 LOW severity.

## 2. CRA Mandatory Reporting Triggers  
No CRA mandatory reporting triggers identified (no CISA KEV entries or confirmed wild exploitation).

## 3. Exploit Availability Assessment  
Top exploitable CVEs with PoC evidence:  
1. [CVE-2023-37466] vm2@3.9.17 (CRITICAL, CVSS 9.8) - Sandbox escape via Promise handler bypass  
2. [CVE-2023-37903] vm2@3.9.17 (CRITICAL, CVSS 9.8) - RCE via inspect function manipulation  
3. [CVE-2018-3721] lodash@2.4.2 (MEDIUM, CVSS 6.5) - Prototype pollution via `defaultsDeep`  
4. [CVE-2018-16487] lodash@2.4.2 (MEDIUM, CVSS 6.8) - Prototype pollution via `merge`  
5. [CVE-2020-8203] lodash.set@4.3.2 (HIGH, CVSS 7.4) - Prototype pollution via `set`  
*3 additional CVEs have exploit evidence.*

## 4. Critical & High Findings  
1. [CVE-2015-9235] jsonwebtoken@0.1.0 (CRITICAL, CVSS 9.8, EPSS 32.5%) - JWT verification bypass  
2. [CVE-2026-23950] tar@4.4.19 (HIGH, CVSS 8.8) - Race condition in path handling  
3. [CVE-2022-23539] jsonwebtoken@0.1.0 (HIGH, CVSS 8.1) - Legacy key type misuse  
4. [CVE-2023-46233] crypto-js@3.3.0 (CRITICAL, CVSS 9.1) - Weak PBKDF2 implementation  
*and 8 more HIGH findings across 5 packages.*

## 5. Risk Distribution  
Severity: 4 CRITICAL, 12 HIGH, 15 MEDIUM, 1 LOW  
Most affected packages:  
1. jsonwebtoken (5 advisories, 2 CVEs)  
2. tar (4 advisories, 4 CVEs)  
3. lodash (4 advisories, 3 CVEs)  

## 6. CRA Compliance Actions  
1. **Immediate**: Patch vm2 to ≥3.9.19 (CVE-2023-37466/37903) - active exploits  
2. **Urgent**: Update jsonwebtoken to ≥9.0.0 (CVE-2015-9235) - critical auth bypass  
3. **Urgent**: Upgrade tar to ≥8.0.0 (multiple file traversal flaws)  
4. **Planned**: Migrate from crypto-js to Web Crypto API (CVE-2023-46233)  
5. **SBOM Hygiene**: Remove unused lodash.set (CVE-2020-8203)  

Priority based on CRA Article 14 obligations, exploitability, and CVSS scores.