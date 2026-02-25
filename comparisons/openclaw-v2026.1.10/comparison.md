# Source Comparison: openclaw-v2026.1.10

## Overview

| Metric | Value |
|--------|-------|
| Vulners CVEs | 96 |
| Grype CVEs | 93 |
| Total unique CVEs | 96 |
| Overlap | 93 (96.9%) |
| Vulners-only | 3 |
| Grype-only | 0 |

## Package Coverage

**In both sources:**
- @angular/compiler@21.0.3
- @angular/core@21.0.3
- @isaacs/brace-expansion@5.0.0
- ajv@8.17.1
- axios@1.13.2
- clawdbot@2026.1.10
- diff@8.0.2
- fast-xml-parser@4.5.3
- hono@4.11.3
- jws@3.2.2
- jws@4.0.0
- lodash@4.17.21
- markdown-it@14.1.0
- minimatch@10.1.1
- minimatch@9.0.5
- node-forge@1.3.1
- openclaw@2026.1.10
- qs@6.13.0
- qs@6.14.0
- qs@6.14.1

**Vulners only:**
- express@4.21.2

## CVEs Found in Both Sources

| CVE | Severity | Vulners CVSS | Grype CVSS | Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |
|-----|----------|-------------|------------|-------------|------------|-------------|------------|-------|
| CVE-2025-12816 | HIGH/HIGH ✅ | 8.7 | 8.6 | 0.00059 | 0.00059 | 9.2 🔴 Critical | 8.6 🟠 High | ⚠️ |
| CVE-2025-13465 | HIGH/MEDIUM ⚠️ | 7.9 | 6.5 | 0.00025 | 0.00025 | 8.4 🟠 High | 6.5 🟡 Medium | ⚠️ |
| CVE-2025-15284 | HIGH/HIGH ✅ | 8.7 | 7.5 | 0.00085 | 0.00085 | 9.2 🔴 Critical | 7.5 🟠 High | ⚠️ |
| CVE-2025-65945 | HIGH/HIGH ✅ | 7.5 | 7.5 | 9e-05 | 9e-05 | 9.0 🔴 Critical | 7.5 🟠 High | ✅ |
| CVE-2025-66030 | MEDIUM/MEDIUM ✅ | 6.3 | 6.3 | 0.00042 | 0.00042 | 6.8 🟡 Medium | 6.3 🟡 Medium | ✅ |
| CVE-2025-66031 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.00115 | 0.00115 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| CVE-2025-69873 | HIGH/MEDIUM ⚠️ | 8.2 | 5.5 | 0.00069 | 0.00069 | 9.7 🔴 Critical | 5.5 🟡 Medium | ⚠️ |
| CVE-2026-22610 | HIGH/HIGH ✅ | 8.5 | 8.5 | 0.00014 | 0.00014 | 10.0 🔴 Critical | 8.5 🟠 High | ✅ |
| CVE-2026-22817 | HIGH/HIGH ✅ | 8.2 | 8.2 | 0.00017 | 0.00017 | 8.7 🟠 High | 8.2 🟠 High | ✅ |
| CVE-2026-22818 | HIGH/HIGH ✅ | 8.2 | 8.2 | 0.00017 | 0.00017 | 8.7 🟠 High | 8.2 🟠 High | ✅ |
| CVE-2026-2327 | HIGH/MEDIUM ⚠️ | 7.5 | 5.3 | 0.00018 | 0.00018 | 8.0 🟠 High | 5.3 🟡 Medium | ⚠️ |
| CVE-2026-2391 | HIGH/LOW ⚠️ | 7.5 | 3.7 | 0.00085 | 0.00019 | 8.0 🟠 High | 3.7 🟢 Low | ⚠️ |
| CVE-2026-24001 | HIGH/LOW ⚠️ | 7.5 | 2.7 | 0.0002 | 0.0002 | 8.0 🟠 High | 2.7 🟢 Low | ⚠️ |
| CVE-2026-24398 | MEDIUM/MEDIUM ✅ | 4.8 | 4.8 | 0.00012 | 0.00012 | 5.3 🟡 Medium | 4.8 🟡 Medium | ✅ |
| CVE-2026-24472 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00013 | 0.00013 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2026-24473 | MEDIUM/MEDIUM ✅ | 6.3 | 5.3 | 0.00013 | 0.00013 | 6.8 🟡 Medium | 5.3 🟡 Medium | ⚠️ |
| CVE-2026-24763 | HIGH/HIGH ✅ | 8.8 | 8.8 | 0.00083 | 0.00083 | 10.0 🔴 Critical | 8.8 🟠 High | ✅ |
| CVE-2026-24764 | LOW/LOW ✅ | 3.7 | 3.7 | 0.00029 | 0.00029 | 4.2 🟡 Medium | 3.7 🟢 Low | ✅ |
| CVE-2026-24771 | MEDIUM/MEDIUM ✅ | 4.7 | 4.7 | 0.00041 | 0.00041 | 5.2 🟡 Medium | 4.7 🟡 Medium | ✅ |
| CVE-2026-25157 | HIGH/HIGH ✅ | 7.7 | 7.7 | 6e-05 | 6e-05 | 9.2 🔴 Critical | 7.7 🟠 High | ✅ |
| CVE-2026-25253 | HIGH/HIGH ✅ | 8.8 | 8.8 | 0.00049 | 0.00049 | 10.0 🔴 Critical | 8.8 🟠 High | ✅ |
| CVE-2026-25474 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00015 | 0.00015 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-25475 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.00093 | 0.00093 | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| CVE-2026-25547 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.00018 | 0.00018 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| CVE-2026-25593 | HIGH/HIGH ✅ | 8.4 | 8.4 | 0.00023 | 0.00023 | 8.9 🟠 High | 8.4 🟠 High | ✅ |
| CVE-2026-25639 | HIGH/HIGH ✅ | 8.7 | 7.5 | 0.00033 | 0.00033 | 9.2 🔴 Critical | 7.5 🟠 High | ⚠️ |
| CVE-2026-25896 | CRITICAL/CRITICAL ✅ | 9.3 | 9.3 | 0.00273 | 0.00029 | 9.8 🔴 Critical | 9.3 🔴 Critical | ✅ |
| CVE-2026-26278 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00049 | 0.00049 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-26316 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00061 | 0.00061 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-26317 | HIGH/HIGH ✅ | 7.1 | 7.1 | 0.00014 | 0.00014 | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| CVE-2026-26319 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00031 | 0.00031 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-26321 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.0006 | 0.0006 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-26322 | HIGH/HIGH ✅ | 7.6 | 7.6 | 0.00013 | 0.00013 | 8.1 🟠 High | 7.6 🟠 High | ✅ |
| CVE-2026-26323 | HIGH/HIGH ✅ | 8.6 | 8.6 | 0.00175 | 0.00175 | 9.1 🔴 Critical | 8.6 🟠 High | ✅ |
| CVE-2026-26324 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00011 | 0.00011 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-26325 | HIGH/HIGH ✅ | 7.2 | 7.2 | 0.00024 | 0.00024 | 7.7 🟠 High | 7.2 🟠 High | ✅ |
| CVE-2026-26326 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 9e-05 | 9e-05 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2026-26327 | HIGH/HIGH ✅ | 7.1 | 7.1 | 4e-05 | 4e-05 | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| CVE-2026-26328 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.00025 | 0.00025 | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| CVE-2026-26329 | HIGH/HIGH ✅ | 7.1 | 7.1 | 0.0004 | 0.0004 | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| CVE-2026-26996 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.0004 | 0.0004 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| CVE-2026-27001 | HIGH/HIGH ✅ | 8.6 | 8.6 | 0.00018 | 0.00018 | 9.1 🔴 Critical | 8.6 🟠 High | ✅ |
| CVE-2026-27002 | HIGH/HIGH ✅ | 7.7 | 7.7 | 0.00045 | 0.00045 | 8.2 🟠 High | 7.7 🟠 High | ✅ |
| CVE-2026-27003 | MEDIUM/MEDIUM ✅ | 6.9 | 6.9 | 0.00013 | 0.00013 | 7.4 🟠 High | 6.9 🟡 Medium | ✅ |
| CVE-2026-27004 | MEDIUM/MEDIUM ✅ | 6.9 | 6.9 | 6e-05 | 6e-05 | 7.4 🟠 High | 6.9 🟡 Medium | ✅ |
| CVE-2026-27007 | MEDIUM/MEDIUM ✅ | 4.8 | 4.8 | 0.00011 | 0.00011 | 5.3 🟡 Medium | 4.8 🟡 Medium | ✅ |
| CVE-2026-27008 | MEDIUM/MEDIUM ✅ | 6.8 | 6.8 | 0.00014 | 0.00014 | 7.3 🟠 High | 6.8 🟡 Medium | ✅ |
| CVE-2026-27009 | MEDIUM/MEDIUM ✅ | 5.8 | 5.8 | 0.0002 | 0.0002 | 6.3 🟡 Medium | 5.8 🟡 Medium | ✅ |
| CVE-2026-27484 | LOW/LOW ✅ | 2.3 | 2.3 | 0.00022 | 0.00022 | 2.8 🟢 Low | 2.3 🟢 Low | ✅ |
| CVE-2026-27485 | MEDIUM/MEDIUM ✅ | 4.6 | 4.6 | 5e-05 | 5e-05 | 5.1 🟡 Medium | 4.6 🟡 Medium | ✅ |
| CVE-2026-27486 | MEDIUM/MEDIUM ✅ | 4.3 | 4.3 | 0.00013 | 0.00013 | 4.8 🟡 Medium | 4.3 🟡 Medium | ✅ |
| CVE-2026-27487 | HIGH/HIGH ✅ | 7.6 | 7.6 | 0.00051 | 0.00051 | 8.1 🟠 High | 7.6 🟠 High | ✅ |
| CVE-2026-27488 | MEDIUM/MEDIUM ✅ | 6.9 | 6.9 | 0.00012 | 0.00012 | 7.4 🟠 High | 6.9 🟡 Medium | ✅ |
| CVE-2026-27576 | MEDIUM/MEDIUM ✅ | 4.8 | 4.8 | 5e-05 | 5e-05 | 5.3 🟡 Medium | 4.8 🟡 Medium | ✅ |
| GHSA-3HCM-GGVF-RCH5 | HIGH/HIGH ✅ | 7.4 | 7.4 | — | — | 7.9 🟠 High | 7.4 🟠 High | ✅ |
| GHSA-4685-C5CP-VP95 | LOW/LOW ✅ | 3.6 | 3.6 | — | — | 4.1 🟡 Medium | 3.6 🟢 Low | ✅ |
| GHSA-4RJ2-GPMH-QQ5X | CRITICAL/CRITICAL ✅ | 9.4 | 9.4 | — | — | 9.9 🔴 Critical | 9.4 🔴 Critical | ✅ |
| GHSA-56F2-HVWG-5743 | HIGH/HIGH ✅ | 7.6 | 7.6 | — | — | 8.1 🟠 High | 7.6 🟠 High | ✅ |
| GHSA-5XFQ-5MR7-426Q | MEDIUM/MEDIUM ✅ | 5.5 | 5.5 | — | — | 6.0 🟡 Medium | 5.5 🟡 Medium | ✅ |
| GHSA-64QX-VPXX-MVQF | HIGH/HIGH ✅ | 7.1 | 7.1 | — | — | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| GHSA-6C9J-X93C-RW6J | MEDIUM/MEDIUM ✅ | 4.3 | 4.3 | — | — | 4.8 🟡 Medium | 4.3 🟡 Medium | ✅ |
| GHSA-7RCP-MXPQ-72PJ | MEDIUM/MEDIUM ✅ | 5.1 | 5.1 | — | — | 5.6 🟡 Medium | 5.1 🟡 Medium | ✅ |
| GHSA-7VWX-582J-J332 | HIGH/HIGH ✅ | 7.4 | 7.4 | — | — | 7.9 🟠 High | 7.4 🟠 High | ✅ |
| GHSA-C37P-4QQG-3P76 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | — | — | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| GHSA-CHM2-M3W2-WCXM | LOW/LOW ✅ | 2.1 | 2.1 | — | — | 2.6 🟢 Low | 2.1 🟢 Low | ✅ |
| GHSA-FH3F-Q9QW-93J9 | MEDIUM/MEDIUM ✅ | 5.4 | 5.4 | — | — | 5.9 🟡 Medium | 5.4 🟡 Medium | ✅ |
| GHSA-FHVM-J76F-QMJV | CRITICAL/CRITICAL ✅ | 9.1 | 9.1 | — | — | 9.6 🔴 Critical | 9.1 🔴 Critical | ✅ |
| GHSA-G27F-9QJV-22PM | LOW/LOW ✅ | 3.1 | 3.1 | — | — | 3.6 🟢 Low | 3.1 🟢 Low | ✅ |
| GHSA-GQ3J-XVXP-8HRF | LOW/LOW ✅ | 3.7 | 3.7 | — | — | 4.2 🟡 Medium | 3.7 🟢 Low | ✅ |
| GHSA-GQ9C-WG68-GWJ2 | HIGH/HIGH ✅ | 7.5 | 7.5 | — | — | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| GHSA-H89V-J3X9-8WQJ | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | — | — | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| GHSA-HV93-R4J3-Q65F | HIGH/HIGH ✅ | 7.1 | 7.1 | — | — | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| GHSA-J27P-HQ53-9WGC | HIGH/HIGH ✅ | 7.5 | 7.5 | — | — | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| GHSA-JQPQ-MGVM-F9R6 | HIGH/HIGH ✅ | 8.8 | 8.8 | — | — | 9.3 🔴 Critical | 8.8 🟠 High | ✅ |
| GHSA-MJ5R-HH7J-4GXF | MEDIUM/MEDIUM ✅ | 5.9 | 5.9 | — | — | 6.4 🟡 Medium | 5.9 🟡 Medium | ✅ |
| GHSA-MQPW-46FH-299H | HIGH/HIGH ✅ | 7.2 | 7.2 | — | — | 7.7 🟠 High | 7.2 🟠 High | ✅ |
| GHSA-MV9J-6XHH-G383 | MEDIUM/MEDIUM ✅ | 6.3 | 6.3 | — | — | 6.8 🟡 Medium | 6.3 🟡 Medium | ✅ |
| GHSA-P536-VVPP-9MC8 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | — | — | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| GHSA-PG2V-8XWH-QHCC | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | — | — | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| GHSA-Q447-RJ3R-2CGH | HIGH/HIGH ✅ | 7.5 | 7.5 | — | — | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| GHSA-QJ77-C3C8-9C3Q | HIGH/HIGH ✅ | 7.4 | 7.4 | — | — | 7.9 🟠 High | 7.4 🟠 High | ✅ |
| GHSA-R5FQ-947M-XM57 | HIGH/HIGH ✅ | 8.8 | 8.8 | — | — | 9.3 🔴 Critical | 8.8 🟠 High | ✅ |
| GHSA-RQ6G-PX6M-C248 | HIGH/HIGH ✅ | 8.3 | 8.3 | — | — | 8.8 🟠 High | 8.3 🟠 High | ✅ |
| GHSA-RV39-79C4-7459 | CRITICAL/CRITICAL ✅ | 9.3 | 9.3 | — | — | 9.8 🔴 Critical | 9.3 🔴 Critical | ✅ |
| GHSA-RWJ8-P9VQ-25GV | HIGH/HIGH ✅ | 7.5 | 7.5 | — | — | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| GHSA-V6C6-VQQG-W888 | HIGH/HIGH ✅ | 7.2 | 7.2 | — | — | 7.7 🟠 High | 7.2 🟠 High | ✅ |
| GHSA-V773-R54F-Q32W | MEDIUM/MEDIUM ✅ | 4.8 | 4.8 | — | — | 5.3 🟡 Medium | 4.8 🟡 Medium | ✅ |
| GHSA-W2CG-VXX6-5XJG | MEDIUM/MEDIUM ✅ | 5.5 | 5.5 | — | — | 6.0 🟡 Medium | 5.5 🟡 Medium | ✅ |
| GHSA-W5C7-9QQW-6645 | HIGH/HIGH ✅ | 7.1 | 7.1 | — | — | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| GHSA-WFP2-V9C7-FH79 | MEDIUM/MEDIUM ✅ | 5.9 | 5.9 | — | — | 6.4 🟡 Medium | 5.9 🟡 Medium | ✅ |
| GHSA-X22M-J5QQ-J49M | HIGH/HIGH ✅ | 8.6 | 8.6 | — | — | 9.1 🔴 Critical | 8.6 🟠 High | ✅ |
| GHSA-XC7W-V5X6-CC87 | MEDIUM/MEDIUM ✅ | 5.9 | 5.9 | — | — | 6.4 🟡 Medium | 5.9 🟡 Medium | ✅ |
| GHSA-XVHF-X56F-2HPP | MEDIUM/MEDIUM ✅ | 5.7 | 5.7 | — | — | 6.2 🟡 Medium | 5.7 🟡 Medium | ✅ |

## CVEs Only in Vulners

| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |
|-----|----------|------|------|---------|---------------|-----|------|
| CVE-2023-34104 | CRITICAL | 9.3 | 0.00273 | fast-xml-parser@4.5.3 | No | No | 9.8 🔴 Critical |
| CVE-2026-25128 | HIGH | 8.7 | 0.00027 | fast-xml-parser@4.5.3 | No | No | 9.2 🔴 Critical |
| CVE-2024-51999 | MEDIUM | 6.9 | 0.00014 | express@4.21.2 | No | No | 7.4 🟠 High |

## Risk Summary

| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |
|--------|------|----------|----------|----------|------|--------|-----|
| Vulners | 96 | 7.5 | 10.0 | 5 | 52 | 33 | 6 |
| Grype | 93 | 6.7 | 9.4 | 4 | 46 | 35 | 8 |
