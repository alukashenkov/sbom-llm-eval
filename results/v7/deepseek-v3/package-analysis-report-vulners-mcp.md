## 1. SBOM Overview  
**Product:** vulners-mcp (container)  
**Format:** CycloneDX  
**Scan date:** 2026-02-24  
**Packages:** 560 total / 20 affected  
**Unique CVEs:** 188  
**CRA tiers:**  
- ACTIVELY_EXPLOITED: 1  
- EXPLOITABLE: 90  
- VULNERABILITY: 97  

---

## 2. CRA Art. 14 — Mandatory Reporting  

**Track 1 — Actively Exploited (Art. 14(1)–(2)):**  
- **CVE-2025-48384** (git@1:2.47.3-0+deb13u1):  
  CVSS 8.0 (AV:N/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H)  
  EPSS 0.00456 (63rd percentile), 235 days public  
  Fix: "Git vulnerability leads to incorrect submodule paths and potential script execution risks."  
  **Action:** Notify ENISA Single Reporting Platform ≤24h early warning → ≤72h vulnerability notification → ≤14 days final report.  

**Track 2 — Severe Incidents (Art. 14(3)–(5)):**  
12 CVEs qualify (CVSS≥9 + AV:N + CIA:H), including:  
- **CVE-2026-22770** (ImageMagick): CVSS 9.8 heap overflow in BilateralBlur  
- **CVE-2025-15467** (OpenSSL): CVSS 9.8 stack overflow in CMS AuthEnvelopedData  
  **Action:** ≤24h early warning → ≤72h incident notification → ≤1 month final report.  

---

## 3. Art. 3(41) Exploitability Assessment  
**POC sources:** 32 total (GitHub:9, PacketStorm:13, HackerOne:7)  
Top 5 EXPLOITABLE CVEs:  
1. **CVE-2026-22770** (ImageMagick): CVSS 9.8, EPSS 0.00065  
2. **CVE-2025-15467** (OpenSSL): CVSS 9.8, EPSS 0.00672  
3. **CVE-2025-48384** (git): CVSS 8.0, EPSS 0.00456 (actively exploited)  
4. **CVE-2024-56171** (libxml2): CVSS 9.8, EPSS 0.00048  
5. **CVE-2025-53014** (ImageMagick): CVSS 9.8, EPSS 0.00031  
**Note:** 15 CVEs have stale EPSS scores (>90 days old).  

---

## 4. Critical & High Findings (Annex I Part II §2)  
Remaining critical/high CVEs:  
- **CVE-2025-57807** (ImageMagick): CVSS 9.8 heap write via SeekBlob  
- **CVE-2025-53101** (ImageMagick): CVSS 9.8 stack buffer overflow  
- **CVE-2024-40896** (libxml2): CVSS 9.1 XXE via SAX parser  
- **CVE-2025-49794** (libxml2): CVSS 9.1 expired pointer dereference  
*(+4 more across 3 packages)*  

---

## 5. Risk Distribution & Age Risk  
**Severity:** CRITICAL:14, HIGH:82, MEDIUM:79  
**Top affected packages:**  
1. imagemagick (77 CVEs)  
2. binutils (32 CVEs)  
3. libxml2 (17 CVEs)  
**Oldest unpatched critical/high CVEs:**  
1. **CVE-2015-8895** (ImageMagick): 3271 days (integer overflow)  
2. **CVE-2014-9852** (ImageMagick): 3266 days (use-after-free)  
3. **CVE-2014-9846** (ImageMagick): 3266 days (buffer overflow)  

---

## 6. CRA Defensible-Practice Actions  
1. **Immediate (Art. 14 + Annex I §2):** Patch CVE-2025-48384 (git) and 12 Track 2 CVEs.  
2. **Urgent (Annex I §2):** Upgrade ImageMagick to ≥7.1.2-15 (fixes 77 CVEs).  
3. **Planned (Annex I §2):** Address 79 MEDIUM CVEs, prioritizing oldest first.  
4. **SBOM update (Annex I §1):** Refresh CycloneDX SBOM post-remediation.  
5. **Public advisory (Annex I §4):** Publish patched versions for ImageMagick/libxml2.  
6. **CVD hygiene (Annex I §5–6):** Verify disclosure policy for git/openssl.  

*(Word count: 499)*