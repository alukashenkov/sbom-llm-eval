## 1. SBOM Overview
Product: sbom-grbrsm_ui-v12.0.3rc0 (SPDX). Scan date: 2025-07-11. 338 total packages; 7 affected. Identified 9 unique CVEs: 1 Critical, 4 High, 4 Medium.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
1. CVE-2025-7783 form-data@4.0.3 — CVSS 9.4 — EPSS 0.00177 — Unsafe random boundary generation allows request forgery.
2. CVE-2025-54371 axios@1.10.0 — CVSS 7.5 — EPSS N/A — Transitive vulnerability via form-data (withdrawn advisory, PoC present).
0 additional CVEs have exploit evidence.

## 4. Critical & High Findings
1. CVE-2026-26996 minimatch@7.4.6 — CVSS 8.7 — EPSS 0.0004
2. CVE-2026-25639 axios@1.10.0 — CVSS 8.7 — EPSS 0.00033
3. CVE-2025-13465 lodash@4.17.21 — CVSS 8.2 — EPSS 0.00025
4. CVE-2025-58754 axios@1.10.0 — CVSS 7.5 — EPSS 0.00102
and 0 more HIGH findings across 2 packages.

## 5. Risk Distribution
Severity: Critical (1), High (4), Medium (4). Top affected packages: axios (4 advisories), js-yaml (2), lodash (2).

## 6. CRA Compliance Actions
1. **Immediate:** Upgrade **form-data** to v4.1.0+ to resolve Critical CVE-2025-7783 (active exploit).
2. **Urgent:** Upgrade **axios** to v1.7.9+ to fix High severity DoS and Prototype Pollution.
3. **Urgent:** Upgrade **minimatch** to v9.0.0+ to mitigate ReDoS (CVE-2026-26996).
4. **Planned:** Upgrade **lodash** to v4.17.23+ to address Prototype Pollution.
5. **Planned:** Upgrade **js-yaml** to v4.2.0+ to fix Prototype Pollution.