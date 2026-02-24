## Vulnerability Summary for openclaw

### 1. SBOM Overview
This report details vulnerabilities found in the `openclaw` product, based on an SPDX SBOM generated on 2026-02-20. Out of 1112 total packages, 21 are affected by known vulnerabilities. This includes 10 unique Critical CVEs, 31 High CVEs, 16 Medium CVEs, and 4 Low CVEs.

### 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

### 3. Exploit Availability Assessment
The following 5 CVEs have known exploit evidence:
- CVE-2023-34104 (CVSS: 9.3, EPSS: 0.00273) in `fast-xml-parser`
- CVE-2026-25253 (CVSS: 8.8, EPSS: 0.00049) in `clawdbot`
- CVE-2026-24763 (CVSS: 8.8, EPSS: 0.00083) in `clawdbot`
- CVE-2026-22610 (CVSS: 8.5, EPSS: 0.00021) in `@angular/compiler`, `@angular/core`
- CVE-2025-69873 (CVSS: 8.2, EPSS: 0.00069) in `ajv`
2 additional CVEs have exploit evidence.

### 4. Critical & High Findings
- CVE-2026-25896 (CVSS: 9.3, EPSS: 0.00029) in `fast-xml-parser`
- CVE-2026-25593 (CVSS: 8.4, EPSS: 0.00023) in `openclaw`
- CVE-2026-22818 (CVSS: 8.2, EPSS: 0.00017) in `hono`
- CVE-2026-22817 (CVSS: 8.2, EPSS: 0.00017) in `hono`
- CVE-2025-66031 (CVSS: 8.7, EPSS: 0.00115) in `node-forge`
- CVE-2025-12816 (CVSS: 8.7, EPSS: 0.00059) in `node-forge`
- CVE-2025-15284 (CVSS: 8.7, EPSS: 0.00085) in `qs`
- CVE-2026-26996 (CVSS: 8.7, EPSS: 0.00040) in `minimatch`
and 23 more HIGH findings across 10 packages.

### 5. Risk Distribution
- **CRITICAL:** 10 unique CVEs
- **HIGH:** 31 unique CVEs
- **MEDIUM:** 16 unique CVEs
- **LOW:** 4 unique CVEs

Top 3 most-affected packages:
1. `openclaw`: 30 advisories
2. `clawdbot`: 10 advisories
3. `fast-xml-parser`: 5 advisories

### 6. CRA Compliance Actions
1. **Immediate Action:** Patch `fast-xml-parser` to a version fixing CVE-2023-34104 and CVE-2026-25896 to mitigate critical regex injection and entity expansion vulnerabilities.
2. **Urgent Action:** Update `clawdbot` to a version addressing CVE-2026-25253 and CVE-2026-24763 to prevent 1-Click RCE and authenticated command injection.
3. **Urgent Action:** Update `@angular/compiler` and `@angular/core` to a version fixing CVE-2026-22610 to resolve XSS vulnerabilities.
4. **Planned Action:** Upgrade `node-forge` to a version addressing CVE-2025-66031 and CVE-2025-12816 to prevent ASN.1 unbounded recursion and interpretation conflicts.
5. **SBOM Hygiene:** Implement automated dependency scanning to detect and address vulnerabilities proactively, ensuring all packages are kept up-to-date.