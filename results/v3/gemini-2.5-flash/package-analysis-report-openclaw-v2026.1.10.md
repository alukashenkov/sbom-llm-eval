I will now perform the silent checks.

---
## Vulnerability Summary for openclaw (SPDX)

### 1. SBOM Overview
This SBOM, generated on 2026-02-20, details the dependencies for the `openclaw` product. Out of 1112 total packages, 21 are affected by known vulnerabilities. The scan identified 43 unique CVEs, comprising 3 CRITICAL, 26 HIGH, 13 MEDIUM, and 1 LOW severity vulnerabilities.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of exploit availability (e.g., PoC code):
*   **CVE-2026-25253** openclaw@2026.1.10 — CVSS: 8.8 (HIGH) — EPSS: 0.00049 — 1-Click RCE via Auth Token Exfiltration.
*   **CVE-2026-24763** clawdbot@2026.1.10 — CVSS: 8.8 (HIGH) — EPSS: 0.00083 — Authenticated Command Injection via PATH.
*   **CVE-2026-22610** @angular/compiler@21.0.3 — CVSS: 8.5 (HIGH) — EPSS: 0.00021 — XSS via Unsanitized SVG Script Attributes.
*   **CVE-2025-69873** ajv@8.17.1 — CVSS: 8.2 (HIGH) — EPSS: 0.00069 — ReDoS when using `$data` option.
*   **CVE-2025-65945** jws@4.0.0 — CVSS: 7.5 (HIGH) — EPSS: 0.00009 — Improper HMAC Signature Verification.

1 additional CVE has exploit evidence.

### 4. Critical & High Findings
The following CRITICAL and HIGH severity vulnerabilities require urgent attention:
*   **CRITICAL:**
    *   **CVE-2023-34104** fast-xml-parser@4.5.3 — CVSS: 9.3 — EPSS: 0.00273 — Entity encoding bypass via regex injection.
    *   **GHSA-RV39-79C4-7459** openclaw@2026.1.10 — CVSS: 9.3 — EPSS: N/A — Gateway connect could skip device identity checks.
    *   **GHSA-4RJ2-GPMH-QQ5X** openclaw@2026.1.10 — CVSS: 9.4 — EPSS: N/A — Inbound allowlist policy bypass in voice-call extension.
*   **HIGH:**
    *   **GHSA-FHVM-J76F-QMJV** openclaw@2026.1.10 — CVSS: 9.1 — EPSS: N/A — Access-group authorization bypass if channel type lookup fails.
    *   **GHSA-R5FQ-947M-XM57** openclaw@2026.1.10 — CVSS: 8.8 — EPSS: N/A — Path traversal in apply_patch could write/delete files.
    *   **GHSA-JQPQ-MGVM-F9R6** openclaw@2026.1.10 — CVSS: 8.8 — EPSS: N/A — Command hijacking via unsafe PATH handling.
    *   **CVE-2026-25593** openclaw@2026.1.10 — CVSS: 8.4 — EPSS: 0.00023 — Unauthenticated Local RCE via WebSocket config.apply.
    *   **CVE-2026-22818** hono@4.11.3 — CVSS: 8.2 — EPSS: 0.00017 — JWT algorithm confusion when JWK lacks "alg".

And 18 more HIGH findings across 7 packages.

### 5. Risk Distribution
*   **CRITICAL:** 3
*   **HIGH:** 26
*   **MEDIUM:** 13
*   **LOW:** 1

The top 3 most-affected packages are:
1.  `openclaw`: 30 advisories
2.  `clawdbot`: 8 advisories
3.  `qs`: 6 advisories

### 6. CRA Compliance Actions
1.  **Urgent Patching for RCE/Auth Bypass (openclaw, clawdbot):** Immediately update `openclaw` to version `2026.2.15` (or later) to address GHSA-FHVM-J76F-QMJV (CRITICAL Auth Bypass), GHSA-4RJ2-GPMH-QQ5X (CRITICAL Auth Bypass), GHSA-RV39-79C4-7459 (CRITICAL Auth Bypass), and CVE-2026-25593 (HIGH RCE). Also, update `clawdbot` to a fixed version to mitigate CVE-2026-25253 (HIGH RCE) and CVE-2026-24763 (HIGH Command Injection).
2.  **Address Critical Data Integrity/Availability (fast-xml-parser):** Update `fast-xml-parser` to a version beyond `4.5.3` to remediate CVE-2023-34104 (CRITICAL Entity Encoding Bypass) and CVE-2026-25896 (CRITICAL Regex Injection).
3.  **Mitigate High-Severity Exploitable Vulnerabilities (hono, @angular/compiler, @angular/core, ajv, jws, axios, diff, lodash, markdown-it, minimatch, @isaacs/brace-expansion):** Prioritize patching for all HIGH severity CVEs with exploit evidence across these packages. Consult vendor advisories for specific fixed versions.
4.  **Review and Harden Configuration (openclaw):** Investigate and harden configurations related to `openclaw`'s Telegram webhook (CVE-2026-25474), MS Teams (GHSA-7VWX-582J-J332), and exec allowlist bypasses (GHSA-QJ77-C3C8-92MQ, GHSA-3HCM-GGVF-RCH5).
5.  **SBOM Hygiene and Continuous Monitoring:** Implement automated SBOM generation and vulnerability scanning in the CI/CD pipeline to ensure continuous compliance with CRA Article 15 (Vulnerability Handling) and Article 16 (Technical Documentation).