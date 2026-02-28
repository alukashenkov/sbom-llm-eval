## 1. SBOM Overview
*   **Product:** la-vulners-mcp (sha256:571bf2600c309bc636c6a4b4af23f08b15eb5f3ad184d540126647d0ed1e8aaf)
*   **Format:** CycloneDX | **Scan Date:** 2026-02-24
*   **Packages:** 97 total / 3 affected
*   **Unique CVEs:** 7
*   **CRA Tier Breakdown (Art. 3):** 0 ACTIVELY_EXPLOITED / 3 EXPLOITABLE / 4 VULNERABILITY

---

## 2. CRA Art. 14 — Mandatory Reporting

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2)):**
*   No Art. 14(1) triggers — no actively exploited vulnerabilities detected.

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**
*   **CVE-2023-45853** | zlib@1.3.1-r2 | CVSS: 9.8 | Vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | Fix: Upgrade to zlib 1.3.1 or higher.
*   **CVE-2026-22184** | zlib@1.3.1-r2 | CVSS: 9.8 | Vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | Fix: Upgrade to zlib 1.3.1.2 or higher.
*   **State:** Notify via ENISA Single Reporting Platform to designated CSIRT + ENISA simultaneously: ≤24h early warning → ≤72h incident notification → ≤1 month final report.

---

## 3. Art. 3(41) Exploitability Assessment
*   **Total EXPLOITABLE CVEs:** 3
*   **CVE-2023-45853** | zlib@1.3.1-r2 | CVSS: 9.8 | EPSS: 1.40% (80th percentile) | Age: 868 days | Fix: Upgrade to zlib 1.3.1 or higher.
*   **CVE-2026-22184** | zlib@1.3.1-r2 | CVSS: 9.8 | EPSS: 0.04% (12th percentile) | Age: 52 days | Fix: Upgrade to zlib 1.3.1.2.
*   **CVE-2025-60876** | busybox@1.37.0-r30 | CVSS: 6.5 | EPSS: 0.05% (16th percentile) | Age: 110 days | Fix: BusyBox wget 1.3.7 accepts CR/LF; monitor for patches.

---

## 4. Critical & High Findings (Annex I Part II §2)
*   **CVE-2025-26519** | musl@1.2.5-r21 | CVSS: 8.1 | Vector: Local/High Complexity/System-wide Impact | EPSS: 0.02% | Tier: VULNERABILITY | Fix: Upgrade to musl 1.2.6 or higher.

---

## 5. Risk Distribution & Age Risk
*   **Severity Distribution:** CRITICAL: 2, HIGH: 1, MEDIUM: 2, LOW: 2.
*   **Top Affected Packages:** zlib@1.3.1-r2 (3), busybox@1.37.0-r30 (3), musl@1.2.5-r21 (1).
*   **Age Risk (Annex I Part II §2 Violation Signals):**
    1.  **CVE-2023-45853** (CRITICAL): 868 days public. Fix: Upgrade zlib to 1.3.1+.
    2.  **CVE-2025-26519** (HIGH): 379 days public. Fix: Upgrade musl to 1.2.6+.
    3.  **CVE-2026-22184** (CRITICAL): 52 days public. Fix: Upgrade zlib to 1.3.1.2+.

---

## 6. CRA Defensible-Practice Actions
1.  **Immediate — Art. 14 + Annex I Part II §2**: Submit Art. 14(3) notifications for CVE-2023-45853 and CVE-2026-22184 within 24 hours.
2.  **Urgent — Annex I Part II §2**: Remediate zlib vulnerabilities by upgrading to version 1.3.1.2 to address multiple CRITICAL overflows.
3.  **Urgent — Annex I Part II §2**: Patch musl libc (CVE-2025-26519) by upgrading to 1.2.6+ to resolve out-of-bounds write risks.
4.  **SBOM Update — Annex I Part II §1**: Regenerate machine-readable SBOM (CycloneDX/SPDX) following component upgrades to reflect the secure state.
5.  **Public Advisory — Annex I Part II §4**: Publish security advisories for the PDE detailing the zlib and musl remediation steps and CVSS vectors.
6.  **CVD Hygiene — Annex I Part II §5–6**: Ensure the security contact point is reachable for reporting future vulnerabilities in the `la-vulners-mcp` product.