# Source Comparison: la-vulners-mcp

## Overview

| Metric | Value |
|--------|-------|
| Vulners CVEs | 7 |
| Grype CVEs | 9 |
| Total unique CVEs | 15 |
| Overlap | 1 (6.7%) |
| Vulners-only | 6 |
| Grype-only | 8 |

## Package Coverage

**In both sources:**
- busybox@1.37.0-r30

**Vulners only:**
- musl@1.2.5-r21
- zlib@1.3.1-r2

**Grype only:**
- busybox-binsh@1.37.0-r30
- python@3.14.3
- ssl_client@1.37.0-r30

## CVEs Found in Both Sources

| CVE | Severity | Vulners CVSS | Grype CVSS | Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |
|-----|----------|-------------|------------|-------------|------------|-------------|------------|-------|
| CVE-2025-60876 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.00052 | 0.00052 | 7.0 🟠 High | 7.0 🟠 High | ✅ |

## CVEs Only in Vulners

| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |
|-----|----------|------|------|---------|---------------|-----|------|
| CVE-2023-45853 | CRITICAL | 9.8 | 0.01396 | zlib@1.3.1-r2 | No | No | 10.0 🔴 Critical |
| CVE-2026-22184 | CRITICAL | 9.8 | 0.00042 | zlib@1.3.1-r2 | No | No | 10.0 🔴 Critical |
| CVE-2025-26519 | HIGH | 8.1 | 0.00022 | musl@1.2.5-r21 | No | No | 8.6 🟠 High |
| CVE-2026-27171 | MEDIUM | 5.5 | 6e-05 | zlib@1.3.1-r2 | No | No | 6.0 🟡 Medium |
| CVE-2025-46394 | LOW | 3.3 | 0.00083 | busybox@1.37.0-r30 | No | No | 3.8 🟢 Low |
| CVE-2024-58251 | LOW | 2.5 | 0.00077 | busybox@1.37.0-r30 | No | No | 3.0 🟢 Low |

## CVEs Only in Grype

| CVE | Severity | CVSS | EPSS | Package | Fix Available | Fix Versions | Risk |
|-----|----------|------|------|---------|--------------|-------------|------|
| CVE-2025-15282 | MEDIUM | 6 | 0.00046 | python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2026-0672 | MEDIUM | 6 | 0.00164 | python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2026-1299 | MEDIUM | 6 | 0.00046 | python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2025-15366 | MEDIUM | 5.9 | 0.00093 | python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2025-15367 | MEDIUM | 5.9 | 0.00093 | python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2026-0865 | MEDIUM | 5.9 | 0.00165 | python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2025-11468 | MEDIUM | 5.7 | 0.0003 | python@3.14.3 | Yes | 3.15.0 | 5.7 🟡 Medium |
| CVE-2025-12781 | MEDIUM | 5.3 | 0.0004 | python@3.14.3 | Yes | 3.15.0 | 5.3 🟡 Medium |

## Risk Summary

| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |
|--------|------|----------|----------|----------|------|--------|-----|
| Vulners | 7 | 6.9 | 10.0 | 2 | 1 | 2 | 2 |
| Grype | 9 | 6.0 | 7.0 | 0 | 0 | 9 | 0 |
