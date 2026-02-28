## 1. SBOM Overview
*   **Product:** vulners-mcp (CycloneDX container)
*   **Scan Date:** 2026-02-24
*   **Packages:** 560 total / 20 affected
*   **Unique CVEs:** 188
*   **CRA Tier Breakdown (Art. 3):** 1 ACTIVELY_EXPLOITED / 90 EXPLOITABLE / 97 VULNERABILITY

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
*   **CVE-2025-48384** (git): CVSS 8.0 (AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H). EPSS: 0.00456. Age: 235 days. **Fix:** Git vulnerability leads to incorrect submodule paths and script execution risks.
*   **Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously:** ≤24h early warning → ≤72h vulnerability notification → ≤14 days after fix: final report (severity, impact, actor info).

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
*   **CVE-2026-22770** (imagemagick): CVSS 9.8. **Fix:** ImageMagick before 7.1.2-13 may release invalid pointer in BilateralBlur.
*   **CVE-2014-9852** (imagemagick): CVSS 9.8. **Fix:** Patch use-after-free bug causing DoS.
*   **CVE-2014-9846** (imagemagick): CVSS 9.8. **Fix:** Patch buffer overflow vulnerability.
*   **CVE-2026-23876** (imagemagick): CVSS 9.8. **Fix:** Patch heap overflow in XBM decoder.
*   **CVE-2026-25897** (imagemagick): CVSS 9.8. **Fix:** Patch heap overflow in sun decoder.
*   **CVE-2025-53014** (imagemagick): CVSS 9.8. **Fix:** Patch heap buffer overflow in InterpretImageFilename.
*   **CVE-2025-53101** (imagemagick): CVSS 9.8. **Fix:** Patch stack buffer overflow in filename template.
*   **CVE-2025-57807** (imagemagick): CVSS 9.8. **Fix:** Fixed in 14.8.2.
*   **CVE-2025-15467** (openssl): CVSS 9.8. **Fix:** Upgrade OpenSSL 3.0.19 or newer.
*   **CVE-2024-56171** (libxml2): CVSS 9.8. **Fix:** Use-after-free fixed in 2.12.10/2.13.6.
*   **≤24h early warning → ≤72h incident notification → ≤1 month final report.**

## 3. Art. 3(41) Exploitability Assessment
*   **Total EXPLOITABLE CVEs:** 90. PoC sources detected: 33 (GitHub, PacketStorm, HackerOne, etc.).
*   **CVE-2026-26284** (imagemagick): CVSS 9.1. EPSS: 0.00037. Age: 4 days. **Fix:** Patch heap overflow in Photo CD decoder.
*   **CVE-2024-40896** (libxml2): CVSS 9.1. EPSS: 0.00553. Age: 432 days. **Fix:** Patch SAX parser XXE vulnerability.
*   **CVE-2025-49794** (libxml2): CVSS 9.1. EPSS: 0.00078. Age: 261 days. **Fix:** Upgrade libxml2 to 2.14.5.
*   **CVE-2025-49796** (libxml2): CVSS 9.1. EPSS: 0.0055. Age: 261 days. **Fix:** Upgrade libxml2 to 2.14.5.
*   **CVE-2025-55298** (imagemagick): CVSS 8.8. EPSS: 0.0043. Age: 186 days. **Fix:** Fixed in 6.9.13-28 and 7.1.2-2.
*   **Note:** 15 CVEs have EPSS scores >90 days old — exploitability confidence reduced.

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2024-41817** (imagemagick): CVSS 7.8. Local Attack. EPSS: 0.18593. **Fix:** ImageMagick AppImage Arbitrary Code Execution Vulnerability.
*   **CVE-2025-68973** (gnupg): CVSS 7.8. Local Attack. EPSS: 0.00016. **Fix:** Armor_filter index increment fix in 2.4.9.
*   **CVE-2021-32804** (tar): CVSS 8.2. Local Attack. EPSS: 0.00147. **Fix:** Upgrade npm tar to 6.1.1+.
*   **CVE-2025-11082** (binutils): CVSS 7.8. Local Attack. EPSS: 0.00016. **Fix:** Patch memory corruption in ld component.
*   **CVE-2025-6297** (dpkg): CVSS 8.2. Network Attack. EPSS: 0.00136. **Fix:** Patch directory permission sanitization in dpkg-deb.
*   **CVE-2025-66416** (mcp): CVSS 7.6. Network Attack. EPSS: 0.00037. **Fix:** Upgrade to version 1.23.0 for DNS rebinding protection.
*   **CVE-2025-5399** (curl): CVSS 7.5. Network Attack. EPSS: 0.00146. **Fix:** Patch WebSocket busy-loop DoS.
*   **CVE-2025-9086** (curl): CVSS 7.5. Network Attack. EPSS: 0.00035. **Fix:** Patch out-of-bounds read in cookie path handling.
*   **and 88 more across 20 packages.**

## 5. Risk Distribution & Age Risk
*   **Severity:** 14 CRITICAL, 82 HIGH, 79 MEDIUM.
*   **Top Affected:** imagemagick (77), binutils (32), libxml2 (17).
*   **Oldest Unpatched (Annex I Part II §2 violation risk):**
    1.  **CVE-2015-8895** (imagemagick): 3271 days. **Fix:** Patch integer overflow in icon.c.
    2.  **CVE-2014-9852** (imagemagick): 3266 days. **Fix:** Patch use-after-free.
    3.  **CVE-2014-9850** (imagemagick): 3266 days. **Fix:** Patch threading logic error.

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2:** Patch Track 1 (CVE-2025-48384) and Track 2 (imagemagick/openssl/libxml2) vulnerabilities; submit mandatory Art. 14 notifications.
2.  **Urgent — Annex I Part II §2:** Remediate EXPLOITABLE CRITICAL/HIGH findings in libxml2 (2.14.5+) and imagemagick (7.1.2-15+).
3.  **Planned — Annex I Part II §2:** Address remaining HIGH/MEDIUM findings, prioritizing the 3,000+ day old legacy vulnerabilities in imagemagick.
4.  **SBOM update — Annex I Part II §1:** Update SBOM to reflect patched states of git, openssl, and imagemagick.
5.  **Public advisory — Annex I Part II §4:** Publish security advisory detailing the git and imagemagick remediations.
6.  **CVD hygiene — Annex I Part II §5–6:** Ensure security contact for "vulners-mcp" is active for coordinated disclosure.