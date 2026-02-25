# CRA-Aligned Vulnerability Summary

## 1. SBOM Overview
- **Product**: sbom-grbrsm_ui-v12.0.3rc0 (SPDX format)
- **Scan date**: 2025-07-11
- **Packages**: 338 total / 7 affected
- **Unique CVEs**: 9 (1 CRITICAL, 5 HIGH, 3 MEDIUM)

## 2. CRA Mandatory Reporting (Article 14)
No CRA Article 14 mandatory reporting triggers (no wildExploited or CISA KEV entries).

## 3. Exploit Assessment
- **CVE-2025-7783** (form-data@4.0.3, CVSS 9.4 CRITICAL, EPSS 0.00177) - GitHub PoC
- **CVE-2025-54371** (axios@1.10.0, CVSS 7.5 HIGH, EPSS N/A) - GitHub PoC  
1 additional CVE has PoC evidence.

## 4. Critical & High Findings
- **CVE-2026-25639** (axios@1.10.0, CVSS 8.7 HIGH, EPSS 0.00033)
- **CVE-2025-58754** (axios@1.10.0, CVSS 7.5 HIGH, EPSS 0.00102)
- **CVE-2025-13465** (lodash@4.17.21, CVSS 8.2 HIGH, EPSS 0.00025)
- **CVE-2026-26996** (minimatch@7.4.6, CVSS 8.7 HIGH, EPSS 0.0004)  
and 1 more across 4 packages.

## 5. Risk Distribution
- **Severity**: 1 CRITICAL, 5 HIGH, 3 MEDIUM
- **Top packages**: 
  - axios@1.10.0 (4 CVEs)
  - js-yaml@4.1.0 (1 CVE)
  - lodash@4.17.21 (1 CVE)

## 6. CRA Compliance Actions
1. **Immediate**: Patch form-data@4.0.3 (CVE-2025-7783) - Critical exploit
2. **Urgent**: Update axios@1.10.0 (CVE-2025-54371, CVE-2026-25639) - Exploited/High risk
3. **Planned**: Address lodash@4.17.21 (CVE-2025-13465) - High severity
4. **Hygiene**: Maintain SBOM per CRA Article 10(6) with quarterly reviews