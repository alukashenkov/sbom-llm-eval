## 1. SBOM Overview
*   **Product**: la-vulners-mcp (container)
*   **Format**: CycloneDX
*   **Scan Date**: 2026-02-24
*   **Packages**: 97 total / 3 affected
*   **Unique CVEs**: 7 (CRITICAL: 2, HIGH: 1, MEDIUM: 2, LOW: 2)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   0 CVEs have PoC evidence per `cveAnalytics.pocSummary`.
*   Note: Advisory data indicates public discussion/issue links for CVE-2026-27171 (zlib) and CVE-2025-60876 (busybox), but these are not classified as verified exploits in summary totals.

## 4. Critical & High Findings
*   **CVE-2023-45853** | zlib | CVSS: 9.8 | EPSS: 0.01396 (Integer Overflow in MiniZip)
*   **CVE-2026-22184** | zlib | CVSS: 9.8 | EPSS: 0.00042 (Global Buffer Overflow in untgz)
*   **CVE-2025-26519** | musl | CVSS: 8.1 | EPSS: 0.00022 (Out-of-bounds write in iconv)

## 5. Risk Distribution
*   **Severity**: CRITICAL (2), HIGH (1), MEDIUM (2), LOW (2).
*   **Top Affected Packages**: 
    1. zlib@1.3.1-r2 (3 unique CVEs)
    2. busybox@1.37.0-r30 (3 unique CVEs)
    3. musl@1.2.5-r21 (1 unique CVE)

## 6. CRA Compliance Actions
1.  **Immediate**: No Article 14 triggers present; however, prioritize patching `zlib` to v1.3.2+ to address CRITICAL CVE-2023-45853 and CVE-2026-22184 per Article 10 security requirements.
2.  **Urgent**: Update `musl` to v1.2.6 or later to remediate HIGH severity CVE-2025-26519 (Article 11 vulnerability handling).
3.  **Planned**: Update `busybox` to address MEDIUM severity request-splitting (CVE-2025-60876) and terminal escape vulnerabilities.
4.  **Hygiene**: Maintain SBOM accuracy and perform regular rescans to ensure compliance with Article 10(6) regarding the duty of care in software component monitoring.