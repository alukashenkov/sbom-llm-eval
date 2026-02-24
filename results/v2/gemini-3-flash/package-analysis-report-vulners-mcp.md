## 1. SBOM Overview
**Product:** vulners-mcp (Container)  
**Scan Date:** 2026-02-24  
**Format:** CycloneDX  
**Stats:** 560 total packages, 20 affected.  
**Unique CVE Count:** 82 total (6 Critical, 31 High, 36 Medium, 9 Low).

## 2. CRA Mandatory Reporting Triggers (Article 14)
The following vulnerability is actively exploited in the wild or listed in CISA KEV, requiring notification to ENISA/CSIRT (24h/72h/14d timeline):

*   **[CVE-2025-48384]** git@1:2.47.3-0+deb13u1 — CVSS 8.0 — EPSS 0.00456 — Arbitrary code execution via broken config quoting (CISA KEV).

## 3. Exploit Availability Assessment
The following CVEs have confirmed proof-of-concept or exploit code available:

1.  **CVE-2025-15467** (openssl) — CVSS 9.8 (Critical)
2.  **CVE-2024-41817** (imagemagick) — CVSS 7.8 (High)
3.  **CVE-2021-32804** (tar) — CVSS 8.2 (High)
4.  **CVE-2025-11187** (openssl) — CVSS 7.5 (High)
5.  **CVE-2025-69419** (openssl) — CVSS 8.1 (High)
*6 additional CVEs have exploit evidence (CVE-2025-15468, CVE-2025-15469, CVE-2025-66199, CVE-2025-68160, CVE-2025-69420, CVE-2025-69421).*

## 4. Critical & High Findings
Top critical and high-severity vulnerabilities not listed above:

*   **CVE-2026-22770** (imagemagick) — CVSS 9.8 (Critical)
*   **CVE-2026-23876** (imagemagick) — CVSS 9.8 (Critical)
*   **CVE-2025-53101** (imagemagick) — CVSS 9.8 (Critical)
*   **CVE-2024-56171** (libxml2) — CVSS 9.8 (Critical)
*   **CVE-2024-40896** (libxml2) — CVSS 9.1 (Critical)
*   **CVE-2025-55298** (imagemagick) — CVSS 8.8 (High)
*   **CVE-2025-57803** (imagemagick) — CVSS 8.8 (High)
*   **CVE-2026-23950** (tar) — CVSS 8.8 (High)
*and 23 more HIGH findings across 10 packages.*

## 5. Risk Distribution
*   **Critical:** 6
*   **High:** 31
*   **Medium:** 36
*   **Low:** 9

**Most Affected Packages:**
1.  **imagemagick:** 33 advisories
2.  **openssl:** 18 advisories
3.  **tar:** 12 advisories

## 6. CRA Compliance Actions
1.  **Immediate:** Patch `git` to version 2.47.3-0+deb13u1 or higher to address **CVE-2025-48384** (CISA KEV).
2.  **Urgent:** Update `openssl` to address **CVE-2025-15467** and `imagemagick` to address **CVE-2026-22770** and **CVE-2026-23876** (Critical/Exploited PoCs).
3.  **Urgent:** Update `libxml2` to address **CVE-2024-56171** and **CVE-2024-40896**.
4.  **Planned:** Update `tar` to address directory traversal and file overwrite risks (**CVE-2021-32804**, **CVE-2026-23950**).
5.  **Hygiene:** Review `mcp` and `fastmcp` configurations regarding DNS rebinding protection (**CVE-2025-66416**).