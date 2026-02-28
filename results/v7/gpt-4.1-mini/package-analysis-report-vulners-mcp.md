## 1. SBOM Overview
- Product: vulners-mcp, format: CycloneDX, scan date: 2026-02-24
- Total packages: 560, affected packages: 20
- Unique CVEs: 188
- CRA tiers: ACTIVELY_EXPLOITED: 1, EXPLOITABLE: 90, VULNERABILITY: 97

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
- CVE-2025-48384 (git@1:2.47.3-0+deb13u1): CVSS 8.0, CVSS Vector CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H, EPSS 0.00456 (not stale), 235 days public. Fix: Git vulnerability CVE-2025-48384 leads to incorrect submodule paths and potential script execution risks.
- Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h vulnerability notification → ≤14 days after fix: final report (severity, impact, actor info) per Art. 14(1)–(2).

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
- CVE-2026-22770 (imagemagick@8:7.1.1.43+dfsg1-1+deb13u5): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: ImageMagick before 7.1.2-13 may release an invalid pointer in BilateralBlur on allocation failure.
- CVE-2014-9852 (imagemagick): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: ImageMagick vulnerable to denial of service attacks due to use after free bu.
- CVE-2014-9846 (imagemagick): CVSS 9.8, CVSS Vector CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: ImageMagick buffer overflow vulnerabilit.
- CVE-2026-23876 (imagemagick): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: CVE-2026-23876 causes heap overflow in ImageMagick's XBM decoder from attacker-controlled data.
- CVE-2026-25897 (imagemagick): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: CVE-2026-25897 fixes a heap overflow in the sun decoder on 32-bit ImageMagick that can cause out-of-bounds writes.
- CVE-2025-57807 (imagemagick): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: ImageMagick before 14.8.2 exposes SeekBlob and WriteBlob flaws causing heap writes on sixty four bit systems; fixed in 14.8.2.
- CVE-2025-15467 (openssl@3.5.4-1~deb13u2): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: Bell CVE-2025-15467 bulletin has no description for the library.
- CVE-2024-56171 (libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2): CVSS 9.8, CVSS Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, fixHint: BELL-CVE-2024-56171 security bulletin for software vulnerabilities.
- Notify per Art. 14(3): ≤24h early warning → ≤72h incident notification → ≤1 month final report.

## 3. Art. 3(41) Exploitability Assessment
- PoC sources: githubexploit 9, packetstorm 13, hackerone 7, cisa_kev 1, gitee 1, nuclei 1, kitploit 1
- EXPLOITABLE CVEs: 90
- Top 5 EXPLOITABLE CVEs by CVSS score:
  - CVE-2026-22770 (imagemagick): 9.8, EPSS 0.00065/20.1 percentile, 39 days public, fix: ImageMagick before 7.1.2-13 may release invalid pointer on allocation failure.
  - CVE-2014-9852 (imagemagick): 9.8, EPSS 0.01316 (stale), 3266 days public, fix: ImageMagick use after free bug causing DoS.
  - CVE-2014-9846 (imagemagick): 9.8, EPSS 0.04666, 3266 days public, fix: ImageMagick buffer overflow vulnerability.
  - CVE-2026-23876 (imagemagick): 9.8, EPSS 0.00062, 39 days public, fix: Heap overflow in XBM decoder.
  - CVE-2026-25897 (imagemagick): 9.8, EPSS 0.00038, 4 days public, fix: Heap overflow in sun decoder on 32-bit.
- Note: 15 CVEs have EPSS scores >90 days old — exploitability confidence reduced.

## 4. Critical & High Findings (Annex I Part II §2 — Remediate Without Delay)
- CVE-2025-53014 (imagemagick): 9.8, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00031, EXPLOITABLE, fix: Heap buffer overflow in InterpretImageFilename prior to 7.1.2-0.
- CVE-2025-53101 (imagemagick): 9.8, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00069, EXPLOITABLE, fix: Stack buffer overflow due to filename template issue prior to 7.1.2-0.
- CVE-2026-26284 (imagemagick): 9.1, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H, EPSS 0.00037, EXPLOITABLE, fix: Heap overflow in Photo CD decoder from Huffman data.
- CVE-2025-49794 (libxml2): 9.1, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H, EPSS 0.00078, EXPLOITABLE, fix: No description; upgrade libxml2.
- CVE-2025-49796 (libxml2): 9.1, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H, EPSS 0.0055, EXPLOITABLE, fix: No description; upgrade libxml2.
- CVE-2025-48385 (git): 8.6, CVSS Vector CVSS:4.0/AV:N/AC:L/PR:N/UI:A/S:U/C:H/I:H/A:H, EPSS 0.00039, EXPLOITABLE, fix: Protocol injection leads to remote code execution.
- CVE-2025-48384 (git): 8.0, CVSS Vector CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H, EPSS 0.00456, ACTIVELY_EXPLOITED, fix: Incorrect submodule paths and potential script execution.
- CVE-2025-57807 (imagemagick): 9.8, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00042, EXPLOITABLE, fix: SeekBlob and WriteBlob flaws causing heap writes on 64-bit systems.
- CVE-2025-15467 (openssl): 9.8, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00672, EXPLOITABLE, fix: Stack buffer overflow in CMS AuthEnvelopedData parsing.
- CVE-2024-56171 (libxml2): 9.8, CVSS Vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, EPSS 0.00048, EXPLOITABLE, fix: Use-after-free in xmlSchemaIDCFillNodeTables.
- And 72 more across 17 packages.

## 5. Risk Distribution & Age Risk
- Severity distribution: HIGH 82, MEDIUM 79, CRITICAL 14, LOW 12, NONE 1
- Top affected packages by unique CVEs:
  1. imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 (77 CVEs)
  2. binutils@2.44-3 (32 CVEs)
  3. libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 (17 CVEs)
- Top 3 longest-unpatched CRITICAL/HIGH CVEs (Annex I Part II §2 signals):
  - CVE-2015-8895 (imagemagick): HIGH, 3271 days, fix: integer overflow in icon.c causing DoS.
  - CVE-2014-9852 (imagemagick): CRITICAL, 3266 days, fix: use after free causing DoS.
  - CVE-2014-9846 (imagemagick): CRITICAL, 3266 days, fix: buffer overflow vulnerability.

## 6. CRA Defensible-Practice Actions
1. Immediate — Art. 14 + Annex I Part II §2:
   - Patch all Track 1 and Track 2 CVEs immediately.
   - Submit Art. 14 notifications for CVE-2025-48384 and CVE-2026-22770 plus others listed.
   - Use fix hints for remediation versions.
2. Urgent — Annex I Part II §2:
   - Patch all EXPLOITABLE CRITICAL/HIGH CVEs, e.g. imagemagick CVE-2025-53014, CVE-2025-53101, CVE-2026-26284; libxml2 CVE-2025-49794, CVE-2025-49796; openssl CVE-2025-15467.
3. Planned — Annex I Part II §2:
   - Remediate remaining HIGH and MEDIUM CVEs prioritizing oldest first.
4. SBOM update — Annex I Part II §1:
   - Update SBOM to reflect current component versions, minimum top-level dependencies in CycloneDX format.
5. Public advisory — Annex I Part II §4:
   - Publish advisories with CVE IDs, severities, vectors, affected versions, and remediation steps once patches are available.
6. CVD hygiene — Annex I Part II §5–6:
   - Verify coordinated vulnerability disclosure policy and security contact info are published and current.