## 1. SBOM Overview
The product **openclaw** (SPDX format) was scanned on 2026-02-20. Out of 1,112 total packages, 21 are affected by vulnerabilities. The scan identified **32 unique CVEs** across 125 advisory entries. The deduplicated severity distribution is: 3 Critical, 18 High, 10 Medium, and 1 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities were flagged as actively exploited in the wild or present in the CISA KEV catalog.

## 3. Exploit Availability Assessment
The following vulnerabilities have public proof-of-concept (PoC) or exploit code available:
*   **[CVE-2026-25253]** clawdbot@2026.1.10 — 8.8 (High) — EPSS 0.00049 — 1-Click RCE via token exfiltration.
*   **[CVE-2026-24763]** clawdbot@2026.1.10 — 8.8 (High) — EPSS 0.00083 — Authenticated command injection via PATH.
*   **[CVE-2026-22610]** @angular/core@21.0.3 — 8.5 (High) — EPSS 0.00021 — XSS via unsanitized SVG attributes.
*   **[CVE-2025-69873]** ajv@8.17.1 — 8.2 (High) — EPSS 0.00069 — ReDoS via $data option.
*   **[CVE-2026-25157]** clawdbot@2026.1.10 — 7.7 (High) — EPSS 0.00006 — Command injection in SSH handling.
1 additional CVE (CVE-2025-65945) has exploit evidence.

## 4. Critical & High Findings
The following significant risks require immediate attention:
*   **[GHSA-RV39-79C4-7459]** openclaw@2026.1.10 — 9.3 (Critical) — Device identity check bypass.
*   **[CVE-2026-25896]** fast-xml-parser@4.5.3 — 9.3 (Critical) — Entity encoding bypass/Regex injection.
*   **[GHSA-FHVM-J76F-QMJV]** openclaw@2026.1.10 — 9.1 (Critical) — Unauthenticated Telegram webhook access.
*   **[CVE-2026-25128]** fast-xml-parser@4.5.3 — 8.7 (High) — Uncaught exception DoS.
*   **[CVE-2025-66031]** node-forge@1.3.1 — 8.7 (High) — Unbounded recursion DoS.
*   **[CVE-2025-15284]** qs@6.13.0 — 8.7 (High) — Memory exhaustion DoS.
*   **[CVE-2026-25593]** openclaw@2026.1.10 — 8.4 (High) — Unauthenticated Local RCE.
*   **[CVE-2026-22818]** hono@4.11.3 — 8.2 (High) — JWT algorithm confusion.
and 6 more HIGH findings across 4 packages.

## 5. Risk Distribution
*   **Critical:** 3
*   **High:** 18
*   **Medium:** 10
*   **Low:** 1
**Top Affected Packages:** `openclaw` (56 advisories), `clawdbot` (12 advisories), `hono` (7 advisories).

## 6. CRA Compliance Actions
1.  **Immediate:** Patch `openclaw` to version 2026.2.15 or later to resolve Critical identity bypasses and unauthenticated webhook vulnerabilities.
2.  **Urgent:** Update `fast-xml-parser` to version 4.5.4+ and `node-forge` to 1.3.2+ to mitigate Critical injection and High-severity DoS risks.
3.  **Urgent:** Update `clawdbot` to address RCE and command injection vulnerabilities (CVE-2026-25253, CVE-2026-24763).
4.  **Planned:** Update `hono` to 4.11.4+ and `lodash` to 4.17.23+ to resolve JWT confusion and prototype pollution.
5.  **Hygiene:** Consolidate `qs` and `minimatch` versions to the latest stable releases to eliminate redundant ReDoS and memory exhaustion vectors.