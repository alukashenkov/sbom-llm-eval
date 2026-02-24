## Vulnerability Summary for vulners-mcp

**SBOM Overview**

*   **Product Name:** vulners-mcp
*   **Format:** CycloneDX
*   **Scan Date:** 2026-02-24T14:35:34.000Z
*   **Total Packages:** 560
*   **Affected Packages:** 20
*   **Vulnerability Counts by Severity:**
    *   CRITICAL: 8
    *   HIGH: 45
    *   MEDIUM: 46
    *   LOW: 6
    *   NONE: 1

**CRA Mandatory Reporting Triggers (Article 14)**

The following vulnerabilities require immediate notification to ENISA/CSIRT:

*   **CVE-2025-48384** git@1:2.47.3-0+deb13u1 — CVSS: 8.0 (HIGH) — EPSS: 0.00456 — Arbitrary code execution through broken config quoting.

**Exploit Availability Assessment**

*   **Public PoC available:**
    *   CVE-2025-15467 (openssl) - Multiple GitHub exploits.
    *   CVE-2024-41817 (imagemagick) - Multiple GitHub exploits.
    *   CVE-2021-32804 (tar) - GitHub exploit available.
    *   CVE-2026-23745 (tar) - GitHub exploit available.
    *   CVE-2025-48384 (git) - Multiple GitHub exploits and Gitee exploit available.
    *   CVE-2025-48385 (git) - GitHub exploit available.
    *   CVE-2025-69872 (diskcache) - GitHub exploit available.
    *   CVE-2025-68973 (gnupg) - GitHub exploit available.
*   **Exploit framework integration:**
    *   CVE-2024-21485 (dash) - Nuclei integration.
*   **Bug bounty disclosed:**
    *   CVE-2025-14524 (curl) - HackerOne report.
    *   CVE-2025-15079 (curl) - HackerOne report.
    *   CVE-2025-15224 (curl) - HackerOne report.
    *   CVE-2025-5399 (curl) - HackerOne report.
    *   CVE-2025-10966 (curl) - HackerOne report.
    *   CVE-2025-10148 (curl) - HackerOne report.
    *   CVE-2025-9086 (curl) - HackerOne report.

**Critical & High Findings**

*   **CVE-2025-15467** openssl@3.5.4-1~deb13u2 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00672 — Stack buffer overflow in CMS AuthEnvelopedData message parsing.
*   **CVE-2026-22770** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00065 — Heap buffer overflow in BilateralBlurImage method.
*   **CVE-2026-23876** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00062 — Heap buffer overflow in XBM image decoder.
*   **CVE-2014-9852** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.01316 — Use-after-free vulnerability.
*   **CVE-2014-9846** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.04666 — Buffer overflow in rle file processing.
*   **CVE-2025-53014** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00031 — Heap buffer overflow in InterpretImageFilename.
*   **CVE-2025-53101** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00069 — Command injection in `magick mogrify`.
*   **CVE-2025-57807** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00042 — Insecure SeekBlob() function.
*   **CVE-2024-40896** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.00553 — SAX parser external entity processing vulnerability.
*   **CVE-2025-49794** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.00078 — Expired pointer dereference in Schematron validator.
*   **CVE-2025-49796** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.0055 — Out-of-bounds read in Schematron report formatting.
*   **CVE-2024-56171** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00048 — Use-after-free in xmlSchemaIDCFillNodeTables.

**Risk Distribution**

*   **Critical:** 8
*   **High:** 45
*   **Medium:** 46
*   **Low:** 6
*   **None:** 1

**Top 3 Most-Affected Packages:**

1.  **imagemagick:** 41 vulnerabilities (7 Critical, 15 High, 19 Medium)
2.  **openssl:** 25 vulnerabilities (1 Critical, 10 High, 14 Medium)
3.  **libxml2:** 18 vulnerabilities (4 Critical, 10 High, 4 Medium)

**Exploitation Landscape Stats:**

*   **Wild Exploited:** 1 (CVE-2025-48384 in git)
*   **Public PoC Available:** 8 unique CVEs
*   **Exploit Frameworks:** 1 unique CVE
*   **Bug Bounty Disclosed:** 7 unique CVEs

**CRA Compliance Actions**

1.  **Immediate Remediation for CVE-2025-48384 (git):** This vulnerability is actively exploited in the wild and requires mandatory reporting under CRA Article 14. Prioritize patching or mitigating `git` to version `1:2.47.3-0+deb13u1` or newer. Notify ENISA/CSIRT within 24 hours of discovery, followed by detailed reports within 72 hours and a final report within 14 days.
2.  **Urgent Patching of Critical Vulnerabilities with Public PoCs:** Address `CVE-2025-15467` in `openssl`, `CVE-2024-41817` in `imagemagick`, `CVE-2021-32804` and `CVE-2026-23745` in `tar`, `CVE-2025-48385` in `git`, `CVE-2025-69872` in `diskcache`, and `CVE-2025-68973` in `gnupg`. The presence of public exploits significantly increases the risk of attack.
3.  **Prioritize All Other Critical and High Vulnerabilities:** Systematically address the remaining 7 Critical and 44 High vulnerabilities across `imagemagick`, `openssl`, `libxml2`, `binutils`, `tar`, `curl`, `git`, `gnupg`, `subversion`, `perl`, and `dpkg`. Focus on those with higher EPSS scores first.
4.  **Investigate and Mitigate Bug Bounty Disclosed Vulnerabilities:** Review and address the 7 vulnerabilities in `curl` that have been reported through bug bounty programs. While not yet publicly exploited, these indicate known weaknesses that could be leveraged.
5.  **Maintain SBOM Hygiene and Regular Scanning:** Implement continuous vulnerability scanning and ensure the SBOM is regularly updated to accurately reflect the software components and their associated vulnerabilities. This proactive approach is crucial for ongoing CRA compliance.