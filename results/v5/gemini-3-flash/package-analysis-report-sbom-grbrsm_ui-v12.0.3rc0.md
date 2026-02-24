## 1. SBOM Overview
The product **sbom-grbrsm_ui-v12.0.3rc0** (SPDX format) was scanned on July 11, 2025. Out of 338 total packages, 7 are affected by known vulnerabilities. The scan identified **9 unique CVEs** with a risk distribution of **1 CRITICAL**, **5 HIGH**, and **3 MEDIUM** findings.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities in this set are currently listed in the CISA KEV or have evidence of active exploitation in the wild.

## 3. Exploit Availability Assessment
There are **2** unique CVEs with publicly available Proof-of-Concept (PoC) exploits identified in GitHub repositories.

**Top CVEs with PoC Evidence:**
1.  **CVE-2025-7783** (form-data): CVSS 9.4 (CRITICAL). Unsafe random function for boundary selection.
2.  **CVE-2025-7783** (axios): CVSS 7.5 (HIGH). Transitive vulnerability via form-data dependency.

0 additional CVEs have exploit evidence.

## 4. Critical & High Findings
The following high-impact vulnerabilities require immediate attention:
*   **CVE-2026-25639** (axios): CVSS 8.7, EPSS 0.00033. Prototype Pollution leading to Denial of Service.
*   **CVE-2026-26996** (minimatch): CVSS 8.7, EPSS 0.00040. Regular Expression Denial of Service (ReDoS).
*   **CVE-2025-13465** (lodash): CVSS 8.2, EPSS 0.00025. Prototype Pollution in `_.unset` and `_.omit`.
*   **CVE-2025-58754** (axios): CVSS 7.5, EPSS 0.00102. DoS via lack of data size check in Node.js adapter.

And **0** more HIGH findings across **0** packages.

## 5. Risk Distribution
The vulnerability landscape is concentrated in core utility libraries. **axios** is the most affected package with 4 unique CVEs, followed by **js-yaml**, **lodash**, **minimatch**, and **@babel/runtime** with 1 unique CVE each. The severity is skewed toward HIGH and CRITICAL impacts, primarily affecting availability (DoS) and integrity (Prototype Pollution).

## 6. CRA Compliance Actions
1.  **Immediate (CRITICAL):** Update `form-data` to a version using a cryptographically secure random number generator to resolve **CVE-2025-7783**.
2.  **Urgent (Exploitable HIGH):** Update `axios` to the latest patched version (v1.x.x+) to address Prototype Pollution (**CVE-2026-25639**) and DoS (**CVE-2025-58754**).
3.  **Urgent:** Update `minimatch` to version 9.0.0 or higher to mitigate ReDoS (**CVE-2026-26996**).
4.  **Planned:** Update `lodash` to v4.17.23+ to resolve Prototype Pollution (**CVE-2025-13465**).
5.  **Hygiene:** Review `js-yaml` and `prismjs` for non-breaking minor version updates to clear remaining MEDIUM findings.