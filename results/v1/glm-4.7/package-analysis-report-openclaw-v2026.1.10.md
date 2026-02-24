### 1. SBOM Overview
**Product:** openclaw | **Format:** SPDX | **Scan Date:** 2026-02-20
**Scope:** 1,112 total packages; 21 affected; 125 total advisories.
**Severity:** 4 Critical, ~40 High, 81 Medium/Low.

### 2. CRA Mandatory Reporting Triggers (Article 14)
**Status:** No CRA mandatory reporting triggers identified.
*Analysis:* No vulnerabilities detected with `wildExploited=true` or listed in CISA KEV. No 24h/72h/14d notification obligation is currently active.

### 3. Exploit Availability Assessment
**Public PoC Available (High Risk):**
*   **CVE-2026-25253** (clawdbot): 1-Click RCE via Auth Token Exfiltration.
*   **CVE-2026-24763** (clawdbot): Authenticated Command Injection via PATH.
*   **CVE-2026-25157** (clawdbot): OS Command Injection via SSH Node Command.
*   **CVE-2026-22610** (@angular/core, @angular/compiler): XSS via Unsanitized SVG Script Attributes.
*   **CVE-2025-69873** (ajv): ReDoS via `$data` option.
*   **CVE-2025-65945** (jws): Improper HMAC Signature Verification.

### 4. Critical & High Findings (Remaining)
*   **CVE-2023-34104** (fast-xml-parser@4.5.3) — CVSS 9.3 (CRITICAL) — EPSS 0.50% — Entity encoding bypass.
*   **GHSA-4RJ2-GPMH-QQ5X** (openclaw@2026.1.10) — CVSS 9.4 (CRITICAL) — EPSS N/A — Voice-call auth bypass.
*   **GHSA-RV39-79C4-7459** (openclaw@2026.1.10) — CVSS 9.3 (CRITICAL) — EPSS N/A — Gateway identity check skip.
*   **GHSA-FHVM-J76F-QMJV** (openclaw@2026.1.10) — CVSS 9.1 (CRITICAL) — EPSS N/A — Telegram webhook auth bypass.
*   **CVE-2025-66031** (node-forge@1.3.1) — CVSS 8.7 (HIGH) — EPSS 0.31% — ASN.1 Unbounded Recursion.
*   **CVE-2026-25639** (axios@1.13.2) — CVSS 8.7 (HIGH) — EPSS 0.10% — Prototype Pollution.
*   **CVE-2025-15284** (qs@6.13.0) — CVSS 8.7 (HIGH) — EPSS 0.25% — DoS via arrayLimit bypass.

### 5. Risk Distribution
**Severity:** 4 Critical (3.2%), 40 High (32%), 81 Other (64.8%).
**Top Affected Packages:** `openclaw` (80+ advisories), `fast-xml-parser`, `hono`, `node-forge`.
**Exploitation Landscape:** 6 CVEs have public PoCs (GitHub); 0 confirmed active exploits in the wild.

### 6. CRA Compliance Actions
1.  **Immediate:** Patch `clawdbot` to resolve CVE-2026-25253 (1-Click RCE) and CVE-2026-24763 (Command Injection).
2.  **Immediate:** Update `fast-xml-parser` to mitigate Critical entity encoding bypass (CVE-2023-34104).
3.  **Urgent:** Upgrade `openclaw` core to fix Critical auth bypasses (GHSA-4RJ2, GHSA-RV39, GHSA-FHVM).
4.  **Planned:** Update `node-forge`, `axios`, and `qs` to address High-severity DoS and prototype pollution risks.
5.  **Hygiene:** Audit transitive dependencies (`hono`, `angular`) for exploitability and update SBOM metadata.