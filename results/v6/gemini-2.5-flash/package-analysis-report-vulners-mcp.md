## 1. SBOM Overview
- **Product:** vulners-mcp (CycloneDX)
- **Scan Date:** 2026-02-24
- **Total Packages:** 560
- **Affected Packages:** 20
- **Unique CVEs:** 188 (12 CRITICAL, 76 HIGH, 87 MEDIUM, 12 LOW, 1 NONE)

## 2. CRA Mandatory Reporting (Article 14)
- **CVE-2025-48384** (git@1:2.47.3-0+deb13u1): CVSS 8.0, EPSS 0.00456. Wildly exploited and listed in CISA KEV.
- Requires ENISA/CSIRT notification per CRA Article 14(2): 24h early warning → 72h assessment → 14-day final report.

## 3. Exploit Assessment
- **CVE-2025-48384** (git@1:2.47.3-0+deb13u1): CVSS 8.0 (HIGH), EPSS 0.00456. PoC available.
- **CVE-2014-9846** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.04666. No PoC listed.
- **CVE-2015-8895** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 7.5 (HIGH), EPSS 0.01472. No PoC listed.
- **CVE-2014-9850** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 7.5 (HIGH), EPSS 0.02408. No PoC listed.
- **CVE-2017-9098** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 7.5 (HIGH), EPSS 0.0146. No PoC listed.
- 30 additional CVEs have PoC evidence.

## 4. Critical & High Findings
- **CVE-2025-15467** (openssl@3.5.4-1~deb13u2): CVSS 9.8 (CRITICAL), EPSS 0.00672.
- **CVE-2026-22770** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.00065.
- **CVE-2026-23876** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.00062.
- **CVE-2014-9852** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.01316.
- **CVE-2025-57807** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.00042.
- **CVE-2025-53014** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.00031.
- **CVE-2025-53101** (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8 (CRITICAL), EPSS 0.00069.
- **CVE-2024-56171** (libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2): CVSS 9.8 (CRITICAL), EPSS 0.00048.
- and 69 more across 19 packages.

## 5. Risk Distribution
- **CRITICAL:** 12 CVEs
- **HIGH:** 76 CVEs
- **MEDIUM:** 87 CVEs
- **LOW:** 12 CVEs
- **NONE:** 1 CVE
- **Top 3 Affected Packages:**
    1. imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 (77 unique CVEs)
    2. binutils@2.44-3 (32 unique CVEs)
    3. libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 (17 unique CVEs)

## 6. CRA Compliance Actions
- **Immediate (Article 14):** Patch `git@1:2.47.3-0+deb13u1` for CVE-2025-48384 (wildly exploited, CISA KEV listed).
- **Urgent (Article 10, 11):**
    - Patch `openssl@3.5.4-1~deb13u2` for CVE-2025-15467 (CRITICAL, PoC available).
    - Patch `imagemagick@8:7.1.1.43+dfsg1-1+deb13u5` for CVE-2014-9846 (CRITICAL, PoC available).
    - Patch `imagemagick@8:7.1.1.43+dfsg1-1+deb13u5` for CVE-2024-41817 (HIGH, PoC available).
- **Planned (Article 10, 11):** Address remaining 73 HIGH severity CVEs and 87 MEDIUM severity CVEs in affected packages.
- **Hygiene (Article 10(6)):** Maintain accurate and up-to-date SBOMs for all software components.