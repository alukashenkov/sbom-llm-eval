## 1. SBOM Overview
*   **Product:** openclaw (SPDX)
*   **Scan Date:** 2026-02-20
*   **Packages:** 1112 total / 21 affected
*   **Unique CVEs:** 96
*   **CRA Tier Breakdown:** 41 EXPLOITABLE / 55 VULNERABILITY (Art. 3(40-42))

---

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
*   No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
*   **OSV:GHSA-4RJ2-GPMH-QQ5X** | openclaw@2026.1.10 | **9.4** | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L | Fix: OpenClaw voice-call extension bypasses inbound allowlist using empty caller IDs or suffix matching; fixed in 2026.2.2.
*   **OSV:GHSA-RV39-79C4-7459** | openclaw@2026.1.10 | **9.3** | CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N | Fix: OpenClaw gateway connect could skip identity checks when auth.token is present but not validated.
*   **CVE-2023-34104** | fast-xml-parser@4.5.3 | **9.3** | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N | Fix: DOCTYPE entity names in fast-xml-parser allow shadowing built-in entities via regex, enabling cross site scripting.
*   **CVE-2026-25896** | fast-xml-parser@4.5.3 | **9.3** | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N | Fix: DOCTYPE entity names in fast-xml-parser allow shadowing built-in entities via regex, enabling cross site scripting.
*   **OSV:GHSA-FHVM-J76F-QMJV** | openclaw@2026.1.10 | **9.1** | CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N | Fix: OpenClaw may accept unauthenticated Telegram webhooks without a secret, enabling spoofed updates.
*   **State:** ≤24h early warning → ≤72h incident notification → ≤1 month final report.

---

## 3. Art. 3(41) Exploitability Assessment
*   **Exploit Summary:** 41 EXPLOITABLE tier vulnerabilities; 6 unique PoC/exploit sources identified.
*   **Top Exploitables:**
    1.  **OSV:GHSA-4RJ2-GPMH-QQ5X** (openclaw): 9.4 | EPSS: N/A | 11 days public | Fix: Upgrade voice-call extension to 2026.2.2.
    2.  **OSV:GHSA-RV39-79C4-7459** (openclaw): 9.3 | EPSS: N/A | 11 days public | Fix: Identity check bypass; upgrade openclaw.
    3.  **CVE-2023-34104** (fast-xml-parser): 9.3 | EPSS: 0.00273 | 8 days public | Fix: Upgrade to 5.3.5+.
    4.  **CVE-2026-25896** (fast-xml-parser): 9.3 | EPSS: 0.00273 | 8 days public | Fix: Upgrade to 5.3.5+.
    5.  **OSV:GHSA-FHVM-J76F-QMJV** (openclaw): 9.1 | EPSS: N/A | 11 days public | Fix: Configure Telegram webhook secret.

---

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2026-25253** | clawdbot | 8.8 | AV:N (Network) | EPSS: 0.00049 | EXPLOITABLE | Fix: 1-click RCE via gatewayUrl exfiltration.
*   **CVE-2026-24763** | clawdbot | 8.8 | AV:N (Network) | EPSS: 0.00083 | EXPLOITABLE | Fix: PATH injection in Docker sandbox.
*   **OSV:GHSA-R5FQ-947M-XM57** | openclaw | 8.8 | AV:N (Network) | EPSS: N/A | VULNERABILITY | Fix: apply_patch path traversal.
*   **OSV:GHSA-JQPQ-MGVM-F9R6** | openclaw | 8.8 | AV:N (Network) | EPSS: N/A | VULNERABILITY | Fix: Command hijacking via PATH handling.
*   **CVE-2026-25128** | fast-xml-parser | 8.7 | AV:N (Network) | EPSS: 0.00027 | EXPLOITABLE | Fix: Upgrade to 5.3.4+.
*   **CVE-2025-66031** | node-forge | 8.7 | AV:N (Network) | EPSS: 0.00115 | EXPLOITABLE | Fix: ASN.1 unbounded recursion DoS.
*   **CVE-2025-12816** | node-forge | 8.7 | AV:N (Network) | EPSS: 0.00059 | EXPLOITABLE | Fix: ASN.1 validation desync.
*   **CVE-2025-15284** | qs | 8.7 | AV:N (Network) | EPSS: 0.00085 | EXPLOITABLE | Fix: arrayLimit bypass DoS.
*   *And 44 more across 13 packages.*

---

## 5. Risk Distribution & Age Risk
*   **Severity:** 5 CRITICAL, 52 HIGH, 33 MEDIUM, 6 LOW.
*   **Top Affected:** openclaw@2026.1.10 (67), clawdbot@2026.1.10 (11), hono@4.11.3 (7).
*   **Oldest Unpatched (Annex I Part II §2 Violation Risk):**
    1.  **CVE-2026-2327** (markdown-it): 238 days public | Fix: Upgrade to 14.1.1+.
    2.  **CVE-2025-66031** (node-forge): 94 days public | Fix: Upgrade node-forge.
    3.  **CVE-2025-12816** (node-forge): 94 days public | Fix: Upgrade node-forge.

---

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2:** Remediate Track 2 candidates (openclaw, fast-xml-parser) and submit notifications to ENISA/CSIRT within 24h.
2.  **Urgent — Annex I Part II §2:** Patch EXPLOITABLE HIGH/CRITICAL vulnerabilities, specifically the 1-click RCE (CVE-2026-25253) and Docker escapes (CVE-2026-24763).
3.  **Planned — Annex I Part II §2:** Address 238-day old ReDoS in markdown-it to mitigate "without delay" compliance failure.
4.  **SBOM Update — Annex I Part II §1:** Regenerate SBOM following openclaw 2026.2.15+ and fast-xml-parser 5.3.5+ upgrades.
5.  **Public Advisory — Annex I Part II §4:** Publish security advisories for openclaw-specific findings (e.g., GHSA-4RJ2-GPMH-QQ5X) once patches are deployed.
6.  **CVD Hygiene — Annex I Part II §5–6:** Ensure security contact for openclaw is reachable for coordinated disclosure of the 96 identified vulnerabilities.