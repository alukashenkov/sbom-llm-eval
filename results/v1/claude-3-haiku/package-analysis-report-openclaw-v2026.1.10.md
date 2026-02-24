## SBOM Overview
The SBOM is for the `openclaw` product, in SPDX format, created on 2026-02-20. It contains a total of 1112 packages, with 21 affected packages and 125 total advisories.

The vulnerability severity distribution is:
- CRITICAL: 1 
- HIGH: 12
- MEDIUM: 9
- LOW: 3

## CRA Mandatory Reporting Triggers (Article 14)
The following vulnerabilities require ENISA/CSIRT notification:

[CVE-2026-25593] openclaw@2026.1.10 — CVSS 8.4 — EPSS 0.00023 — Unauthenticated Local RCE via WebSocket config.apply
[CVE-2026-26316] openclaw@2026.1.10 — CVSS 7.5 — EPSS 0.00061 — BlueBubbles webhook auth bypass via loopback proxy trust

No other CRA mandatory reporting triggers were identified.

## Exploit Availability Assessment
The following CVEs have public exploit evidence:

Public PoC available:
- [CVE-2026-25253] openclaw@2026.1.10 — 1-Click RCE via Authentication Token Exfiltration From gatewayUrl
- [CVE-2026-24763] clawdbot@2026.1.10 — Authenticated Command Injection via PATH Environment Variable
- [CVE-2026-25157] clawdbot@2026.1.10 — OS Command Injection via Project Root Path in sshNodeCommand

## Critical & High Findings
The remaining CRITICAL and HIGH CVEs are:

[CVE-2026-25475] openclaw@2026.1.10 — CVSS 6.5 — EPSS 0.00093 — Local File Inclusion via MEDIA: Path Extraction
[CVE-2026-25474] openclaw@2026.1.10 — CVSS 7.5 — EPSS 0.00015 — Telegram webhook request forgery (missing `channels.telegram.webhookSecret`) → auth bypass
[CVE-2026-26325] clawdbot@2026.1.10 — CVSS 7.2 — EPSS 0.00018 — Node host system.run rawCommand/command mismatch can bypass allowlist/approvals
[CVE-2026-26321] clawdbot@2026.1.10 — CVSS 7.5 — EPSS 0.0006 — Local file disclosure via sendMediaFeishu in Feishu extension
[CVE-2026-26323] clawdbot@2026.1.10 — CVSS 8.6 — EPSS 0.00175 — Command injection in maintainer clawtributors updater

## Risk Distribution
In total, there are 21 affected packages with 125 advisories.

The top 3 most-affected packages are:
1. openclaw (19 advisories)
2. clawdbot (9 advisories) 
3. hono (6 advisories)

The exploitation landscape shows:
- 5 CVEs with public PoC/exploit evidence
- 2 CVEs with exploit framework integration
- 0 CVEs with bug bounty disclosure

## CRA Compliance Actions
1. (Immediate) Patch CVE-2026-25593, CVE-2026-26316 to address CRA mandatory reporting triggers.
2. (Urgent) Patch CVE-2026-25253, CVE-2026-24763, CVE-2026-25157 to address publicly disclosed exploits.
3. (Planned) Patch remaining CRITICAL/HIGH CVEs: CVE-2026-25475, CVE-2026-25474, CVE-2026-26325, CVE-2026-26321, CVE-2026-26323.
4. (SBOM hygiene) Review and update SBOM metadata to ensure accuracy and completeness.
5. (SBOM hygiene) Implement automated SBOM generation and vulnerability scanning in the build/release process.