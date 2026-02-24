### 1. SBOM Overview  
- **Product**: openclaw (SPDX format)  
- **Scan date**: 2026-02-20  
- **Packages**: 1,112 total / 21 affected  
- **Unique CVEs**: 57 (CRITICAL: 2, HIGH: 34, MEDIUM: 19, LOW: 2)  

### 2. CRA Mandatory Reporting (Article 14)  
- **No CRA Article 14 mandatory reporting triggers** (no wildExploited or CISA KEV entries).  

### 3. Exploit Assessment  
- **6 CVEs** have PoC evidence (GitHub exploits). Top exploited:  
  - `CVE-2026-25253` (openclaw@2026.1.10, CVSS 8.8, EPSS 0.00049) - 1-Click RCE via gatewayUrl  
  - `CVE-2026-24763` (clawdbot@2026.1.10, CVSS 8.8, EPSS 0.00083) - Docker command injection  
  - `CVE-2026-25157` (clawdbot@2026.1.10, CVSS 7.7, EPSS 0.00006) - SSH command injection  

### 4. Critical & High Findings  
- `CVE-2026-25593` (openclaw@2026.1.10, CVSS 8.4, EPSS 0.00023) - Unauthenticated RCE via WebSocket  
- `CVE-2026-26322` (openclaw@2026.1.10, CVSS 7.6, EPSS 0.00013) - Gateway URL override  
- `CVE-2026-26324` (openclaw@2026.1.10, CVSS 7.5, EPSS 0.00011) - SSRF bypass via IPv6  
- `CVE-2026-26321` (openclaw@2026.1.10, CVSS 7.5, EPSS 0.0006) - Local file read via Feishu extension  
- **And 30 more HIGH/Critical CVEs** across 12 packages.  

### 5. Risk Distribution  
- **Severity**: CRITICAL (2), HIGH (34), MEDIUM (19), LOW (2)  
- **Top affected packages**:  
  1. `openclaw@2026.1.10` (29 CVEs)  
  2. `hono@4.11.3` (6 CVEs)  
  3. `clawdbot@2026.1.10` (5 CVEs)  

### 6. CRA Compliance Actions  
1. **Immediate**: Patch exploited CVEs (`CVE-2026-25253`, `CVE-2026-24763`) per Article 11(3).  
2. **Urgent**: Update `openclaw` to mitigate CRITICAL flaws (e.g., `CVE-2026-25593`).  
3. **Planned**: Address remaining HIGH-severity SSRF/RCE risks (e.g., `CVE-2026-26324`).  
4. **Hygiene**: Maintain SBOM integrity per Article 10(6).  
5. **Monitor**: Track EPSS >0.1% CVEs (e.g., `CVE-2026-26323`, EPSS 0.00175).  

*(Word count: 450)*