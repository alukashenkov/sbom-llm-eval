## 1. SBOM Overview
The product **vulners-mcp** (version `sha256:1cb722...`) was scanned on 2026-02-24. The container image contains **560 total packages**, of which **20 are affected** by known vulnerabilities. Direct pre-computed analytics identify **188 unique CVEs**. The risk distribution includes **12 CRITICAL**, **76 HIGH**, **87 MEDIUM**, and **12 LOW** severity findings.

## 2. CRA Mandatory Reporting Triggers (Article 14)
The following vulnerability meets the criteria for mandatory reporting under Article 14 (actively exploited in the wild/CISA KEV):

*   **CVE-2025-48384**: Found in `git` (1:2.47.3-0+deb13u1). **CVSS: 8.0**, **EPSS: 0.00456**. This vulnerability is listed in the CISA KEV and is actively exploited.

**Compliance Deadline:** Under the CRA, the manufacturer must provide an initial notification to ENISA/CSIRT within **24 hours** of becoming aware of the exploitation, followed by a detailed report within **72 hours** and a final report within **14 days**.

## 3. Exploit Availability Assessment
There are **33 unique PoC sources** identified (13 PacketStorm, 9 GitHub, 7 HackerOne, 1 CISA KEV).

**Top 5 CVEs with Public Exploit Evidence:**
1.  **CVE-2025-15467** (openssl): CRITICAL (9.8) - PoC on GitHub/PacketStorm.
2.  **CVE-2025-48384** (git): HIGH (8.0) - CISA KEV / Active Exploitation.
3.  **CVE-2021-32804** (tar): HIGH (8.2) - PoC on GitHub.
4.  **CVE-2024-41817** (imagemagick): HIGH (7.8) - PoC on GitHub.
5.  **CVE-2025-11187** (openssl): MEDIUM (6.1) - PoC on PacketStorm.

**183 additional CVEs** have exploit evidence or associated advisories.

## 4. Critical & High Findings
Key remaining findings requiring immediate attention:
*   **CVE-2026-22770**: `imagemagick` | CVSS: 9.8 | EPSS: 0.00065
*   **CVE-2026-23876**: `imagemagick` | CVSS: 9.8 | EPSS: 0.00062
*   **CVE-2025-53014**: `imagemagick` | CVSS: 9.8 | EPSS: 0.00031
*   **CVE-2024-56171**: `libxml2` | CVSS: 9.8 | EPSS: 0.00048
*   **CVE-2024-40896**: `libxml2` | CVSS: 9.1 | EPSS: 0.00553
*   **CVE-2025-55298**: `imagemagick` | CVSS: 8.8 | EPSS: 0.00430
*   **CVE-2025-48385**: `git` | CVSS: 8.6 | EPSS: 0.00039
*   **CVE-2025-9230**: `openssl` | CVSS: 7.5 | EPSS: 0.00031

And **68 more HIGH findings** across **12 packages**.

## 5. Risk Distribution
The attack surface is heavily concentrated in five packages:
1.  **imagemagick**: 77 unique CVEs
2.  **binutils**: 32 unique CVEs
3.  **libxml2**: 17 unique CVEs
4.  **openssl**: 16 unique CVEs
5.  **curl**: 11 unique CVEs

## 6. CRA Compliance Actions
1.  **Immediate (24h):** Submit CRA Article 14 notification for **CVE-2025-48384** (`git`) and initiate emergency patch to version 2.47.3 or higher.
2.  **Urgent (72h):** Update `openssl` to resolve **CVE-2025-15467** (Critical/PoC) and `libxml2` to resolve **CVE-2024-56171**.
3.  **Urgent:** Remediate `imagemagick` (77 CVEs) by upgrading to version 7.1.2-15 or higher to clear multiple Critical/High findings.
4.  **Planned:** Update `tar` and `curl` to latest stable versions to mitigate directory traversal and WebSocket vulnerabilities.
5.  **Hygiene:** Review `binutils` usage; if not required for production runtime, remove from the container to reduce the unique CVE count by 17%.