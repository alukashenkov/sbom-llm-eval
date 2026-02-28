## 1. SBOM Overview
- Product: la-vulners-mcp, format: CycloneDX, scan date: 2026-02-24
- Total packages: 97, affected packages: 3
- Unique CVEs: 7
- CRA tier distribution (Art. 3(40/41/42)):
  - EXPLOITABLE: 3
  - VULNERABILITY: 4
  - ACTIVELY_EXPLOITED: 0

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
- CVE-2023-45853 (zlib@1.3.1-r2): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.01396 (not stale), fixHint: "Zlib MiniZip integer overflow with long filenames or fields; upgrade to version 1.3.1 or higher."
- CVE-2026-22184 (zlib@1.3.1-r2): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00042 (not stale), fixHint: "CVE-2026-22184: Zlib until 1.3.1.2 has untgz overflow via strcpy into 1024-byte buffer from attacker name."
- Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h incident notification → ≤1 month final report.

## 3. Art. 3(41) Exploitability Assessment
- PoC/exploit sources present but no EPSS stale advisories (0 stale).
- EXPLOITABLE CVEs: 3 total.
- Top 3 EXPLOITABLE CVEs by CVSS score:
  1. CVE-2023-45853 (zlib@1.3.1-r2): CVSS 9.8, EPSS 0.01396/80.04 percentile, days public 868, fixHint: "Zlib MiniZip integer overflow with long filenames or fields; upgrade to version 1.3.1 or higher."
  2. CVE-2026-22184 (zlib@1.3.1-r2): CVSS 9.8, EPSS 0.00042/12.52 percentile, days public 52, fixHint: "CVE-2026-22184: Zlib until 1.3.1.2 has untgz overflow via strcpy into 1024-byte buffer from attacker name."
  3. CVE-2025-60876 (busybox@1.37.0-r30): CVSS 6.5, EPSS 0.00052/16.69 percentile, days public 110, fixHint: "CVE-2025-60876: BusyBox wget 1.3.7 accepts CR/LF in Http request-target, enabling header injection."
- No EPSS stale advisories; exploitability confidence not reduced.

## 4. Critical & High Findings (Annex I Part II §2 — Remediate Without Delay)
- CVE-2025-26519 (musl@1.2.5-r21): CVSS 8.1, CVSS Vector CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:L, EPSS 0.00022, Tier: VULNERABILITY, fixHint: "musl libc versions 0.9.13 to 1.2.5 have an out-of-bounds write vulnerability via iconv conversion."
- and 1 more across 1 package.

## 5. Risk Distribution & Age Risk
- Severity distribution: CRITICAL 2, HIGH 1, MEDIUM 2, LOW 2
- Top affected packages by unique CVEs:
  1. zlib@1.3.1-r2 (3 CVEs)
  2. busybox@1.37.0-r30 (3 CVEs)
  3. musl@1.2.5-r21 (1 CVE)
- Top 3 longest-unpatched CRITICAL/HIGH CVEs:
  1. CVE-2023-45853 (zlib@1.3.1-r2), CRITICAL, 868 days public, fixHint: "Zlib MiniZip integer overflow with long filenames or fields; upgrade to version 1.3.1 or higher."
  2. CVE-2025-26519 (musl@1.2.5-r21), HIGH, 379 days public, fixHint: "musl libc versions 0.9.13 to 1.2.5 have an out-of-bounds write vulnerability via iconv conversion."
  3. CVE-2026-22184 (zlib@1.3.1-r2), CRITICAL, 52 days public, fixHint: "CVE-2026-22184: Zlib until 1.3.1.2 has untgz overflow via strcpy into 1024-byte buffer from attacker name."

## 6. CRA Defensible-Practice Actions
1. **Immediate — Art. 14 + Annex I Part II §2**: Patch/mitigate CVE-2023-45853 and CVE-2026-22184 in zlib@1.3.1-r2; submit Art. 14 Track 2 notifications. Upgrade to zlib 1.3.1 or higher and 1.3.1.2 respectively.
2. **Urgent — Annex I Part II §2**: Patch EXPLOITABLE CVE-2025-60876 in busybox@1.37.0-r30; upgrade BusyBox wget to fixed version.
3. **Planned — Annex I Part II §2**: Remediate HIGH CVE-2025-26519 in musl@1.2.5-r21; upgrade musl libc beyond 1.2.5.
4. **SBOM update — Annex I Part II §1**: Update SBOM to reflect current component versions and fixes; maintain CycloneDX format.
5. **Public advisory — Annex I Part II §4**: Publish advisories for fixed CVEs including CVE IDs, severity, CVSS vectors, affected versions, and remediation steps.
6. **CVD hygiene — Annex I Part II §5–6**: Verify coordinated vulnerability disclosure policy and security contact details are published and up to date.