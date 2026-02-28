## 1. SBOM Overview  
- **Product**: sbom-grbrsm_ui-v12.0.3rc0 (SPDX)  
- **Scan date**: 2025-07-11  
- **Packages**: 338 total / 7 affected  
- **Unique CVEs**: 9  
- **CRA tiers**:  
  - EXPLOITABLE: 7 (Art. 3(41))  
  - VULNERABILITY: 2 (Art. 3(42))  

---  

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited (Art. 14(1)–(2))**:  
- No Art. 14(1) triggers — no actively exploited vulnerabilities detected.  

**Track 2 — Severe Incidents (Art. 14(3)–(5))**:  
- **CVE-2025-7783** (CRITICAL, CVSS 9.4, `AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/SC:H/VI:H/SI:H`):  
  - Affects: axios@1.10.0, form-data@4.0.3  
  - Fix: "Critical vulnerability in axios form-data allowing predictable boundary values for attacks."  
  - **Action**: ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

---  

## 3. Art. 3(41) Exploitability Assessment  
- **Exploitable CVEs**: 7 (2 with PoC via GitHub)  
- Top 5 EXPLOITABLE CVEs:  
  1. **CVE-2026-25639** (HIGH, CVSS 8.7, axios@1.10.0): Prototype pollution via `mergeConfig`.  
     - Fix: "Prototype pollution in axios via mergeConfig allows __proto__ to crash or cause code execution."  
  2. **CVE-2025-58754** (HIGH, CVSS 7.5, axios@1.10.0): DoS via unconstrained `data:` URI decoding.  
     - Fix: "Axios on Node decodes data: URIs into memory, ignoring size limits."  
  3. **CVE-2025-13465** (HIGH, CVSS 7.9, lodash@4.17.21): Prototype pollution in `_.unset`/`_.omit`.  
     - Fix: "Upgrade to lodash 4.17.23."  
  4. **CVE-2026-26996** (HIGH, CVSS 8.7, minimatch@7.4.6): ReDoS via wildcard patterns.  
     - Fix: "Minimatch ReDoS: patch catastrophic backtracking."  
  5. **CVE-2025-54371** (HIGH, CVSS 7.5, axios@1.10.0): Withdrawn advisory (transitive form-data issue).  

---  

## 4. Critical & High Findings (Annex I Part II §2)  
- **CVE-2025-7783** (CRITICAL, CVSS 9.4): form-data boundary prediction (axios/form-data).  
- **CVE-2025-13465** (HIGH, CVSS 7.9): Lodash prototype pollution.  
- **And 3 more HIGH** across axios and minimatch.  

---  

## 5. Risk Distribution & Age Risk  
- **Severity**: CRITICAL (1), HIGH (5), MEDIUM (3).  
- **Top affected**: axios@1.10.0 (4 CVEs), js-yaml@4.1.0 (1), lodash@4.17.21 (1).  
- **Oldest unpatched**:  
  1. **CVE-2025-7783** (222 days, CRITICAL): form-data boundary issue.  
  2. **CVE-2025-54371** (220 days, HIGH): axios form-data transitive flaw.  
  3. **CVE-2025-58754** (170 days, HIGH): axios DoS via `data:` URIs.  

---  

## 6. CRA Defensible-Practice Actions  
1. **Immediate (Art. 14 + Annex I §2)**: Patch CVE-2025-7783 (Track 2) and notify ENISA/CSIRT.  
2. **Urgent (Annex I §2)**: Upgrade axios (CVE-2026-25639, CVE-2025-58754), lodash (CVE-2025-13465).  
3. **Planned (Annex I §2)**: Address remaining HIGH/MEDIUM CVEs (e.g., minimatch ReDoS).  
4. **SBOM update (Annex I §1)**: Refresh SBOM with patched versions.  
5. **Public advisory (Annex I §4)**: Publish fixes for exploitable CVEs.  
6. **CVD hygiene (Annex I §5–6)**: Verify disclosure policy and security contacts.  

---  
*Word count: 499*