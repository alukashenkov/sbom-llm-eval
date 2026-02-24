## Vulnerability Summary for vulners-mcp

### 1. SBOM Overview
This CycloneDX SBOM for `vulners-mcp:sha256:1cb7222c81317af65f1a4fb535ccbd3627926d1ab84f583f3358fc841b94ddd9` was generated on 2026-02-24. Out of 560 total packages, 20 are affected by vulnerabilities. The unique CVE count by severity is: CRITICAL: 7, HIGH: 48, MEDIUM: 40, LOW: 7.

### 2. CRA Mandatory Reporting Triggers (Article 14)
The following vulnerabilities require mandatory reporting to ENISA/CSIRT within 24 hours (initial notification), 72 hours (detailed), and 14 days (final):

- **CVE-2025-48384** git@1:2.47.3-0+deb13u1 — CVSS:8.0 — EPSS:0.00456 — Arbitrary code execution through broken config quoting.

### 3. Exploit Availability Assessment
The following top 5 most critical CVEs have known exploit evidence:

- **CVE-2021-32804** tar@1.35+dfsg-3.1 — CVSS:8.2 — EPSS:0.84982
- **CVE-2014-9846** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.04666
- **CVE-2014-9850** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:7.5 — EPSS:0.02408
- **CVE-2017-9098** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:7.5 — EPSS:0.0146
- **CVE-2014-9852** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.01316

4 additional CVEs have exploit evidence.

### 4. Critical & High Findings
The following critical and high severity vulnerabilities were identified:

- **CVE-2025-15467** openssl@3.5.4-1~deb13u2 — CVSS:9.8 — EPSS:0.00672
- **CVE-2026-22770** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.00065
- **CVE-2026-23876** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.00062
- **CVE-2024-56171** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS:9.8 — EPSS:0.00048
- **CVE-2025-53014** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.00031
- **CVE-2025-53101** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.00069
- **CVE-2025-57807** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS:9.8 — EPSS:0.00042
- **CVE-2024-40896** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS:9.1 — EPSS:0.00553
and 40 more HIGH findings across 10 packages.

### 5. Risk Distribution
- **CRITICAL:** 7 unique CVEs
- **HIGH:** 48 unique CVEs
- **MEDIUM:** 40 unique CVEs
- **LOW:** 7 unique CVEs

Top 3 most-affected packages:
1. **imagemagick:** 41 advisories
2. **openssl:** 15 advisories
3. **binutils:** 15 advisories

### 6. CRA Compliance Actions
1. **Immediate Action:** Patch `git` to address CVE-2025-48384 (wildExploited). This requires urgent notification to ENISA/CSIRT.
2. **Urgent Action:** Update `tar` to a version addressing CVE-2021-32804 (EPSS: 0.84982) to mitigate arbitrary file creation/overwrite risks.
3. **Urgent Action:** Update `imagemagick` to mitigate critical vulnerabilities CVE-2014-9846, CVE-2026-22770, CVE-2026-23876, CVE-2025-53014, CVE-2025-53101, CVE-2025-57807, and CVE-2014-9852.
4. **Planned Action:** Update `libxml2` to address critical vulnerabilities CVE-2024-56171 and CVE-2024-40896.
5. **SBOM Hygiene:** Implement automated vulnerability scanning and SBOM generation in CI/CD pipelines to proactively identify and address vulnerabilities.