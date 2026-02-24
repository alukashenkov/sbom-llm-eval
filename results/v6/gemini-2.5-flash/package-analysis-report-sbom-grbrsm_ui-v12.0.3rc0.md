## 1. SBOM Overview
- **Product:** sbom-grbrsm_ui-v12.0.3rc0 (SPDX format)
- **Scan Date:** 2025-07-11T08:54:40.000Z
- **Packages:** 338 total, 7 affected
- **Unique CVEs:** 9
  - CRITICAL: 1
  - HIGH: 5
  - MEDIUM: 3

## 2. CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
- **CVE-2025-7783** (form-data): CRITICAL (CVSS 9.4), EPSS 0.00177
- **CVE-2025-13465** (lodash): HIGH (CVSS 8.2), EPSS 0.00025
- 2 additional CVEs have PoC evidence.

## 4. Critical & High Findings
- **CVE-2026-25639** (axios): HIGH (CVSS 8.7), EPSS 0.00033
- **CVE-2025-54371** (axios): HIGH (CVSS 7.5)
- **CVE-2025-58754** (axios): HIGH (CVSS 7.5), EPSS 0.00102
- **CVE-2026-26996** (minimatch): HIGH (CVSS 8.7), EPSS 0.0004
- and 0 more across 0 packages.

## 5. Risk Distribution
- **Severity Counts:**
  - CRITICAL: 1
  - HIGH: 5
  - MEDIUM: 3
- **Top 3 Affected Packages:**
  - `axios@1.10.0`: 4 unique CVEs
  - `js-yaml@4.1.0`: 1 unique CVE
  - `lodash@4.17.21`: 1 unique CVE

## 6. CRA Compliance Actions
- Per CRA Article 10 (security requirements) and Article 11 (vulnerability handling):
  1. **Immediate Action (Article 11(1)):** Patch `form-data` to address CVE-2025-7783 (CRITICAL, PoC).
  2. **Urgent Action (Article 10(1)):** Patch `lodash` to address CVE-2025-13465 (HIGH, PoC).
  3. **Planned Action (Article 10(1)):** Plan patches for `axios` (CVE-2026-25639, CVE-2025-54371, CVE-2025-58754) and `minimatch` (CVE-2026-26996).
  4. **Hygiene (Article 10(6)):** Maintain accurate SBOM for all product components.