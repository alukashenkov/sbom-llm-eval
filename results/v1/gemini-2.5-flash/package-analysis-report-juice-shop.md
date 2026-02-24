## Vulnerability Summary for bkimminich/juice-shop

**Scan Date:** 2026-02-24T14:44:13.000Z
**Product Name:** bkimminich/juice-shop (CycloneDX container)
**Total Packages:** 998
**Affected Packages:** 38
**Total Advisories:** 82

**Vulnerability Counts by Severity:**
*   **CRITICAL:** 5
*   **HIGH:** 24
*   **MEDIUM:** 12
*   **LOW:** 1
*   **NONE:** 1

---

## 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers identified.

---

## 3. Exploit Availability Assessment

**Public PoC available:**
*   CVE-2026-23745 (tar@4.4.19, tar@6.2.1, tar@7.5.2) - Arbitrary File Overwrite and Symlink Poisoning
*   CVE-2023-37466 (vm2@3.9.17) - Sandbox Escape vulnerability
*   CVE-2023-37903 (vm2@3.9.17) - Sandbox Escape vulnerability
*   CVE-2022-24785 (moment@2.0.0) - Path Traversal
*   CVE-2025-65945 (jws@0.2.6) - Improperly Verifies HMAC Signature

**Bug bounty disclosed:**
*   CVE-2018-3721 (lodash@2.4.2) - Prototype Pollution
*   CVE-2018-16487 (lodash@2.4.2) - Prototype Pollution
*   CVE-2020-8203 (lodash.set@4.3.2) - Prototype Pollution

---

## 4. Critical & High Findings

*   **CRITICAL:** CVE-2015-9235 jsonwebtoken@0.1.0, jsonwebtoken@0.4.0 - CVSS: 9.8, EPSS: 0.3247 - Verification Bypass
*   **CRITICAL:** CVE-2023-32314 vm2@3.9.17 - CVSS: 9.8, EPSS: 0.69875 - Sandbox Escape vulnerability
*   **CRITICAL:** CVE-2023-37466 vm2@3.9.17 - CVSS: 9.8, EPSS: 0.04997 - Sandbox Escape vulnerability
*   **CRITICAL:** CVE-2023-37903 vm2@3.9.17 - CVSS: 9.8, EPSS: 0.39234 - Sandbox Escape vulnerability
*   **CRITICAL:** CVE-2026-22709 vm2@3.9.17 - CVSS: 9.8, EPSS: 0.0003 - Sandbox Escape
*   **CRITICAL:** CVE-2019-10744 lodash@2.4.2 - CVSS: 9.1, EPSS: 0.02441 - Prototype Pollution
*   **CRITICAL:** CVE-2023-46233 crypto-js@3.3.0 - CVSS: 9.1, EPSS: 0.00823 - PBKDF2 1,000 times weaker than specified
*   **HIGH:** CVE-2022-25887 sanitize-html@1.4.2 - CVSS: 7.5, EPSS: 0.00447 - Regular Expression Denial of Service (ReDoS)
*   **HIGH:** CVE-2022-23529 jsonwebtoken@0.1.0, jsonwebtoken@0.4.0 - CVSS: 7.6, EPSS: 0.00044 - Insecure input validation in jwt.verify function
*   **HIGH:** CVE-2022-23539 jsonwebtoken@0.1.0, jsonwebtoken@0.4.0 - CVSS: 8.1, EPSS: 0.00072 - Unrestricted key type could lead to legacy keys usage
*   **HIGH:** CVE-2026-23950 tar@4.4.19, tar@6.2.1, tar@7.5.2 - CVSS: 8.8, EPSS: 0.00006 - Race Condition in node-tar Path Reservations
*   **HIGH:** CVE-2026-24842 tar@4.4.19, tar@6.2.1, tar@7.5.2 - CVSS: 8.2, EPSS: 0.00012 - Arbitrary File Creation/Overwrite via Hardlink Path Traversal
*   **HIGH:** CVE-2026-26960 tar@4.4.19, tar@6.2.1, tar@7.5.2 - CVSS: 7.1, EPSS: 0.00013 - Arbitrary File Read/Write via Hardlink Target Escape
*   **HIGH:** CVE-2021-23337 lodash@2.4.2 - CVSS: 7.2, EPSS: 0.00741 - Command Injection
*   **HIGH:** CVE-2016-4055 moment@2.0.0 - CVSS: 7.8, EPSS: 0.04049 - Regular Expression Denial of Service
*   **HIGH:** CVE-2017-18214 moment@2.0.0 - CVSS: 7.5, EPSS: 0.00311 - Regular Expression Denial of Service
*   **HIGH:** CVE-2025-47935 multer@1.4.5-lts.2 - CVSS: 7.5, EPSS: 0.00048 - Denial of Service via memory leaks
*   **HIGH:** CVE-2025-47944 multer@1.4.5-lts.2 - CVSS: 7.5, EPSS: 0.00011 - Denial of Service from maliciously crafted requests
*   **HIGH:** CVE-2025-48997 multer@1.4.5-lts.2 - CVSS: 8.7, EPSS: 0.00081 - Denial of Service via unhandled exception
*   **HIGH:** CVE-2025-7338 multer@1.4.5-lts.2 - CVSS: 7.5, EPSS: 0.00012 - Denial of Service via unhandled exception
*   **HIGH:** CVE-2025-15284 qs@6.14.0 - CVSS: 8.7, EPSS: 0.00085 - arrayLimit bypass allows DoS
*   **HIGH:** CVE-2026-2391 qs@6.14.0 - CVSS: 6.3, EPSS: 0.00019 - Allocation of Resources Without Limits or Throttling
*   **HIGH:** CVE-2026-24001 diff@4.0.2 - CVSS: 7.5, EPSS: 0.0002 - Regular Expression Denial of Service (ReDoS)
*   **HIGH:** CVE-2016-1000223 jws@0.2.6 - CVSS: 8.7, EPSS: N/A - Forgeable Public/Private Tokens
*   **HIGH:** CVE-2025-13465 lodash@4.17.21 - CVSS: 8.2, EPSS: 0.00025 - Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions
*   **HIGH:** CVE-2026-26996 minimatch@5.1.6, minimatch@9.0.5, minimatch@3.0.5, minimatch@3.0.8, minimatch@3.1.2 - CVSS: 8.7, EPSS: 0.0004 - ReDoS via repeated wildcards
*   **HIGH:** CVE-2024-4068 braces@2.3.2 - CVSS: 7.5, EPSS: 0.00225 - Uncontrolled resource consumption
*   **HIGH:** CVE-2022-25881 http-cache-semantics@3.8.1 - CVSS: 7.5, EPSS: 0.00196 - Regular Expression Denial of Service
*   **HIGH:** CVE-2023-42282 ip@2.0.1 - CVSS: 8.1, EPSS: 0.00539 - SSRF improper categorization in isPublic
*   **HIGH:** CVE-2024-29415 ip@2.0.1 - CVSS: 8.1, EPSS: 0.86505 - SSRF improper categorization in isPublic
*   **HIGH:** CVE-2020-15084 express-jwt@0.1.3 - CVSS: 7.7, EPSS: 0.00222 - Authorization bypass
*   **HIGH:** CVE-2024-38355 socket.io@3.1.2 - CVSS: 7.3, EPSS: 0.00136 - Unhandled 'error' event
*   **HIGH:** CVE-2023-32695 socket.io-parser@4.0.5 - CVSS: 7.3, EPSS: 0.00203 - Insufficient validation when decoding a Socket.IO packet
*   **HIGH:** CVE-2024-37890 ws@7.4.6 - CVSS: 8.7, EPSS: 0.00541 - DoS when handling a request with many HTTP headers

---

## 5. Risk Distribution

**Severity Counts:**
*   CRITICAL: 5
*   HIGH: 24
*   MEDIUM: 12
*   LOW: 1
*   NONE: 1

**Top 3 Most-Affected Packages:**
1.  **sanitize-html:** 7 advisories (1 HIGH, 6 MEDIUM)
2.  **jsonwebtoken:** 5 advisories (1 CRITICAL, 3 HIGH, 1 MEDIUM)
3.  **tar:** 5 advisories (4 HIGH, 1 MEDIUM)

**Exploitation Landscape Stats:**
*   CVEs with Public PoC: 5
*   CVEs with Bug Bounty Disclosed: 3
*   CVEs with EPSS > 0.9: 2 (CVE-2023-32314, CVE-2024-29415)

---

## 6. CRA Compliance Actions

1.  **Immediate Action: Address Critical Sandbox Escapes in `vm2` (CVE-2023-32314, CVE-2023-37466, CVE-2023-37903, CVE-2026-22709).** These vulnerabilities allow for remote code execution and are highly exploitable. Update `vm2` to a patched version immediately. This directly impacts the security of processing of data, as per CRA Article 10(1)(a).
2.  **Urgent Action: Remediate Critical JWT Verification Bypass in `jsonwebtoken` (CVE-2015-9235).** This vulnerability allows attackers to bypass authentication. Update `jsonwebtoken` to a version that enforces strong algorithm validation. This is crucial for maintaining confidentiality and integrity of data, as per CRA Article 10(1)(a) and (b).
3.  **Urgent Action: Patch `crypto-js` for Weak PBKDF2 Implementation (CVE-2023-46233).** The significantly weaker PBKDF2 implementation compromises cryptographic strength. Update `crypto-js` to a version with a stronger implementation to ensure data confidentiality and integrity, aligning with CRA Article 10(1)(b).
4.  **Planned Action: Address High Severity Denial of Service (DoS) vulnerabilities.** Multiple packages (`sanitize-html`, `multer`, `qs`, `diff`, `ws`, `minimatch`, `braces`, `http-cache-semantics`) are susceptible to DoS attacks. Prioritize updates for these components to ensure availability of the product, as per CRA Article 10(1)(c).
5.  **Ongoing Action: Maintain and Update SBOM for `bkimminich/juice-shop`.** Regularly scan and update the Software Bill of Materials to ensure accurate and up-to-date information on all components and their vulnerabilities. This is a foundational requirement for demonstrating compliance with CRA Article 13(1) and facilitating proactive vulnerability management.