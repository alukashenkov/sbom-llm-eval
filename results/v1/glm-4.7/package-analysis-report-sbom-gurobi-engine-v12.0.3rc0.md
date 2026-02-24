## 1. SBOM Overview
**Product:** sbom-gurobi-engine-v12.0.3rc0
**Format:** SPDX | **Scan Date:** 2025-07-11
**Scope:** 12 total packages; 3 affected (Python, OpenSSL, Curl).
**Vulnerabilities:** 154 total advisories (deduped: ~3 Critical, ~13 High, ~20 Medium).

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. (Zero vulnerabilities flagged as `wildExploited` or present in CISA KEV).

## 3. Exploit Availability Assessment
**Public PoC Available (High Risk)**
*   **CVE-2025-4517** (Python@3.11.4): CVSS 9.4. Arbitrary filesystem writes via tarfile. 11 GitHub exploits.
*   **CVE-2025-15467** (OpenSSL@3.0.16): CVSS 9.8. Stack buffer overflow in CMS. 2 GitHub/Packetstorm exploits.
*   **CVE-2007-4559** (Python@3.11.4): CVSS 9.8. Directory traversal via tarfile. 1 GitHub exploit.
*   **CVE-2025-4138** (Python@3.11.4): CVSS 7.5. Symlink bypass in tarfile. 7 GitHub/Packetstorm exploits.

**Bug Bounty / Framework Integration**
*   **CVE-2025-14524** (Curl@8.14.1): OAuth2 token leak on cross-protocol redirect. HackerOne disclosed.
*   **CVE-2025-9086** (Curl@8.14.1): Secure cookie downgrade. HackerOne disclosed.

## 4. Critical & High Findings (Remaining)
*   **CVE-2024-8088** (Python@3.11.4) — CVSS 8.7 — EPSS 0.15% — Infinite loop in zipfile.
*   **CVE-2025-9230** (OpenSSL@3.0.16) — CVSS 7.5 — EPSS 0.03% — Out-of-bounds read in CMS.
*   **CVE-2024-7592** (Python@3.11.4) — CVSS 7.5 — EPSS 0.73% — DoS in cookie parsing.
*   **CVE-2025-69419** (OpenSSL@3.0.16) — CVSS 7.4 — EPSS 0.06% — Out-of-bounds write in PKCS12.
*   **CVE-2024-4032** (Python@3.11.4) — CVSS 7.5 — EPSS 1.13% — Incorrect IPv4/IPv6 range handling.

## 5. Risk Distribution
**Severity:** 3 Critical | 13 High | 20 Medium | Low.
**Top Affected Packages:** Python (High volume of critical/high exploits), OpenSSL (Highest severity CVSS 9.8), Curl (Protocol logic flaws).
**Exploitation Landscape:** High. 3 Critical vulnerabilities have public, weaponized exploits (GitHub/Packetstorm).

## 6. CRA Compliance Actions
1.  **Immediate:** Patch Python (CVE-2025-4517) and OpenSSL (CVE-2025-15467) immediately due to Critical CVSS scores (9.4/9.8) and active public exploits.
2.  **Urgent:** Remediate Python tarfile vulnerabilities (CVE-2025-4138, CVE-2007-4559) to prevent arbitrary file writes/traversal.
3.  **Urgent:** Update OpenSSL to address HIGH severity buffer overflows (CVE-2025-9230, CVE-2025-69419).
4.  **Planned:** Upgrade Python from 3.11.4 to a supported, stable release to resolve legacy CVEs and reduce technical debt.
5.  **Hygiene:** Audit SBOM generation to remove duplicate advisories and verify component provenance.