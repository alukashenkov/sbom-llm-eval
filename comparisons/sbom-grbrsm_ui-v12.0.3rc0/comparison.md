# Source Comparison: sbom-grbrsm_ui-v12.0.3rc0

## Overview

| Metric | Value |
|--------|-------|
| Vulners CVEs | 9 |
| Grype CVEs | 8 |
| Total unique CVEs | 9 |
| Overlap | 8 (88.9%) |
| Vulners-only | 1 |
| Grype-only | 0 |

## Package Coverage

**In both sources:**
- @babel/runtime@7.0.0
- axios@1.10.0
- form-data@4.0.3
- js-yaml@4.1.0
- lodash@4.17.21
- minimatch@7.4.6
- prismjs@1.27.0

## CVEs Found in Both Sources

| CVE | Severity | Vulners CVSS | Grype CVSS | Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |
|-----|----------|-------------|------------|-------------|------------|-------------|------------|-------|
| CVE-2024-53382 | MEDIUM/MEDIUM ✅ | 4.9 | 4.9 | 0.00083 | 0.00083 | 5.4 🟡 Medium | 4.9 🟡 Medium | ✅ |
| CVE-2025-13465 | HIGH/MEDIUM ⚠️ | 7.9 | 6.5 | 0.00025 | 0.00025 | 8.4 🟠 High | 6.5 🟡 Medium | ⚠️ |
| CVE-2025-27789 | MEDIUM/MEDIUM ✅ | 6.2 | 6.2 | 0.00139 | 0.00139 | 6.7 🟡 Medium | 6.2 🟡 Medium | ✅ |
| CVE-2025-58754 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00102 | 0.00102 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2025-64718 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.0002 | 0.0002 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2025-7783 | CRITICAL/CRITICAL ✅ | 9.4 | 9.4 | 0.00177 | 0.00177 | 10.0 🔴 Critical | 9.4 🔴 Critical | ✅ |
| CVE-2026-25639 | HIGH/HIGH ✅ | 8.7 | 7.5 | 0.00033 | 0.00033 | 9.2 🔴 Critical | 7.5 🟠 High | ⚠️ |
| CVE-2026-26996 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.0004 | 0.0004 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |

## CVEs Only in Vulners

| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |
|-----|----------|------|------|---------|---------------|-----|------|
| CVE-2025-54371 | HIGH | 7.5 | 0.00177 | axios@1.10.0 | No | Yes | 9.0 🔴 Critical |

## Risk Summary

| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |
|--------|------|----------|----------|----------|------|--------|-----|
| Vulners | 9 | 8.0 | 10.0 | 1 | 5 | 3 | 0 |
| Grype | 8 | 7.0 | 9.4 | 1 | 3 | 4 | 0 |
