## 1. SBOM Overview
*   **Product**: vulners-mcp (Container)
*   **Format**: CycloneDX
*   **Scan Date**: 2026-02-24
*   **Packages**: 560 total / 20 affected
*   **Unique CVEs**: 188 (14 CRITICAL, 82 HIGH, 79 MEDIUM, 12 LOW, 1 NONE)

## 2. CRA Mandatory Reporting (Article 14)
*   **CVE-2025-48384**: git (CVSS: 8.0, EPSS: 0.00456). **Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.**

## 3. Exploit Assessment
*   **PoC Summary**: 9 GitHub exploits, 13 PacketStorm, 7 HackerOne, 1 CISA KEV, 1 Gitee, 1 Nuclei, 1 Kitploit.
*   **Top Exploited CVEs**:
    *   **CVE-2025-48384**: git (CVSS 8.0) - CISA KEV / Wild Exploited.
    *   **CVE-2024-41817**: imagemagick (CVSS 7.8) - GitHub PoC.
    *   **CVE-2021-32804**: tar (CVSS 8.2) - GitHub PoC.
    *   **CVE-2026-23745**: tar (CVSS 8.2) - GitHub PoC.
    *   **CVE-2025-15467**: openssl (CVSS 9.8) - GitHub/PacketStorm PoC.
*   28 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2026-22770**: imagemagick (CVSS: 9.8, EPSS: 0.00065)
*   **CVE-2014-9852**: imagemagick (CVSS: 9.8, EPSS: 0.01316)
*   **CVE-2014-9846**: imagemagick (CVSS: 9.8, EPSS: 0.04666)
*   **CVE-2026-23876**: imagemagick (CVSS: 9.8, EPSS: 0.00062)
*   **CVE-2026-25897**: imagemagick (CVSS: 9.8, EPSS: 0.00038)
*   **CVE-2026-26284**: imagemagick (CVSS: 9.1, EPSS: 0.00037)
*   **CVE-2024-40896**: libxml2 (CVSS: 9.1, EPSS: 0.00553)
*   **CVE-2025-53101**: imagemagick (CVSS: 9.8, EPSS: 0.00069)
*   ...and 88 more across 12 packages.

## 5. Risk Distribution
*   **Severity**: 14 Critical, 82 High, 79 Medium, 12 Low.
*   **Top Affected Packages**:
    1.  **imagemagick**: 77 unique CVEs
    2.  **binutils**: 32 unique CVEs
    3.  **libxml2**: 17 unique CVEs

## 6. CRA Compliance Actions
1.  **Immediate**: Patch `git` to resolve **CVE-2025-48384** and fulfill Article 14 reporting obligations due to active exploitation.
2.  **Urgent**: Update `openssl` to address **CVE-2025-15467** (CVSS 9.8) and `imagemagick` to resolve multiple Critical overflows (e.g., **CVE-2026-22770**).
3.  **Planned**: Remediate remaining 82 HIGH severity vulnerabilities in `binutils`, `libxml2`, and `tar` to meet Article 10 security requirements.
4.  **Hygiene**: Implement automated SBOM regression testing per Article 10(6) to monitor the high volume of vulnerabilities in image processing libraries.