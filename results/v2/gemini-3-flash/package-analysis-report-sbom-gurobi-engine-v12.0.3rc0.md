## 1. SBOM Overview
**Product:** sbom-gurobi-engine-v12.0.3rc0  
**Format:** SPDX | **Scan Date:** 2025-07-11  
The scan identified 12 total packages, of which 3 (25%) are affected by vulnerabilities. A deduplicated analysis reveals **43 unique CVEs**: 3 Critical, 18 High, 21 Medium, and 1 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities in this dataset are marked as `wildExploited: true` or present in the CISA KEV.

## 3. Exploit Availability Assessment
The following vulnerabilities have documented Proof-of-Concept (PoC) or exploit evidence:
*   **[CVE-2025-15467]** openssl@3.0.16 — 9.8 (Critical) — EPSS 0.00672 — Stack buffer overflow in CMS AuthEnvelopedData.
*   **[CVE-2025-4517]** python@3.11.4 — 9.4 (Critical) — EPSS 0.00071 — Arbitrary writes via tarfile realpath overflow.
*   **[CVE-2007-4559]** python@3.11.4 — 9.8 (Critical) — EPSS 0.90582 — Legacy directory traversal in tarfile module.
*   **[CVE-2025-4138]** python@3.11.4 — 7.5 (High) — EPSS 0.00066 — Symlink bypass in extraction filters.
*   **[CVE-2024-6232]** python@3.11.4 — 7.5 (High) — EPSS 0.02874 — ReDoS in TarFile header parsing.
*   **7 additional CVEs** have exploit evidence (including CVE-2025-4330, CVE-2025-4435, and CVE-2024-12718).

## 4. Critical & High Findings
*   **[CVE-2025-9230]** openssl@3.0.16 — 7.5 (High) — EPSS 0.00031
*   **[CVE-2025-69419]** openssl@3.0.16 — 7.4 (High) — EPSS 0.00056
*   **[CVE-2025-69420]** openssl@3.0.16 — 7.5 (High) — EPSS 0.00070
*   **[CVE-2025-69421]** openssl@3.0.16 — 7.5 (High) — EPSS 0.00059
*   **[CVE-2024-8088]** python@3.11.4 — 8.7 (High) — EPSS 0.00154
*   **[CVE-2024-9287]** python@3.11.4 — 7.8 (High) — EPSS 0.00062
*   **[CVE-2023-6597]** python@3.11.4 — 7.8 (High) — EPSS 0.00071
*   **[CVE-2025-9086]** curl@8.14.1 — 7.5 (High) — EPSS 0.00035
and **8 more** HIGH findings across 2 packages.

## 5. Risk Distribution
*   **Critical:** 3
*   **High:** 18
*   **Medium:** 21
*   **Low:** 1
**Top Affected Packages:** Python (28 unique CVEs), OpenSSL (10 unique CVEs), Curl (5 unique CVEs).

## 6. CRA Compliance Actions
1.  **Immediate:** Patch **OpenSSL to v3.0.17+** or v3.4.1+ to remediate Critical CVE-2025-15467 and multiple High-severity buffer/type confusion risks.
2.  **Urgent:** Update **Python to v3.11.11+** (or latest 3.12/3.13) to address Critical CVE-2025-4517 and the legacy tarfile traversal (CVE-2007-4559).
3.  **Urgent:** Update **Curl to v8.12.0+** to resolve High-severity cookie handling (CVE-2025-9086) and WebSocket masking issues.
4.  **Planned:** Review application usage of `tarfile` and `zipfile` modules; implement manual path validation if immediate patching is delayed.
5.  **Hygiene:** Regenerate SBOM after patching to verify resolution of 43 identified CVEs.