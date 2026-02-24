## 1. SBOM Overview

The SBOM is in the SPDX format and was created on 2025-07-11T08:54:40.000Z. The product name is "sbom-grbrsm_ui-v12.0.3rc0". The SBOM contains a total of 338 packages, of which 7 are affected by 13 advisories.

The vulnerability severity distribution is as follows:
- CRITICAL: 1
- HIGH: 5
- MEDIUM: 7
- LOW: 0

## 2. CRA Mandatory Reporting Triggers (Article 14)

The following vulnerabilities require ENISA/CSIRT notification as per the EU Cyber Resilience Act (CRA):

[CVE-2025-7783] form-data@4.0.3 — CVSS 9.4 — EPSS 0.00177 — Critical vulnerability in form-data's random boundary selection.
[CVE-2026-25639] axios@1.10.0 — CVSS 8.7 — EPSS 0.00033 — Axios is vulnerable to Denial of Service via __proto__ key in mergeConfig.

No other CRA mandatory reporting triggers were identified.

## 3. Exploit Availability Assessment

The following CVEs have public proof-of-concept (PoC) or exploit evidence available:

Public PoC available:
- [CVE-2025-7783] form-data@4.0.3 — PoC on GitHub

## 4. Critical & High Findings

The remaining CRITICAL and HIGH severity vulnerabilities are:

[CVE-2025-54371] axios@1.10.0 — CVSS 7.5 — EPSS 0.00177 — Axios has Transitive Critical Vulnerability via form-data.
[CVE-2025-58754] axios@1.10.0 — CVSS 7.5 — EPSS 0.00102 — Axios is vulnerable to DoS attack through lack of data size check.
[CVE-2025-13465] lodash@4.17.21 — CVSS 7.9 — EPSS 0.00025 — Lodash has Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions.
[CVE-2026-26996] minimatch@7.4.6 — CVSS 8.7 — EPSS 0.0004 — minimatch has a ReDoS via repeated wildcards with non-matching literal in pattern.
[CVE-2025-27789] @babel/runtime@7.0.0 — CVSS 6.2 — EPSS 0.00139 — Babel has inefficient RegExp complexity in generated code with .replace when transpiling named capturing groups.

## 5. Risk Distribution

The vulnerability severity distribution is:
- CRITICAL: 1
- HIGH: 5
- MEDIUM: 7
- LOW: 0

The top 3 most-affected packages are:
1. axios (4 advisories)
2. lodash (2 advisories)
3. minimatch (2 advisories)

The exploitation landscape shows that 1 CVE has a public PoC available, and no CVEs have been observed as actively exploited in the wild.

## 6. CRA Compliance Actions (max 5)

1. IMMEDIATE: Patch the CRITICAL vulnerability in form-data (CVE-2025-7783) and notify ENISA/CSIRT within 24 hours.
2. URGENT: Patch the HIGH vulnerabilities in axios (CVE-2025-54371, CVE-2025-58754) and lodash (CVE-2025-13465) within 72 hours, and provide a detailed report to ENISA/CSIRT.
3. PLANNED: Patch the HIGH vulnerability in minimatch (CVE-2026-26996) and the MEDIUM vulnerability in @babel/runtime (CVE-2025-27789) within 14 days, and provide a final report to ENISA/CSIRT.
4. SBOM HYGIENE: Regularly review the SBOM for new advisories and update dependencies accordingly to maintain CRA compliance.
5. SBOM HYGIENE: Implement a vulnerability management process to proactively identify and address security issues in a timely manner.