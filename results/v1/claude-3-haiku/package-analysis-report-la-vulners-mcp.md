## 1. SBOM Overview

The SBOM is in CycloneDX format, created on 2026-02-24T14:40:52.000Z. It covers the "la-vulners-mcp" container with version "sha256:571bf2600c309bc636c6a4b4af23f08b15eb5f3ad184d540126647d0ed1e8aaf".

The SBOM contains a total of 97 packages, with 3 affected packages and 13 total advisories.

The vulnerability severity breakdown is as follows:
- CRITICAL: 4 vulnerabilities
- HIGH: 2 vulnerabilities
- MEDIUM: 3 vulnerabilities
- LOW: 4 vulnerabilities

## 2. CRA Mandatory Reporting Triggers (Article 14)

No CRA mandatory reporting triggers identified. There are no vulnerabilities with wildExploited=true or a CISA KEV present.

## 3. Exploit Availability Assessment

The following CVEs have public proof-of-concept (PoC) or exploit evidence available:

Public PoC available:
- [CVE-2026-22184] zlib@1.3.1.2 — CVSS 9.8 — EPSS 0.00042 — Global buffer overflow in untgz utility

Exploit framework integration:
- [CVE-2025-60876] busybox@1.37.0 — CVSS 6.5 — EPSS 0.00052 — Accepted raw CR/LF and other control bytes in HTTP request-target

## 4. Critical & High Findings

Critical Vulnerabilities:
- [CVE-2023-45853] zlib@1.3.1-r2 — CVSS 9.8 — EPSS 0.01396 — Integer Overflow or Wraparound in MiniZip
- [CVE-2026-22184] zlib@1.3.1.2 — CVSS 9.8 — EPSS 0.00042 — Global buffer overflow in untgz utility

High Vulnerabilities:
- [CVE-2025-26519] musl@1.2.5-r21 — CVSS 8.1 — EPSS 0.00022 — Out-of-bounds write vulnerability in iconv conversion

## 5. Risk Distribution

Severity Counts:
- CRITICAL: 4
- HIGH: 2
- MEDIUM: 3
- LOW: 4

Top 3 Most-Affected Packages:
1. zlib (5 vulnerabilities)
2. busybox (4 vulnerabilities)
3. musl (2 vulnerabilities)

Exploitation Landscape:
- Public PoC available for 1 vulnerability
- Exploit framework integration for 1 vulnerability
- No bug bounty disclosures identified

## 6. CRA Compliance Actions

1. (Immediate) Patch CVE-2023-45853 and CVE-2026-22184 in zlib 1.3.1-r2 and 1.3.1.2, respectively, as they are critical vulnerabilities with high EPSS scores.
2. (Urgent) Patch CVE-2025-26519 in musl 1.2.5-r21, as it is a high-severity vulnerability.
3. (Planned) Investigate and patch CVE-2025-60876 in busybox 1.37.0, as it has a public exploit available.
4. (Planned) Investigate and patch CVE-2025-46394 and CVE-2024-58251 in busybox 1.37.0, as they are low-severity vulnerabilities.
5. (SBOM Hygiene) Ensure the SBOM is kept up-to-date and reviewed regularly for new vulnerabilities.