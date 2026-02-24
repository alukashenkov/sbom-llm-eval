## 1. SBOM Overview
The scan of **sbom-gurobi-engine-v12.0.3rc0** (SPDX format, 2025-07-11) identified **62 unique CVEs** across 3 affected packages out of 12 total. The vulnerability landscape is significant, consisting of **3 CRITICAL**, **23 HIGH**, **32 MEDIUM**, and **3 LOW** severity findings. The primary exposure stems from the inclusion of an outdated Python runtime and core networking libraries.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified. No vulnerabilities in this set are currently listed in the CISA KEV or confirmed as actively exploited in the wild.

## 3. Exploit Availability Assessment
Public exploit code is available for a substantial portion of the identified vulnerabilities. According to `pocSummary`, there are 8 GitHub exploits, 10 PacketStorm entries, and 6 HackerOne reports.

**Top 5 CVEs with PoC Evidence:**
1. **CVE-2025-15467** (CRITICAL, CVSS 9.8): Stack-based buffer overflow in OpenSSL.
2. **CVE-2025-4517** (CRITICAL, CVSS 9.4): Arbitrary writes via tarfile overflow in Python.
3. **CVE-2007-4559** (CRITICAL, CVSS 9.8): Directory traversal in Python tarfile module.
4. **CVE-2024-6232** (HIGH, CVSS 7.5): ReDoS in Python TarFile header parsing.
5. **CVE-2025-4138** (HIGH, CVSS 7.5): Python extraction filter bypass for symlinks.

*57 additional CVEs have exploit evidence or technical documentation.*

## 4. Critical & High Findings
The following high-impact vulnerabilities require immediate attention:
- **CVE-2024-8088** | python@3.11.4 | CVSS 8.7 | EPSS 0.00154 (Infinite loop in zipfile)
- **CVE-2024-9287** | python@3.11.4 | CVSS 7.8 | EPSS 0.00062 (Venv command injection)
- **CVE-2023-6597** | python@3.11.4 | CVSS 7.8 | EPSS 0.00071 (TempDir symlink dereference)
- **CVE-2025-9230** | openssl@3.0.16 | CVSS 7.5 | EPSS 0.00031 (OOB read/write in CMS)
- **CVE-2025-9086** | curl@8.14.1 | CVSS 7.5 | EPSS 0.00035 (Secure cookie leak)
- **CVE-2023-41105** | python@3.11.4 | CVSS 7.5 | EPSS 0.00370 (Path truncation)
- **CVE-2024-4032** | python@3.11.4 | CVSS 7.5 | EPSS 0.01127 (IP address misclassification)
- **CVE-2023-5363** | openssl@3.0.16 | CVSS 7.5 | EPSS 0.04390 (Cipher key length bypass)

And **15 more HIGH findings** across 3 packages.

## 5. Risk Distribution
The risk is heavily concentrated in **python@3.11.4** (40 unique CVEs), followed by **openssl@3.0.16** (12 CVEs) and **curl@8.14.1** (10 CVEs). The distribution is skewed toward High and Medium risks, primarily affecting file handling and cryptographic operations.

## 6. CRA Compliance Actions
1. **Immediate:** Patch **OpenSSL** to v3.0.17+ to remediate the CRITICAL stack buffer overflow (CVE-2025-15467).
2. **Urgent:** Upgrade **Python** to v3.11.11+ or v3.12+ to address CRITICAL tarfile vulnerabilities and multiple HIGH-severity ReDoS/Injection flaws.
3. **Urgent:** Update **curl** to v8.12.0+ to resolve cookie handling and protocol redirect vulnerabilities.
4. **Planned:** Review all internal usage of `tarfile` and `zipfile` modules to ensure "filter" arguments are explicitly set to 'data' or 'tar' as per new security defaults.
5. **Hygiene:** Implement automated SBOM generation in the CI/CD pipeline to ensure real-time compliance with CRA Article 10 requirements.