## Vulnerability Summary for bkimminich/juice-shop

### 1. SBOM Overview
This CycloneDX SBOM for `bkimminich/juice-shop` (sha256:75b03f3f5336b39d1358d4280c09b8b265ae21e4cb215a9bf68e27f96ac76e3c), generated on 2026-02-24, details 998 packages. Of these, 38 packages are affected by vulnerabilities. There are 25 unique CVEs identified, with 5 rated CRITICAL, 15 HIGH, and 5 MEDIUM severity.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following CVEs have evidence of exploitability:
- CVE-2023-37466 vm2@3.9.17 — CRITICAL (CVSS: 9.8) — EPSS: 0.04997 — Sandbox escape with multiple public exploits.
- CVE-2023-37903 vm2@3.9.17 — CRITICAL (CVSS: 9.8) — EPSS: 0.39234 — Sandbox escape with multiple public exploits.
- CVE-2015-9235 jsonwebtoken@0.1.0 — CRITICAL (CVSS: 9.8) — EPSS: 0.3247 — Verification bypass.
- CVE-2023-32314 vm2@3.9.17 — CRITICAL (CVSS: 9.8) — EPSS: 0.69875 — Sandbox escape.
- CVE-2026-22709 vm2@3.9.17 — CRITICAL (CVSS: 9.8) — EPSS: 0.0003 — Sandbox escape.
2 additional CVEs have exploit evidence.

### 4. Critical & High Findings
- CVE-2023-46233 crypto-js@3.3.0 — CRITICAL (CVSS: 9.1) — EPSS: 0.00823 — Weak PBKDF2 implementation.
- CVE-2019-10744 lodash@2.4.2 — CRITICAL (CVSS: 9.1) — EPSS: 0.02441 — Prototype Pollution.
- CVE-2026-23950 tar@4.4.19 — HIGH (CVSS: 8.8) — EPSS: 0.00006 — Race condition in path reservations.
- CVE-2025-48997 multer@1.4.5-lts.2 — HIGH (CVSS: 8.7) — EPSS: 0.00081 — DoS via unhandled exception.
- CVE-2026-26996 minimatch@5.1.6 — HIGH (CVSS: 8.7) — EPSS: 0.0004 — ReDoS via repeated wildcards.
- CVE-2016-1000223 jws@0.2.6 — HIGH (CVSS: 8.7) — EPSS: 0.0 — Forgeable Public/Private Tokens.
- CVE-2025-15284 qs@6.14.0 — HIGH (CVSS: 8.7) — EPSS: 0.00085 — DoS via arrayLimit bypass.
- CVE-2024-37890 ws@7.4.6 — HIGH (CVSS: 8.7) — EPSS: 0.00541 — DoS when handling many HTTP headers.
and 7 more HIGH findings across 10 packages.

### 5. Risk Distribution
- CRITICAL: 5
- HIGH: 15
- MEDIUM: 5
The top 3 most-affected packages are:
- vm2: 5 advisories
- jsonwebtoken: 5 advisories
- tar: 4 advisories

### 6. CRA Compliance Actions
1.  **Immediate Action (CRITICAL, Exploitable):** Patch `vm2` to a version beyond 3.9.17 to remediate multiple sandbox escape vulnerabilities (CVE-2023-37466, CVE-2023-37903, CVE-2023-32314, CVE-2026-22709).
2.  **Urgent Action (CRITICAL):** Update `jsonwebtoken` to a version past 4.2.1 to address the verification bypass (CVE-2015-9235).
3.  **Planned Action (HIGH, Exploitable):** Upgrade `tar` to a version beyond 7.5.2 to mitigate arbitrary file overwrite and race condition issues (CVE-2026-23745, CVE-2026-23950).
4.  **Planned Action (HIGH):** Update `crypto-js` to a version addressing CVE-2023-46233 to strengthen cryptographic security.
5.  **SBOM Hygiene:** Implement automated dependency updates and regular SBOM scanning to proactively identify and address vulnerabilities, especially for widely used libraries like `lodash` and `minimatch`.