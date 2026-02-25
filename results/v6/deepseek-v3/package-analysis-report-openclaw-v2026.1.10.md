### 1. SBOM Overview  
- **Product**: openclaw (SPDX format)  
- **Scan date**: 2026-02-20  
- **Packages**: 1,112 total / 21 affected  
- **Unique CVEs**: 96 (CRITICAL: 5, HIGH: 52, MEDIUM: 33, LOW: 6)  

### 2. CRA Mandatory Reporting (Article 14)  
- **No CRA Article 14 mandatory reporting triggers** (no wildExploited or CISA KEV entries).  

### 3. Exploit Assessment  
- **6 CVEs** have PoC evidence (GitHub exploits). Top exploited:  
  - `CVE-2026-25253` (clawdbot, CVSS 8.8, EPSS 0.00049) - 1-Click RCE via gatewayUrl token exfiltration  
  - `CVE-2026-24763` (clawdbot, CVSS 8.8, EPSS 0.00083) - Docker command injection via PATH  
  - `CVE-2026-25157` (clawdbot, CVSS 7.7, EPSS 0.00006) - SSH remote command injection  
  - `CVE-2026-22610` (@angular/core, CVSS 8.5, EPSS 0.00014) - XSS via SVG script attributes  
  - `CVE-2025-65945` (jws, CVSS 7.5, EPSS 0.00009) - HMAC signature verification bypass  

### 4. Critical & High Findings  
- `CVE-2026-25593` (openclaw, CVSS 8.4, EPSS 0.00023) - Unauthenticated RCE via WebSocket  
- `CVE-2026-26322` (openclaw, CVSS 7.6, EPSS 0.00013) - Unrestricted gatewayUrl override  
- `CVE-2026-26324` (openclaw, CVSS 7.5, EPSS 0.00011) - SSRF bypass via IPv6  
- `CVE-2026-26321` (openclaw, CVSS 7.5, EPSS 0.00060) - Local file disclosure in Feishu extension  
- `CVE-2026-26325` (openclaw, CVSS 7.2, EPSS 0.00024) - Command mismatch bypass  
- **And 47 more HIGH/Critical CVEs** across 21 packages.  

### 5. Risk Distribution  
- **Severity**: CRITICAL (5), HIGH (52), MEDIUM (33), LOW (6)  
- **Top affected packages**:  
  1. `openclaw@2026.1.10` (67 CVEs)  
  2. `clawdbot@2026.1.10` (11 CVEs)  
  3. `hono@4.11.3` (7 CVEs)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch clawdbot (`CVE-2026-25253`, `CVE-2026-24763`) per Article 11(3).  
2. **Urgent**: Update openclaw to fix CRITICAL auth bypasses (e.g., `CVE-2026-25593`).  
3. **Planned**: Address HIGH-severity SSRF/LFI in openclaw extensions.  
4. **Hygiene**: Maintain SBOM per Article 10(6) for transitive dependencies.  
5. **Monitor**: Track EPSS >0.1% for emerging exploit trends.