### 1. SBOM Overview
**Product:** sbom-grbrsm_ui-v12.0.3rc0
**Format:** SPDX | **Scan Date:** 2025-07-11
**Scope:** 338 total packages; 7 affected.
**Vulnerability Count:** 13 advisories (1 Critical, 5 High, 3 Medium).

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. (Zero vulnerabilities flagged as `wildExploited` or present in CISA KEV).

### 3. Exploit Availability Assessment
**Public PoC Available:**
*   **CVE-2025-7783** (form-data@4.0.3) — Critical severity. Unsafe random function boundary selection.
*   **CVE-2025-54371** (axios@1.10.0) — High severity. Note: Advisory is withdrawn, but exploit code exists on GitHub.

### 4. Critical & High Findings
*   **CVE-2025-58754** | axios@1.10.0 | CVSS 7.5 (High) | EPSS 0.00102 | Fix: Upgrade available.
*   **CVE-2026-25639** | axios@1.10.0 | CVSS 8.7 (High) | EPSS 0.00033 | Fix: Upgrade available.
*   **CVE-2025-13465** | lodash@4.17.21 | CVSS 8.2 (High) | EPSS 0.00025 | Fix: Upgrade available.
*   **CVE-2026-26996** | minimatch@7.4.6 | CVSS 8.7 (High) | EPSS 0.00040 | Fix: Upgrade available.

### 5. Risk Distribution
**Severity:** 1 Critical, 5 High, 3 Medium.
**Top Affected Packages:**
1.  axios (4 advisories)
2.  lodash (1 advisory)
3.  minimatch (1 advisory)
**Exploitation Landscape:** 15% of advisories have public Proof-of-Concept (PoC) code. No active exploitation detected.

### 6. CRA Compliance Actions
1.  **Immediate:** Upgrade `form-data` to resolve CVE-2025-7783 (Critical) due to public exploit availability.
2.  **Urgent:** Update `axios` to patch multiple High-severity DoS and Prototype Pollution vulnerabilities.
3.  **Urgent:** Upgrade `lodash` to mitigate Prototype Pollution (CVE-2025-13465).
4.  **Planned:** Address remaining Medium/High issues in `minimatch`, `js-yaml`, `@babel/runtime`, and `prismjs`.
5.  **Hygiene:** Re-scan and update SBOM post-remediation to maintain accurate vulnerability transparency.