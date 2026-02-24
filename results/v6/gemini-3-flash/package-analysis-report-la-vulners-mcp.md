## 1. SBOM Overview
*   **Product**: la-vulners-mcp (Container)
*   **Format**: CycloneDX
*   **Scan Date**: 2026-02-24
*   **Packages**: 97 total / 3 affected
*   **Unique CVEs**: 7 (CRITICAL: 2, HIGH: 1, MEDIUM: 2, LOW: 2)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   0 CVEs have PoC evidence according to `pocSummary`.
*   *Note: While `pocSummary` is empty, advisory data indicates public discussion/issue links for CVE-2026-27171 and CVE-2025-60876.*

## 4. Critical & High Findings
*   **CVE-2023-45853**: zlib (1.3.1-r2), CVSS: 9.8, EPSS: 0.01396. Integer overflow in MiniZip.
*   **CVE-2026-22184**: zlib (1.3.1-r2), CVSS: 9.8, EPSS: 0.00042. Global buffer overflow in untgz utility.
*   **CVE-2025-26519**: musl (1.2.5-r21), CVSS: 8.1, EPSS: 0.00022. Out-of-bounds write in iconv conversion.
*   and 0 more across 0 packages.

## 5. Risk Distribution
*   **Severity**: CRITICAL (2), HIGH (1), MEDIUM (2), LOW (2).
*   **Top Affected Packages**: 
    1. zlib@1.3.1-r2 (3 unique CVEs)
    2. busybox@1.37.0-r30 (3 unique CVEs)
    3. musl@1.2.5-r21 (1 unique CVE)

## 6. CRA Compliance Actions
1.  **Immediate**: No Article 14 triggers identified; however, prioritize patching `zlib` to version 1.3.2 or higher to resolve CRITICAL overflows (Article 10).
2.  **Urgent**: Update `musl` to version 1.2.6 to remediate the HIGH severity out-of-bounds write (CVE-2025-26519) per Article 11 vulnerability handling requirements.
3.  **Planned**: Update `busybox` to address MEDIUM/LOW findings (CVE-2025-60876, CVE-2025-46394) to maintain security-by-design standards.
4.  **Hygiene**: Maintain and regularly update SBOM records to ensure continued compliance with CRA Article 10(6) documentation obligations.