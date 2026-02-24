## 1. SBOM Overview
SBOM for `bkimminich/juice-shop` (CycloneDX, scanned 2026-02-24). 998 total packages; 38 affected. Identified 55 unique CVEs: 6 Critical, 28 High, 20 Medium, 1 Low.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
1. CVE-2023-37466 (vm2) — 9.8 CRITICAL
2. CVE-2023-37903 (vm2) — 9.8 CRITICAL
3. CVE-2026-23745 (tar) — 8.2 HIGH
4. CVE-2022-24785 (moment) — 7.5 HIGH
5. CVE-2020-8203 (lodash.set) — 7.4 HIGH
2 additional CVEs have exploit evidence.

## 4. Critical & High Findings
1. CVE-2015-9235 (jsonwebtoken) — 9.8 CRITICAL — EPSS 0.32
2. CVE-2023-32314 (vm2) — 9.8 CRITICAL — EPSS 0.70
3. CVE-2026-22709 (vm2) — 9.8 CRITICAL — EPSS 0.0003
4. CVE-2023-46233 (crypto-js) — 9.1 CRITICAL — EPSS 0.008
5. CVE-2026-23950 (tar) — 8.8 HIGH — EPSS 0.00006
6. CVE-2025-48997 (multer) — 8.7 HIGH — EPSS 0.0008
7. CVE-2025-15284 (qs) — 8.7 HIGH — EPSS 0.0008
8. CVE-2024-37890 (ws) — 8.7 HIGH — EPSS 0.005
and 21 more HIGH findings across 15 packages.

## 5. Risk Distribution
Severity: 6 Critical, 28 High, 20 Medium, 1 Low. Top 3 affected packages: sanitize-html (7 advisories), vm2 (5), jsonwebtoken (5).

## 6. CRA Compliance Actions
1. **Immediate:** Patch `vm2@3.9.17` (Critical RCE) and `jsonwebtoken@0.1.0/0.4.0` (Auth bypass).
2. **Urgent:** Update `crypto-js@3.3.0` (Weak crypto) and `tar@4.4.19/6.2.1/7.5.2` (Path traversal).
3. **Planned:** Upgrade `multer@1.4.5-lts.2` and `ip@2.0.1` to resolve DoS/SSRF risks.
4. **Hygiene:** Consolidate duplicate `jsonwebtoken` and `tar` versions to reduce attack surface.
5. **Hygiene:** Review `sanitize-html` (7 advisories) for latest stable version.