## 1. SBOM Overview
*   **Product**: `vulners-mcp` (Container)
*   **Format**: CycloneDX
*   **Scan Date**: 2026-02-24
*   **Packages**: 560 total; 20 affected.
*   **Unique CVEs**: 188 (12 CRITICAL, 76 HIGH, 87 MEDIUM, 12 LOW, 1 NONE).

## 2. CRA Mandatory Reporting (Article 14)
*   **CVE-2025-48384** | `git` | CVSS: 8.0 | EPSS: 0.00456
*   **Requires ENISA/CSIRT notification per CRA Article 14(2)**: 24h early warning → 72h assessment → 14-day final report. This vulnerability is confirmed as wild-exploited and listed in the CISA KEV catalog.

## 3. Exploit Assessment
*   **PoC Summary**: 13 PacketStorm, 9 GitHub, 7 HackerOne, 1 CISA KEV, 1 Gitee, 1 Nuclei, 1 KitPloit.
*   **Top Exploited CVEs**:
    *   **CVE-2025-15467** | `openssl` | CVSS: 9.8 (CRITICAL)
    *   **CVE-2025-48384** | `git` | CVSS: 8.0 (HIGH)
    *   **CVE-2024-41817** | `imagemagick` | CVSS: 7.8 (HIGH)
    *   **CVE-2021-32804** | `tar` | CVSS: 8.2 (HIGH)
    *   **CVE-2025-11187** | `openssl` | CVSS: 7.5 (HIGH)
*   27 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2026-22770** | `imagemagick` | CVSS: 9.8 | EPSS: 0.00065
*   **CVE-2026-23876** | `imagemagick` | CVSS: 9.8 | EPSS: 0.00062
*   **CVE-2025-53014** | `imagemagick` | CVSS: 9.8 | EPSS: 0.00031
*   **CVE-2025-53101** | `imagemagick` | CVSS: 9.8 | EPSS: 0.00069
*   **CVE-2024-56171** | `libxml2` | CVSS: 9.8 | EPSS: 0.00048
*   **CVE-2024-40896** | `libxml2` | CVSS: 9.1 | EPSS: 0.00553
*   **CVE-2025-55298** | `imagemagick` | CVSS: 8.8 | EPSS: 0.00430
*   **CVE-2026-23950** | `tar` | CVSS: 8.8 | EPSS: 0.00006
*   ...and 75 more across 12 packages.

## 5. Risk Distribution
*   **Severity**: 12 CRITICAL, 76 HIGH, 87 MEDIUM, 12 LOW.
*   **Top Affected Packages**:
    1.  `imagemagick@8:7.1.1.43+dfsg1-1+deb13u5` (77 unique CVEs)
    2.  `binutils@2.44-3` (32 unique CVEs)
    3.  `libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2` (17 unique CVEs)

## 6. CRA Compliance Actions
1.  **Immediate**: Patch `git` to resolve **CVE-2025-48384** to satisfy Article 14 mandatory reporting and mitigation requirements.
2.  **Urgent**: Update `openssl` to address **CVE-2025-15467** and `imagemagick` to address **CVE-2026-22770** (CRITICAL severity with PoC/High Impact).
3.  **Planned**: Remediate remaining 76 HIGH severity vulnerabilities in `libxml2`, `binutils`, and `tar` per Article 11 vulnerability handling.
4.  **Hygiene**: Implement automated SBOM regression testing and version pinning for `imagemagick` to reduce the attack surface per Article 10(6).