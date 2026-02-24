## 1. SBOM Overview
This report summarizes the security posture of **openclaw**, analyzed via an SPDX SBOM on 2026-02-20. Out of **1,112 total packages**, **21 are affected** by a total of **57 unique CVEs**. The risk profile is significant, with **2 CRITICAL** and **34 HIGH** severity vulnerabilities identified. The remaining findings include 19 Medium and 2 Low severity issues.

## 2. CRA Mandatory Reporting Triggers (Article 14)
No CRA mandatory reporting triggers identified.

## 3. Exploit Availability Assessment
There are **6 unique CVEs** with publicly available Proof-of-Concept (PoC) exploits. The following high-risk vulnerabilities have active PoC evidence:

1.  **CVE-2026-25253** (CVSS 8.8): `clawdbot` - 1-Click RCE via token exfiltration.
2.  **CVE-2026-24763** (CVSS 8.8): `clawdbot` - Authenticated Command Injection via PATH.
3.  **CVE-2026-25157** (CVSS 7.7): `clawdbot` - OS Command Injection in SSH handling.
4.  **CVE-2026-22610** (CVSS 8.5): `@angular/core` - XSS via SVG attributes.
5.  **CVE-2025-65945** (CVSS 7.5): `jws` - Improper HMAC Signature verification.

**1 additional CVE** (`ajv`) has exploit evidence available via GitHub.

## 4. Critical & High Findings
The following critical and high-severity findings require immediate attention:

*   **GHSA-4RJ2-GPMH-QQ5X** (CVSS 9.4): `openclaw` - Critical auth bypass in voice-call extension.
*   **GHSA-RV39-79C4-7459** (CVSS 9.3): `openclaw` - Critical identity check skip in Gateway.
*   **CVE-2026-25896** (CVSS 9.3): `fast-xml-parser` - Critical regex injection/bypass.
*   **GHSA-FHVM-J76F-QMJV** (CVSS 9.1): `openclaw` - Critical Telegram webhook auth bypass.
*   **CVE-2026-25593** (CVSS 8.4): `openclaw` - Unauthenticated Local RCE via WebSocket.
*   **CVE-2026-22818** (CVSS 8.2): `hono` - JWT algorithm confusion leading to forgery.
*   **CVE-2025-13465** (CVSS 8.2): `lodash` - Prototype Pollution in `unset`/`omit`.
*   **CVE-2025-66031** (CVSS 8.7): `node-forge` - Unbounded recursion DoS.

And **24 more HIGH findings** across **8 packages**.

## 5. Risk Distribution
The vulnerability density is heavily concentrated in the core product:
*   **openclaw@2026.1.10**: 29 unique CVEs (Primary Risk Driver)
*   **hono@4.11.3**: 6 unique CVEs
*   **clawdbot@2026.1.10**: 5 unique CVEs
*   **fast-xml-parser@4.5.3**: 4 unique CVEs
*   **node-forge@1.3.1**: 3 unique CVEs

## 6. CRA Compliance Actions
1.  **Immediate**: Patch `openclaw` and `clawdbot` to version 2026.2.15 or later to resolve critical authentication bypasses and RCE vulnerabilities.
2.  **Urgent**: Update `fast-xml-parser` to >= 4.5.4 to mitigate the CVSS 9.3 regex injection.
3.  **Urgent**: Update `hono` to >= 4.11.4 to address JWT algorithm confusion and authentication forgery risks.
4.  **Planned**: Upgrade `lodash` to >= 4.17.23 and `node-forge` to >= 1.3.2 to resolve high-severity prototype pollution and DoS.
5.  **Hygiene**: Review optional extensions (MS Teams, Feishu, Voice-call) and disable any not in active use to reduce the attack surface.