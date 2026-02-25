## 1. SBOM Overview
*   **Product**: openclaw (SPDX)
*   **Scan Date**: 2026-02-20
*   **Packages**: 1,112 total / 21 affected
*   **Unique CVEs**: 96 (5 CRITICAL, 52 HIGH, 33 MEDIUM, 6 LOW)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **CVE-2026-25253** (clawdbot): HIGH (8.8), EPSS 0.00049. 1-Click RCE via token exfiltration.
*   **CVE-2026-24763** (clawdbot): HIGH (8.8), EPSS 0.00083. Authenticated Command Injection via PATH.
*   **CVE-2026-25157** (clawdbot): HIGH (7.7), EPSS 0.00006. OS Command Injection via Project Root.
*   **CVE-2026-22610** (@angular/core): HIGH (8.5), EPSS 0.00014. XSS via SVG Script Attributes.
*   **CVE-2025-69873** (ajv): MEDIUM (6.9), EPSS 0.00069. ReDoS via $data option.
*   6 additional CVEs have PoC evidence.

## 4. Critical & High Findings
*   **CVE-2026-25896** (fast-xml-parser): CRITICAL (9.3), EPSS 0.00029. Regex injection bypass.
*   **CVE-2026-25593** (openclaw): HIGH (8.4), EPSS 0.00023. Unauthenticated Local RCE.
*   **CVE-2026-22818** (hono): HIGH (8.2), EPSS 0.00017. JWT Algorithm Confusion.
*   **CVE-2025-66031** (node-forge): HIGH (8.7), EPSS 0.00115. ASN.1 Unbounded Recursion.
*   **CVE-2025-15284** (qs): HIGH (8.7), EPSS 0.00085. DoS via memory exhaustion.
*   **CVE-2025-13465** (lodash): HIGH (8.2), EPSS 0.00025. Prototype Pollution.
*   **CVE-2026-25128** (fast-xml-parser): HIGH (8.7), EPSS 0.00027. Uncaught Exception DoS.
*   **CVE-2026-25639** (axios): HIGH (8.7), EPSS 0.00033. Prototype Pollution/DoS.
*   and 44 more across 12 packages.

## 5. Risk Distribution
*   **Severity**: 5 CRITICAL, 52 HIGH, 33 MEDIUM, 6 LOW.
*   **Top Affected**: `openclaw@2026.1.10` (67 CVEs), `clawdbot@2026.1.10` (11 CVEs), `hono@4.11.3` (7 CVEs).

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `clawdbot` to resolve exploited RCE/Command Injection (CVE-2026-25253, CVE-2026-24763).
2.  **Urgent**: Update `fast-xml-parser` to remediate CRITICAL regex injection (CVE-2026-25896) per Article 10.
3.  **Planned**: Update `openclaw` to version 2026.2.15+ to resolve unauthenticated RCE and SSRF findings.
4.  **Planned**: Upgrade `hono`, `lodash`, and `axios` to latest stable versions to mitigate HIGH-severity auth bypass and pollution risks.
5.  **Hygiene**: Implement automated SBOM generation and vulnerability monitoring to meet Article 10(6) and Article 11 requirements.