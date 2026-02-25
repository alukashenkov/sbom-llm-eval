1) SBOM Overview
- Product: openclaw
- Format: SPDX
- Scan date: 2026-02-20
- Packages: total 1112; affected 21
- Unique CVEs (cveAnalytics.severityDistribution): 57
  - HIGH: 34
  - MEDIUM: 19
  - LOW: 2
  - CRITICAL: 2

2) CRA Mandatory Reporting (Article 14)
- No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

3) Exploit Assessment
- PoC evidence totals (cveAnalytics.pocSummary): 6 listed as GitHub exploits
- Top 5 exploited CVEs by severity (from advisory data)
  - CVE-2026-25896 — fast-xml-parser (package fast-xml-parser, 4.5.3). CVSS score 9.3 (CRITICAL). EPSS not provided.
  - CVE-2026-25474 — OpenClaw Telegram webhook forgery (Telegram webhook). CVSS 9.1 (CRITICAL). EPSS not provided.
  - CVE-2026-25157 — OpenClaw/Clawdbot SSH/root path injection via sshNodeCommand. CVSS 7.7 (HIGH). EPSS 6e-05.
  - CVE-2026-22610 — Angular XSS through SVG script attributes. CVSS 8.5 (HIGH). EPSS 0.00021.
  - CVE-2026-25253 — OpenClaw gateway URL exfil/1-click RCE via gatewayUrl. CVSS 8.8 (HIGH). EPSS 0.00049 (from advisories).
- N additional CVEs have PoC evidence: 1

4) Critical & High Findings
- Remaining CRITICAL/HIGH CVEs not in §2-3 (max 8 shown here; N more across multiple packages)
  - CVE-2026-26323 — OpenClaw: command injection in maintainer clawtributors updater (package openclaw). CVSS 8.6 HIGH.
  - CVE-2026-26329 — OpenClaw: path traversal in browser upload (package openclaw). CVSS 7.1 HIGH.
  - CVE-2026-26324 — OpenClaw SSRF guard bypass (package openclaw). CVSS 7.5 HIGH.
  - CVE-2026-27002 — OpenClaw Docker container escape via Docker tool sandbox (package openclaw). CVSS 7.7 HIGH.
  - CVE-2026-26325 — OpenClaw Windows host system.run/command mismatch bypass (package openclaw). CVSS 7.2 HIGH.
  - CVE-2026-26321 — OpenClaw Feishu extension local file read in media flow (package hono/feishu-related). CVSS 7.5 HIGH.
- and 25 more across several packages.

5) Risk Distribution
- Severity distribution: HIGH 34, MEDIUM 19, LOW 2, CRITICAL 2
- Top affected packages (by unique CVE count)
  - openclaw@2026.1.10 — 29 unique CVEs
  - hono@4.11.3 — 6 unique CVEs
  - clawdbot@2026.1.10 — 5 unique CVEs

6) CRA Compliance Actions (max 5)
- Immediate (Article 10): Patch critical/high CVEs with fixes as they become available; verify remediation paths and re-scan SBOMs.
- Urgent (Article 11): Apply patches for exploited CRITICAL/HIGH CVEs with defined target versions; e.g., OpenClaw-related fixes are planned (e.g., 2026.2.15 for certain updates) and other packages with fixes should be deployed promptly.
- Planned (Article 11): Remediate remaining HIGH fixes lacking immediate patches; implement upgrade plans and risk-based remediation timelines.
- Hygiene (Article 10(6)): Maintain SBOM accuracy via regular updates, dependency pinning reviews, and ensure CVE metadata and remediation statuses are current.
- CRA Article 14 reference: only when triggers exist; none present here.