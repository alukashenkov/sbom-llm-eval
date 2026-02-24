## 1. SBOM Overview

This SPDX SBOM for `grbrsm_ui-v12.0.3rc0`, generated on 2025-07-11, identifies 7 affected packages out of 338 total. The scan revealed 8 unique CVEs: 1 CRITICAL, 5 HIGH, and 2 MEDIUM.

## 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment

The following CVEs have evidence of exploit availability (PoC):

*   **CVE-2025-7783** form-data@4.0.3 — CVSS 9.4 — EPSS 0.00177 — Unsafe random function in form-data for choosing boundary.
*   **CVE-2025-54371** axios@1.10.0 — CVSS 7.5 — EPSS 0.00177 — Transitive Critical Vulnerability via form-data.
*   **CVE-2025-13465** lodash@4.17.21 — CVSS 8.2 — EPSS 0.00025 — Prototype Pollution in `_.unset` and `_.omit` functions.
*   **CVE-2026-26996** minimatch@7.4.6 — CVSS 8.7 — EPSS 0.0004 — Regular Expression Denial of Service (ReDoS).
*   **CVE-2026-25639** axios@1.10.0 — CVSS 8.7 — EPSS 0.00033 — Prototype Pollution via `__proto__` key in `mergeConfig`.

## 4. Critical & High Findings

*   **CVE-2025-58754** axios@1.10.0 — CVSS 7.5 — EPSS 0.00102 — DoS through lack of data size check.

## 5. Risk Distribution

Severity distribution (unique CVEs): CRITICAL: 1, HIGH: 5, MEDIUM: 2.
Top 3 most-affected packages: `axios` (4 advisories), `lodash` (2 advisories), `js-yaml` (2 advisories).

## 6. CRA Compliance Actions

1.  **URGENT:** Upgrade `form-data` to a patched version (e.g., `form-data@^4.0.4` or higher) to mitigate CVE-2025-7783 (CRITICAL, PoC available). This directly addresses the unsafe random function.
2.  **URGENT:** Upgrade `axios` to a version that addresses CVE-2025-54371, CVE-2025-58754, and CVE-2026-25639. This will likely involve upgrading its dependency on `form-data` and addressing DoS and Prototype Pollution vulnerabilities.
3.  **PLANNED:** Upgrade `lodash` to a version addressing CVE-2025-13465 (HIGH, PoC available) to prevent Prototype Pollution.
4.  **PLANNED:** Upgrade `minimatch` to a version addressing CVE-2026-26996 (HIGH, PoC available) to mitigate ReDoS vulnerabilities.
5.  **SBOM HYGIENE:** Review and update `js-yaml` and `@babel/runtime` to address their respective MEDIUM severity vulnerabilities (CVE-2025-64718 and CVE-2025-27789).