## 1. SBOM Overview
SBOM for **sbom-gurobi-engine-v12.0.3rc0** (SPDX, 2025-07-11) covers 12 packages; 3 are affected. Analysis identified **59 unique CVEs**: 3 Critical, 20 High, 30 Medium, and 6 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
1. **CVE-2025-15467** (OpenSSL@3.0.16) — CVSS 9.8 — EPSS 0.67% — Stack buffer overflow.
2. **CVE-2007-4559** (Python@3.11.4) — CVSS 9.8 — EPSS 90.58% — Directory traversal.
3. **CVE-2025-4517** (Python@3.11.4) — CVSS 9.4 — EPSS 0.07% — Arbitrary filesystem writes.
4. **CVE-2025-4138** (Python@3.11.4) — CVSS 7.5 — EPSS 0.06% — Symlink bypass.
5. **CVE-2025-4330** (Python@3.11.4) — CVSS 7.5 — EPSS 0.25% — Symlink bypass.
17 additional CVEs have exploit evidence.

## 4. Critical & High Findings
1. **CVE-2024-8088** (Python@3.11.4) — CVSS 8.7 — EPSS 0.15% — Infinite loop.
2. **CVE-2023-6597** (Python@3.11.4) — CVSS 7.8 — EPSS 0.07% — TemporaryDirectory symlink.
3. **CVE-2024-9287** (Python@3.11.4) — CVSS 7.8 — EPSS 0.06% — Command injection.
4. **CVE-2023-41105** (Python@3.11.4) — CVSS 7.5 — EPSS 0.37% — Path truncation.
5. **CVE-2023-36632** (Python@3.11.4) — CVSS 7.5 — EPSS 0.11% — RecursionError.
6. **CVE-2025-8194** (Python@3.11.4) — CVSS 7.5 — EPSS 0.16% — Infinite loop.
7. **CVE-2025-13836** (Python@3.11.4) — CVSS 7.5 — EPSS 0.15% — DoS.
8. **CVE-2024-4032** (Python@3.11.4) — CVSS 7.5 — EPSS 1.12% — IP range check.
and 2 more HIGH findings across 1 package.

## 5. Risk Distribution
**Severity:** 3 Critical, 20 High, 30 Medium, 6 Low.
**Top Packages:** Python (120 advisories), OpenSSL (20), Curl (14).

## 6. CRA Compliance Actions
1.  **Immediate:** Upgrade **Python** to 3.11.5+ to patch CVE-2025-4517 and CVE-2007-4559 (Critical/Exploited).
2.  **Immediate:** Update **OpenSSL** to 3.0.17+ to fix CVE-2025-15467 (Critical/Exploited).
3.  **Urgent:** Patch **Python** for CVE-2025-4138 and CVE-2025-4330 (High/Exploited).
4.  **Urgent:** Upgrade **Curl** to 8.15.0+ for CVE-2025-9086 (High/Exploited).
5.  **Planned:** Remediate remaining Python Highs (CVE-2024-8088, CVE-2024-9287) and OpenSSL Highs (CVE-2025-69419, CVE-2025-69420).