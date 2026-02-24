## 1. SBOM Overview
This vulnerability summary is based on a CycloneDX SBOM for the product `vulners-mcp` (version `sha256:1cb7222c81317af65f1a4fb535ccbd3627926d1ab84f583f3358fc841b94ddd9`), generated on 2026-02-24T14:35:34.000Z. Out of 560 total packages, 20 are affected by 188 unique CVEs. The severity distribution includes 12 Critical, 76 High, 87 Medium, 12 Low, and 1 None severity vulnerabilities.

## 2. CRA Mandatory Reporting Triggers (Article 14)
The following CVEs are identified as CRA mandatory reporting triggers due to active exploitation (wildExploited=true or CISA KEV listing):
- **CVE-2025-48384** (CVSS: 8, EPSS: 0.00456) affecting `git@1:2.47.3-0+deb13u1`.
Immediate notification to ENISA and relevant CSIRT within 24 hours of becoming aware is required, followed by a detailed report within 72 hours, and a final report within 14 days.

## 3. Exploit Availability Assessment
A total of 33 CVEs have publicly available exploit evidence from various sources. The top 5 CVEs with known PoCs by severity are:
- **CVE-2025-15467** (CRITICAL, CVSS: 9.8) in `openssl`
- **CVE-2024-41817** (HIGH, CVSS: 7.8) in `imagemagick`
- **CVE-2021-32804** (HIGH, CVSS: 8.2) in `tar`
- **CVE-2025-48384** (HIGH, CVSS: 8) in `git`
- **CVE-2026-23745** (HIGH, CVSS: 8.2) in `tar`
28 additional CVEs have exploit evidence.

## 4. Critical & High Findings
Beyond the mandatory reporting triggers, the following Critical and High severity CVEs warrant immediate attention:
- **CVE-2025-15467** (CRITICAL, CVSS: 9.8) in `openssl`
- **CVE-2026-22770** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2026-23876** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2014-9852** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2014-9846** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2025-53014** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2025-53101** (CRITICAL, CVSS: 9.8) in `imagemagick`
- **CVE-2025-57807** (CRITICAL, CVSS: 9.8) in `imagemagick`
and 69 more HIGH findings across 12 packages.

## 5. Risk Distribution
The vulnerabilities are distributed as follows: 12 Critical, 76 High, 87 Medium, 12 Low, and 1 None. The packages with the most unique CVEs are:
- `imagemagick@8:7.1.1.43+dfsg1-1+deb13u5` (77 unique CVEs)
- `binutils@2.44-3` (32 unique CVEs)
- `libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2` (17 unique CVEs)
- `openssl@3.5.4-1~deb13u2` (16 unique CVEs)
- `curl@8.14.1-2+deb13u2` (11 unique CVEs)

## 6. CRA Compliance Actions
1. **Immediate Action (CRA Mandatory Reporting):** Address **CVE-2025-48384** in `git@1:2.47.3-0+deb13u1` due to active exploitation. Upgrade `git` to a patched version immediately and report to ENISA/CSIRT.
2. **Urgent Patching (Critical with PoC):** Prioritize patching `openssl` to mitigate **CVE-2025-15467** (CRITICAL, CVSS: 9.8) and `imagemagick` for **CVE-2026-23876** (CRITICAL, CVSS: 9.8), both having public exploit evidence.
3. **High-Priority Patching:** Upgrade `imagemagick` to address the numerous Critical and High vulnerabilities, including **CVE-2026-22770**, **CVE-2014-9852**, **CVE-2014-9846**, **CVE-2025-53014**, **CVE-2025-53101**, and **CVE-2025-57807**.
4. **Regular Patching Cycle:** Plan upgrades for `binutils`, `libxml2`, and `curl` to address their respective High and Medium severity vulnerabilities.
5. **SBOM Hygiene:** Implement continuous monitoring for newly disclosed vulnerabilities and ensure regular SBOM updates for all components to maintain CRA compliance.