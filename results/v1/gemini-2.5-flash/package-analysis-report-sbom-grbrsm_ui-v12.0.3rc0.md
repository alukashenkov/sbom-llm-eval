## Vulnerability Summary for `sbom-grbrsm_ui-v12.0.3rc0`

**SBOM Overview**
* Product Name: `sbom-grbrsm_ui-v12.0.3rc0`
* Format: SPDX
* Scan Date: 2025-07-11T08:54:40.000Z
* Total Packages: 338
* Affected Packages: 7
* Total Advisories: 13
* Vulnerability Counts:
    * CRITICAL: 1
    * HIGH: 8
    * MEDIUM: 4

**CRA Mandatory Reporting Triggers (Article 14)**
No CRA mandatory reporting triggers identified (no `wildExploited=true` or CISA KEV entries).

**Exploit Availability Assessment**
* **Public PoC available:**
    * CVE-2025-54371 (axios@1.10.0) - GHSA-RM8P-CX58-HCVX
    * CVE-2025-7783 (form-data@4.0.3) - GHSA-FJXV-7RQG-78G4

**Critical & High Findings**
* CVE-2025-58754 (axios@1.10.0) - CVSS: 7.5, EPSS: 0.00102 - Axios is vulnerable to DoS attack through lack of data size check.
* CVE-2026-25639 (axios@1.10.0) - CVSS: 8.7, EPSS: 0.00033 - Prototype Pollution.
* CVE-2026-25639 (axios@1.10.0) - CVSS: 7.5, EPSS: 0.00033 - Axios is Vulnerable to Denial of Service via `__proto__` Key in mergeConfig.
* CVE-2025-13465 (lodash@4.17.21) - CVSS: 7.9, EPSS: 0.00025 - Lodash has Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions.
* CVE-2025-13465 (lodash@4.17.21) - CVSS: 8.2, EPSS: 0.00025 - Prototype Pollution.
* CVE-2026-26996 (minimatch@7.4.6) - CVSS: 8.7, EPSS: 0.0004 - Regular Expression Denial of Service (ReDoS).
* CVE-2026-26996 (minimatch@7.4.6) - CVSS: 8.7, EPSS: N/A - minimatch has a ReDoS via repeated wildcards with non-matching literal in pattern.

**Risk Distribution**
* **Severity Counts:** CRITICAL: 1, HIGH: 8, MEDIUM: 4
* **Top 3 Most-Affected Packages:**
    1. axios (4 advisories)
    2. lodash (2 advisories)
    3. minimatch (2 advisories)
* **Exploitation Landscape Stats:** 2 CVEs have publicly available Proof-of-Concepts (PoCs).

**CRA Compliance Actions**
1. **Immediate Action: Address CVE-2025-7783 in `form-data` (CRITICAL, PoC available).** This vulnerability, affecting `form-data@4.0.3`, has a CVSSv4 score of 9.4 and a public PoC. Prioritize upgrading `form-data` to a patched version to mitigate the risk of compromise.
2. **Urgent Action: Address `axios` vulnerabilities with available PoCs.** The `axios@1.10.0` package has multiple HIGH severity vulnerabilities (CVE-2025-54371, CVE-2025-58754, CVE-2026-25639) with public PoCs. Upgrade `axios` to a secure version to prevent potential exploitation.
3. **Planned Action: Remediate all remaining HIGH severity vulnerabilities.** Prioritize upgrading `lodash@4.17.21` (CVE-2025-13465) and `minimatch@7.4.6` (CVE-2026-26996) to versions that address their respective prototype pollution and ReDoS vulnerabilities.
4. **Planned Action: Address MEDIUM severity vulnerabilities.** Review and plan remediation for `js-yaml@4.1.0` (CVE-2025-64718) and `@babel/runtime@7.0.0` (CVE-2025-27789) to reduce overall attack surface.
5. **SBOM Hygiene: Implement continuous monitoring for `wildExploited` and CISA KEV.** Regularly scan dependencies and integrate threat intelligence feeds to promptly identify and report any vulnerabilities that become subject to mandatory CRA reporting.