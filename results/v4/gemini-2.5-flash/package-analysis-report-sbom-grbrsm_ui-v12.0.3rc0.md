## EU Cyber Resilience Act (CRA) Vulnerability Summary

### 1. SBOM Overview
This report summarizes vulnerabilities for `sbom-grbrsm_ui-v12.0.3rc0`, an SPDX-formatted SBOM generated on 2025-07-11. Out of 338 total packages, 7 are affected by vulnerabilities. There are 9 unique CVEs identified, comprising 1 CRITICAL, 5 HIGH, and 3 MEDIUM severity vulnerabilities.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of exploit availability:
- CVE-2025-7783 form-data@4.0.3 — CVSS 9.4 — EPSS 0.00177 — Unsafe random function in form-data for choosing boundary.
- CVE-2026-25639 axios@1.10.0 — CVSS 8.7 — EPSS 0.00033 — Prototype Pollution.
- CVE-2026-26996 minimatch@7.4.6 — CVSS 8.7 — EPSS 0.0004 — Regular Expression Denial of Service (ReDoS).
- CVE-2025-13465 lodash@4.17.21 — CVSS 8.2 — EPSS 0.00025 — Prototype Pollution.
- CVE-2025-7783 axios@1.10.0 — CVSS 7.5 — EPSS 0.00177 — Transitive Critical Vulnerability via form-data.
1 additional CVE has exploit evidence.

### 4. Critical & High Findings
- CVE-2025-58754 axios@1.10.0 — CVSS 7.5 — EPSS 0.00102 — DoS attack through lack of data size check.
- CVE-2025-54371 axios@1.10.0 — CVSS 7.5 — EPSS 0.00177 — Transitive Critical Vulnerability via form-data.
- CVE-2026-25639 axios@1.10.0 — CVSS 7.5 — EPSS 0.00033 — Denial of Service via __proto__ Key in mergeConfig.

### 5. Risk Distribution
- CRITICAL: 1
- HIGH: 5
- MEDIUM: 3

Top 3 most-affected packages:
1. axios (4 advisories)
2. js-yaml (2 advisories)
3. lodash (2 advisories)

### 6. CRA Compliance Actions
1. **Immediate Action (Target: form-data@4.0.3):** Upgrade `form-data` to a version that addresses CVE-2025-7783 (CVSS 9.4 CRITICAL) to mitigate the unsafe random function vulnerability. This is a critical security flaw with exploit availability.
2. **Urgent Action (Target: axios@1.10.0):** Upgrade `axios` to a patched version to remediate CVE-2026-25639 (CVSS 8.7 HIGH) and CVE-2025-58754 (CVSS 7.5 HIGH), addressing Prototype Pollution and DoS vulnerabilities.
3. **Planned Action (Target: minimatch@7.4.6):** Upgrade `minimatch` to a version that fixes CVE-2026-26996 (CVSS 8.7 HIGH) to prevent Regular Expression Denial of Service (ReDoS) attacks.
4. **Planned Action (Target: lodash@4.17.21):** Upgrade `lodash` to a version addressing CVE-2025-13465 (CVSS 8.2 HIGH) to resolve Prototype Pollution vulnerabilities.
5. **SBOM Hygiene:** Implement automated scanning for `cisa_kev` and `wildExploited` flags to ensure rapid identification and reporting of CRA Article 14 mandatory triggers.