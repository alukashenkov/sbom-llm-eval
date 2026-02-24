## 1. SBOM Overview
**Product:** la-vulners-mcp (Container)  
**Scan Date:** 2026-02-24  
**Summary:** Out of 97 total packages, 3 are affected by vulnerabilities. There are **7 unique CVEs** identified across 13 advisory entries.  
**Unique Severity Counts:** 2 Critical, 1 High, 2 Medium, 2 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. (No vulnerabilities flagged as `wildExploited` or present in `cisa_kev`).

## 3. Exploit Availability Assessment
The following CVEs have documented exploit evidence or public PoC links:
*   **CVE-2026-27171** — zlib@1.3.1-r2 — CVSS 5.5 (Medium) — PoC on GitHub.
*   **CVE-2025-60876** — busybox@1.37.0-r30 — CVSS 6.5 (Medium) — PoC on Gist.

0 additional CVEs have exploit evidence.

## 4. Critical & High Findings
The following findings represent the highest unexploited technical risk:
*   **CVE-2023-45853** — zlib@1.3.1-r2 — CVSS 9.8 (Critical) — EPSS 0.01396
*   **CVE-2026-22184** — zlib@1.3.1-r2 — CVSS 9.8 (Critical) — EPSS 0.00042
*   **CVE-2025-26519** — musl@1.2.5-r21 — CVSS 8.1 (High) — EPSS 0.00022

and 0 more HIGH findings across 0 packages.

## 5. Risk Distribution
*   **Critical:** 2
*   **High:** 1
*   **Medium:** 2
*   **Low:** 2

**Top Affected Packages:**
1.  **zlib:** 3 unique CVEs (2 Critical, 1 Medium)
2.  **busybox:** 3 unique CVEs (1 Medium, 2 Low)
3.  **musl:** 1 unique CVE (1 High)

## 6. CRA Compliance Actions
1.  **Immediate:** Patch `zlib` to version **1.3.2** or later to remediate Critical overflows (CVE-2023-45853, CVE-2026-22184) and the Medium DoS (CVE-2026-27171).
2.  **Urgent:** Update `musl` to version **1.2.6** to resolve the High-severity out-of-bounds write (CVE-2025-26519).
3.  **Planned:** Update `busybox` to a version beyond **1.37.0** to address request splitting (CVE-2025-60876) and terminal escape vulnerabilities.
4.  **SBOM Hygiene:** Consolidate duplicate advisory entries for `zlib` and `musl` in future reporting cycles to improve data clarity.