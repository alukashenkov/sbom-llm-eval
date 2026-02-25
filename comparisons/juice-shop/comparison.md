# Source Comparison: juice-shop

## Overview

| Metric | Value |
|--------|-------|
| Vulners CVEs | 60 |
| Grype CVEs | 82 |
| Total unique CVEs | 87 |
| Overlap | 55 (63.2%) |
| Vulners-only | 5 |
| Grype-only | 27 |

## Package Coverage

**In both sources:**
- base64url@0.0.6
- braces@2.3.2
- cookie@0.4.2
- crypto-js@3.3.0
- diff@4.0.2
- engine.io@4.1.2
- express-jwt@0.1.3
- got@8.3.2
- http-cache-semantics@3.8.1
- ip@2.0.1
- js-yaml@3.14.1
- jsonwebtoken@0.1.0
- jsonwebtoken@0.4.0
- jws@0.2.6
- lodash.set@4.3.2
- lodash@2.4.2
- lodash@4.17.21
- micromatch@3.1.10
- minimatch@3.0.5
- minimatch@3.0.8
- minimatch@3.1.2
- minimatch@5.1.6
- minimatch@9.0.5
- moment@2.0.0
- multer@1.4.5-lts.2
- notevil@1.3.3
- qs@6.14.0
- sanitize-html@1.4.2
- socket.io-parser@4.0.5
- socket.io@3.1.2
- tar@4.4.19
- tar@6.2.1
- tar@7.5.2
- vm2@3.9.17
- ws@7.4.6

**Vulners only:**
- cacheable-request@2.1.4
- messageformat@2.3.0
- minimist@0.2.4

**Grype only:**
- gcc-12-base@12.2.0-14+deb12u1
- libc6@2.36-9+deb12u13
- libgcc-s1@12.2.0-14+deb12u1
- libgomp1@12.2.0-14+deb12u1
- libssl3@3.0.17-1~deb12u3
- libstdc++6@12.2.0-14+deb12u1
- marsdb@0.6.11
- node@22.21.1

## CVEs Found in Both Sources

| CVE | Severity | Vulners CVSS | Grype CVSS | Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |
|-----|----------|-------------|------------|-------------|------------|-------------|------------|-------|
| CVE-2015-9235 | CRITICAL/CRITICAL ✅ | 9.8 | — | 0.3247 | 0.3247 | 10.0 🔴 Critical | 0.0 ⚪ None | ⚠️ |
| CVE-2016-1000223 | HIGH/HIGH ✅ | 8.7 | 8.7 | — | — | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| CVE-2016-1000237 | MEDIUM/MEDIUM ✅ | 6.1 | 6.1 | 0.00328 | 0.00328 | 6.6 🟡 Medium | 6.1 🟡 Medium | ✅ |
| CVE-2016-4055 | HIGH/MEDIUM ⚠️ | 7.8 | 6.5 | 0.04049 | 0.04049 | 8.3 🟠 High | 6.5 🟡 Medium | ⚠️ |
| CVE-2017-16016 | MEDIUM/MEDIUM ✅ | 6.1 | — | 0.00286 | 0.00286 | 6.6 🟡 Medium | 0.0 ⚪ None | ⚠️ |
| CVE-2017-18214 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00311 | 0.00311 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2018-16487 | MEDIUM/HIGH ⚠️ | 6.8 | — | 0.00345 | 0.00345 | 8.3 🟠 High | 0.0 ⚪ None | ⚠️ |
| CVE-2018-3721 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.00252 | 0.00252 | 8.0 🟠 High | 6.5 🟡 Medium | ✅ |
| CVE-2019-10744 | CRITICAL/CRITICAL ✅ | 9.1 | 9.1 | 0.02441 | 0.02441 | 9.6 🔴 Critical | 9.1 🔴 Critical | ✅ |
| CVE-2019-25225 | MEDIUM/MEDIUM ✅ | 6.1 | 6.1 | 0.0004 | 0.0004 | 6.6 🟡 Medium | 6.1 🟡 Medium | ✅ |
| CVE-2020-15084 | HIGH/HIGH ✅ | 7.7 | 7.7 | 0.00222 | 0.00222 | 8.2 🟠 High | 7.7 🟠 High | ✅ |
| CVE-2020-8203 | HIGH/HIGH ✅ | 7.4 | 7.4 | 0.02546 | 0.02546 | 8.9 🟠 High | 7.9 🟠 High | ✅ |
| CVE-2021-23337 | HIGH/HIGH ✅ | 7.2 | 7.2 | 0.00741 | 0.00741 | 7.7 🟠 High | 7.2 🟠 High | ✅ |
| CVE-2021-23771 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.00304 | 0.00304 | 7.0 🟠 High | 7.0 🟠 High | ✅ |
| CVE-2021-26539 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00288 | 0.00288 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2021-26540 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00288 | 0.00288 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2022-23539 | HIGH/HIGH ✅ | 8.1 | 8.1 | 0.00072 | 0.00072 | 8.6 🟠 High | 8.1 🟠 High | ✅ |
| CVE-2022-23540 | MEDIUM/MEDIUM ✅ | 6.4 | 6.4 | 0.00017 | 0.00017 | 6.9 🟡 Medium | 6.4 🟡 Medium | ✅ |
| CVE-2022-23541 | MEDIUM/MEDIUM ✅ | 5 | 5 | 0.0006 | 0.0006 | 5.5 🟡 Medium | 5.0 🟡 Medium | ✅ |
| CVE-2022-24785 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.01673 | 0.01673 | 9.0 🔴 Critical | 7.5 🟠 High | ✅ |
| CVE-2022-25881 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00196 | 0.00196 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2022-25887 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00447 | 0.00447 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2022-33987 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00807 | 0.00807 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2022-41940 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.0206 | 0.0206 | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| CVE-2023-32313 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.0057 | 0.0057 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2023-32314 | CRITICAL/CRITICAL ✅ | 9.8 | 9.8 | 0.69875 | 0.69875 | 10.0 🔴 Critical | 10.0 🔴 Critical | ✅ |
| CVE-2023-32695 | HIGH/MEDIUM ⚠️ | 7.3 | 7.3 | 0.00203 | 0.00203 | 7.8 🟠 High | 7.3 🟠 High | ⚠️ |
| CVE-2023-37466 | CRITICAL/CRITICAL ✅ | 9.8 | 9.8 | 0.04997 | 0.04997 | 10.0 🔴 Critical | 9.8 🔴 Critical | ✅ |
| CVE-2023-37903 | CRITICAL/CRITICAL ✅ | 9.8 | 9.8 | 0.04997 | 0.39234 | 10.0 🔴 Critical | 10.0 🔴 Critical | ✅ |
| CVE-2023-46233 | CRITICAL/CRITICAL ✅ | 9.1 | 9.1 | 0.00823 | 0.00823 | 9.6 🔴 Critical | 9.1 🔴 Critical | ✅ |
| CVE-2024-21501 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.01341 | 0.01341 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2024-28863 | MEDIUM/MEDIUM ✅ | 6.5 | 6.5 | 0.0045 | 0.0045 | 7.0 🟠 High | 6.5 🟡 Medium | ✅ |
| CVE-2024-29415 | HIGH/HIGH ✅ | 8.1 | 8.1 | 0.00539 | 0.86505 | 8.6 🟠 High | 10.0 🔴 Critical | ✅ |
| CVE-2024-37890 | HIGH/HIGH ✅ | 8.7 | 7.5 | 0.00541 | 0.00541 | 9.2 🔴 Critical | 7.5 🟠 High | ⚠️ |
| CVE-2024-38355 | HIGH/MEDIUM ⚠️ | 7.3 | 7.3 | 0.00136 | 0.00136 | 7.8 🟠 High | 7.3 🟠 High | ⚠️ |
| CVE-2024-4067 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00126 | 0.00126 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2024-4068 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00225 | 0.00225 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2024-47764 | MEDIUM/LOW ⚠️ | 6.9 | — | 0.00205 | 0.00205 | 7.4 🟠 High | 0.0 ⚪ None | ⚠️ |
| CVE-2025-13465 | HIGH/MEDIUM ⚠️ | 7.9 | 6.5 | 0.00025 | 0.00025 | 8.4 🟠 High | 6.5 🟡 Medium | ⚠️ |
| CVE-2025-15284 | HIGH/HIGH ✅ | 8.7 | 7.5 | 0.00085 | 0.00085 | 9.2 🔴 Critical | 7.5 🟠 High | ⚠️ |
| CVE-2025-47935 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00048 | 0.00048 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2025-47944 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00011 | 0.00011 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2025-48997 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.00081 | 0.00081 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| CVE-2025-64718 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.0002 | 0.0002 | 5.8 🟡 Medium | 5.3 🟡 Medium | ✅ |
| CVE-2025-65945 | HIGH/HIGH ✅ | 7.5 | 7.5 | 9e-05 | 9e-05 | 9.0 🔴 Critical | 7.5 🟠 High | ✅ |
| CVE-2025-7338 | HIGH/HIGH ✅ | 7.5 | 7.5 | 0.00012 | 0.00012 | 8.0 🟠 High | 7.5 🟠 High | ✅ |
| CVE-2026-22709 | CRITICAL/CRITICAL ✅ | 9.8 | 9.8 | 0.0003 | 0.0003 | 10.0 🔴 Critical | 9.8 🔴 Critical | ✅ |
| CVE-2026-23745 | HIGH/HIGH ✅ | 8.2 | 8.2 | 6e-05 | 6e-05 | 9.7 🔴 Critical | 8.2 🟠 High | ✅ |
| CVE-2026-2391 | HIGH/LOW ⚠️ | 7.5 | 3.7 | 0.00085 | 0.00019 | 8.0 🟠 High | 3.7 🟢 Low | ⚠️ |
| CVE-2026-23950 | HIGH/HIGH ✅ | 8.8 | 8.8 | 6e-05 | 6e-05 | 9.3 🔴 Critical | 8.8 🟠 High | ✅ |
| CVE-2026-24001 | HIGH/LOW ⚠️ | 7.5 | 2.7 | 0.0002 | 0.0002 | 8.0 🟠 High | 2.7 🟢 Low | ⚠️ |
| CVE-2026-24842 | HIGH/HIGH ✅ | 8.2 | 8.2 | 0.00012 | 0.00012 | 8.7 🟠 High | 8.2 🟠 High | ✅ |
| CVE-2026-26960 | HIGH/HIGH ✅ | 7.1 | 7.1 | 0.00013 | 0.00013 | 7.6 🟠 High | 7.1 🟠 High | ✅ |
| CVE-2026-26996 | HIGH/HIGH ✅ | 8.7 | 8.7 | 0.0004 | 0.0004 | 9.2 🔴 Critical | 8.7 🟠 High | ✅ |
| GHSA-RVG8-PWQ2-XJ7Q | NONE/MEDIUM ⚠️ | — | — | — | — | 0.5 🟢 Low | 0.0 ⚪ None | ⚠️ |

## CVEs Only in Vulners

| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |
|-----|----------|------|------|---------|---------------|-----|------|
| CVE-2023-42282 | HIGH | 8.1 | 0.00539 | ip@2.0.1 | No | No | 8.6 🟠 High |
| CVE-2022-23529 | HIGH | 7.6 | 0.00044 | jsonwebtoken@0.1.0, jsonwebtoken@0.4.0 | No | No | 8.1 🟠 High |
| GHSA-8X6C-CV3V-VP6G | HIGH | 7.5 | — | cacheable-request@2.1.4 | No | No | 8.0 🟠 High |
| CVE-2020-7598 | MEDIUM | 6.8 | 0.00253 | minimist@0.2.4 | No | No | 7.3 🟠 High |
| CVE-2025-57349 | MEDIUM | 6.3 | 0.0028 | messageformat@2.3.0 | No | No | 6.8 🟡 Medium |

## CVEs Only in Grype

| CVE | Severity | CVSS | EPSS | Package | Fix Available | Fix Versions | Risk |
|-----|----------|------|------|---------|--------------|-------------|------|
| CVE-2025-15467 | CRITICAL | 9.8 | 0.00672 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 9.8 🔴 Critical |
| CVE-2025-55130 | CRITICAL | 9.1 | 0.00012 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 9.1 🔴 Critical |
| CVE-2026-0861 | HIGH | 8.4 | 6e-05 | libc6@2.36-9+deb12u13 | No | — | 8.9 🟠 High |
| CVE-2025-15281 | HIGH | 7.5 | 0.00053 | libc6@2.36-9+deb12u13 | No | — | 8.0 🟠 High |
| CVE-2026-0915 | HIGH | 7.5 | 0.00019 | libc6@2.36-9+deb12u13 | No | — | 8.0 🟠 High |
| CVE-2025-59465 | HIGH | 7.5 | 0.00069 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 7.5 🟠 High |
| CVE-2025-59466 | HIGH | 7.5 | 0.00026 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 7.5 🟠 High |
| CVE-2025-69420 | HIGH | 7.5 | 0.0007 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 7.5 🟠 High |
| CVE-2025-69421 | HIGH | 7.5 | 0.00059 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 7.5 🟠 High |
| CVE-2026-21637 | HIGH | 7.5 | 0.00035 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 7.5 🟠 High |
| CVE-2025-69419 | HIGH | 7.4 | 0.00056 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 7.4 🟠 High |
| CVE-2025-55131 | HIGH | 7.1 | 0.00027 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 7.1 🟠 High |
| CVE-2026-22795 | MEDIUM | 5.5 | 0.00015 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 5.5 🟡 Medium |
| CVE-2025-55132 | MEDIUM | 5.3 | 9e-05 | node@22.21.1 | Yes | 24.13.0, 22.22.0, 20.20.0, 25.3.0 | 5.3 🟡 Medium |
| CVE-2026-22796 | MEDIUM | 5.3 | 0.0007 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 5.3 🟡 Medium |
| CVE-2025-68160 | MEDIUM | 4.7 | 0.00014 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 4.7 🟡 Medium |
| CVE-2025-69418 | MEDIUM | 4 | 5e-05 | libssl3@3.0.17-1~deb12u3 | Yes | 3.0.18-1~deb12u2 | 4.0 🟡 Medium |
| CVE-2010-4756 | UNKNOWN | — | 0.00394 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2018-20796 | UNKNOWN | — | 0.01669 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2019-1010022 | UNKNOWN | — | 0.00131 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2019-1010023 | UNKNOWN | — | 0.00322 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2019-1010024 | UNKNOWN | — | 0.00646 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2019-1010025 | UNKNOWN | — | 0.00856 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2019-9192 | UNKNOWN | — | 0.00841 | libc6@2.36-9+deb12u13 | No | — | 0.5 🟢 Low |
| CVE-2022-27943 | UNKNOWN | — | 0.0005 | gcc-12-base@12.2.0-14+deb12u1, libgcc-s1@12.2.0-14+deb12u1, libgomp1@12.2.0-14+deb12u1, libstdc++6@12.2.0-14+deb12u1 | No | — | 0.5 🟢 Low |
| CVE-2025-27587 | UNKNOWN | — | 0.00051 | libssl3@3.0.17-1~deb12u3 | No | — | 0.5 🟢 Low |
| GHSA-5MRR-RGP6-X4GR | CRITICAL | — | — | marsdb@0.6.11 | No | — | 0.5 🟢 Low |

## Risk Summary

| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |
|--------|------|----------|----------|----------|------|--------|-----|
| Vulners | 60 | 7.9 | 10.0 | 7 | 32 | 20 | 0 |
| Grype | 82 | 5.9 | 10.0 | 10 | 34 | 26 | 3 |
