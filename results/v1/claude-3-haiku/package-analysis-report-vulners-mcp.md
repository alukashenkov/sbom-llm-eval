## 1. SBOM Overview

The provided SBOM is for the product "vulners-mcp" with the format "CycloneDX" and was scanned on 2026-02-24T14:35:34.000Z. The SBOM contains a total of 560 packages, with 20 affected packages and 369 total advisories.

The vulnerability severity breakdown is as follows:
- Critical: 1 vulnerability
- High: 9 vulnerabilities 
- Medium: 10 vulnerabilities
- Low: 0 vulnerabilities

## 2. CRA Mandatory Reporting Triggers (Article 14)

The following vulnerabilities require ENISA/CSIRT notification per the EU Cyber Resilience Act (CRA):

[CVE-2025-15467] openssl@3.5.4-1~deb13u2 — CVSS 9.8, EPSS 0.00672 — Critical vulnerability that may lead to a crash, causing denial of service.

## 3. Exploit Availability Assessment

The following CVEs have public proof-of-concept (PoC) or exploit evidence available:

Public PoC available:
- [CVE-2025-15467] openssl@3.5.4-1~deb13u2 — PoC on GitHub and Packetstorm

Exploit framework integration:
- [CVE-2025-11187] openssl@3.5.4-1~deb13u2 — PoC on Packetstorm

## 4. Critical & High Findings

The remaining critical and high vulnerabilities are:

[CVE-2025-9230] openssl@3.5.4-1~deb13u2 — CVSS 7.5, EPSS 0.00031 — Out-of-bounds read/write vulnerability
[CVE-2025-9231] openssl@3.5.4-1~deb13u2 — CVSS 6.5, EPSS 0.00019 — Timing side-channel vulnerability
[CVE-2025-9232] openssl@3.5.4-1~deb13u2 — CVSS 5.9, EPSS 0.00039 — Out-of-bounds read vulnerability
[CVE-2025-69419] openssl@3.5.4-1~deb13u2 — CVSS 7.4, EPSS 0.00056 — One-byte write vulnerability
[CVE-2025-69420] openssl@3.5.4-1~deb13u2 — CVSS 7.5, EPSS 0.0007 — Type confusion vulnerability
[CVE-2025-69421] openssl@3.5.4-1~deb13u2 — CVSS 7.5, EPSS 0.00059 — NULL pointer dereference vulnerability

## 5. Risk Distribution

In total, there are 20 affected packages with 369 total advisories.

The top 3 most-affected packages are:
1. openssl (15 advisories)
2. imagemagick (12 advisories)
3. binutils (13 advisories)

The exploitation landscape shows that 1 vulnerability (CVE-2025-15467) has public proof-of-concept (PoC) or exploit evidence available, and 1 vulnerability (CVE-2025-11187) has exploit framework integration.

## 6. CRA Compliance Actions

Priority-ordered CRA compliance actions:

1. (Immediate) Patch CVE-2025-15467 in openssl@3.5.4-1~deb13u2 as it is a critical vulnerability with public exploit evidence.
2. (Urgent) Patch the remaining high-severity vulnerabilities in openssl (CVE-2025-9230, CVE-2025-9231, CVE-2025-9232, CVE-2025-69419, CVE-2025-69420, CVE-2025-69421).
3. (Planned) Review and patch the medium-severity vulnerabilities across the affected packages.
4. (SBOM hygiene) Regularly update the SBOM to ensure it accurately reflects the current software composition and vulnerability status.
5. (SBOM hygiene) Implement a vulnerability management process to continuously monitor for new advisories and proactively patch affected components.