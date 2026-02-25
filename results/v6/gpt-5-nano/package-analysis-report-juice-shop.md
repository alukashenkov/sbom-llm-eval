1) SBOM Overview
- Product: OWASP Juice Shop
- Format: CycloneDX
- Scan date: 2026-02-24T14:44:13.000Z
- Packages: total 998, affected 38
- Unique CVEs (from cveAnalytics.severityDistribution): 58
- Severity distribution (for reference): MEDIUM 21, HIGH 30, CRITICAL 7

2) CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3) Exploit Assessment
- Top exploited CVEs by severity (based on advisory data):
  - CVE-2015-9235, jsonwebtoken — package jsonwebtoken — CVSS 9.8 (CRITICAL) — EPSS 0.3247
  - CVE-2023-32314, vm2 — package vm2 — CVSS 9.8 (CRITICAL) — EPSS 0.69875
  - CVE-2023-37466, vm2 — package vm2 — CVSS 9.8 (CRITICAL) — EPSS 0.04997
  - CVE-2023-37903, vm2 — package vm2 — CVSS 9.8 (CRITICAL) — EPSS 0.39234
  - CVE-2019-10744, lodash — package lodash — CVSS 9.1 (CRITICAL) — EPSS 0.02441
- N additional CVEs have PoC evidence (PoC sources total from cveAnalytics.pocSummary = 16).

4) Critical & High Findings
- Remaining CRITICAL/HIGH CVEs (selected, up to 8 entries):
  - CVE-2015-9235, jsonwebtoken — jsonwebtoken — CVSS 9.8 — EPSS 0.3247
  - CVE-2023-32314, vm2 — vm2 — CVSS 9.8 — EPSS 0.69875
  - CVE-2023-37466, vm2 — vm2 — CVSS 9.8 — EPSS 0.04997
  - CVE-2023-37903, vm2 — vm2 — CVSS 9.8 — EPSS 0.39234
  - CVE-2019-10744, lodash — lodash — CVSS 9.1 — EPSS 0.02441
  - CVE-2022-25881, http-cache-semantics — http-cache-semantics — CVSS 7.5 — EPSS 0.00196
  - CVE-2026-23745, tar (node-tar) — tar — CVSS 8.2 — EPSS 0.00447
  - CVE-2026-26960, tar (node-tar) — tar — CVSS 7.1 — EPSS 0.00013
- and N more across M packages.

5) Risk Distribution
- Severity counts: CRITICAL 7, HIGH 30, MEDIUM 21
- Top affected packs: sanitize-html@1.4.2, jsonwebtoken@0.1.0, jsonwebtoken@0.4.0

6) CRA Compliance Actions (max 5)
- Immediate (Article 10): Patch CRITICAL CVEs by upgrading affected packages to secure releases; priority on jsonwebtoken and vm2.
- Urgent (Article 11): Patch exploited/near-exploited CRITICAL/HIGH CVEs with target versions:
  - jsonwebtoken: upgrade to version later than 4.2.1
  - vm2: upgrade to a release beyond 3.9.19
  - lodash: upgrade to 4.17.12 or newer
  - tar: upgrade to a patched release beyond 7.5.2
  - http-cache-semantics: upgrade to 4.1.1 or newer
- Planned (Article 11): Complete remaining HIGH patches not yet escalated; implement upgrade plan for http-cache-semantics TAR family and related dependencies.
- Hygiene (Article 10(6)): Maintain SBOM freshness; re-scan periodically; enforce dependency pinning and fix-version tracking; document remediation timelines.