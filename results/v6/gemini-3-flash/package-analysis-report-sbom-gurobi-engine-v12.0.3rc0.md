## 1. SBOM Overview
*   **Product**: `sbom-gurobi-engine-v12.0.3rc0`
*   **Format**: SPDX
*   **Scan Date**: 2025-07-11
*   **Packages**: 12 total, 3 affected.
*   **Unique CVEs**: 62 (3 CRITICAL, 23 HIGH, 32 MEDIUM, 3 LOW, 1 NONE).

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **PoC Evidence**: 8 GitHub exploits, 10 Packetstorm entries, 6 HackerOne reports.
*   **Top Exploited CVEs**:
    *   **CVE-2025-15467** (OpenSSL): CRITICAL (9.8), EPSS: 0.00672. Stack buffer overflow in CMS AuthEnvelopedData.
    *   **CVE-2025-4517** (Python): CRITICAL (9.4), EPSS: 0.00071. Arbitrary writes via tarfile realpath overflow.
    *   **CVE-2007-4559** (Python): CRITICAL (9.8), EPSS: 0.90582. Directory traversal in tarfile module.
    *   **CVE-2025-4138** (Python): HIGH (7.5), EPSS: 0.00077. Extraction filter bypass for symlinks.
    *   **CVE-2025-4330** (Python): HIGH (7.5), EPSS: 0.00298. Extraction filter bypass for linking.
*   19 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2023-6597**, python, CVSS 7.8, EPSS 0.00071.
*   **CVE-2024-9287**, python, CVSS 7.8, EPSS 0.00062.
*   **CVE-2023-41105**, python, CVSS 7.5, EPSS 0.00370.
*   **CVE-2023-36632**, python, CVSS 7.5, EPSS 0.00112.
*   **CVE-2024-4032**, python, CVSS 7.5, EPSS 0.01127.
*   **CVE-2024-6232**, python, CVSS 7.5, EPSS 0.02874.
*   **CVE-2025-9230**, openssl, CVSS 7.5, EPSS 0.00031.
*   **CVE-2025-9086**, curl, CVSS 7.5, EPSS 0.00035.
*   And 11 more across 3 packages.

## 5. Risk Distribution
*   **Severity**: 3 CRITICAL, 23 HIGH, 32 MEDIUM.
*   **Top Affected Packages**:
    1.  `python@3.11.4` (40 unique CVEs)
    2.  `openssl@3.0.16` (12 unique CVEs)
    3.  `curl@8.14.1` (10 unique CVEs)

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `openssl` to v3.0.17+ to remediate CRITICAL stack overflow (CVE-2025-15467) per Article 10.
2.  **Urgent**: Update `python` to v3.11.5+ to address multiple HIGH/CRITICAL tarfile and path vulnerabilities (CVE-2025-4517, CVE-2023-41105) per Article 11.
3.  **Planned**: Update `curl` to remediate HIGH severity cookie handling (CVE-2025-9086).
4.  **Hygiene**: Implement automated SBOM generation and vulnerability monitoring for all 12 components to maintain compliance with Article 10(6).
5.  **Audit**: Review use of `tarfile` and `base64` modules in application code to ensure input validation against PoC-verified bypasses.