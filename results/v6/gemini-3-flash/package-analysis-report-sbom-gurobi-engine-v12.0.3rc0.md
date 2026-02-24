## 1. SBOM Overview
*   **Product**: sbom-gurobi-engine-v12.0.3rc0
*   **Format**: SPDX
*   **Scan Date**: 2025-07-11
*   **Packages**: 12 total / 3 affected
*   **Unique CVEs**: 62 (3 CRITICAL, 23 HIGH, 32 MEDIUM, 3 LOW, 1 NONE)

## 2. CRA Mandatory Reporting (Article 14)
*   No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
*   **CVE-2007-4559** (python, CVSS 9.8): Directory Traversal via `tarfile` module.
*   **CVE-2025-15467** (openssl, CVSS 9.8): Stack-based Buffer Overflow in CMS AuthEnvelopedData.
*   **CVE-2024-6232** (python, CVSS 7.5): Regular-expression DoS in TarFile headers.
*   **CVE-2025-4517** (python, CVSS 9.4): Arbitrary writes via tarfile realpath overflow.
*   **CVE-2025-4138** (python, CVSS 7.5): Extraction filter bypass for symlinks.
*   **24** additional CVEs have PoC evidence (GitHub, PacketStorm, or HackerOne).

## 4. Critical & High Findings
*   **CVE-2025-9230** (openssl, CVSS 7.5, EPSS 0.00031): Out-of-bounds read in CMS decryption.
*   **CVE-2025-69419** (openssl, CVSS 7.4, EPSS 0.00056): One-byte write via malformed PKCS#12.
*   **CVE-2024-8088** (python, CVSS 8.7, EPSS 0.00154): Infinite loop in `zipfile.Path`.
*   **CVE-2024-9287** (python, CVSS 7.8, EPSS 0.00062): Command injection in `venv` scripts.
*   **CVE-2023-6597** (python, CVSS 7.8, EPSS 0.00071): Symlink dereference in `TemporaryDirectory`.
*   **CVE-2025-9086** (curl, CVSS 7.5, EPSS 0.00035): Secure cookie leakage over cleartext HTTP.
*   **CVE-2023-41105** (python, CVSS 7.5, EPSS 0.00370): Path truncation via null bytes.
*   **CVE-2024-4032** (python, CVSS 7.5, EPSS 0.01127): Incorrect IP range classification.
*   ...and **12** more across **3** packages.

## 5. Risk Distribution
*   **Severity**: 3 CRITICAL, 23 HIGH, 32 MEDIUM.
*   **Top Affected Packages**:
    1.  `python@3.11.4` (40 unique CVEs)
    2.  `openssl@3.0.16` (12 unique CVEs)
    3.  `curl@8.14.1` (10 unique CVEs)

## 6. CRA Compliance Actions
1.  **Urgent**: Patch `python` to v3.11.5+ to address CRITICAL arbitrary write (CVE-2025-4517) and HIGH risk directory traversal (CVE-2007-4559).
2.  **Urgent**: Update `openssl` to address CRITICAL stack overflow (CVE-2025-15467) per Article 10 security requirements.
3.  **Planned**: Remediate remaining HIGH severity ReDoS and injection vulnerabilities in `python` and `curl`.
4.  **Hygiene**: Implement automated vulnerability monitoring and SBOM versioning to maintain compliance with CRA Article 10(6) and Article 11.