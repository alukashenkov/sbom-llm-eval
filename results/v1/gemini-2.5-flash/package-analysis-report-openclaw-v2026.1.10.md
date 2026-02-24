## Vulnerability Summary for openclaw

**SBOM Overview**

*   **Product:** openclaw
*   **Format:** SPDX
*   **Scan Date:** 2026-02-20T17:16:42.000Z
*   **Total Packages:** 1112
*   **Affected Packages:** 21
*   **Total Advisories:** 125
*   **Vulnerability Counts by Severity:**
    *   CRITICAL: 3
    *   HIGH: 46
    *   MEDIUM: 19
    *   LOW: 4

**CRA Mandatory Reporting Triggers (Article 14)**

No CRA mandatory reporting triggers identified (no `wildExploited=true` or `cisa_kev` present).

**Exploit Availability Assessment**

*   **Public PoC available:**
    *   CVE-2026-25253 (clawdbot@2026.1.10): 1-Click RCE via Authentication Token Exfiltration From gatewayUrl
    *   CVE-2026-24763 (clawdbot@2026.1.10): Authenticated Command Injection via PATH Environment Variable
    *   CVE-2026-25157 (clawdbot@2026.1.10): OS Command Injection via Project Root Path in sshNodeCommand
    *   CVE-2026-22610 (@angular/compiler@21.0.3, @angular/core@21.0.3): XSS Vulnerability via Unsanitized SVG Script Attributes
    *   CVE-2025-69873 (ajv@8.17.1): ReDoS when using `$data` option
    *   CVE-2025-65945 (jws@4.0.0, jws@3.2.2): Improperly Verifies HMAC Signature

**Critical & High Findings**

*   **CRITICAL:**
    *   GHSA-FHVM-J76F-QMJV (openclaw@2026.1.10): OpenClaw has a potential access-group authorization bypass if channel type lookup fails — CVSS: 9.1 (CRITICAL) — EPSS: N/A
    *   GHSA-4RJ2-GPMH-QQ5X (openclaw@2026.1.10): OpenClaw has an inbound allowlist policy bypass in voice-call extension (empty caller ID + suffix matching) — CVSS: 9.4 (CRITICAL) — EPSS: N/A
    *   GHSA-RV39-79C4-7459 (openclaw@2026.1.10): OpenClaw's gateway connect could skip device identity checks when auth.token was present but not yet validated — CVSS: 9.3 (CRITICAL) — EPSS: N/A
    *   CVE-2023-34104 (fast-xml-parser@4.5.3): Entity encoding bypass via regex injection in DOCTYPE entity names — CVSS: 9.3 (CRITICAL) — EPSS: 0.00273
    *   CVE-2026-25896 (fast-xml-parser@4.5.3): Entity encoding bypass via regex injection in DOCTYPE entity names — CVSS: 9.3 (CRITICAL) — EPSS: 0.00029
*   **HIGH:**
    *   CVE-2026-25593 (openclaw@2026.1.10): Unauthenticated Local RCE via WebSocket config.apply — CVSS: 8.4 (HIGH) — EPSS: 0.00023
    *   CVE-2026-25474 (openclaw@2026.1.10): Telegram webhook request forgery (missing `channels.telegram.webhookSecret`) → auth bypass — CVSS: 7.5 (HIGH) — EPSS: 0.00015
    *   GHSA-7VWX-582J-J332 (openclaw@2026.1.10): MS Teams inbound attachment downloader leaks bearer tokens to allowlisted suffix domains — CVSS: 7.4 (HIGH) — EPSS: N/A
    *   GHSA-MQPW-46FH-299H (openclaw@2026.1.10): authorization bypass: operator.write can resolve exec approvals via chat.send -> /approve — CVSS: 7.2 (HIGH) — EPSS: N/A
    *   GHSA-QJ77-C3C8-9C3Q (openclaw@2026.1.10): Windows cmd.exe parsing may bypass exec allowlist/approval gating — CVSS: 7.4 (HIGH) — EPSS: N/A
    *   GHSA-56F2-HVWG-5743 (openclaw@2026.1.10): SSRF in Image Tool Remote Fetch — CVSS: 7.6 (HIGH) — EPSS: N/A
    *   GHSA-3HCM-GGVF-RCH5 (openclaw@2026.1.10): exec allowlist bypass via command substitution/backticks inside double quotes — CVSS: 7.4 (HIGH) — EPSS: N/A
    *   GHSA-64QX-VPXX-MVQF (openclaw@2026.1.10): arbitrary transcript path file write via gateway sessionFile — CVSS: 7.1 (HIGH) — EPSS: N/A
    *   GHSA-HV93-R4J3-Q65F (openclaw@2026.1.10): Hook Session Key Override Enables Targeted Cross-Session Routing — CVSS: 7.1 (HIGH) — EPSS: N/A
    *   CVE-2026-26316 (openclaw@2026.1.10): BlueBubbles webhook auth bypass via loopback proxy trust — CVSS: 7.5 (HIGH) — EPSS: 0.00061
    *   GHSA-GQ9C-WG68-GWJ2 (openclaw@2026.1.10): path traversal in browser trace/download output paths may allow arbitrary file writes — CVSS: 7.5 (HIGH) — EPSS: N/A
    *   GHSA-Q447-RJ3R-2CGH (openclaw@2026.1.10): denial of service via unbounded webhook request body buffering — CVSS: 7.5 (HIGH) — EPSS: N/A
    *   GHSA-W5C7-9QQW-6645 (openclaw@2026.1.10): inter-session prompts could be treated as direct user instructions — CVSS: 7.1 (HIGH) — EPSS: N/A
    *   CVE-2026-26327 (openclaw@2026.1.10): unauthenticated discovery TXT records to steer routing and TLS pinning — CVSS: 7.1 (HIGH) — EPSS: 0.00004
    *   CVE-2026-27487 (openclaw@2026.1.10): Prevent shell injection in macOS keychain credential write — CVSS: 7.6 (HIGH) — EPSS: 0.00054
    *   GHSA-X22M-J5QQ-J49M (openclaw@2026.1.10): two SSRF via sendMediaFeishu and markdown image fetching in Feishu extension — CVSS: 8.6 (HIGH) — EPSS: N/A
    *   CVE-2026-26322 (openclaw@2026.1.10): Gateway tool allowed unrestricted gatewayUrl override — CVSS: 7.6 (HIGH) — EPSS: 0.00013
    *   CVE-2026-26325 (openclaw@2026.1.10): Node host system.run rawCommand/command mismatch can bypass allowlist/approvals — CVSS: 7.2 (HIGH) — EPSS: 0.00018
    *   CVE-2026-26324 (openclaw@2026.1.10): SSRF guard bypass via full-form IPv4-mapped IPv6 (loopback / metadata reachable) — CVSS: 7.5 (HIGH) — EPSS: 0.00011
    *   CVE-2026-26321 (openclaw@2026.1.10): local file disclosure via sendMediaFeishu in Feishu extension — CVSS: 7.5 (HIGH) — EPSS: 0.0006
    *   GHSA-RWJ8-P9VQ-25GV (openclaw@2026.1.10): LFI in BlueBubbles media path handling — CVSS: 7.5 (HIGH) — EPSS: N/A
    *   GHSA-R5FQ-947M-XM57 (openclaw@2026.1.10): path traversal in apply_patch could write/delete files outside the workspace — CVSS: 8.8 (HIGH) — EPSS: N/A
    *   GHSA-V6C6-VQQG-W888 (openclaw@2026.1.10): potential code execution via unsafe hook module path handling in Gateway — CVSS: 7.2 (HIGH) — EPSS: N/A
    *   CVE-2026-26323 (openclaw@2026.1.10): command injection in maintainer clawtributors updater — CVSS: 8.6 (HIGH) — EPSS: 0.00175
    *   CVE-2026-26319 (openclaw@2026.1.10): Missing Webhook Authentication in Telnyx Provider Allows Unauthenticated Requests — CVSS: 7.5 (HIGH) — EPSS: 0.00031
    *   CVE-2026-26317 (openclaw@2026.1.10, clawdbot@2026.1.10): cross-site request forgery (CSRF) through loopback browser mutation endpoints — CVSS: 7.1 (HIGH) — EPSS: 0.00014
    *   CVE-2026-26329 (openclaw@2026.1.10): path traversal in browser upload allows local file read — CVSS: 7.1 (HIGH) — EPSS: 0.0004
    *   GHSA-J27P-HQ53-9WGC (openclaw@2026.1.10): denial of service via unbounded URL-backed media fetch — CVSS: 7.5 (HIGH) — EPSS: N/A
    *   GHSA-JQPQ-MGVM-F9R6 (openclaw@2026.1.10): Command hijacking via unsafe PATH handling (bootstrapping + node-host PATH overrides) — CVSS: 8.8 (HIGH) — EPSS: N/A
    *   GHSA-RQ6G-PX6M-C248 (openclaw@2026.1.10, clawdbot@2026.1.10): Google Chat shared-path webhook target ambiguity allowed cross-account policy-context misrouting — CVSS: 8.3 (HIGH) — EPSS: N/A
    *   CVE-2026-27002 (openclaw@2026.1.10): Docker container escape via unvalidated bind mount config injection — CVSS: 7.7 (HIGH) — EPSS: 0.00045
    *   CVE-2026-27001 (openclaw@2026.1.10): Unsanitized CWD path injection into LLM prompts — CVSS: 8.6 (HIGH) — EPSS: 0.00018
    *   CVE-2026-25253 (clawdbot@2026.1.10): 1-Click RCE via Authentication Token Exfiltration From gatewayUrl — CVSS: 8.8 (HIGH) — EPSS: 0.00049
    *   CVE-2026-24763 (clawdbot@2026.1.10): Authenticated Command Injection via PATH Environment Variable — CVSS: 8.8 (HIGH) — EPSS: 0.00083
    *   CVE-2026-25157 (clawdbot@2026.1.10): OS Command Injection via Project Root Path in sshNodeCommand — CVSS: 7.7 (HIGH) — EPSS: 0.00006
    *   CVE-2026-22818 (hono@4.11.3): JWK Auth Middleware has JWT algorithm confusion when JWK lacks "alg" (untrusted header.alg fallback) — CVSS: 8.2 (HIGH) — EPSS: 0.00017
    *   CVE-2026-22817 (hono@4.11.3): JWT Middleware's JWT Algorithm Confusion via Unsafe Default (HS256) Allows Token Forgery and Auth Bypass — CVSS: 8.2 (HIGH) — EPSS: 0.00017
    *   CVE-2026-25128 (fast-xml-parser@4.5.3): Uncaught Exception — CVSS: 8.7 (HIGH) — EPSS: 0.00027
    *   CVE-2026-26278 (fast-xml-parser@4.5.3): DoS through entity expansion in DOCTYPE (no expansion limit) — CVSS: 7.5 (HIGH) — EPSS: 0.00049
    *   CVE-2025-66031 (node-forge@1.3.1): ASN.1 Unbounded Recursion — CVSS: 8.7 (HIGH) — EPSS: 0.00115
    *   CVE-2025-12816 (node-forge@1.3.1): Interpretation Conflict vulnerability via its ASN.1 Validator Desynchronization — CVSS: 8.7 (HIGH) — EPSS: 0.00059
    *   CVE-2025-15284 (qs@6.13.0, qs@6.14.0): arrayLimit bypass in its bracket notation allows DoS via memory exhaustion — CVSS: 8.7 (HIGH) — EPSS: 0.00085
    *   CVE-2026-22610 (@angular/compiler@21.0.3, @angular/core@21.0.3): XSS Vulnerability via Unsanitized SVG Script Attributes — CVSS: 8.5 (HIGH) — EPSS: 0.00021
    *   CVE-2026-25639 (axios@1.13.2): Prototype Pollution — CVSS: 8.7 (HIGH) — EPSS: 0.00033
    *   CVE-2026-24001 (diff@8.0.2): jsdiff has a Denial of Service vulnerability in parsePatch and applyPatch — CVSS: 7.5 (HIGH) — EPSS: 0.0002
    *   CVE-2025-65945 (jws@4.0.0, jws@3.2.2): Improperly Verifies HMAC Signature — CVSS: 7.5 (HIGH) — EPSS: 0.00009
    *   CVE-2025-13465 (lodash@4.17.21): Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions — CVSS: 7.9 (HIGH) — EPSS: 0.00025
    *   CVE-2026-26996 (minimatch@10.1.1, minimatch@9.0.5): ReDoS via repeated wildcards with non-matching literal in pattern — CVSS: 8.7 (HIGH) — EPSS: 0.0004
    *   CVE-2026-25547 (@isaacs/brace-expansion@5.0.0): Uncontrolled Resource Consumption — CVSS: 8.7 (HIGH) — EPSS: 0.00018

**Risk Distribution**

*   **Critical:** 3
*   **High:** 46
*   **Medium:** 19
*   **Low:** 4

**Top 3 Most-Affected Packages:**

1.  **openclaw:** 36 advisories (3 Critical, 30 High, 3