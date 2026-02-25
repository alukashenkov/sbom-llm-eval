# Source Comparison: vulners-mcp

## Overview

| Metric | Value |
|--------|-------|
| Vulners CVEs | 188 |
| Grype CVEs | 264 |
| Total unique CVEs | 374 |
| Overlap | 78 (20.9%) |
| Vulners-only | 110 |
| Grype-only | 186 |

## Package Coverage

**In both sources:**
- apt@3.0.3
- binutils@2.44-3
- coreutils@9.7-3
- curl@8.14.1-2+deb13u2
- diskcache@5.6.3
- fastmcp@2.13.3
- git@1:2.47.3-0+deb13u1
- gnupg@2.4.7-21+deb13u1
- imagemagick@8:7.1.1.43+dfsg1-1+deb13u5
- libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2
- mcp@1.22.0
- perl@5.40.1-6
- tar@1.35+dfsg-3.1
- wget@1.25.0-2

**Vulners only:**
- dash@0.5.12-12
- dpkg@1.22.21
- mercurial@7.0.1-2
- openssl@3.5.4-1~deb13u2
- pkgconf@1.8.1-4
- subversion@1.14.5-3

**Grype only:**
- binutils-aarch64-linux-gnu@2.44-3
- binutils-common@2.44-3
- bsdutils@1:2.41-5
- dirmngr@2.4.7-21+deb13u1+b1
- gir1.2-glib-2.0-dev@2.84.4-3~deb13u2
- gir1.2-glib-2.0@2.84.4-3~deb13u2
- gir1.2-harfbuzz-0.0@10.2.0-1+b1
- girepository-tools@2.84.4-3~deb13u2
- git-man@1:2.47.3-0+deb13u1
- gnupg-l10n@2.4.7-21+deb13u1
- gpg-agent@2.4.7-21+deb13u1+b1
- gpg@2.4.7-21+deb13u1+b1
- gpgconf@2.4.7-21+deb13u1+b1
- gpgsm@2.4.7-21+deb13u1+b1
- imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5
- imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5
- krb5-multidev@1.21.3-5
- libapt-pkg7.0@3.0.3
- libbinutils@2.44-3
- libblkid-dev@2.41-5
- libblkid1@2.41-5
- libbluetooth-dev@5.82-1.1
- libbluetooth3@5.82-1.1
- libc-bin@2.41-12+deb13u1
- libc-dev-bin@2.41-12+deb13u1
- libc6-dev@2.41-12+deb13u1
- libc6@2.41-12+deb13u1
- libcairo-gobject2@1.18.4-1+b1
- libcairo-script-interpreter2@1.18.4-1+b1
- libcairo2-dev@1.18.4-1+b1
- libcairo2@1.18.4-1+b1
- libctf-nobfd0@2.44-3
- libctf0@2.44-3
- libcurl3t64-gnutls@8.14.1-2+deb13u2
- libcurl4-openssl-dev@8.14.1-2+deb13u2
- libcurl4t64@8.14.1-2+deb13u2
- libde265-0@1.0.15-1+b3
- libelf1t64@0.192-4
- libexpat1-dev@2.7.1-2
- libexpat1@2.7.1-2
- libgcrypt20@1.11.0-7
- libgio-2.0-dev-bin@2.84.4-3~deb13u2
- libgio-2.0-dev@2.84.4-3~deb13u2
- libgirepository-2.0-0@2.84.4-3~deb13u2
- libglib2.0-0t64@2.84.4-3~deb13u2
- libglib2.0-bin@2.84.4-3~deb13u2
- libglib2.0-data@2.84.4-3~deb13u2
- libglib2.0-dev-bin@2.84.4-3~deb13u2
- libglib2.0-dev@2.84.4-3~deb13u2
- libgnutls-dane0t64@3.8.9-3+deb13u1
- libgnutls-openssl27t64@3.8.9-3+deb13u1
- libgnutls28-dev@3.8.9-3+deb13u1
- libgnutls30t64@3.8.9-3+deb13u1
- libgprofng0@2.44-3
- libgssapi-krb5-2@1.21.3-5
- libgssrpc4t64@1.21.3-5
- libharfbuzz-cairo0@10.2.0-1+b1
- libharfbuzz-dev@10.2.0-1+b1
- libharfbuzz-gobject0@10.2.0-1+b1
- libharfbuzz-icu0@10.2.0-1+b1
- libharfbuzz-subset0@10.2.0-1+b1
- libharfbuzz0b@10.2.0-1+b1
- libheif-plugin-dav1d@1.19.8-1
- libheif-plugin-libde265@1.19.8-1
- libheif1@1.19.8-1
- libjansson4@2.14-2+b3
- libjbig-dev@2.1-6.1+b2
- libjbig0@2.1-6.1+b2
- libk5crypto3@1.21.3-5
- libkadm5clnt-mit12@1.21.3-5
- libkadm5srv-mit12@1.21.3-5
- libkdb5-10t64@1.21.3-5
- libkrb5-3@1.21.3-5
- libkrb5-dev@1.21.3-5
- libkrb5support0@1.21.3-5
- liblastlog2-2@2.41-5
- liblcms2-2@2.16-2
- liblcms2-dev@2.16-2
- libldap-dev@2.6.10+dfsg-1
- libldap2@2.6.10+dfsg-1
- libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5
- libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5
- libmariadb-dev-compat@1:11.8.3-0+deb13u1
- libmariadb-dev@1:11.8.3-0+deb13u1
- libmariadb3@1:11.8.3-0+deb13u1
- libmount-dev@2.41-5
- libmount1@2.41-5
- libncurses-dev@6.5+20250216-2
- libncurses6@6.5+20250216-2
- libncursesw6@6.5+20250216-2
- libopenexr-3-1-30@3.1.13-2
- libopenexr-dev@3.1.13-2
- libopenjp2-7-dev@2.5.3-2.1~deb13u1
- libopenjp2-7@2.5.3-2.1~deb13u1
- libperl5.40@5.40.1-6
- libpixman-1-0@0.44.0-3
- libpixman-1-dev@0.44.0-3
- libpng-dev@1.6.48-1+deb13u1
- libpng16-16t64@1.6.48-1+deb13u1
- libpq-dev@17.7-0+deb13u1
- libpq5@17.7-0+deb13u1
- libpython3.13-minimal@3.13.5-2
- libpython3.13-stdlib@3.13.5-2
- libraw23t64@0.21.4-2
- libsframe1@2.44-3
- libsmartcols1@2.41-5
- libsqlite3-0@3.46.1-7
- libsqlite3-dev@3.46.1-7
- libsystemd0@257.9-1~deb13u1
- libtasn1-6-dev@4.20.0-2
- libtasn1-6@4.20.0-2
- libtcl8.6@8.6.16+dfsg-1
- libtiff-dev@4.7.0-3+deb13u1
- libtiff6@4.7.0-3+deb13u1
- libtiffxx6@4.7.0-3+deb13u1
- libtinfo6@6.5+20250216-2
- libudev1@257.9-1~deb13u1
- libuuid1@2.41-5
- libwmf-0.2-7@0.2.13-1.1+b3
- libwmf-dev@0.2.13-1.1+b3
- libwmflite-0.2-7@0.2.13-1.1+b3
- libxml2-dev@2.12.7+dfsg+really2.9.14-2.1+deb13u2
- libxslt1-dev@1.1.35-1.2+deb13u2
- libxslt1.1@1.1.35-1.2+deb13u2
- login.defs@1:4.17.4-2
- login@1:4.16.0-2+really2.41-5
- m4@1.4.19-8
- mariadb-common@1:11.8.3-0+deb13u1
- mount@2.41-5
- ncurses-base@6.5+20250216-2
- ncurses-bin@6.5+20250216-2
- openssh-client@1:10.0p1-7
- passwd@1:4.17.4-2
- patch@2.8-2
- perl-base@5.40.1-6
- perl-modules-5.40@5.40.1-6
- python3.13-minimal@3.13.5-2
- python3.13@3.13.5-2
- python@3.14.3
- tcl8.6-dev@8.6.16+dfsg-1
- tcl8.6@8.6.16+dfsg-1
- unzip@6.0-29
- util-linux@2.41-5
- uuid-dev@2.41-5
- zlib1g-dev@1:1.3.dfsg+really1.3.1-1+b1
- zlib1g@1:1.3.dfsg+really1.3.1-1+b1

## CVEs Found in Both Sources

| CVE | Severity | Vulners CVSS | Grype CVSS | Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |
|-----|----------|-------------|------------|-------------|------------|-------------|------------|-------|
| CVE-2011-3374 | LOW/UNKNOWN ⚠️ | 3.7 | — | 0.01509 | 0.01509 | 5.2 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2018-15607 | MEDIUM/UNKNOWN ⚠️ | 6.5 | — | 0.00908 | 0.00908 | 7.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-10966 | MEDIUM/UNKNOWN ⚠️ | 4.3 | — | 0.00015 | 0.00015 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11082 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.00016 | 0.00016 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11083 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.00017 | 0.00017 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11412 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00035 | 0.00035 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11413 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00033 | 0.00033 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11414 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00035 | 0.00035 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1147 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.0039 | 0.0039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1148 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00405 | 0.00405 | 3.6 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1149 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00181 | 0.00181 | 3.6 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11494 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00035 | 0.00035 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11495 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00035 | 0.00035 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1150 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00181 | 0.00181 | 3.6 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1151 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00167 | 0.00167 | 3.6 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1152 | LOW/UNKNOWN ⚠️ | 3.7 | — | 0.00181 | 0.00181 | 4.2 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1153 | MEDIUM/UNKNOWN ⚠️ | 5.9 | — | 0.00599 | 0.00599 | 6.4 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1176 | MEDIUM/UNKNOWN ⚠️ | 5 | — | 0.00113 | 0.00113 | 5.5 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1178 | MEDIUM/UNKNOWN ⚠️ | 5.6 | — | 0.00357 | 0.00357 | 6.1 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1180 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00279 | 0.00279 | 3.6 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1181 | MEDIUM/UNKNOWN ⚠️ | 5 | — | 0.00408 | 0.00408 | 5.5 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-1182 | MEDIUM/UNKNOWN ⚠️ | 5 | — | 0.00306 | 0.00306 | 5.5 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11839 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00021 | 0.00021 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-11840 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00035 | 0.00035 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-13034 | MEDIUM/MEDIUM ✅ | 5.9 | 5.9 | 8e-05 | 8e-05 | 6.4 🟡 Medium | 6.4 🟡 Medium | ✅ |
| CVE-2025-14017 | MEDIUM/UNKNOWN ⚠️ | 6.3 | — | 7e-05 | 7e-05 | 6.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-14524 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.0003 | 0.0003 | 6.8 🟡 Medium | 5.8 🟡 Medium | ✅ |
| CVE-2025-14819 | MEDIUM/MEDIUM ✅ | 5.3 | 5.3 | 0.00039 | 0.00039 | 5.8 🟡 Medium | 5.8 🟡 Medium | ✅ |
| CVE-2025-15079 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.0003 | 0.0003 | 6.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-15224 | LOW/UNKNOWN ⚠️ | 3.1 | — | 0.00072 | 0.00072 | 4.6 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-3198 | MEDIUM/UNKNOWN ⚠️ | 5.5 | — | 0.00068 | 0.00068 | 6.0 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-5244 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.0003 | 0.0003 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-5245 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.00031 | 0.00031 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-5278 | MEDIUM/UNKNOWN ⚠️ | 4.4 | — | 0.00029 | 0.00029 | 4.9 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-55160 | MEDIUM/UNKNOWN ⚠️ | 6.1 | — | 0.00038 | 0.00038 | 6.6 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2025-66416 | HIGH/HIGH ✅ | 7.6 | 7.6 | 0.00037 | 0.00037 | 8.1 🟠 High | 7.6 🟠 High | ✅ |
| CVE-2025-68972 | MEDIUM/MEDIUM ✅ | 5.9 | 4.7 | 3e-05 | 3e-05 | 6.4 🟡 Medium | 5.2 🟡 Medium | ⚠️ |
| CVE-2025-69872 | HIGH/MEDIUM ⚠️ | 7 | 5.2 | 0.00102 | 0.00102 | 8.5 🟠 High | 5.7 🟡 Medium | ⚠️ |
| CVE-2025-7545 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.00017 | 0.00017 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-7546 | HIGH/UNKNOWN ⚠️ | 7.8 | — | 0.00017 | 0.00017 | 8.3 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2025-8225 | LOW/UNKNOWN ⚠️ | 3.3 | — | 0.00022 | 0.00022 | 3.8 🟢 Low | 0.5 🟢 Low | ⚠️ |
| CVE-2026-0989 | LOW/LOW ✅ | 3.7 | 3.7 | 0.0002 | 0.0002 | 4.2 🟡 Medium | 4.2 🟡 Medium | ✅ |
| CVE-2026-0990 | MEDIUM/MEDIUM ✅ | 5.9 | 5.9 | 0.00058 | 0.00058 | 6.4 🟡 Medium | 6.4 🟡 Medium | ✅ |
| CVE-2026-0992 | LOW/LOW ✅ | 2.9 | 2.9 | 0.00022 | 0.00022 | 3.4 🟢 Low | 3.4 🟢 Low | ✅ |
| CVE-2026-1757 | MEDIUM/UNKNOWN ⚠️ | 6.2 | — | 0.00016 | 0.00016 | 6.7 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-24481 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00031 | 0.00031 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-24484 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00037 | 0.00037 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-24485 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00038 | 0.00038 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-24882 | HIGH/HIGH ✅ | 8.4 | 7.8 | 6e-05 | 6e-05 | 8.9 🟠 High | 8.3 🟠 High | ⚠️ |
| CVE-2026-25576 | MEDIUM/UNKNOWN ⚠️ | 5.1 | — | 0.00011 | 0.00011 | 5.6 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25637 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00037 | 0.00037 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25638 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00039 | 0.00039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25794 | HIGH/UNKNOWN ⚠️ | 8.2 | — | 0.00038 | 0.00038 | 8.7 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25795 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00039 | 0.00039 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25796 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00039 | 0.00039 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25797 | MEDIUM/UNKNOWN ⚠️ | 5.7 | — | 0.00021 | 0.00021 | 6.2 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25798 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00103 | 0.00103 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25799 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00039 | 0.00039 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25897 | CRITICAL/UNKNOWN ⚠️ | 9.8 | — | 0.00038 | 0.00038 | 10.0 🔴 Critical | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25898 | MEDIUM/UNKNOWN ⚠️ | 6.5 | — | 0.00037 | 0.00037 | 7.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25965 | HIGH/UNKNOWN ⚠️ | 8.6 | — | 0.00033 | 0.00033 | 9.1 🔴 Critical | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25966 | MEDIUM/UNKNOWN ⚠️ | 5.9 | — | 0.00012 | 0.00012 | 6.4 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25967 | HIGH/UNKNOWN ⚠️ | 7.4 | — | 0.0004 | 0.0004 | 7.9 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25968 | HIGH/UNKNOWN ⚠️ | 7.4 | — | 0.00043 | 0.00043 | 7.9 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25969 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00039 | 0.00039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25970 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00039 | 0.00039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25971 | MEDIUM/UNKNOWN ⚠️ | 6.2 | — | 0.00013 | 0.00013 | 6.7 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25982 | MEDIUM/UNKNOWN ⚠️ | 6.5 | — | 0.00037 | 0.00037 | 7.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25983 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00045 | 0.00045 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25985 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.0004 | 0.0004 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25986 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00039 | 0.00039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25987 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00028 | 0.00028 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25988 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00039 | 0.00039 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |
| CVE-2026-25989 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.0004 | 0.0004 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-26066 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00013 | 0.00013 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-26283 | HIGH/UNKNOWN ⚠️ | 7.5 | — | 0.00013 | 0.00013 | 8.0 🟠 High | 0.5 🟢 Low | ⚠️ |
| CVE-2026-26284 | CRITICAL/UNKNOWN ⚠️ | 9.1 | — | 0.00037 | 0.00037 | 9.6 🔴 Critical | 0.5 🟢 Low | ⚠️ |
| CVE-2026-26983 | MEDIUM/UNKNOWN ⚠️ | 5.3 | — | 0.00033 | 0.00033 | 5.8 🟡 Medium | 0.5 🟢 Low | ⚠️ |

## CVEs Only in Vulners

| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |
|-----|----------|------|------|---------|---------------|-----|------|
| CVE-2014-9846 | CRITICAL | 9.8 | 0.04666 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2014-9852 | CRITICAL | 9.8 | 0.01316 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2020-24972 | HIGH | 8.8 | 0.21343 | gnupg@2.4.7-21+deb13u1 | No | No | 10.0 🔴 Critical |
| CVE-2024-41817 | HIGH | 7.8 | 0.18593 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | Yes | 10.0 🔴 Critical |
| CVE-2024-56171 | CRITICAL | 9.8 | 0.00048 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 10.0 🔴 Critical |
| CVE-2025-15467 | CRITICAL | 9.8 | 0.00672 | openssl@3.5.4-1~deb13u2 | No | Yes | 10.0 🔴 Critical |
| CVE-2025-48384 | HIGH | 8 | 0.00456 | git@1:2.47.3-0+deb13u1 | Yes | Yes | 10.0 🔴 Critical |
| CVE-2025-48385 | HIGH | 8.6 | 0.00039 | git@1:2.47.3-0+deb13u1 | No | Yes | 10.0 🔴 Critical |
| CVE-2025-53014 | CRITICAL | 9.8 | 0.00031 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2025-53101 | CRITICAL | 9.8 | 0.00069 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2025-57807 | CRITICAL | 9.8 | 0.00042 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2026-22770 | CRITICAL | 9.8 | 0.00065 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2026-23876 | CRITICAL | 9.8 | 0.00062 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 10.0 🔴 Critical |
| CVE-2021-32803 | HIGH | 8.2 | 0.00147 | tar@1.35+dfsg-3.1 | No | Yes | 9.7 🔴 Critical |
| CVE-2021-32804 | HIGH | 8.2 | 0.00147 | tar@1.35+dfsg-3.1 | No | Yes | 9.7 🔴 Critical |
| CVE-2025-15468 | HIGH | 8.2 | 0.00048 | openssl@3.5.4-1~deb13u2 | No | Yes | 9.7 🔴 Critical |
| CVE-2026-23745 | HIGH | 8.2 | 6e-05 | tar@1.35+dfsg-3.1 | No | Yes | 9.7 🔴 Critical |
| CVE-2024-40896 | CRITICAL | 9.1 | 0.00553 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 9.6 🔴 Critical |
| CVE-2025-49794 | CRITICAL | 9.1 | 0.00078 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 9.6 🔴 Critical |
| CVE-2025-49796 | CRITICAL | 9.1 | 0.0055 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 9.6 🔴 Critical |
| CVE-2017-12668 | HIGH | 8.8 | 0.0031 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2017-15016 | HIGH | 8.8 | 0.00298 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2017-16545 | HIGH | 8.8 | 0.0066 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2018-9135 | HIGH | 8.8 | 0.00329 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2025-55154 | HIGH | 8.8 | 0.00047 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2025-55298 | HIGH | 8.8 | 0.0043 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2025-57803 | HIGH | 8.8 | 0.00075 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 9.3 🔴 Critical |
| CVE-2025-68973 | HIGH | 7.8 | 0.00016 | gnupg@2.4.7-21+deb13u1 | No | Yes | 9.3 🔴 Critical |
| CVE-2026-23950 | HIGH | 8.8 | 6e-05 | tar@1.35+dfsg-3.1 | No | No | 9.3 🔴 Critical |
| CVE-2021-37713 | HIGH | 8.6 | 0.00606 | tar@1.35+dfsg-3.1 | No | No | 9.1 🔴 Critical |
| CVE-2025-27614 | HIGH | 8.6 | 0.00019 | git@1:2.47.3-0+deb13u1 | No | No | 9.1 🔴 Critical |
| CVE-2025-11187 | HIGH | 7.5 | 0.00011 | openssl@3.5.4-1~deb13u2 | No | Yes | 9.0 🔴 Critical |
| CVE-2025-46835 | HIGH | 8.5 | 0.00024 | git@1:2.47.3-0+deb13u1 | No | No | 9.0 🔴 Critical |
| CVE-2025-5399 | HIGH | 7.5 | 0.00146 | curl@8.14.1-2+deb13u2 | No | Yes | 9.0 🔴 Critical |
| CVE-2025-69420 | HIGH | 7.5 | 0.0007 | openssl@3.5.4-1~deb13u2 | No | Yes | 9.0 🔴 Critical |
| CVE-2025-69421 | HIGH | 7.5 | 0.00059 | openssl@3.5.4-1~deb13u2 | No | Yes | 9.0 🔴 Critical |
| CVE-2025-9086 | HIGH | 7.5 | 0.00035 | curl@8.14.1-2+deb13u2 | No | Yes | 9.0 🔴 Critical |
| CVE-2024-53589 | HIGH | 8.4 | 0.0018 | binutils@2.44-3 | No | No | 8.9 🟠 High |
| CVE-2024-56406 | HIGH | 8.4 | 0.00131 | perl@5.40.1-6 | No | No | 8.9 🟠 High |
| CVE-2025-69419 | HIGH | 7.4 | 0.00056 | openssl@3.5.4-1~deb13u2 | No | Yes | 8.9 🟠 High |
| CVE-2026-26960 | HIGH | 8.4 | 0.00013 | tar@1.35+dfsg-3.1 | No | No | 8.9 🟠 High |
| CVE-2025-6297 | HIGH | 8.2 | 0.00136 | dpkg@1.22.21 | No | No | 8.7 🟠 High |
| CVE-2026-24842 | HIGH | 8.2 | 0.00012 | tar@1.35+dfsg-3.1 | No | No | 8.7 🟠 High |
| CVE-2025-22795 | HIGH | 7.1 | 0.00187 | openssl@3.5.4-1~deb13u2 | No | Yes | 8.6 🟠 High |
| CVE-2026-22795 | HIGH | 7.1 | 0.00015 | openssl@3.5.4-1~deb13u2 | No | Yes | 8.6 🟠 High |
| CVE-2017-9047 | HIGH | 7.8 | 0.0302 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.3 🟠 High |
| CVE-2019-13304 | HIGH | 7.8 | 0.00134 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.3 🟠 High |
| CVE-2024-45720 | HIGH | 7.8 | 0.00046 | subversion@1.14.5-3 | No | No | 8.3 🟠 High |
| CVE-2025-24928 | HIGH | 7.7 | 0.00044 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.2 🟠 High |
| CVE-2025-55004 | HIGH | 7.6 | 0.00041 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.1 🟠 High |
| CVE-2014-9850 | HIGH | 7.5 | 0.02408 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2015-8860 | HIGH | 7.5 | 0.00365 | tar@1.35+dfsg-3.1 | No | No | 8.0 🟠 High |
| CVE-2015-8895 | HIGH | 7.5 | 0.01472 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2017-9098 | HIGH | 7.5 | 0.0146 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2018-20834 | HIGH | 7.5 | 0.00747 | tar@1.35+dfsg-3.1 | No | No | 8.0 🟠 High |
| CVE-2024-52006 | HIGH | 7.5 | 0.01025 | git@1:2.47.3-0+deb13u1 | No | No | 8.0 🟠 High |
| CVE-2025-0840 | HIGH | 7.5 | 0.00443 | binutils@2.44-3 | No | No | 8.0 🟠 High |
| CVE-2025-1179 | HIGH | 7.5 | 0.00337 | binutils@2.44-3 | No | No | 8.0 🟠 High |
| CVE-2025-27113 | HIGH | 7.5 | 0.00217 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-32414 | HIGH | 7.5 | 0.00178 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-32415 | HIGH | 7.5 | 0.00071 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-49795 | HIGH | 7.5 | 0.00169 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-53015 | HIGH | 7.5 | 0.00039 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-53019 | HIGH | 7.5 | 0.00058 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-55212 | HIGH | 7.5 | 0.0026 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-6021 | HIGH | 7.5 | 0.006 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-62171 | HIGH | 7.5 | 0.00075 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-66628 | HIGH | 7.5 | 0.00048 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-68618 | HIGH | 7.5 | 0.00096 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-69204 | HIGH | 7.5 | 0.00098 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 8.0 🟠 High |
| CVE-2025-9230 | HIGH | 7.5 | 0.00031 | openssl@3.5.4-1~deb13u2 | No | No | 8.0 🟠 High |
| CVE-2025-66199 | MEDIUM | 5.9 | 0.00059 | openssl@3.5.4-1~deb13u2 | No | Yes | 7.4 🟠 High |
| CVE-2025-26434 | MEDIUM | 6.8 | 5e-05 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 7.3 🟠 High |
| CVE-2016-7513 | MEDIUM | 6.5 | 0.00613 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2016-7519 | MEDIUM | 6.5 | 0.00616 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2016-7525 | MEDIUM | 6.5 | 0.00961 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2016-7540 | MEDIUM | 6.5 | 0.00995 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2019-13454 | MEDIUM | 6.5 | 0.00357 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2019-14980 | MEDIUM | 6.5 | 0.00197 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2024-10524 | MEDIUM | 6.5 | 0.00436 | wget@1.25.0-2 | No | No | 7.0 🟠 High |
| CVE-2024-28863 | MEDIUM | 6.5 | 0.0045 | tar@1.35+dfsg-3.1 | No | No | 7.0 🟠 High |
| CVE-2025-15469 | MEDIUM | 5.5 | 5e-05 | openssl@3.5.4-1~deb13u2 | No | Yes | 7.0 🟠 High |
| CVE-2025-9231 | MEDIUM | 6.5 | 0.00019 | openssl@3.5.4-1~deb13u2 | No | No | 7.0 🟠 High |
| CVE-2026-23952 | MEDIUM | 6.5 | 0.00017 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 7.0 🟠 High |
| CVE-2024-21485 | MEDIUM | 5.4 | 0.00493 | dash@0.5.12-12 | No | Yes | 6.9 🟡 Medium |
| CVE-2025-10148 | MEDIUM | 5.3 | 0.00102 | curl@8.14.1-2+deb13u2 | No | Yes | 6.8 🟡 Medium |
| CVE-2025-48386 | MEDIUM | 6.3 | 0.00014 | git@1:2.47.3-0+deb13u1 | No | No | 6.8 🟡 Medium |
| CVE-2026-22796 | MEDIUM | 5.3 | 0.0007 | openssl@3.5.4-1~deb13u2 | No | Yes | 6.8 🟡 Medium |
| CVE-2023-5341 | MEDIUM | 6.2 | 0.00036 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.7 🟡 Medium |
| CVE-2025-68950 | MEDIUM | 6.2 | 0.00023 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.7 🟡 Medium |
| CVE-2025-65955 | MEDIUM | 6.1 | 0.00022 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.6 🟡 Medium |
| CVE-2025-9232 | MEDIUM | 5.9 | 0.00039 | openssl@3.5.4-1~deb13u2 | No | No | 6.4 🟡 Medium |
| CVE-2025-68160 | MEDIUM | 4.7 | 0.00014 | openssl@3.5.4-1~deb13u2 | No | Yes | 6.2 🟡 Medium |
| CVE-2015-8894 | MEDIUM | 5.5 | 0.00187 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2016-10053 | MEDIUM | 5.5 | 0.00407 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2017-6502 | MEDIUM | 5.5 | 0.00151 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2023-24056 | MEDIUM | 5.5 | 0.00029 | pkgconf@1.8.1-4 | No | No | 6.0 🟡 Medium |
| CVE-2024-57360 | MEDIUM | 5.5 | 0.00028 | binutils@2.44-3 | No | No | 6.0 🟡 Medium |
| CVE-2025-55005 | MEDIUM | 5.5 | 0.00024 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2025-62594 | MEDIUM | 5.5 | 0.00028 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2025-8224 | MEDIUM | 5.5 | 0.0003 | binutils@2.44-3 | No | No | 6.0 🟡 Medium |
| CVE-2026-23874 | MEDIUM | 5.5 | 0.00017 | imagemagick@8:7.1.1.43+dfsg1-1+deb13u5 | No | No | 6.0 🟡 Medium |
| CVE-2022-43410 | MEDIUM | 5.3 | 0.00298 | mercurial@7.0.1-2 | No | No | 5.8 🟡 Medium |
| CVE-2025-69418 | MEDIUM | 4 | 5e-05 | openssl@3.5.4-1~deb13u2 | No | Yes | 5.5 🟡 Medium |
| CVE-2024-50349 | MEDIUM | 4.7 | 0.01141 | git@1:2.47.3-0+deb13u1 | No | No | 5.2 🟡 Medium |
| CVE-2025-30258 | MEDIUM | 4.7 | 0.00025 | gnupg@2.4.7-21+deb13u1 | No | No | 5.2 🟡 Medium |
| CVE-2025-6170 | MEDIUM | 4.5 | 0.0002 | libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | No | 5.0 🟡 Medium |
| CVE-2024-46901 | MEDIUM | 4.3 | 0.05806 | subversion@1.14.5-3 | No | No | 4.8 🟡 Medium |
| CVE-2025-27613 | LOW | 3.6 | 0.00031 | git@1:2.47.3-0+deb13u1 | No | No | 4.1 🟡 Medium |
| CVE-2025-11563 | NONE | — | — | curl@8.14.1-2+deb13u2 | No | No | 0.5 🟢 Low |

## CVEs Only in Grype

| CVE | Severity | CVSS | EPSS | Package | Fix Available | Fix Versions | Risk |
|-----|----------|------|------|---------|--------------|-------------|------|
| CVE-2026-0861 | HIGH | 8.4 | 6e-05 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 8.9 🟠 High |
| CVE-2026-2004 | HIGH | 8.8 | 0.00115 | libpq-dev@17.7-0+deb13u1, libpq5@17.7-0+deb13u1 | Yes | 17.8-0+deb13u1 | 8.8 🟠 High |
| CVE-2026-2005 | HIGH | 8.8 | 0.00066 | libpq-dev@17.7-0+deb13u1, libpq5@17.7-0+deb13u1 | Yes | 17.8-0+deb13u1 | 8.8 🟠 High |
| CVE-2026-2006 | HIGH | 8.8 | 0.00075 | libpq-dev@17.7-0+deb13u1, libpq5@17.7-0+deb13u1 | Yes | 17.8-0+deb13u1 | 8.8 🟠 High |
| CVE-2023-44431 | HIGH | 8 | 0.02464 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 8.5 🟠 High |
| CVE-2025-12495 | HIGH | 7.8 | 0.0005 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 8.3 🟠 High |
| CVE-2025-12839 | HIGH | 7.8 | 0.0005 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 8.3 🟠 High |
| CVE-2025-12840 | HIGH | 7.8 | 0.0005 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 8.3 🟠 High |
| CVE-2026-25646 | HIGH | 8.3 | 0.00063 | libpng-dev@1.6.48-1+deb13u1, libpng16-16t64@1.6.48-1+deb13u1 | Yes | 1.6.48-1+deb13u3 | 8.3 🟠 High |
| CVE-2025-13151 | HIGH | 7.5 | 0.00059 | libtasn1-6-dev@4.20.0-2, libtasn1-6@4.20.0-2 | No | — | 8.0 🟠 High |
| CVE-2025-13836 | HIGH | 7.5 | 0.00152 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 8.0 🟠 High |
| CVE-2025-15281 | HIGH | 7.5 | 0.00053 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 8.0 🟠 High |
| CVE-2025-59375 | HIGH | 7.5 | 0.00051 | libexpat1-dev@2.7.1-2, libexpat1@2.7.1-2 | No | — | 8.0 🟠 High |
| CVE-2025-64181 | HIGH | 7.5 | 0.00048 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 8.0 🟠 High |
| CVE-2025-8194 | HIGH | 7.5 | 0.00162 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 8.0 🟠 High |
| CVE-2026-0915 | HIGH | 7.5 | 0.00019 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 8.0 🟠 High |
| CVE-2026-22801 | HIGH | 7.8 | 0.00019 | libpng-dev@1.6.48-1+deb13u1, libpng16-16t64@1.6.48-1+deb13u1 | Yes | 1.6.48-1+deb13u2 | 7.8 🟠 High |
| CVE-2023-51596 | HIGH | 7.1 | 0.02808 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 7.6 🟠 High |
| CVE-2025-13699 | HIGH | 7 | 0.00136 | libmariadb-dev-compat@1:11.8.3-0+deb13u1, libmariadb-dev@1:11.8.3-0+deb13u1, libmariadb3@1:11.8.3-0+deb13u1, mariadb-common@1:11.8.3-0+deb13u1 | No | — | 7.5 🟠 High |
| CVE-2025-7709 | MEDIUM | 6.9 | 0.00043 | libsqlite3-0@3.46.1-7, libsqlite3-dev@3.46.1-7 | No | — | 7.4 🟠 High |
| CVE-2026-25210 | MEDIUM | 6.9 | 6e-05 | libexpat1-dev@2.7.1-2, libexpat1@2.7.1-2 | No | — | 7.4 🟠 High |
| CVE-2026-22695 | HIGH | 7.1 | 0.00032 | libpng-dev@1.6.48-1+deb13u1, libpng16-16t64@1.6.48-1+deb13u1 | Yes | 1.6.48-1+deb13u2 | 7.1 🟠 High |
| CVE-2023-39329 | MEDIUM | 6.5 | 0.00108 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 7.0 🟠 High |
| CVE-2024-38949 | MEDIUM | 6.5 | 0.00132 | libde265-0@1.0.15-1+b3 | No | — | 7.0 🟠 High |
| CVE-2024-38950 | MEDIUM | 6.5 | 0.00179 | libde265-0@1.0.15-1+b3 | No | — | 7.0 🟠 High |
| CVE-2025-68431 | MEDIUM | 6.5 | 0.00038 | libheif-plugin-dav1d@1.19.8-1, libheif-plugin-libde265@1.19.8-1, libheif1@1.19.8-1 | No | — | 7.0 🟠 High |
| CVE-2021-31879 | MEDIUM | 6.1 | 0.00154 | wget@1.25.0-2 | No | — | 6.6 🟡 Medium |
| CVE-2025-14104 | MEDIUM | 6.1 | 6e-05 | bsdutils@1:2.41-5, libblkid-dev@2.41-5, libblkid1@2.41-5, liblastlog2-2@2.41-5, libmount-dev@2.41-5, libmount1@2.41-5, libsmartcols1@2.41-5, libuuid1@2.41-5, login@1:4.16.0-2+really2.41-5, mount@2.41-5, util-linux@2.41-5, uuid-dev@2.41-5 | No | — | 6.6 🟡 Medium |
| CVE-2023-51580 | MEDIUM | 5.7 | 0.00043 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 6.2 🟡 Medium |
| CVE-2023-51589 | MEDIUM | 5.7 | 0.0004 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 6.2 🟡 Medium |
| CVE-2023-51592 | MEDIUM | 5.7 | 0.00029 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 6.2 🟡 Medium |
| CVE-2023-51594 | MEDIUM | 5.7 | 0.00038 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 6.2 🟡 Medium |
| CVE-2023-39328 | MEDIUM | 5.5 | 0.00013 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 6.0 🟡 Medium |
| CVE-2025-10911 | MEDIUM | 5.5 | 0.00011 | libxslt1-dev@1.1.35-1.2+deb13u2, libxslt1.1@1.1.35-1.2+deb13u2 | No | — | 6.0 🟡 Medium |
| CVE-2025-13837 | MEDIUM | 5.5 | 0.00022 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 6.0 🟡 Medium |
| CVE-2025-15282 | MEDIUM | 6 | 0.00046 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2025-48074 | MEDIUM | 5.5 | 0.00033 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 6.0 🟡 Medium |
| CVE-2025-6075 | MEDIUM | 5.5 | 0.00025 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 6.0 🟡 Medium |
| CVE-2025-66382 | MEDIUM | 5.5 | 0.00016 | libexpat1-dev@2.7.1-2, libexpat1@2.7.1-2 | No | — | 6.0 🟡 Medium |
| CVE-2026-0672 | MEDIUM | 6 | 0.00164 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2026-1299 | MEDIUM | 6 | 0.00046 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 6.0 🟡 Medium |
| CVE-2025-15366 | MEDIUM | 5.9 | 0.00093 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2025-15367 | MEDIUM | 5.9 | 0.00093 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2026-0865 | MEDIUM | 5.9 | 0.00165 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 5.9 🟡 Medium |
| CVE-2026-1489 | MEDIUM | 5.4 | 0.00067 | gir1.2-glib-2.0-dev@2.84.4-3~deb13u2, gir1.2-glib-2.0@2.84.4-3~deb13u2, girepository-tools@2.84.4-3~deb13u2, libgio-2.0-dev-bin@2.84.4-3~deb13u2, libgio-2.0-dev@2.84.4-3~deb13u2, libgirepository-2.0-0@2.84.4-3~deb13u2, libglib2.0-0t64@2.84.4-3~deb13u2, libglib2.0-bin@2.84.4-3~deb13u2, libglib2.0-data@2.84.4-3~deb13u2, libglib2.0-dev-bin@2.84.4-3~deb13u2, libglib2.0-dev@2.84.4-3~deb13u2 | No | — | 5.9 🟡 Medium |
| CVE-2025-12084 | MEDIUM | 5.3 | 0.00049 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 5.8 🟡 Medium |
| CVE-2026-22693 | MEDIUM | 5.3 | 0.00066 | gir1.2-harfbuzz-0.0@10.2.0-1+b1, libharfbuzz-cairo0@10.2.0-1+b1, libharfbuzz-dev@10.2.0-1+b1, libharfbuzz-gobject0@10.2.0-1+b1, libharfbuzz-icu0@10.2.0-1+b1, libharfbuzz-subset0@10.2.0-1+b1, libharfbuzz0b@10.2.0-1+b1 | No | — | 5.8 🟡 Medium |
| CVE-2025-11468 | MEDIUM | 5.7 | 0.0003 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 5.7 🟡 Medium |
| CVE-2025-12781 | MEDIUM | 5.3 | 0.0004 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2, python@3.14.3 | Yes | 3.15.0 | 5.3 🟡 Medium |
| CVE-2025-14831 | MEDIUM | 5.3 | 0.00039 | libgnutls-dane0t64@3.8.9-3+deb13u1, libgnutls-openssl27t64@3.8.9-3+deb13u1, libgnutls28-dev@3.8.9-3+deb13u1, libgnutls30t64@3.8.9-3+deb13u1 | Yes | 3.8.9-3+deb13u2 | 5.3 🟡 Medium |
| CVE-2025-6141 | MEDIUM | 4.8 | 0.00019 | libncurses-dev@6.5+20250216-2, libncurses6@6.5+20250216-2, libncursesw6@6.5+20250216-2, libtinfo6@6.5+20250216-2, ncurses-base@6.5+20250216-2, ncurses-bin@6.5+20250216-2 | No | — | 5.3 🟡 Medium |
| CVE-2023-39327 | MEDIUM | 4.3 | 0.00048 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 4.8 🟡 Medium |
| CVE-2025-6069 | MEDIUM | 4.3 | 0.00194 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 4.8 🟡 Medium |
| CVE-2025-8291 | MEDIUM | 4.3 | 0.00169 | libpython3.13-minimal@3.13.5-2, libpython3.13-stdlib@3.13.5-2, python3.13-minimal@3.13.5-2, python3.13@3.13.5-2 | No | — | 4.8 🟡 Medium |
| CVE-2026-1484 | MEDIUM | 4.2 | 0.00067 | gir1.2-glib-2.0-dev@2.84.4-3~deb13u2, gir1.2-glib-2.0@2.84.4-3~deb13u2, girepository-tools@2.84.4-3~deb13u2, libgio-2.0-dev-bin@2.84.4-3~deb13u2, libgio-2.0-dev@2.84.4-3~deb13u2, libgirepository-2.0-0@2.84.4-3~deb13u2, libglib2.0-0t64@2.84.4-3~deb13u2, libglib2.0-bin@2.84.4-3~deb13u2, libglib2.0-data@2.84.4-3~deb13u2, libglib2.0-dev-bin@2.84.4-3~deb13u2, libglib2.0-dev@2.84.4-3~deb13u2 | No | — | 4.7 🟡 Medium |
| CVE-2026-2003 | MEDIUM | 4.3 | 0.00049 | libpq-dev@17.7-0+deb13u1, libpq5@17.7-0+deb13u1 | Yes | 17.8-0+deb13u1 | 4.3 🟡 Medium |
| CVE-2026-0988 | LOW | 3.7 | 0.00083 | gir1.2-glib-2.0-dev@2.84.4-3~deb13u2, gir1.2-glib-2.0@2.84.4-3~deb13u2, girepository-tools@2.84.4-3~deb13u2, libgio-2.0-dev-bin@2.84.4-3~deb13u2, libgio-2.0-dev@2.84.4-3~deb13u2, libgirepository-2.0-0@2.84.4-3~deb13u2, libglib2.0-0t64@2.84.4-3~deb13u2, libglib2.0-bin@2.84.4-3~deb13u2, libglib2.0-data@2.84.4-3~deb13u2, libglib2.0-dev-bin@2.84.4-3~deb13u2, libglib2.0-dev@2.84.4-3~deb13u2 | No | — | 4.2 🟡 Medium |
| CVE-2024-56433 | LOW | 3.6 | 0.04509 | login.defs@1:4.17.4-2, passwd@1:4.17.4-2 | No | — | 4.1 🟡 Medium |
| CVE-2025-61984 | LOW | 3.6 | 8e-05 | openssh-client@1:10.0p1-7 | No | — | 4.1 🟡 Medium |
| CVE-2025-61985 | LOW | 3.6 | 0.00015 | openssh-client@1:10.0p1-7 | No | — | 4.1 🟡 Medium |
| CVE-2025-11731 | LOW | 3.1 | 0.0009 | libxslt1-dev@1.1.35-1.2+deb13u2, libxslt1.1@1.1.35-1.2+deb13u2 | No | — | 3.6 🟢 Low |
| CVE-2025-50422 | LOW | 2.9 | 0.00017 | libcairo-gobject2@1.18.4-1+b1, libcairo-script-interpreter2@1.18.4-1+b1, libcairo2-dev@1.18.4-1+b1, libcairo2@1.18.4-1+b1 | No | — | 3.4 🟢 Low |
| CVE-2026-1485 | LOW | 2.8 | 7e-05 | gir1.2-glib-2.0-dev@2.84.4-3~deb13u2, gir1.2-glib-2.0@2.84.4-3~deb13u2, girepository-tools@2.84.4-3~deb13u2, libgio-2.0-dev-bin@2.84.4-3~deb13u2, libgio-2.0-dev@2.84.4-3~deb13u2, libgirepository-2.0-0@2.84.4-3~deb13u2, libglib2.0-0t64@2.84.4-3~deb13u2, libglib2.0-bin@2.84.4-3~deb13u2, libglib2.0-data@2.84.4-3~deb13u2, libglib2.0-dev-bin@2.84.4-3~deb13u2, libglib2.0-dev@2.84.4-3~deb13u2 | No | — | 3.3 🟢 Low |
| CVE-2026-24515 | LOW | 2.5 | 5e-05 | libexpat1-dev@2.7.1-2, libexpat1@2.7.1-2 | No | — | 3.0 🟢 Low |
| CVE-2005-0406 | UNKNOWN | — | 0.00122 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2005-2541 | UNKNOWN | — | 0.02806 | tar@1.35+dfsg-3.1 | No | — | 0.5 🟢 Low |
| CVE-2007-2243 | UNKNOWN | — | 0.00264 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2007-2768 | UNKNOWN | — | 0.00119 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2007-3476 | LOW | — | 0.05321 | libwmf-0.2-7@0.2.13-1.1+b3, libwmf-dev@0.2.13-1.1+b3, libwmflite-0.2-7@0.2.13-1.1+b3 | No | — | 0.5 🟢 Low |
| CVE-2007-3477 | LOW | — | 0.07483 | libwmf-0.2-7@0.2.13-1.1+b3, libwmf-dev@0.2.13-1.1+b3, libwmflite-0.2-7@0.2.13-1.1+b3 | No | — | 0.5 🟢 Low |
| CVE-2007-3996 | MEDIUM | — | 0.09573 | libwmf-0.2-7@0.2.13-1.1+b3, libwmf-dev@0.2.13-1.1+b3, libwmflite-0.2-7@0.2.13-1.1+b3 | No | — | 0.5 🟢 Low |
| CVE-2007-5686 | UNKNOWN | — | 0.00196 | login.defs@1:4.17.4-2, passwd@1:4.17.4-2 | No | — | 0.5 🟢 Low |
| CVE-2008-1687 | UNKNOWN | — | 0.02727 | m4@1.4.19-8 | No | — | 0.5 🟢 Low |
| CVE-2008-1688 | UNKNOWN | — | 0.02196 | m4@1.4.19-8 | No | — | 0.5 🟢 Low |
| CVE-2008-3134 | UNKNOWN | — | 0.01621 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2008-3234 | UNKNOWN | — | 0.02871 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2009-3546 | MEDIUM | — | 0.04125 | libwmf-0.2-7@0.2.13-1.1+b3, libwmf-dev@0.2.13-1.1+b3, libwmflite-0.2-7@0.2.13-1.1+b3 | No | — | 0.5 🟢 Low |
| CVE-2010-4651 | UNKNOWN | — | 0.0183 | patch@2.8-2 | No | — | 0.5 🟢 Low |
| CVE-2010-4756 | UNKNOWN | — | 0.00394 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2011-3389 | UNKNOWN | — | 0.03795 | libgnutls-dane0t64@3.8.9-3+deb13u1, libgnutls-openssl27t64@3.8.9-3+deb13u1, libgnutls28-dev@3.8.9-3+deb13u1, libgnutls30t64@3.8.9-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2011-4116 | UNKNOWN | — | 0.00181 | libperl5.40@5.40.1-6, perl-base@5.40.1-6, perl-modules-5.40@5.40.1-6, perl@5.40.1-6 | No | — | 0.5 🟢 Low |
| CVE-2012-0039 | UNKNOWN | — | 0.00489 | gir1.2-glib-2.0-dev@2.84.4-3~deb13u2, gir1.2-glib-2.0@2.84.4-3~deb13u2, girepository-tools@2.84.4-3~deb13u2, libgio-2.0-dev-bin@2.84.4-3~deb13u2, libgio-2.0-dev@2.84.4-3~deb13u2, libgirepository-2.0-0@2.84.4-3~deb13u2, libglib2.0-0t64@2.84.4-3~deb13u2, libglib2.0-bin@2.84.4-3~deb13u2, libglib2.0-data@2.84.4-3~deb13u2, libglib2.0-dev-bin@2.84.4-3~deb13u2, libglib2.0-dev@2.84.4-3~deb13u2 | No | — | 0.5 🟢 Low |
| CVE-2013-4392 | UNKNOWN | — | 0.00042 | libsystemd0@257.9-1~deb13u1, libudev1@257.9-1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2015-3276 | UNKNOWN | — | 0.01757 | libldap-dev@2.6.10+dfsg-1, libldap2@2.6.10+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2015-9019 | UNKNOWN | — | 0.00595 | libxslt1-dev@1.1.35-1.2+deb13u2, libxslt1.1@1.1.35-1.2+deb13u2 | No | — | 0.5 🟢 Low |
| CVE-2016-10505 | UNKNOWN | — | 0.00656 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-20012 | UNKNOWN | — | 0.14603 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2016-8678 | UNKNOWN | — | 0.00212 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2016-9113 | UNKNOWN | — | 0.00448 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9114 | UNKNOWN | — | 0.00478 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9115 | UNKNOWN | — | 0.00374 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9116 | UNKNOWN | — | 0.00581 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9117 | UNKNOWN | — | 0.00581 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9580 | UNKNOWN | — | 0.00379 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9581 | UNKNOWN | — | 0.0033 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2016-9797 | UNKNOWN | — | 0.00479 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9798 | UNKNOWN | — | 0.00487 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9799 | UNKNOWN | — | 0.00476 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9800 | UNKNOWN | — | 0.00387 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9801 | UNKNOWN | — | 0.00387 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9802 | UNKNOWN | — | 0.00476 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9803 | UNKNOWN | — | 0.00422 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9804 | UNKNOWN | — | 0.0036 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9917 | UNKNOWN | — | 0.00454 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2016-9918 | UNKNOWN | — | 0.00489 | libbluetooth-dev@5.82-1.1, libbluetooth3@5.82-1.1 | No | — | 0.5 🟢 Low |
| CVE-2017-11754 | UNKNOWN | — | 0.00528 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2017-11755 | UNKNOWN | — | 0.00528 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2017-13716 | UNKNOWN | — | 0.00237 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2017-14159 | UNKNOWN | — | 0.00092 | libldap-dev@2.6.10+dfsg-1, libldap2@2.6.10+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2017-14988 | UNKNOWN | — | 0.00377 | libopenexr-3-1-30@3.1.13-2, libopenexr-dev@3.1.13-2 | No | — | 0.5 🟢 Low |
| CVE-2017-16232 | UNKNOWN | — | 0.01072 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2017-17740 | UNKNOWN | — | 0.01643 | libldap-dev@2.6.10+dfsg-1, libldap2@2.6.10+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2017-18018 | UNKNOWN | — | 0.00056 | coreutils@9.7-3 | No | — | 0.5 🟢 Low |
| CVE-2017-7275 | UNKNOWN | — | 0.00406 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2017-7475 | LOW | — | 0.00282 | libcairo-gobject2@1.18.4-1+b1, libcairo-script-interpreter2@1.18.4-1+b1, libcairo2-dev@1.18.4-1+b1, libcairo2@1.18.4-1+b1 | No | — | 0.5 🟢 Low |
| CVE-2017-9937 | UNKNOWN | — | 0.0054 | libjbig-dev@2.1-6.1+b2, libjbig0@2.1-6.1+b2 | No | — | 0.5 🟢 Low |
| CVE-2018-1000021 | UNKNOWN | — | 0.00372 | git-man@1:2.47.3-0+deb13u1, git@1:2.47.3-0+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2018-10126 | UNKNOWN | — | 0.003 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2018-15919 | UNKNOWN | — | 0.02073 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2018-16376 | UNKNOWN | — | 0.00597 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2018-18064 | UNKNOWN | — | 0.0051 | libcairo-gobject2@1.18.4-1+b1, libcairo-script-interpreter2@1.18.4-1+b1, libcairo2-dev@1.18.4-1+b1, libcairo2@1.18.4-1+b1 | No | — | 0.5 🟢 Low |
| CVE-2018-20673 | UNKNOWN | — | 0.00119 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2018-20712 | UNKNOWN | — | 0.00801 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2018-20796 | UNKNOWN | — | 0.01669 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2018-5709 | UNKNOWN | — | 0.01485 | krb5-multidev@1.21.3-5, libgssapi-krb5-2@1.21.3-5, libgssrpc4t64@1.21.3-5, libk5crypto3@1.21.3-5, libkadm5clnt-mit12@1.21.3-5, libkadm5srv-mit12@1.21.3-5, libkdb5-10t64@1.21.3-5, libkrb5-3@1.21.3-5, libkrb5-dev@1.21.3-5, libkrb5support0@1.21.3-5 | No | — | 0.5 🟢 Low |
| CVE-2018-6829 | UNKNOWN | — | 0.00515 | libgcrypt20@1.11.0-7 | No | — | 0.5 🟢 Low |
| CVE-2018-6951 | UNKNOWN | — | 0.15333 | patch@2.8-2 | No | — | 0.5 🟢 Low |
| CVE-2018-6952 | UNKNOWN | — | 0.11805 | patch@2.8-2 | No | — | 0.5 🟢 Low |
| CVE-2018-9996 | UNKNOWN | — | 0.00385 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2019-1010022 | UNKNOWN | — | 0.00131 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2019-1010023 | UNKNOWN | — | 0.00322 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2019-1010024 | UNKNOWN | — | 0.00646 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2019-1010025 | UNKNOWN | — | 0.00856 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2019-6110 | UNKNOWN | — | 0.51287 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2019-6988 | LOW | — | 0.00327 | libopenjp2-7-dev@2.5.3-2.1~deb13u1, libopenjp2-7@2.5.3-2.1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2019-9192 | UNKNOWN | — | 0.00841 | libc-bin@2.41-12+deb13u1, libc-dev-bin@2.41-12+deb13u1, libc6-dev@2.41-12+deb13u1, libc6@2.41-12+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2020-14145 | UNKNOWN | — | 0.01254 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2020-15719 | UNKNOWN | — | 0.00216 | libldap-dev@2.6.10+dfsg-1, libldap2@2.6.10+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2020-15778 | UNKNOWN | — | 0.61479 | openssh-client@1:10.0p1-7 | No | — | 0.5 🟢 Low |
| CVE-2020-24890 | UNKNOWN | — | 0.00449 | libraw23t64@0.21.4-2 | No | — | 0.5 🟢 Low |
| CVE-2020-36325 | UNKNOWN | — | 0.00257 | libjansson4@2.14-2+b3 | No | — | 0.5 🟢 Low |
| CVE-2021-32256 | UNKNOWN | — | 0.00162 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2021-35331 | UNKNOWN | — | 0.0029 | libtcl8.6@8.6.16+dfsg-1, tcl8.6-dev@8.6.16+dfsg-1, tcl8.6@8.6.16+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2021-4214 | UNKNOWN | — | 0.0013 | libpng-dev@1.6.48-1+deb13u1, libpng16-16t64@1.6.48-1+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2021-4217 | UNKNOWN | — | 0.00195 | unzip@6.0-29 | No | — | 0.5 🟢 Low |
| CVE-2021-45261 | UNKNOWN | — | 0.00202 | patch@2.8-2 | No | — | 0.5 🟢 Low |
| CVE-2021-45346 | UNKNOWN | — | 0.00378 | libsqlite3-0@3.46.1-7, libsqlite3-dev@3.46.1-7 | No | — | 0.5 🟢 Low |
| CVE-2022-0563 | UNKNOWN | — | 0.0002 | bsdutils@1:2.41-5, libblkid-dev@2.41-5, libblkid1@2.41-5, liblastlog2-2@2.41-5, libmount-dev@2.41-5, libmount1@2.41-5, libsmartcols1@2.41-5, libuuid1@2.41-5, login@1:4.16.0-2+really2.41-5, mount@2.41-5, util-linux@2.41-5, uuid-dev@2.41-5 | No | — | 0.5 🟢 Low |
| CVE-2022-1210 | UNKNOWN | — | 0.0005 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2022-24975 | UNKNOWN | — | 0.00666 | git-man@1:2.47.3-0+deb13u1, git@1:2.47.3-0+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2022-3219 | UNKNOWN | — | 0.00013 | dirmngr@2.4.7-21+deb13u1+b1, gnupg-l10n@2.4.7-21+deb13u1, gnupg@2.4.7-21+deb13u1, gpg-agent@2.4.7-21+deb13u1+b1, gpg@2.4.7-21+deb13u1+b1, gpgconf@2.4.7-21+deb13u1+b1, gpgsm@2.4.7-21+deb13u1+b1 | No | — | 0.5 🟢 Low |
| CVE-2023-31437 | UNKNOWN | — | 0.00128 | libsystemd0@257.9-1~deb13u1, libudev1@257.9-1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2023-31438 | UNKNOWN | — | 0.001 | libsystemd0@257.9-1~deb13u1, libudev1@257.9-1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2023-31439 | UNKNOWN | — | 0.00094 | libsystemd0@257.9-1~deb13u1, libudev1@257.9-1~deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2023-34152 | UNKNOWN | — | 0.74836 | imagemagick-7-common@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick-7.q16@8:7.1.1.43+dfsg1-1+deb13u5, imagemagick@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-arch-config@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10-extra@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickcore-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7-headers@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-10@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-7.q16-dev@8:7.1.1.43+dfsg1-1+deb13u5, libmagickwand-dev@8:7.1.1.43+dfsg1-1+deb13u5 | No | — | 0.5 🟢 Low |
| CVE-2023-37769 | UNKNOWN | — | 0.00047 | libpixman-1-0@0.44.0-3, libpixman-1-dev@0.44.0-3 | No | — | 0.5 🟢 Low |
| CVE-2024-2236 | UNKNOWN | — | 0.00222 | libgcrypt20@1.11.0-7 | No | — | 0.5 🟢 Low |
| CVE-2024-25260 | UNKNOWN | — | 0.00014 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2024-26458 | UNKNOWN | — | 0.00212 | krb5-multidev@1.21.3-5, libgssapi-krb5-2@1.21.3-5, libgssrpc4t64@1.21.3-5, libk5crypto3@1.21.3-5, libkadm5clnt-mit12@1.21.3-5, libkadm5srv-mit12@1.21.3-5, libkdb5-10t64@1.21.3-5, libkrb5-3@1.21.3-5, libkrb5-dev@1.21.3-5, libkrb5support0@1.21.3-5 | No | — | 0.5 🟢 Low |
| CVE-2024-26461 | UNKNOWN | — | 0.00063 | krb5-multidev@1.21.3-5, libgssapi-krb5-2@1.21.3-5, libgssrpc4t64@1.21.3-5, libk5crypto3@1.21.3-5, libkadm5clnt-mit12@1.21.3-5, libkadm5srv-mit12@1.21.3-5, libkdb5-10t64@1.21.3-5, libkrb5-3@1.21.3-5, libkrb5-dev@1.21.3-5, libkrb5support0@1.21.3-5 | No | — | 0.5 🟢 Low |
| CVE-2024-52005 | UNKNOWN | — | 0.00384 | git-man@1:2.47.3-0+deb13u1, git@1:2.47.3-0+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-11081 | UNKNOWN | — | 0.00019 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-1352 | UNKNOWN | — | 0.00398 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-1365 | UNKNOWN | — | 0.00067 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-1371 | UNKNOWN | — | 0.00055 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-1372 | UNKNOWN | — | 0.00104 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-1376 | UNKNOWN | — | 0.00068 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-1377 | UNKNOWN | — | 0.00073 | libelf1t64@0.192-4 | No | — | 0.5 🟢 Low |
| CVE-2025-29070 | UNKNOWN | — | 0.00654 | liblcms2-2@2.16-2, liblcms2-dev@2.16-2 | No | — | 0.5 🟢 Low |
| CVE-2025-61143 | UNKNOWN | — | 0.00017 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-61144 | UNKNOWN | — | 0.00018 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-61145 | UNKNOWN | — | 0.00017 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-61147 | UNKNOWN | — | 0.00012 | libde265-0@1.0.15-1+b3 | No | — | 0.5 🟢 Low |
| CVE-2025-66861 | UNKNOWN | — | 0.00027 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-66862 | UNKNOWN | — | 0.00073 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-66863 | UNKNOWN | — | 0.00073 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-66864 | UNKNOWN | — | 0.00042 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-66865 | UNKNOWN | — | 0.00073 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-66866 | UNKNOWN | — | 0.00042 | binutils-aarch64-linux-gnu@2.44-3, binutils-common@2.44-3, binutils@2.44-3, libbinutils@2.44-3, libctf-nobfd0@2.44-3, libctf0@2.44-3, libgprofng0@2.44-3, libsframe1@2.44-3 | No | — | 0.5 🟢 Low |
| CVE-2025-8176 | UNKNOWN | — | 0.00018 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-8177 | UNKNOWN | — | 0.00019 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-8534 | UNKNOWN | — | 0.00028 | libtiff-dev@4.7.0-3+deb13u1, libtiff6@4.7.0-3+deb13u1, libtiffxx6@4.7.0-3+deb13u1 | No | — | 0.5 🟢 Low |
| CVE-2025-8732 | UNKNOWN | — | 0.00013 | libxml2-dev@2.12.7+dfsg+really2.9.14-2.1+deb13u2, libxml2@2.12.7+dfsg+really2.9.14-2.1+deb13u2 | No | — | 0.5 🟢 Low |
| CVE-2026-22185 | UNKNOWN | — | 0.0002 | libldap-dev@2.6.10+dfsg-1, libldap2@2.6.10+dfsg-1 | No | — | 0.5 🟢 Low |
| CVE-2026-27171 | UNKNOWN | — | 6e-05 | zlib1g-dev@1:1.3.dfsg+really1.3.1-1+b1, zlib1g@1:1.3.dfsg+really1.3.1-1+b1 | No | — | 0.5 🟢 Low |
| GHSA-RCFX-77HG-W2WV | HIGH | — | — | fastmcp@2.13.3 | Yes | 2.14.0 | 0.0 ⚪ None |

## Risk Summary

| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |
|--------|------|----------|----------|----------|------|--------|-----|
| Vulners | 188 | 7.4 | 10.0 | 14 | 82 | 79 | 12 |
| Grype | 264 | 2.1 | 8.9 | 0 | 23 | 44 | 14 |
