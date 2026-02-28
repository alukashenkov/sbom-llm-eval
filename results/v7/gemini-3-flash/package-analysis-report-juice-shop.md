## 1. SBOM Overview
*   **Product:** bkimminich/juice-shop (sha256:75b03f3f5336b39d1358d4280c09b8b265ae21e4cb215a9bf68e27f96ac76e3c)
*   **Format:** CycloneDX | **Scan Date:** 2026-02-24
*   **Packages:** 998 total / 38 affected
*   **Unique CVEs:** 60
*   **CRA Tier Breakdown:** 0 ACTIVELY_EXPLOITED / 39 EXPLOITABLE / 21 VULNERABILITY

---

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
The following vulnerabilities meet the severe-incident heuristic (CVSS≥9 + AV:N + CIA:H):
*   **CVE-2015-9235** (jsonwebtoken): CVSS 9.8, `CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Fix: Upgrade to v4.2.2+.
*   **CVE-2023-32314** (vm2): CVSS 9.8, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Fix: Upgrade to v3.9.18+.
*   **CVE-2023-37466** (vm2): CVSS 9.8, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Fix: Upgrade beyond v3.9.19.
*   **CVE-2023-37903** (vm2): CVSS 9.8, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Fix: Upgrade beyond v3.9.19.
*   **CVE-2026-22709** (vm2): CVSS 9.8, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Fix: Upgrade to v3.10.0+.
*   **CVE-2019-10744** (lodash): CVSS 9.1, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H`. Fix: Upgrade to v4.17.12+.
*   **CVE-2023-46233** (crypto-js): CVSS 9.1, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`. Fix: Use current industry standards (PBKDF2 iteration count).

**State:** ≤24h early warning → ≤72h incident notification → ≤1 month final report.

---

## 3. Art. 3(41) Exploitability Assessment
39 vulnerabilities are classified as EXPLOITABLE. PoC/Exploit sources: GitHub (5), Exploit-DB (2), PacketStorm (2), ZDT (2), HackerOne (3), KitPloit (2).

**Top 5 EXPLOITABLE CVEs:**
1.  **CVE-2023-32314** (vm2): CVSS 9.8, EPSS 0.69875 (98th percentile), 1020 days public. Fix: Upgrade to v3.9.18.
2.  **CVE-2015-9235** (jsonwebtoken): CVSS 9.8, EPSS 0.32470 (96th percentile), 2699 days public. Fix: Upgrade to v4.2.2.
3.  **CVE-2023-37466** (vm2): CVSS 9.8, EPSS 0.04997 (89th percentile), 961 days public. Fix: Upgrade beyond v3.9.19.
4.  **CVE-2023-37903** (vm2): CVSS 9.8, EPSS 0.04997 (89th percentile), 961 days public. Fix: Upgrade beyond v3.9.19.
5.  **CVE-2026-22709** (vm2): CVSS 9.8, EPSS 0.00030 (8th percentile), 33 days public. Fix: Upgrade to v3.10.0.

*Note: 9 CVEs have EPSS scores >90 days old — exploitability confidence reduced.*

---

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2026-26996** (minimatch): CVSS 8.7, AV:N (ReDoS), EPSS 0.00040, EXPLOITABLE. Fix: Upgrade to latest.
*   **CVE-2025-65945** (jws): CVSS 7.5, AV:N (HMAC bypass), EPSS 0.00009, EXPLOITABLE. Fix: Upgrade auth0/node-jws.
*   **CVE-2024-37890** (ws): CVSS 8.7, AV:N (DoS), EPSS 0.00541, EXPLOITABLE. Fix: Upgrade ws server.
*   **CVE-2025-48997** (multer): CVSS 8.7, AV:N (DoS), EPSS 0.00081, EXPLOITABLE. Fix: Upgrade to v2.0.1.
*   **CVE-2026-23745** (tar): CVSS 8.2, AV:L (File Overwrite), EPSS 0.00006, EXPLOITABLE. Fix: Upgrade node-tar >7.5.2.
*   **CVE-2025-13465** (lodash): CVSS 8.2, AV:N (Prototype Pollution), EPSS 0.00025, EXPLOITABLE. Fix: Upgrade to v4.17.23.
*   **CVE-2024-29415** (ip): CVSS 8.1, AV:N (SSRF), EPSS 0.00539, VULNERABILITY. Fix: Upgrade ip package.
*   **CVE-2022-23539** (jsonwebtoken): CVSS 8.1, AV:N (Legacy Keys), EPSS 0.00072, VULNERABILITY. Fix: Upgrade to v9.0.0.

And 31 more across 38 packages.

---

## 5. Risk Distribution & Age Risk
*   **Severity:** 7 Critical, 32 High, 20 Medium.
*   **Top Affected:** `sanitize-html` (7), `jsonwebtoken` (5), `tar` (5), `vm2` (5).
*   **Age Risk (Annex I Part II §2 violation signals):**
    1.  **CVE-2016-4055** (moment): 3049 days public. Fix: Upgrade to v2.11.2.
    2.  **CVE-2017-18214** (moment): 2917 days public. Fix: Upgrade to v2.19.3.
    3.  **CVE-2015-9235** (jsonwebtoken): 2699 days public. Fix: Upgrade to v4.2.2.

---

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2**: Patch Track 2 candidates (jsonwebtoken, vm2, lodash, crypto-js) immediately; notify CSIRT/ENISA of severe incident potential.
2.  **Urgent — Annex I Part II §2**: Remediate EXPLOITABLE Critical/High CVEs in `tar`, `multer`, and `ws` using provided `fixHint` upgrade paths.
3.  **Planned — Annex I Part II §2**: Address 3000+ day old vulnerabilities in `moment` and `lodash` to resolve long-standing non-compliance with "patch without delay" obligations.
4.  **SBOM update — Annex I Part II §1**: Regenerate CycloneDX SBOM following remediation to verify removal of components like `vm2@3.9.17`.
5.  **Public advisory — Annex I Part II §4**: Publish security advisories for the PDE detailing the mitigation of the 60 identified CVEs.
6.  **CVD hygiene — Annex I Part II §5–6**: Ensure the `maintainer` contact (Bjoern Kimminich) is active for coordinated disclosure.