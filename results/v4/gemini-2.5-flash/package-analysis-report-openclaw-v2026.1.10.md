## Vulnerability Summary for openclaw

### 1. SBOM Overview
This SBOM for `openclaw`, generated in SPDX format on 2026-02-20T17:16:42.000Z, details the software components and their associated vulnerabilities. Out of 1112 total packages, 21 are affected by known vulnerabilities. The scan identified 39 unique CVEs, categorized by severity as follows: 3 CRITICAL, 26 HIGH, 9 MEDIUM, and 1 LOW.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of Proof-of-Concept (PoC) exploits:
- CVE-2026-25253 (openclaw@2026.1.10, clawdbot@2026.1.10) — CVSS: 8.8 — EPSS: 0.00049 — 1-Click RCE via Authentication Token Exfiltration.
- CVE-2026-24763 (clawdbot@2026.1.10) — CVSS: 8.8 — EPSS: 0.00083 — Authenticated Command Injection via PATH Environment Variable.
- CVE-2026-22610 (@angular/compiler@21.0.3, @angular/core@21.0.3) — CVSS: 8.5 — EPSS: 0.00021 — XSS Vulnerability via Unsanitized SVG Script Attributes.
- CVE-2025-69873 (ajv@8.17.1) — CVSS: 8.2 — EPSS: 0.00069 — ReDoS when using `$data` option.
- CVE-2025-65945 (jws@4.0.0, jws@3.2.2) — CVSS: 7.5 — EPSS: 0.00009 — Improperly Verifies HMAC Signature.
1 additional CVE has exploit evidence.

### 4. Critical & High Findings
The following CRITICAL and HIGH vulnerabilities require immediate attention:
- CVE-2026-25896 (fast-xml-parser@4.5.3) — CVSS: 9.3 — EPSS: 0.00029 — Entity encoding bypass via regex injection in DOCTYPE entity names.
- OSV:GHSA-RV39-79C4-7459 (openclaw@2026.1.10) — CVSS: 9.3 — EPSS: N/A — Gateway connect could skip device identity checks.
- OSV:GHSA-4RJ2-GPMH-QQ5X (openclaw@2026.1.10) — CVSS: 9.4 — EPSS: N/A — Inbound allowlist policy bypass in voice-call extension.
- OSV:GHSA-FHVM-J76F-QMJV (openclaw@2026.1.10) — CVSS: 9.1 — EPSS: N/A — Potential access-group authorization bypass.
- OSV:GHSA-R5FQ-947M-XM57 (openclaw@2026.1.10) — CVSS: 8.8 — EPSS: N/A — Path traversal in apply_patch.
- OSV:GHSA-JQPQ-MGVM-F9R6 (openclaw@2026.1.10) — CVSS: 8.8 — EPSS: N/A — Command hijacking via unsafe PATH handling.
- CVE-2025-66031 (node-forge@1.3.1) — CVSS: 8.7 — EPSS: 0.00115 — ASN.1 Unbounded Recursion.
- CVE-2025-15284 (qs@6.13.0, qs@6.14.0, qs@6.14.1) — CVSS: 8.7 — EPSS: 0.00085 — arrayLimit bypass in bracket notation allows DoS.
and 18 more HIGH findings across 4 packages.

### 5. Risk Distribution
- **CRITICAL:** 3 unique CVEs
- **HIGH:** 26 unique CVEs
- **MEDIUM:** 9 unique CVEs
- **LOW:** 1 unique CVEs

Top 3 most-affected packages:
1. `openclaw`: 31 advisories
2. `clawdbot`: 8 advisories
3. `hono`: 7 advisories

### 6. CRA Compliance Actions
1. **Immediate Action:** Upgrade `fast-xml-parser` to a version that remediates CVE-2026-25896 (CRITICAL, CVSS 9.3) to prevent entity encoding bypass.
2. **Urgent Action:** Address all CRITICAL and HIGH vulnerabilities in `openclaw` (e.g., OSV:GHSA-RV39-79C4-7459, OSV:GHSA-4RJ2-GPMH-QQ5X, OSV:GHSA-FHVM-J76F-QMJV, OSV:GHSA-R5FQ-947M-XM57, OSV:GHSA-JQPQ-MGVM-F9R6) by upgrading to the latest secure version (e.g., `openclaw@2026.2.15` or newer if available) to mitigate severe security risks including RCE and authorization bypasses.
3. **Urgent Action:** Upgrade `clawdbot` to a version addressing CVE-2026-25253 and CVE-2026-24763 (HIGH, CVSS 8.8) to prevent RCE and command injection.
4. **Planned Action:** Review and upgrade `node-forge` to a version fixing CVE-2025-66031 and CVE-2025-12816 (HIGH, CVSS 8.7) to prevent ASN.1 processing vulnerabilities.
5. **SBOM Hygiene:** Implement automated vulnerability scanning and dependency management to ensure continuous compliance with CRA requirements, particularly for identifying and addressing new vulnerabilities promptly.