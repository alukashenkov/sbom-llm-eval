## Vulnerability Summary for vulners-mcp

### 1. SBOM Overview
This CycloneDX-formatted SBOM for `vulners-mcp` (sha256:1cb7222c81317af65f1a4fb535ccbd3627926d1ab84f583f3358fc841b94ddd9) was generated on 2026-02-24. Out of 560 total packages, 20 are affected by vulnerabilities. There are 10 Critical, 36 High, 39 Medium, and 8 Low unique CVEs identified.

### 2. CRA Mandatory Reporting Triggers (Article 14)
- CVE-2025-48384 Git@1:2.47.3-0+deb13u1 — HIGH — 0.00456 — This vulnerability has been identified as actively exploited in the wild and is listed on CISA's KEV catalog. Immediate notification to ENISA/CSIRT is required within 24 hours.

### 3. Exploit Availability Assessment
The following CVEs have evidence of public exploits:
- CVE-2025-15467 openssl@3.5.4-1~deb13u2 — CRITICAL — 0.00672 — Multiple public exploits available.
- CVE-2024-41817 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — HIGH — 0.18593 — Public exploits available on GitHub.
- CVE-2021-32804 tar@1.35+dfsg-3.1 — HIGH — 0.84982 — Public exploit available on GitHub.
- CVE-2025-11187 openssl@3.5.4-1~deb13u2 — HIGH — 0.00011 — Public exploit available on Packetstorm.
- CVE-2025-15468 openssl@3.5.4-1~deb13u2 — MEDIUM — 0.00048 — Public exploit available on Packetstorm.
18 additional CVEs have exploit evidence.

### 4. Critical & High Findings
- CVE-2024-40896 libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CRITICAL — 0.00553
- CVE-2024-56171 libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CRITICAL — 0.00048
- CVE-2025-53014 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.00031
- CVE-2025-53101 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.00069
- CVE-2025-57807 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.00042
- CVE-2026-22770 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.00065
- CVE-2026-23876 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.00062
- CVE-2014-9846 imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CRITICAL — 0.04666
and 28 more HIGH findings across 6 packages.

### 5. Risk Distribution
- **Critical:** 10 CVEs
- **High:** 36 CVEs
- **Medium:** 39 CVEs
- **Low:** 8 CVEs

Most affected packages:
1. imagemagick: 42 advisories
2. openssl: 18 advisories
3. binutils: 18 advisories

### 6. CRA Compliance Actions
1. **Immediate Action Required:** Patch `git` to a version that remediates CVE-2025-48384, as it is actively exploited. This is a mandatory CRA Article 14 notification event.
2. **Urgent Patching:** Prioritize patching `openssl` to address CVE-2025-15467 (CRITICAL, public exploit) and `imagemagick` for CVE-2024-41817 (HIGH, public exploit).
3. **High Priority Updates:** Update `libxml2` to a version that fixes CVE-2024-40896 and CVE-2024-56171 (both CRITICAL).
4. **Regular Patching Cycle:** Incorporate updates for all other identified High and Critical vulnerabilities into the standard patching schedule.
5. **SBOM Hygiene:** Implement automated scanning for CISA KEV and wild exploitation to ensure timely detection and reporting of CRA Article 14 triggers.