1) SBOM Overview
- Product: sbom-grbrsm_ui-v12.0.3rc0
- Format: SPDX
- Scan date: 2025-07-11
- Packages: total 338, affected 7
- Unique CVEs from severity distribution: 9

2) CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3) Exploit Assessment
- Top exploited CVEs by severity (from advisory data):
  - CVE-2025-7783 — package: form-data; CVSS 9.4 (CVSSv4.0); EPSS 0.00177
  - CVE-2025-58754 — package: axios; CVSS 7.5 (CVSSv3.1); EPSS 0.00102
  - CVE-2026-25639 — package: axios; CVSS 8.7 (CVSSv4.0); EPSS 0.00033
  - CVE-2026-26996 — package: minimatch; CVSS 8.7 (CVSSv4.0); EPSS 0.00040
  - CVE-2025-13465 — package: lodash; CVSS 7.9 (CVSSv4.0); EPSS 0.00025
- PoC evidence: 2 additional CVEs have PoC evidence.

4) Critical & High Findings
- Remaining CRITICAL/HIGH CVEs not in §2-3:
- None. and 0 more across 0 packages.

5) Risk Distribution
- Severity counts: CRITICAL 1, HIGH 5, MEDIUM 3
- Top affected packages:
  - axios@1.10.0 — 4 unique CVEs
  - js-yaml@4.1.0 — 1 unique CVE
  - lodash@4.17.21 — 1 unique CVE

6) CRA Compliance Actions (max 5)
- Immediate (CRA Article 10/11): Patch the CRITICAL CVE-2025-7783 in form-data; apply patches for any other active exploited/critical issues as appropriate.
- Urgent (exploited CRITICAL/HIGH patches with target versions): Patch CVE-2025-58754 (axios), CVE-2026-25639 (axios), CVE-2026-26996 (minimatch), and CVE-2025-13465 (lodash) to their patched releases.
- Planned: Complete remaining HIGH patches where patches exist but are not yet deployed.
- Hygiene: Maintain SBOM per Article 10(6) and continue vulnerability management per Article 11; track patch status and re-scan.