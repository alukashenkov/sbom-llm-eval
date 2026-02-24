## 1. SBOM Overview
*   **Product**: openclaw
*   **Format**: SPDX
*   **Scan Date**: 2026-02-20
*   **Packages**: 1112 total / 21 affected
*   **Unique CVEs**: 57 (2 CRITICAL, 34 HIGH, 19 MEDIUM, 2 LOW)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   6 unique CVEs have PoC evidence (GitHub Exploit sources).
*   **CVE-2026-25253** (clawdbot): HIGH (8.8), EPSS: 0.00049. 1-Click RCE via token exfiltration.
*   **CVE-2026-24763** (clawdbot): HIGH (8.8), EPSS: 0.00083. Authenticated Command Injection via PATH.
*   **CVE-2026-25157** (clawdbot): HIGH (7.7), EPSS: 0.00006. OS Command Injection via Project Root.
*   **CVE-2026-22610** (@angular/core): HIGH (8.5), EPSS: 0.00021. XSS via SVG script attributes.
*   **CVE-2025-69873** (ajv): MEDIUM (6.9), EPSS: 0.00069. ReDoS via $data option.
*   1 additional CVE has PoC evidence (CVE-2025-65945).

## 4. Critical & High Findings
*   **GHSA-RV39-79C4-7459** (openclaw): CRITICAL (9.3), EPSS: N/A. Gateway identity check bypass.
*   **GHSA-FHVM-J76F-QMJV** (openclaw): CRITICAL (9.1), EPSS: N/A. Telegram webhook auth bypass.
*   **CVE-2026-25896** (fast-xml-parser): CRITICAL (9.3), EPSS: 0.00029. Regex injection bypass.
*   **CVE-2026-25593** (openclaw): HIGH (8.4), EPSS: 0.00023. Unauthenticated Local RCE.
*   **CVE-2026-22818** (hono): HIGH (8.2), EPSS: 0.00017. JWT algorithm confusion.
*   **CVE-2026-25639** (axios): HIGH (8.7), EPSS: 0.00033. Prototype Pollution/DoS.
*   **CVE-2025-66031** (node-forge): HIGH (8.7), EPSS: 0.00115. ASN.1 Unbounded Recursion.
*   **CVE-2026-25128** (fast-xml-parser): HIGH (8.7), EPSS: 0.00027. Uncaught Exception DoS.
*   And 26 more across 8 packages.

## 5. Risk Distribution
*   **Critical**: 2
*   **High**: 34
*   **Medium**: 19
*   **Low**: 2
*   **Top Affected**: openclaw@2026.1.10 (29), hono@4.11.3 (6), clawdbot@2026.1.10 (5).

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `openclaw` to >=2026.2.13 to address CRITICAL identity bypass and unauthenticated RCE (Article 10).
2.  **Urgent**: Update `fast-xml-parser` to address CRITICAL regex injection (CVE-2026-25896).
3.  **Planned**: Update `hono` to >=4.11.4 and `axios` to latest to remediate HIGH severity auth bypasses and prototype pollution (Article 11).
4.  **Planned**: Remediate `clawdbot` RCE vulnerabilities (CVE-2026-25253) via configuration hardening of `gatewayUrl`.
5.  **Hygiene**: Establish automated SBOM vulnerability regression testing to meet Article 10(6) continuous monitoring requirements.