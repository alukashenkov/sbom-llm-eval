## SBOM Overview
The SBOM is in SPDX format, created on 2025-07-11T08:53:07.000Z, and named "sbom-gurobi-engine-v12.0.3rc0". It contains a total of 12 packages, with 3 affected packages and 154 total advisories.

The vulnerability severity breakdown is:
- CRITICAL: 1
- HIGH: 10 
- MEDIUM: 7

## CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## Exploit Availability Assessment
The following CVEs have public PoC or exploit evidence:
- Public PoC available: 
  - [CVE-2024-12718] (githubexploit)
- Exploit framework integration:
  - [CVE-2025-4138] (packetstorm)
  - [CVE-2025-4330] (githubexploit)
  - [CVE-2025-4517] (githubexploit)
- Bug bounty disclosed:
  - [CVE-2025-14524] (hackerone)
  - [CVE-2025-10148] (hackerone)
  - [CVE-2025-10966] (hackerone)
  - [CVE-2025-9086] (hackerone)

## Critical & High Findings
- [CVE-2023-41105] python@3.11.4 - CVSS 7.5, EPSS 0.0037 - Fix available
- [CVE-2025-4517] python - CVSS 9.4, EPSS 0.00071 - Fix available
- [CVE-2025-15467] openssl@3.0.16 - CVSS 9.8, EPSS 0.00672 - Fix available
- [CVE-2025-9230] openssl@3.0.16 - CVSS 7.5, EPSS 0.00031 - Fix available

## Risk Distribution
- CRITICAL: 1
- HIGH: 10
- MEDIUM: 7
- LOW: 0

Top 3 most-affected packages:
1. python (12 advisories)
2. openssl (8 advisories) 
3. curl (10 advisories)

Exploitation landscape:
- Public PoC available: 1
- Exploit framework integration: 3
- Bug bounty disclosed: 7

## CRA Compliance Actions
1. (Immediate) Patch CVE-2025-4517 (CRITICAL, EPSS 0.00071) in python.
2. (Urgent) Patch CVE-2025-15467 (CRITICAL, EPSS 0.00672) in openssl.
3. (Planned) Patch CVE-2023-41105 (HIGH, EPSS 0.0037) in python.
4. (Planned) Patch CVE-2025-9230 (HIGH, EPSS 0.00031) in openssl.
5. (SBOM hygiene) Review and update SBOM metadata, including package versions and vulnerability data.