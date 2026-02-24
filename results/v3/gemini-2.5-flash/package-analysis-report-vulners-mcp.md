I will now perform the silent checks.

**Silent Checks:**
1. **CISA KEV / Wild Exploited Scan:**
   - `CVE-2025-48384` (git): `wildExploited=true` and `cisa_kev` in `pocSources`. This is a mandatory trigger.

2. **Deduplicate CVEs:**
   - `CVE-2025-9230`, `CVE-2025-9231`, `CVE-2025-9232`, `CVE-2025-11187`, `CVE-2025-15467`, `CVE-2025-15468`, `CVE-2025-15469`, `CVE-2025-66199`, `CVE-2025-68160`, `CVE-2025-69418`, `CVE-2025-69419`, `CVE-2025-69420`, `CVE-2025-69421`, `CVE-2026-22795`, `CVE-2026-22796`, `CVE-2025-22795` (openssl)
   - `CVE-2025-55212`, `CVE-2025-55298`, `CVE-2025-57803`, `CVE-2025-62171`, `CVE-2025-62594`, `CVE-2025-65955`, `CVE-2025-55004`, `CVE-2025-55005`, `CVE-2017-16545`, `CVE-2019-13454`, `CVE-2019-13304`, `CVE-2019-14980`, `CVE-2017-12668`, `CVE-2016-7519`, `CVE-2018-9135`, `CVE-2018-15607`, `CVE-2026-22770`, `CVE-2026-23874`, `CVE-2015-8894`, `CVE-2015-8895`, `CVE-2023-5341`, `CVE-2014-9852`, `CVE-2014-9850`, `CVE-2014-9846`, `CVE-2016-10053`, `CVE-2017-6502`, `CVE-2016-7513`, `CVE-2016-7540`, `CVE-2016-7525`, `CVE-2017-9098`, `CVE-2025-55154`, `CVE-2024-41817`, `CVE-2025-66628`, `CVE-2026-23876`, `CVE-2026-24481`, `CVE-2026-24484`, `CVE-2026-24485`, `CVE-2026-25576`, `CVE-2026-25638`, `CVE-2026-25795`, `CVE-2026-25796`, `CVE-2026-25797`, `CVE-2026-25798`, `CVE-2026-25799`, `CVE-2026-25897`, `CVE-2026-25898`, `CVE-2026-25965`, `CVE-2026-25966`, `CVE-2026-25968`, `CVE-2026-25970`, `CVE-2026-25971`, `CVE-2026-25982`, `CVE-2026-25983`, `CVE-2026-25985`, `CVE-2026-25986`, `CVE-2026-25987`, `CVE-2026-25988`, `CVE-2026-25989`, `CVE-2026-26066`, `CVE-2026-26283`, `CVE-2026-26284`, `CVE-2026-26983`, `CVE-2025-55160`, `CVE-2025-57807`, `CVE-2025-53014`, `CVE-2025-53015`, `CVE-2025-53019`, `CVE-2025-53101`, `CVE-2025-68618`, `CVE-2025-68950`, `CVE-2025-69204`, `CVE-2026-25637`, `CVE-2026-25794`, `CVE-2026-25967`, `CVE-2026-25969`, `CVE-2026-23952` (imagemagick)
   - `CVE-2025-11082`, `CVE-2025-11083`, `CVE-2025-5244`, `CVE-2025-5245`, `CVE-2025-1153`, `CVE-2025-1148`, `CVE-2025-1149`, `CVE-2025-1150`, `CVE-2025-1151`, `CVE-2025-1152`, `CVE-2025-1176`, `CVE-2025-1178`, `CVE-2025-1180`, `CVE-2025-1181`, `CVE-2025-1182`, `CVE-2025-7545`, `CVE-2025-7546`, `CVE-2025-8225`, `CVE-2025-1147`, `CVE-2025-0840`, `CVE-2024-53589`, `CVE-2025-1179`, `CVE-2024-57360`, `CVE-2025-8224`, `CVE-2025-11412`, `CVE-2025-11413`, `CVE-2025-11414`, `CVE-2025-11494`, `CVE-2025-11495`, `CVE-2025-11839`, `CVE-2025-11840`, `CVE-2025-3198` (binutils)
   - `CVE-2024-40896`, `CVE-2025-32414`, `CVE-2025-32415`, `CVE-2024-56171`, `CVE-2025-24928`, `CVE-2025-49794`, `CVE-2025-49796`, `CVE-2025-6021`, `CVE-2025-6170`, `CVE-2017-9047`, `CVE-2025-27113`, `CVE-2026-0989`, `CVE-2026-0990`, `CVE-2026-0992`, `CVE-2026-1757`, `CVE-2025-49795`, `CVE-2025-26434` (libxml2)
   - `CVE-2021-32804`, `CVE-2026-23950`, `CVE-2026-24842`, `CVE-2026-23745`, `CVE-2026-26960`, `CVE-2021-37713`, `CVE-2018-20834`, `CVE-2021-32803`, `CVE-2024-28863`, `CVE-2015-8860` (tar)
   - `CVE-2025-14017`, `CVE-2025-14524`, `CVE-2025-14819`, `CVE-2025-15079`, `CVE-2025-15224`, `CVE-2025-5399`, `CVE-2025-11563`, `CVE-2025-10966`, `CVE-2025-10148`, `CVE-2025-9086`, `CVE-2025-13034` (curl)
   - `CVE-2025-48384`, `CVE-2025-48385`, `CVE-2025-48386`, `CVE-2024-50349`, `CVE-2024-52006`, `CVE-2025-27613`, `CVE-2025-27614`, `CVE-2025-46835` (git)
   - `CVE-2025-68973`, `CVE-2025-68972`, `CVE-2025-30258`, `CVE-2020-24972`, `CVE-2026-24882` (gnupg)
   - `CVE-2024-46901`, `CVE-2024-45720` (subversion)
   - `CVE-2024-21485` (dash)
   - `CVE-2011-3374` (apt)
   - `CVE-2025-5278` (coreutils)
   - `CVE-2025-69872` (diskcache)
   - `CVE-2025-66416` (fastmcp, mcp)
   - `CVE-2022-43410` (mercurial)
   - `CVE-2024-56406` (perl)
   - `CVE-2023-24056` (pkgconf)
   - `CVE-2024-10524` (wget)

   Total unique CVEs: 109.

3. **Severity Distribution (from unique CVEs):**
   - CRITICAL: 10
   - HIGH: 48
   - MEDIUM: 48
   - LOW: 3
   - NONE: 0

4. **CRA Article 14 Triggers:**
   - `CVE-2025-48384` (git): `wildExploited=true` and `cisa_kev` in `pocSources`.

---

## Vulnerability Summary for vulners-mcp

### 1. SBOM Overview
This report details vulnerabilities identified in the `vulners-mcp` container image (sha256:1cb7222c813177af65f1a4fb535ccbd3627926d1ab84f583f3358fc841b94ddd9) scanned on 2026-02-24. Out of 560 total packages, 20 are affected by 109 unique vulnerabilities. The distribution of these unique CVEs by severity is: 10 Critical, 48 High, 48 Medium, and 3 Low.

### 2. CRA Mandatory Reporting Triggers (Article 14)
The following vulnerability requires mandatory reporting to ENISA/CSIRT within 24 hours (initial notification), 72 hours (detailed update), and 14 days (final report) as per CRA Article 14 due to evidence of active exploitation or inclusion in CISA KEV:

*   **CVE-2025-48384** git@1:2.47.3-0+deb13u1 — CVSS: 8.0 (HIGH) — EPSS: 0.00456 — Arbitrary code execution through broken config quoting.

### 3. Exploit Availability Assessment
Evidence of publicly available Proof-of-Concept (PoC) exploits has been found for 18 unique CVEs. The top 5 by severity are:
*   **CVE-2025-15467** openssl@3.5.4-1~deb13u2 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00672
*   **CVE-2014-9846** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.04666
*   **CVE-2014-9852** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.01316
*   **CVE-2026-23876** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00062
*   **CVE-2025-53014** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00031

13 additional CVEs have exploit evidence.

### 4. Critical & High Findings
Beyond those with exploit evidence or mandatory reporting, the following Critical and High severity vulnerabilities warrant immediate attention:
*   **CVE-2024-56171** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00048
*   **CVE-2025-57807** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00042
*   **CVE-2025-53101** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00069
*   **CVE-2026-22770** imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 — CVSS: 9.8 (CRITICAL) — EPSS: 0.00065
*   **CVE-2024-40896** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.00553
*   **CVE-2025-49794** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.00078
*   **CVE-2025-49796** libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 — CVSS: 9.1 (CRITICAL) — EPSS: 0.0055
*   **CVE-202