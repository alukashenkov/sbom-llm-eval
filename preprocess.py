"""
SBOM Data Preprocessing — Strips audit JSON to CRA-relevant fields.

Extracts:
- Core vulnerability metadata (CVE, CVSS vector/version/source, EPSS + percentile, exploitation status)
- PoC/exploit signals from enchantments reference types
- AI-generated description and short fix hint from enchantments
- Published date → daysPublic age signal
- Pre-computed CRA Art. 3 exploitability tier per CVE
- Pre-computed CRA Art. 14 Track 1 & Track 2 trigger lists
- EPSS staleness count and age-risk top CVEs

Discards:
- Vendor advisory cross-reference ID lists (~90% of file size)
- Full descriptions beyond 300 chars
- Web applicability, tags, redundant reference arrays
"""

import json
from datetime import date, datetime

# Reference types that indicate PoC / exploit availability
POC_REFERENCE_TYPES = {
    "githubexploit",
    "packetstorm",
    "exploitdb",
    "hackerone",
    "nuclei",
    "zdt",
    "kitploit",
    "cisa_kev",
    "gitee",
}

# EPSS age threshold in days — older scores are flagged as lower-confidence
EPSS_STALE_DAYS = 90

# Thresholds for CRA Art. 3(41) exploitable tier
EPSS_EXPLOITABLE_THRESHOLD = 0.1  # 10% probability
CVSS_EXPLOITABLE_THRESHOLD = 9.0  # Critical-range CVSS


def _days_public(published_str: str | None) -> int | None:
    """Return how many days ago the advisory was published."""
    if not published_str:
        return None
    try:
        pub = datetime.fromisoformat(published_str.replace("Z", "+00:00")).date()
        return (date.today() - pub).days
    except (ValueError, TypeError):
        return None


def _epss_stale(epss_date_str: str | None) -> bool:
    """Return True if the EPSS score is older than EPSS_STALE_DAYS."""
    if not epss_date_str:
        return False
    try:
        epss_date = date.fromisoformat(epss_date_str)
        return (date.today() - epss_date).days > EPSS_STALE_DAYS
    except (ValueError, TypeError):
        return False


def _classify_cra_tier(
    wild_exploited: bool,
    cisa_kev: bool,
    epss_score: float | None,
    cvss_score: float | None,
    cvss_vector: str | None,
    has_poc: bool,
) -> str:
    """
    Classify a CVE into the CRA three-tier vulnerability taxonomy:
      ACTIVELY_EXPLOITED  — Art. 3(42): reliable evidence of in-the-wild malicious exploitation
      EXPLOITABLE         — Art. 3(41): potential to be effectively used under practical conditions
      VULNERABILITY       — Art. 3(40): weakness that can be exploited (no current evidence)
    """
    # Tier 3 — Art. 3(42)
    if wild_exploited or cisa_kev:
        return "ACTIVELY_EXPLOITED"

    # Tier 2 — Art. 3(41): practical exploitability signals
    if (
        (epss_score is not None and epss_score >= EPSS_EXPLOITABLE_THRESHOLD)
        or (cvss_score is not None and cvss_score >= CVSS_EXPLOITABLE_THRESHOLD)
        or has_poc
    ):
        return "EXPLOITABLE"

    # Also elevate to EXPLOITABLE if CVSS vector shows: network-reachable, low complexity,
    # no privileges, no user interaction required — regardless of score threshold
    if cvss_vector:
        v = cvss_vector.upper()
        if "AV:N" in v and "AC:L" in v and "PR:N" in v and "UI:N" in v:
            return "EXPLOITABLE"

    # Tier 1 — Art. 3(40)
    return "VULNERABILITY"


def _track2_heuristic(
    cvss_score: float | None,
    cvss_vector: str | None,
) -> bool:
    """
    Pre-flag CVEs as potential Art. 14(3) Track 2 severe-incident triggers.
    A severe incident can "negatively affect the ability of a PDE to protect
    availability, authenticity, integrity or confidentiality" — or enable
    malicious code execution in a user's system.

    Heuristic: CVSS ≥ 9.0 AND network-reachable (AV:N), OR full CIA:H/H/H impact.
    """
    if not cvss_score or cvss_score < 9.0:
        return False
    if not cvss_vector:
        return True  # High score without vector — flag conservatively
    v = cvss_vector.upper()
    # Must be network reachable
    if "AV:N" not in v:
        return False
    # At least one of: full CIA impact or scope change
    return "C:H" in v or "I:H" in v or "A:H" in v or "S:C" in v


def preprocess_advisory(adv: dict) -> dict:
    """Strip an advisory to CRA-relevant fields + PoC extraction."""
    # --- PoC sources from enchantments references ---
    poc_sources = {}
    enchantments = adv.get("enchantments") or {}
    deps = enchantments.get("dependencies") or {}
    for ref in deps.get("references", []):
        rtype = ref.get("type", "")
        if rtype in POC_REFERENCE_TYPES:
            poc_sources[rtype] = len(ref.get("idList", []))

    # --- Fix hint from enchantments short_description ---
    fix_hint = enchantments.get("short_description")
    if fix_hint:
        fix_hint = fix_hint[:150]

    # --- CVSS ---
    metrics = adv.get("metrics") or {}
    cvss = metrics.get("cvss") or {}
    cvss_score = cvss.get("score")
    severity = (cvss.get("severity") or "").upper() or None
    cvss_vector = cvss.get("vector") or None
    cvss_version = cvss.get("version") or None
    cvss_source = cvss.get("source") or None

    # --- EPSS ---
    epss_data = adv.get("epss") or []
    epss_entry = epss_data[0] if epss_data else {}
    epss_score = epss_entry.get("epss")
    epss_percentile = epss_entry.get("percentile")
    epss_date = epss_entry.get("date")

    # --- Description: prefer AI-generated, fall back to plain ---
    ai_desc = adv.get("aiDescription")
    plain_desc = adv.get("description", "")
    if ai_desc:
        description = str(ai_desc)[:300] + ("..." if len(str(ai_desc)) > 300 else "")
    else:
        description = plain_desc[:300] + ("..." if len(plain_desc) > 300 else "")

    # --- Published date → age ---
    published = adv.get("published")
    days_public = _days_public(published)

    # --- Exploitation ---
    exploitation = adv.get("exploitation") or {}
    wild_exploited = exploitation.get("wildExploited", False)
    has_kev = "cisa_kev" in poc_sources
    has_poc = bool(poc_sources)

    # --- CRA tier ---
    cra_tier = _classify_cra_tier(
        wild_exploited, has_kev, epss_score, cvss_score, cvss_vector, has_poc
    )

    return {
        "id": adv.get("id"),
        "title": adv.get("title"),
        "cvelist": adv.get("cvelist", []),
        "description": description,
        "fixHint": fix_hint or None,
        "publishedDate": published,
        "daysPublic": days_public,
        # CVSS
        "cvssScore": cvss_score,
        "cvssSeverity": severity,
        "cvssVector": cvss_vector,
        "cvssVersion": cvss_version,
        "cvssSource": cvss_source,
        # EPSS
        "epssScore": epss_score,
        "epssPercentile": epss_percentile,
        "epssDate": epss_date,
        "epssStale": _epss_stale(epss_date) if epss_date else None,
        # Exploitation
        "wildExploited": wild_exploited or None,
        "pocSources": poc_sources or None,
        "exploits": (
            [
                {"type": e.get("type"), "href": e.get("href")}
                for e in adv.get("exploits", [])
            ]
            or None
        ),
        # AI scoring
        "aiScore": adv.get("aiScore"),
        # CRA classification
        "craTier": cra_tier,
        "craTrack2Candidate": _track2_heuristic(cvss_score, cvss_vector) or None,
    }


def preprocess_file(filepath: str) -> dict:
    """Load a JSON report and strip to CRA-relevant data."""
    with open(filepath) as f:
        raw = json.load(f)

    meta = raw.get("meta", {})
    packages = raw.get("data", [])

    processed_data = []
    total_packages = len(packages)
    for pkg in packages:
        advisories = pkg.get("applicableAdvisories", [])
        if not advisories:
            continue
        processed_data.append(
            {
                "package": pkg.get("package"),
                "version": pkg.get("version"),
                "advisories": [preprocess_advisory(a) for a in advisories],
            }
        )

    analytics = compute_cve_analytics(processed_data)

    return {
        "meta": meta,
        "stats": {
            "totalPackages": total_packages,
            "affectedPackages": len(processed_data),
            "totalAdvisories": sum(len(p["advisories"]) for p in processed_data),
        },
        "cveAnalytics": analytics,
        "data": processed_data,
    }


def compute_cve_analytics(processed_data: list) -> dict:
    """Pre-compute CVE-level analytics to avoid LLM counting errors.

    Deduplicates CVEs across advisories and computes:
    - Unique CVE count and severity distribution
    - CRA Article 14 Track 1 mandatory triggers (wildExploited / cisa_kev)
    - CRA Article 14 Track 2 candidates (severe-incident heuristic)
    - CRA Art. 3 exploitability tier distribution
    - Exploit/PoC summary by source type
    - Per-package CVE breakdown
    - EPSS staleness count
    - Age-risk: top unpatched long-public high/critical CVEs
    """
    cve_map = {}  # cve_id -> merged info
    poc_by_type = {}  # source_type -> set of cve_ids
    pkg_cve_counts = {}  # package -> set of cve_ids

    sev_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}

    for pkg in processed_data:
        pkg_name = f"{pkg['package']}@{pkg['version']}"
        pkg_cves = set()

        for adv in pkg["advisories"]:
            cve_ids = adv.get("cvelist", [])
            if not cve_ids:
                adv_id = adv.get("id", "")
                if adv_id:
                    cve_ids = [adv_id]

            poc = adv.get("pocSources") or {}
            epss_score = adv.get("epssScore")
            epss_percentile = adv.get("epssPercentile")
            epss_date = adv.get("epssDate")
            cvss_score = adv.get("cvssScore")
            severity = adv.get("cvssSeverity")
            cvss_vector = adv.get("cvssVector")
            wild_exploited = adv.get("wildExploited") or False
            has_kev = poc and "cisa_kev" in poc
            cra_tier = adv.get("craTier", "VULNERABILITY")
            track2 = adv.get("craTrack2Candidate") or False
            days_public = adv.get("daysPublic")
            fix_hint = adv.get("fixHint")

            for cve_id in cve_ids:
                pkg_cves.add(cve_id)

                if cve_id not in cve_map:
                    cve_map[cve_id] = {
                        "severity": severity,
                        "cvss": cvss_score,
                        "cvssVector": cvss_vector,
                        "epss": epss_score,
                        "epssPercentile": epss_percentile,
                        "epssDate": epss_date,
                        "packages": set(),
                        "wildExploited": False,
                        "cisa_kev": False,
                        "craTier": cra_tier,
                        "craTrack2": False,
                        "daysPublic": days_public,
                        "fixHint": fix_hint,
                    }

                entry = cve_map[cve_id]
                entry["packages"].add(pkg_name)

                # Escalate exploitation flags
                if wild_exploited:
                    entry["wildExploited"] = True
                if has_kev:
                    entry["cisa_kev"] = True
                if track2:
                    entry["craTrack2"] = True

                # Keep highest CVSS severity
                if sev_order.get(severity, 0) > sev_order.get(entry["severity"], 0):
                    entry["severity"] = severity
                    entry["cvss"] = cvss_score
                    entry["cvssVector"] = cvss_vector

                # Keep highest EPSS score (fixes merge bug — previously took first seen)
                if epss_score is not None and (
                    entry["epss"] is None or epss_score > entry["epss"]
                ):
                    entry["epss"] = epss_score
                    entry["epssPercentile"] = epss_percentile
                    entry["epssDate"] = epss_date

                # Escalate CRA tier (ACTIVELY_EXPLOITED > EXPLOITABLE > VULNERABILITY)
                tier_order = {
                    "ACTIVELY_EXPLOITED": 3,
                    "EXPLOITABLE": 2,
                    "VULNERABILITY": 1,
                }
                if tier_order.get(cra_tier, 0) > tier_order.get(entry["craTier"], 0):
                    entry["craTier"] = cra_tier

                # Keep most days public (oldest first public date)
                if days_public is not None and (
                    entry["daysPublic"] is None or days_public > entry["daysPublic"]
                ):
                    entry["daysPublic"] = days_public

                # Keep first fix hint found
                if fix_hint and not entry["fixHint"]:
                    entry["fixHint"] = fix_hint

            # Track PoC sources
            for src_type in poc:
                if src_type not in poc_by_type:
                    poc_by_type[src_type] = set()
                for cve_id in cve_ids:
                    poc_by_type[src_type].add(cve_id)

        pkg_cve_counts[pkg_name] = len(pkg_cves)

    # --- Severity distribution ---
    severity_dist = {}
    for info in cve_map.values():
        sev = info["severity"] or "UNKNOWN"
        severity_dist[sev] = severity_dist.get(sev, 0) + 1

    # --- CRA tier distribution ---
    tier_dist = {}
    for info in cve_map.values():
        t = info["craTier"]
        tier_dist[t] = tier_dist.get(t, 0) + 1

    # --- Track 1 triggers (Art. 14(1)): actively exploited ---
    cra_triggers = []
    for cve_id, info in cve_map.items():
        if info["wildExploited"] or info["cisa_kev"]:
            cra_triggers.append(
                {
                    "cve": cve_id,
                    "cvss": info["cvss"],
                    "cvssVector": info["cvssVector"],
                    "epss": info["epss"],
                    "epssPercentile": info["epssPercentile"],
                    "packages": sorted(info["packages"]),
                    "wildExploited": info["wildExploited"],
                    "cisa_kev": info["cisa_kev"],
                    "daysPublic": info["daysPublic"],
                    "fixHint": info["fixHint"],
                }
            )
    # Sort by CVSS descending
    cra_triggers.sort(key=lambda x: x["cvss"] or 0, reverse=True)

    # --- Track 2 candidates (Art. 14(3)): severe-incident heuristic ---
    track2_candidates = []
    for cve_id, info in cve_map.items():
        if info["craTrack2"] and not (info["wildExploited"] or info["cisa_kev"]):
            track2_candidates.append(
                {
                    "cve": cve_id,
                    "cvss": info["cvss"],
                    "cvssVector": info["cvssVector"],
                    "epss": info["epss"],
                    "craTier": info["craTier"],
                    "packages": sorted(info["packages"]),
                    "fixHint": info["fixHint"],
                }
            )
    track2_candidates.sort(key=lambda x: x["cvss"] or 0, reverse=True)

    # --- EPSS staleness count ---
    epss_stale_count = sum(
        1 for info in cve_map.values() if _epss_stale(info.get("epssDate"))
    )

    # --- Age risk: top unpatched long-public CRITICAL/HIGH CVEs ---
    age_risk = sorted(
        [
            {
                "cve": cve_id,
                "severity": info["severity"],
                "cvss": info["cvss"],
                "daysPublic": info["daysPublic"],
                "fixHint": info["fixHint"],
                "packages": sorted(info["packages"]),
            }
            for cve_id, info in cve_map.items()
            if info["severity"] in ("CRITICAL", "HIGH")
            and info["daysPublic"] is not None
        ],
        key=lambda x: x["daysPublic"],
        reverse=True,
    )[:5]

    # --- Top affected packages ---
    top_packages = sorted(pkg_cve_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        "uniqueCVECount": len(cve_map),
        "severityDistribution": severity_dist,
        # CRA Art. 3 tier distribution
        "craTierDistribution": tier_dist,
        # CRA Art. 14 Track 1 — mandatory reporting triggers
        "craMandatoryTriggers": cra_triggers if cra_triggers else None,
        # CRA Art. 14 Track 2 — severe incident heuristic
        "craTrack2Candidates": track2_candidates if track2_candidates else None,
        # PoC summary
        "pocSummary": {k: len(v) for k, v in poc_by_type.items()},
        # EPSS confidence signal
        "epssStaleCount": epss_stale_count,
        # Age risk
        "ageRisk": age_risk if age_risk else None,
        # Top packages
        "topAffectedPackages": [
            {"package": p, "uniqueCVEs": c} for p, c in top_packages[:5]
        ],
    }


def preprocess_to_json(filepath: str) -> str:
    """Preprocess a file and return compact JSON string."""
    return json.dumps(preprocess_file(filepath), indent=None, ensure_ascii=False)
