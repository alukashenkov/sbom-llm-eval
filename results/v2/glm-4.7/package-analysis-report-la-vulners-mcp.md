## 1. SBOM Overview
Product: la-vulners-mcp (CycloneDX). Scan Date: 2026-02-24. Total packages: 97. Affected packages: 3. Unique CVEs: 7 (2 Critical, 1 High, 2 Medium, 2 Low).

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
1. [CVE-2025-60876] busybox@1.37.0-r30 — CVSS 6.5 — EPSS 0.00052 — HTTP request splitting via wget.
2. [CVE-2026-27171] zlib@1.3.1-r2 — CVSS 5.5 — EPSS 0.00006 — CPU consumption via crc32 functions.
0 additional CVEs have exploit evidence.

## 4. Critical & High Findings
1. [CVE-2023-45853] zlib@1.3.1-r2 — CVSS 9.8 — EPSS 0.01396 — Heap-based buffer overflow.
2. [CVE-2026-22184] zlib@1.3.1-r2 — CVSS 9.8 — EPSS 0.00042 — Global buffer overflow.
3. [CVE-2025-26519] musl@1.2.5-r21 — CVSS 8.1 — EPSS 0.00022 — Out-of-bounds write in iconv.
and 0 more HIGH findings across 1 package.

## 5. Risk Distribution
Severity: 2 Critical, 1 High, 2 Medium, 2 Low. Top 3 most-affected packages: zlib (6 advisories), busybox (5 advisories), musl (2 advisories).

## 6. CRA Compliance Actions
1. **Immediate:** Upgrade zlib to v1.3.2+ to resolve CRITICAL buffer overflows (CVE-2023-45853, CVE-2026-22184).
2. **Urgent:** Upgrade musl to v1.2.6+ to fix HIGH severity out-of-bounds write (CVE-2025-26519).
3. **Planned:** Upgrade busybox to >v1.37.0 to address MEDIUM severity wget exploit (CVE-2025-60876).
4. **Hygiene:** Deduplicate advisory entries in SBOM to reduce noise.