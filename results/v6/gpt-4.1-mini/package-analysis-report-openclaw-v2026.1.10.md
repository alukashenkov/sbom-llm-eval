1. SBOM Overview  
- Product: openclaw  
- Format: SPDX  
- Scan Date: 2026-02-20  
- Total Packages: 1112  
- Affected Packages: 21  
- Unique CVEs: 57 (Critical: 2, High: 34, Medium: 19, Low: 2)  

2. CRA Mandatory Reporting (Article 14)  
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).  

3. Exploit Assessment  
- Total CVEs with PoC evidence: 6 (GitHub exploits)  
- Top 5 exploited CVEs by severity:  
  - CVE-2026-25253 (openclaw/clawdbot) CVSS 8.8, EPSS 0.00049  
  - CVE-2026-24763 (clawdbot) CVSS 8.8, EPSS 0.00083  
  - CVE-2026-25157 (clawdbot) CVSS 7.7, EPSS 0.00006  
  - CVE-2026-26317 (openclaw/clawdbot) CVSS 7.1, EPSS 0.00014  
  - CVE-2026-22610 (@angular/compiler/core) CVSS 8.5, EPSS 0.00021  
- 1 additional CVE has PoC evidence.  

4. Critical & High Findings (excluding §2-3)  
- CVE-2026-25896 (fast-xml-parser) CVSS 9.3, EPSS 0.00029  
- CVE-2026-25474 (openclaw) CVSS 7.5, EPSS 0.00015  
- CVE-2026-25593 (openclaw) CVSS 8.4, EPSS 0.00023  
- CVE-2026-26316 (openclaw) CVSS 7.5, EPSS 0.00061  
- CVE-2026-26321 (openclaw) CVSS 7.5, EPSS 0.00060  
- CVE-2026-26322 (openclaw) CVSS 7.6, EPSS 0.00013  
- CVE-2026-26324 (openclaw) CVSS 7.5, EPSS 0.00011  
- CVE-2026-26325 (openclaw) CVSS 7.2, EPSS 0.00018  
- and 25 more across 14 packages.  

5. Risk Distribution  
- Severity counts: High 34, Medium 19, Low 2, Critical 2  
- Top affected packages:  
  - openclaw@2026.1.10: 29 CVEs  
  - hono@4.11.3: 6 CVEs  
  - clawdbot@2026.1.10: 5 CVEs  

6. CRA Compliance Actions  
- Immediate:  
  - Patch CVE-2026-25253 (openclaw/clawdbot) with known exploits (target versions > 2026.1.10)  
  - Patch CVE-2026-24763 (clawdbot) with known exploits  
- Urgent:  
  - Patch high-severity exploited CVEs with PoC: CVE-2026-25157, CVE-2026-26317, CVE-2026-22610  
- Planned:  
  - Patch remaining high-severity CVEs including CVE-2026-25896, CVE-2026-25474, CVE-2026-25593, CVE-2026-26316, CVE-2026-26321, CVE-2026-26322, CVE-2026-26324, CVE-2026-26325  
- Hygiene:  
  - Maintain SBOM updates and vulnerability scanning per CRA Article 10(6)  
  - Ensure continuous monitoring for new vulnerabilities and PoC evidence per Article 11  

Summary: The openclaw product SBOM scan identified 57 unique CVEs with a majority high severity. No mandatory CRA Article 14 reporting triggers were found. Six CVEs have public PoC exploits, notably CVE-2026-25253 and CVE-2026-24763 with high CVSS scores and EPSS probabilities. Immediate patching of exploited vulnerabilities is required, followed by urgent and planned remediation of remaining high-risk issues. Continuous SBOM maintenance and vulnerability management are essential for CRA compliance.