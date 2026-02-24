## 1. SBOM Overview

This SBOM for `openclaw` (SPDX format, created 2026-02-20) identifies 1112 packages, with 21 packages affected by known vulnerabilities. The vulnerabilities include 2 CRITICAL, 34 HIGH, 19 MEDIUM, and 2 LOW severity findings.

## 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment

A total of 6 CVEs have publicly available exploit evidence. The top 5 CVEs with Proof-of-Concept (PoC) by severity are:

*   **CVE-2023-34104** (fast-xml-parser): CVSS 9.3, EPSS 0.00273
*   **CVE-2026-25896** (fast-xml-parser): CVSS 9.3, EPSS 0.00029
*   **CVE-2025-66031** (node-forge): CVSS 8.7, EPSS 0.00115
*   **CVE-2025-12816** (node-forge): CVSS 8.7, EPSS 0.00059
*   **CVE-2025-15284** (qs): CVSS 8.7, EPSS 0.00085

1 additional CVEs have exploit evidence.

## 4. Critical & High Findings

The following critical and high severity CVEs require immediate attention:

*   **GHSA-FHVM-J76F-QMJV** (openclaw): CVSS 9.1 (CRITICAL)
*   **GHSA-4RJ2-GPMH-QQ5X** (openclaw): CVSS 9.4 (CRITICAL)
*   **GHSA-RV39-79C4-7459** (openclaw): CVSS 9.3 (CRITICAL)
*   **CVE-2026-25593** (openclaw): CVSS 8.4 (HIGH), EPSS 0.00023
*   **CVE-2026-25474** (openclaw): CVSS 7.5 (HIGH), EPSS 0.00015
*   **GHSA-7VWX-582J-J332** (openclaw): CVSS 7.4 (HIGH)
*   **GHSA-MQPW-46FH-299H** (openclaw): CVSS 7.2 (HIGH)
*   **GHSA-QJ77-C3C8-9C3Q** (openclaw): CVSS 7.4 (HIGH)

and 26 more HIGH findings across 5 packages.

## 5. Risk Distribution

The product contains 57 unique CVEs. The severity distribution is: CRITICAL (2), HIGH (34), MEDIUM (19), LOW (2). The packages with the most unique CVEs are `openclaw@2026.1.10` (29 CVEs), `hono@4.11.3` (6 CVEs), and `clawdbot@2026.1.10` (5 CVEs).

## 6. CRA Compliance Actions

1.  **Immediate Action (CRA Article 14):** Address CVEs with known exploit evidence. Prioritize patching `fast-xml-parser` for CVE-2023-34104 and CVE-2026-25896, and `node-forge` for CVE-2025-66031 and CVE-2025-12816.
2.  **Urgent Patching:** Update `openclaw` to a fixed version to mitigate the 3 CRITICAL vulnerabilities (GHSA-FHVM-J76F-QMJV, GHSA-4RJ2-GPMH-QQ5X, GHSA-RV39-79C4-7459) and numerous HIGH severity issues.
3.  **High Priority Remediation:** Upgrade `hono` to a version that addresses CVE-2026-22818 and CVE-2026-22817 (JWT algorithm confusion).
4.  **Planned Updates:** Update `qs` to a fixed version to resolve DoS vulnerabilities (CVE-2025-15284, CVE-2026-2391).
5.  **SBOM Hygiene:** Implement continuous monitoring for new vulnerabilities in all listed packages and maintain up-to-date SBOMs.