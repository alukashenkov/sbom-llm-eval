### 1. SBOM Overview  
**Product Name:** sbom-gurobi-engine-v12.0.3rc0  
**Format:** SPDX  
**Scan Date:** 2025-07-11  
**Total Packages:** 12  
**Affected Packages:** 3  
**Total Advisories:** 154  

**Vulnerability Distribution by Severity:**  
- **CRITICAL:** 2  
- **HIGH:** 35  
- **MEDIUM:** 117  
- **LOW:** 0  

---

### 2. CRA Mandatory Reporting Triggers (Article 14)  
**No CRA mandatory reporting triggers identified.**  
No vulnerabilities have `wildExploited=true` or `cisa_kev` present.  

---

### 3. Exploit Availability Assessment  
**Public PoC available (githubexploit/exploitdb):**  
- **CVE-2025-4517** (CRITICAL)  
- **CVE-2024-6232** (HIGH)  
- **CVE-2025-4138** (HIGH)  
- **CVE-2025-4330** (HIGH)  
- **CVE-2025-4435** (HIGH)  
- **CVE-2025-4516** (MEDIUM)  
- **CVE-2025-4517** (CRITICAL)  
- **CVE-2025-15366** (MEDIUM)  
- **CVE-2025-15367** (MEDIUM)  
- **CVE-2024-6232** (HIGH)  
- **CVE-2025-4517** (CRITICAL)  

**Exploit Framework Integration (nuclei/packetstorm):**  
- **CVE-2025-4138** (HIGH)  
- **CVE-2025-4330** (HIGH)  
- **CVE-2025-4435** (HIGH)  
- **CVE-2025-4517** (CRITICAL)  

**Bug Bounty Disclosed (hackerone):**  
- **CVE-2025-14524** (MEDIUM)  
- **CVE-2025-15079** (MEDIUM)  
- **CVE-2025-15224** (LOW)  
- **CVE-2025-10966** (MEDIUM)  
- **CVE-2025-14819** (MEDIUM)  
- **CVE-2025-14017** (MEDIUM)  
- **CVE-2025-9086** (HIGH)  
- **CVE-2025-10148** (MEDIUM)  

---

### 4. Critical & High Findings  
- **CVE-2025-4517** (CRITICAL) – Python: Arbitrary writes via tarfile realpath overflow  
- **CVE-2025-15467** (CRITICAL) – OpenSSL: Stack-based buffer overflow in CMS AuthEnvelopedData  
- **CVE-2025-41105** (HIGH) – Python: Untrusted search path vulnerability  
- **CVE-2023-36632** (HIGH) – Python: RecursionError in email.utils.parseaddr  
- **CVE-2025-4516** (MEDIUM) – Python: Use-after-free in "unicode_escape" decoder  
- **CVE-2025-4517** (CRITICAL) – Python: Tarfile extraction filter bypass  
- **CVE-2025-15467** (CRITICAL) – OpenSSL: Stack-based buffer overflow in CMS AuthEnvelopedData  
- **CVE-2025-4138** (HIGH) – Python: Extraction filter bypass for symlinks  
- **CVE-2025-4330** (HIGH) – Python: Extraction filter bypass for symlinks  
- **CVE-2025-4435** (HIGH) – Python: Tarfile extraction filter bypass  

---

### 5. Risk Distribution  
**Severity Counts:**  
- **CRITICAL:** 2  
- **HIGH:** 35  
- **MEDIUM:** 117  

**Top 3 Most-Affected Packages:**  
1. **python (3.11.4)** – 115 advisories  
2. **openssl (3.0.16)** – 16 advisories  
3. **curl (8.14.1)** – 10 advisories  

**Exploitation Landscape:**  
- 13 advisories have public exploit evidence (githubexploit/exploitdb)  
- 6 advisories have exploit framework integration (nuclei/packetstorm)  
- 8 advisories disclosed via bug bounty (hackerone)  

---

### 6. CRA Compliance Actions  
1. **Immediate:** Address **CVE-2025-4517** (CRITICAL) – Arbitrary writes via tarfile.  
2. **Urgent:** Address **CVE-2025-15467** (CRITICAL) – OpenSSL stack overflow.  
3. **Planned:** Address **CVE-2025-41105** (HIGH) – Untrusted search path.  
4. **Planned:** Address **CVE-2025-4516** (MEDIUM) – Use-after-free in "unicode_escape" decoder.  
5. **SBOM Hygiene:** Ensure all advisories are tracked and remediated in future SBOMs.