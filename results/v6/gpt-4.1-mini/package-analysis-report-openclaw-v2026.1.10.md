- **SBOM Overview**
  - Product: openclaw
  - Format: SPDX
  - Scan Date: 2026-02-20T17:16:42Z
  - Total Packages: 1112
  - Affected Packages: 21
  - Unique CVEs: 96 (Critical: 5, High: 52, Medium: 33, Low: 6)

- **CRA Mandatory Reporting (Article 14)**
  - No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

- **Exploit Assessment**
  - Total CVEs with PoC evidence: 6 (GitHub exploits)
  - Top 5 exploited CVEs by severity (from advisory data):
    - CVE-2026-25253 (openclaw/clawdbot): CVSS 8.8, EPSS 0.00049 (GitHub PoC)
    - CVE-2026-24763 (clawdbot): CVSS 8.8, EPSS 0.00083 (GitHub PoC)
    - CVE-2026-25157 (clawdbot): CVSS 7.7, EPSS 0.00006 (GitHub PoC)
    - CVE-2026-26317 (openclaw/clawdbot): CVSS 7.1, EPSS 0.00014
    - CVE-2026-22610 (@angular/compiler, @angular/core): CVSS 8.5, EPSS 0.00014 (GitHub PoC)
  - 1 additional CVE has PoC evidence.

- **Critical & High Findings (excluding above)**
  - CVE-2026-25896 (fast-xml-parser): CVSS 9.3, EPSS 0.00029
  - CVE-2026-27001 (openclaw): CVSS 8.6, EPSS 0.00018
  - CVE-2026-25547 (@isaacs/brace-expansion): CVSS 8.7, EPSS 0.00018
  - CVE-2026-26323 (openclaw): CVSS 8.6, EPSS 0.00175
  - CVE-2026-26322 (openclaw): CVSS 7.6, EPSS 0.00013
  - CVE-2026-26325 (openclaw): CVSS 7.2, EPSS 0.00024
  - CVE-2026-26321 (openclaw): CVSS 7.5, EPSS 0.00060
  - CVE-2026-27487 (openclaw): CVSS 7.6, EPSS 0.00051
  - And 44 more across 13 packages.

- **Risk Distribution**
  - Critical: 5
  - High: 52
  - Medium: 33
  - Low: 6
  - Top affected packages:
    - openclaw@2026.1.10: 67 unique CVEs
    - clawdbot@2026.1.10: 11 unique CVEs
    - hono@4.11.3: 7 unique CVEs

- **CRA Compliance Actions**
  1. **Immediate**: None (no CRA Article 14 triggers).
  2. **Urgent**: Patch exploited HIGH CVEs with PoCs:
     - CVE-2026-25253 (openclaw/clawdbot)
     - CVE-2026-24763 (clawdbot)
     - CVE-2026-25157 (clawdbot)
     - CVE-2026-26317 (openclaw/clawdbot)
     - CVE-2026-22610 (@angular/compiler, @angular/core)
  3. **Planned**: Patch remaining HIGH severity CVEs, including:
     - CVE-2026-25896 (fast-xml-parser)
     - CVE-2026-27001 (openclaw)
     - CVE-2026-25547 (@isaacs/brace-expansion)
     - CVE-2026-26323 (openclaw)
     - CVE-2026-26322 (openclaw)
     - CVE-2026-26325 (openclaw)
     - CVE-2026-26321 (openclaw)
     - CVE-2026-27487 (openclaw)
  4. **Hygiene**: Maintain SBOM accuracy and update per CRA Article 10(6).

---

**References:**  
- CRA Article 10: Security requirements for products.  
- CRA Article 11: Vulnerability handling and disclosure.  
- CRA Article 14: Mandatory reporting triggers and timelines.