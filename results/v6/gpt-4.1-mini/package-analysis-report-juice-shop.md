- **SBOM Overview**
  - Product: bkimminich/juice-shop
  - Format: CycloneDX container
  - Scan date: 2026-02-24
  - Total packages: 998
  - Affected packages: 38
  - Unique CVEs: 58 total
    - CRITICAL: 7
    - HIGH: 30
    - MEDIUM: 21

- **CRA Mandatory Reporting (Article 14)**
  - No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

- **Exploit Assessment**
  - PoC evidence summary: 5 GitHub exploits, 2 ExploitDB, 2 PacketStorm, 2 ZDT, 3 HackerOne, 2 Kitploit.
  - Top 5 exploited CVEs by severity (from advisory data):
    1. CVE-2023-37466 (vm2) - CRITICAL (9.8 CVSS, multiple PoC sources including exploitdb, githubexploit, packetstorm, zdt)
    2. CVE-2023-32314 (vm2) - CRITICAL (9.8 CVSS)
    3. CVE-2015-9235 (jsonwebtoken) - CRITICAL (9.8 CVSS)
    4. CVE-2026-23745 (tar) - HIGH (8.2 CVSS, githubexploit PoC)
    5. CVE-2026-26996 (minimatch) - HIGH (8.7 CVSS)
  - Additional 53 CVEs have PoC evidence.

- **Critical & High Findings (excluding above)**
  - CVE-2026-22709 (vm2) - CRITICAL (9.8 CVSS)
  - CVE-2019-10744 (lodash) - CRITICAL (9.1 CVSS)
  - CVE-2023-46233 (crypto-js) - CRITICAL (9.1 CVSS)
  - CVE-2025-13465 (lodash) - HIGH (7.9 CVSS)
  - CVE-2025-47935 (multer) - HIGH (7.5 CVSS)
  - CVE-2025-47944 (multer) - HIGH (7.5 CVSS)
  - CVE-2025-48997 (multer) - HIGH (8.7 CVSS)
  - CVE-2024-38355 (socket.io) - HIGH (7.3 CVSS)
  - And 21 more across 25 packages.

- **Risk Distribution**
  - Severity counts:
    - CRITICAL: 7
    - HIGH: 30
    - MEDIUM: 21
  - Top 3 affected packages by unique CVEs:
    1. sanitize-html@1.4.2 (7 CVEs)
    2. jsonwebtoken@0.1.0 (5 CVEs)
    3. jsonwebtoken@0.4.0 (5 CVEs)

- **CRA Compliance Actions**
  1. **Immediate**: No CRA Article 14 triggers requiring immediate ENISA/CSIRT notification.
  2. **Urgent**: Patch exploited CRITICAL/HIGH CVEs with PoC:
     - vm2: CVE-2023-37466, CVE-2023-32314, CVE-2026-22709
     - jsonwebtoken: CVE-2015-9235
     - tar: CVE-2026-23745
     - minimatch: CVE-2026-26996
  3. **Planned**: Patch remaining HIGH severity CVEs including:
     - lodash: CVE-2025-13465
     - multer: CVE-2025-47935, CVE-2025-47944, CVE-2025-48997
     - socket.io: CVE-2024-38355
     - Others as per package advisories
  4. **Hygiene**: Maintain SBOM accuracy and update per CRA Article 10(6) for ongoing vulnerability management.
  5. **Vulnerability Handling**: Follow CRA Article 11 for timely patching and vulnerability disclosure processes.

Summary: No mandatory CRA Article 14 reporting triggers detected. Multiple critical and high vulnerabilities with PoC exist, notably in vm2, jsonwebtoken, tar, and minimatch. Immediate patching of exploited CVEs is critical, followed by planned remediation of remaining high risks. Maintain SBOM and vulnerability management per CRA requirements.