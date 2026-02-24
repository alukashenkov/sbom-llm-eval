## 1. SBOM Overview
**Product:** bkimminich/juice-shop (Container)  
**Scan Date:** 2026-02-24  
**Total Packages:** 998 | **Affected Packages:** 38  
**Unique CVE Count:** 48  
**Severity Breakdown:** 5 Critical, 21 High, 21 Medium, 1 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified (no `wildExploited: true` or `cisa_kev` entries found).

## 3. Exploit Availability Assessment
The following CVEs have documented Proof-of-Concept (PoC) or exploit evidence:
1. **[CVE-2023-37466]** vm2@3.9.17 — 9.8 (Critical) — Sandbox escape to RCE.
2. **[CVE-2023-37903]** vm2@3.9.17 — 9.8 (Critical) — Sandbox escape to RCE.
3. **[CVE-2026-23745]** tar@4.4.19 — 8.2 (High) — Arbitrary file overwrite.
4. **[CVE-2025-65945]** jws@0.2.6 — 7.5 (High) — HMAC signature bypass.
5. **[CVE-2022-24785]** moment@2.0.0 — 7.5 (High) — Path traversal.
*4 additional CVEs (CVE-2018-3721, CVE-2018-16487, CVE-2020-8203, CVE-2023-37466) have exploit evidence.*

## 4. Critical & High Findings
1. **[CVE-2015-9235]** jsonwebtoken@0.1.0 — 9.8 (Critical) — EPSS: 0.3247
2. **[CVE-2023-32314]** vm2@3.9.17 — 9.8 (Critical) — EPSS: 0.6987
3. **[CVE-2019-10744]** lodash@2.4.2 — 9.1 (Critical) — EPSS: 0.0244
4. **[CVE-2023-46233]** crypto-js@3.3.0 — 9.1 (Critical) — EPSS: 0.0082
5. **[CVE-2026-22709]** vm2@3.9.17 — 9.8 (Critical) — Sandbox escape.
6. **[CVE-2026-23950]** tar@4.4.19 — 8.8 (High) — Race condition.
7. **[CVE-2025-48997]** multer@1.4.5-lts.2 — 8.7 (High) — Denial of Service.
8. **[CVE-2026-26996]** minimatch@3.0.5 — 8.7 (High) — ReDoS.
*and 13 more HIGH findings across 11 packages.*

## 5. Risk Distribution
*   **Critical:** 5
*   **High:** 21
*   **Medium:** 21
*   **Low:** 1
**Top Affected Packages:** `tar` (5 advisories), `sanitize-html` (7 advisories), `jsonwebtoken` (5 advisories).

## 6. CRA Compliance Actions
1. **Immediate:** Replace or remove `vm2` (v3.9.17). The package is deprecated and contains multiple unpatchable Critical sandbox escapes (CVE-2023-37466, CVE-2023-37903).
2. **Urgent:** Update `jsonwebtoken` to v9.0.0+ to resolve Critical verification bypass (CVE-2015-9235).
3. **Urgent:** Update `lodash` to v4.17.21+ to mitigate Critical prototype pollution (CVE-2019-10744).
4. **Urgent:** Update `tar` to v7.5.3+ to resolve high-severity path traversal and file overwrite vulnerabilities (CVE-2026-23745).
5. **Planned:** Update `multer` to v2.0.2+ and `moment` to v2.29.4+ to address High-severity DoS and path traversal risks.