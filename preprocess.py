"""
SBOM Data Preprocessing — Strips audit JSON to CRA-relevant fields.

Extracts:
- Core vulnerability metadata (CVE, CVSS, EPSS, exploitation status)
- PoC/exploit signals from enchantments reference types
- Package-level grouping with advisory counts

Discards:
- Vendor advisory cross-reference ID lists (~90% of file size)
- Full descriptions beyond 200 chars
- Web applicability, tags, redundant reference arrays
"""

import json

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


def preprocess_advisory(adv: dict) -> dict:
    """Strip an advisory to CRA-relevant fields + PoC extraction."""
    # Extract PoC sources from enchantments references
    poc_sources = {}
    enchantments = adv.get("enchantments", {})
    deps = enchantments.get("dependencies", {})
    for ref in deps.get("references", []):
        rtype = ref.get("type", "")
        if rtype in POC_REFERENCE_TYPES:
            poc_sources[rtype] = len(ref.get("idList", []))

    # Core fields
    desc = adv.get("description", "")
    return {
        "id": adv.get("id"),
        "title": adv.get("title"),
        "cvelist": adv.get("cvelist", []),
        "description": desc[:200] + ("..." if len(desc) > 200 else ""),
        "metrics": adv.get("metrics"),
        "epss": adv.get("epss"),
        "aiScore": adv.get("aiScore"),
        "exploitation": adv.get("exploitation"),
        "exploits": [
            {"type": e.get("type"), "href": e.get("href")}
            for e in adv.get("exploits", [])
        ]
        or None,
        "pocSources": poc_sources or None,
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
    - CRA Article 14 mandatory triggers (wildExploited / cisa_kev)
    - Exploit/PoC summary by source type
    - Per-package CVE breakdown
    """
    # Collect all CVE data: {cve_id: {best_severity, max_cvss, epss, packages, ...}}
    cve_map = {}  # cve_id -> merged info
    cra_triggers = []  # mandatory reporting entries
    poc_by_type = {}  # source_type -> set of cve_ids
    pkg_cve_counts = {}  # package -> set of cve_ids

    for pkg in processed_data:
        pkg_name = f"{pkg['package']}@{pkg['version']}"
        pkg_cves = set()

        for adv in pkg["advisories"]:
            cve_ids = adv.get("cvelist", [])
            if not cve_ids:
                # Use advisory ID for non-CVE advisories (e.g. GHSA)
                adv_id = adv.get("id", "")
                if adv_id:
                    cve_ids = [adv_id]
            poc = adv.get("pocSources") or {}
            exploitation = adv.get("exploitation") or {}
            metrics = adv.get("metrics") or {}
            epss_data = adv.get("epss") or []
            epss_score = epss_data[0].get("epss") if epss_data else None

            # Extract CVSS info
            cvss_score = None
            severity = None
            cvss = metrics.get("cvss")
            if cvss:
                cvss_score = cvss.get("score")
                severity = (cvss.get("severity") or "").upper()

            # Check CRA triggers
            is_wild = exploitation.get("wildExploited", False)
            has_kev = "cisa_kev" in poc

            for cve_id in cve_ids:
                pkg_cves.add(cve_id)

                if cve_id not in cve_map:
                    cve_map[cve_id] = {
                        "severity": severity,
                        "cvss": cvss_score,
                        "epss": epss_score,
                        "packages": set(),
                        "wildExploited": False,
                        "cisa_kev": False,
                    }

                entry = cve_map[cve_id]
                entry["packages"].add(pkg_name)
                if is_wild:
                    entry["wildExploited"] = True
                if has_kev:
                    entry["cisa_kev"] = True
                # Keep highest severity
                sev_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
                if sev_order.get(severity, 0) > sev_order.get(entry["severity"], 0):
                    entry["severity"] = severity
                    entry["cvss"] = cvss_score

            # Track PoC sources
            for src_type in poc:
                if src_type not in poc_by_type:
                    poc_by_type[src_type] = set()
                for cve_id in cve_ids:
                    poc_by_type[src_type].add(cve_id)

        pkg_cve_counts[pkg_name] = len(pkg_cves)

    # Build severity distribution
    severity_dist = {}
    for cve_id, info in cve_map.items():
        sev = info["severity"] or "UNKNOWN"
        severity_dist[sev] = severity_dist.get(sev, 0) + 1

    # Build CRA triggers list
    for cve_id, info in cve_map.items():
        if info["wildExploited"] or info["cisa_kev"]:
            cra_triggers.append(
                {
                    "cve": cve_id,
                    "cvss": info["cvss"],
                    "epss": info["epss"],
                    "packages": sorted(info["packages"]),
                    "wildExploited": info["wildExploited"],
                    "cisa_kev": info["cisa_kev"],
                }
            )

    # Sort packages by CVE count
    top_packages = sorted(pkg_cve_counts.items(), key=lambda x: x[1], reverse=True)

    return {
        "uniqueCVECount": len(cve_map),
        "severityDistribution": severity_dist,
        "craMandatoryTriggers": cra_triggers if cra_triggers else None,
        "pocSummary": {k: len(v) for k, v in poc_by_type.items()},
        "topAffectedPackages": [
            {"package": p, "uniqueCVEs": c} for p, c in top_packages[:5]
        ],
    }


def preprocess_to_json(filepath: str) -> str:
    """Preprocess a file and return compact JSON string."""
    return json.dumps(preprocess_file(filepath), indent=None, ensure_ascii=False)
