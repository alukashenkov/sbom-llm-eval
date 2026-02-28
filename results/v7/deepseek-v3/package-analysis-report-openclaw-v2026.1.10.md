## 1. SBOM Overview  
- **Product**: openclaw (SPDX format)  
- **Scan date**: 2026-02-20  
- **Packages**: 1,112 total / 21 affected  
- **Unique CVEs**: 96  
- **CRA Tiers**:  
  - EXPLOITABLE: 41  
  - VULNERABILITY: 55  

---

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited Vulnerabilities (Art. 14(1)–(2))**:  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

**Track 2 — Severe Incidents (Art. 14(3)–(5))**:  
- **OSV:GHSA-4RJ2-GPMH-QQ5X** (CVSS 9.4, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L`): OpenClaw voice-call extension bypasses inbound allowlist; fixed in 2026.2.2.  
- **OSV:GHSA-RV39-79C4-7459** (CVSS 9.3, `AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N`): OpenClaw gateway connect skips identity checks; fixed in 2026.2.2.  
- **CVE-2023-34104** (CVSS 9.3, `AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:N`): fast-xml-parser regex injection; upgrade to 5.3.4+.  
- **OSV:GHSA-FHVM-J76F-QMJV** (CVSS 9.1, `AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/SC:N/VI:H/SI:N/VA:N/SA:N`): OpenClaw Telegram webhook spoofing; fixed in 2026.2.2.  

**Action**: Submit ENISA reports ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

---

## 3. Art. 3(41) Exploitability Assessment  
- **Exploitable CVEs**: 41 (6 GitHub PoCs)  
- Top EXPLOITABLE CVEs:  
  - **OSV:GHSA-4RJ2-GPMH-QQ5X** (CVSS 9.4): OpenClaw voice-call bypass.  
  - **OSV:GHSA-RV39-79C4-7459** (CVSS 9.3): Gateway identity check bypass.  
  - **CVE-2023-34104** (CVSS 9.3, EPSS 0.00273): fast-xml-parser XSS.  
  - **OSV:GHSA-FHVM-J76F-QMJV** (CVSS 9.1): Telegram webhook spoofing.  
  - **OSV:GHSA-X22M-J5QQ-J49M** (CVSS 8.6): OpenClaw Feishu SSRF; fixed in 2026.2.14.  

---

## 4. Critical & High Findings (Annex I Part II §2)  
- **OSV:GHSA-G55J-C2V4-PJCG** (CVSS 8.4, `AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`): OpenClaw WebSocket RCE; upgrade to 2026.2.2.  
- **OSV:GHSA-R5FQ-947M-XM57** (CVSS 8.8): OpenClaw path traversal in `apply_patch`.  
- **OSV:GHSA-JQPQ-MGVM-F9R6** (CVSS 8.8): OpenClaw command hijacking via PATH.  
- **And 53 more HIGH/Critical across 21 packages**.  

---

## 5. Risk Distribution & Age Risk  
- **Severity**: CRITICAL (5), HIGH (52), MEDIUM (33), LOW (6)  
- **Top affected packages**:  
  1. openclaw@2026.1.10 (67 CVEs)  
  2. clawdbot@2026.1.10 (11 CVEs)  
  3. hono@4.11.3 (7 CVEs)  
- **Oldest unpatched**:  
  - **CVE-2026-2327** (238 days): markdown-it ReDoS; upgrade to 14.1.1.  
  - **CVE-2025-66031** (94 days): node-forge ASN.1 DoS; upgrade to 1.3.2.  

---

## 6. CRA Defensible-Practice Actions  
1. **Immediate**: Patch Track 2 CVEs (Art. 14). Upgrade OpenClaw to 2026.2.2+.  
2. **Urgent**: Fix EXPLOITABLE CRITICAL/HIGH CVEs (Annex I Part II §2).  
3. **Planned**: Remediate remaining HIGH/MEDIUM by `daysPublic` (oldest first).  
4. **SBOM update**: Refresh SPDX/CycloneDX SBOM post-remediation.  
5. **Public advisory**: Publish fixes for CVE-2023-34104, CVE-2026-2327.  
6. **CVD hygiene**: Verify disclosure policy and security contacts (Annex I Part II §5–6).  

**Word count**: 499/500