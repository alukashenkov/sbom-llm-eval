# Vulnerability Summary Report  
**EU Cyber Resilience Act (CRA) Compliance Assessment**  

## 1. SBOM Overview  
- **Product**: `vulners-mcp` (container image)  
- **Format**: CycloneDX  
- **Scan Date**: 2026-02-24  
- **Packages**: 560 total, 20 affected  
- **Vulnerabilities**: 369 advisories  
  - **Critical**: 5  
  - **High**: 18  
  - **Medium**: 326  
  - **Low**: 20  

---

## 2. CRA Mandatory Reporting Triggers (Article 14)  
**Exploited-in-the-Wild or CISA KEV Vulnerabilities**  
- **[CVE-2025-48384]** `git@1:2.47.3-0+deb13u1` — CVSS 8.0 (EPSS 0.45%)  
  - Actively exploited (CISA KEV listed). Arbitrary code execution via malformed Git config.  
  - **CRA Action**: Notify ENISA/CSIRT within 24h (initial) → 72h (detailed) → 14d (final).  

*No other mandatory reporting triggers identified.*  

---

## 3. Exploit Availability Assessment  
**Public Proof-of-Concepts**  
- **GitHub/ExploitDB**:  
  - `CVE-2025-48384` (Git): 9 PoCs (e.g., arbitrary config execution)  
  - `CVE-2025-15467` (OpenSSL): Stack overflow via CMS parsing (2 PoCs)  
- **PacketStorm**:  
  - 12 OpenSSL CVEs (e.g., `CVE-2025-69420` - Type Confusion)  

**Bug Bounty Disclosures**:  
- `CVE-2025-14524` (cURL): OAuth2 token leakage via redirect (HackerOne)  

---

## 4. Critical & High Findings  
- **[CVE-2025-15467]** `openssl@3.5.4` — CVSS 9.8 (EPSS 0.67%)  
  - Stack buffer overflow in CMS parsing. Fix: Upgrade to 3.5.5.  
- **[CVE-2026-22770]** `imagemagick@8:7.1.1.43` — CVSS 9.8  
  - Heap overflow in BilateralBlurImage. No fix in current version.  
- **[CVE-2025-48385]** `git@1:2.47.3` — CVSS 8.6  
  - Arbitrary file write via bundle-uri injection.  

---

## 5. Risk Distribution  
- **Severity**: Critical (5), High (18), Medium (326), Low (20)  
- **Top Affected Packages**:  
  1. OpenSSL (12 CVEs, 1 Critical)  
  2. ImageMagick (9 CVEs, 2 Critical)  
  3. Git (3 CVEs, 1 actively exploited)  
- **Exploit Stats**: 15 CVEs with public PoCs, 1 wild exploitation.  

---

## 6. CRA Compliance Actions  
1. **Immediate**: Patch `git` (CVE-2025-48384) — CISA KEV-listed exploit.  
2. **Urgent**: Upgrade OpenSSL to address critical CMS parsing flaws.  
3. **Planned**: Replace ImageMagick with patched version (v7.1.2-15+).  
4. **SBOM Hygiene**: Consolidate duplicate advisories (e.g., OpenSSL CVEs).  
5. **Monitoring**: Track EPSS >0.5% for emerging threats (e.g., `CVE-2025-15467`).  

**Word Count**: 598