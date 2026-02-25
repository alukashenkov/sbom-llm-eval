#!/usr/bin/env python3
"""
Grype vs Vulners SBOM Audit Comparison.

Cross-references grype and Vulners vulnerability findings per SBOM,
computes per-CVE risk scores, and generates markdown comparison reports.

Usage:
    python compare_sources.py
    python compare_sources.py --vulners vulners_results/ --grype grype_results/ --output comparisons/
"""

import argparse
import json
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Vulnerability ID normalisation
# ---------------------------------------------------------------------------
def normalize_vuln_id(raw_id: str) -> str:
    """Normalise a vulnerability ID for cross-source matching.

    - Strips 'OSV:' prefix (Vulners uses 'OSV:GHSA-xxx')
    - Lowercases GHSA IDs (Vulners uppercase, grype lowercase)
    - CVE IDs are kept as-is (already consistent)
    """
    vid = raw_id.strip()
    # Strip OSV: prefix
    if vid.upper().startswith("OSV:"):
        vid = vid[4:]
    # Normalise GHSA to lowercase
    if vid.upper().startswith("GHSA-"):
        vid = vid.upper()
    return vid


# ---------------------------------------------------------------------------
# Risk score computation
# ---------------------------------------------------------------------------
def compute_risk_score(
    cvss: float | None,
    epss: float | None,
    wild_exploited: bool = False,
    has_poc: bool = False,
    fix_available: bool = True,
) -> float:
    """Compute risk score (0-10) from vulnerability attributes.

    Formula:
    - Base = CVSS score (0-10)
    - EPSS multiplier: ×1.5 if >0.5, ×1.2 if >0.1
    - Exploit bonus: +2 if wildExploited, +1 if PoC
    - Fix penalty: +0.5 if no fix available
    - Capped at 10.0
    """
    score = cvss or 0.0

    if epss is not None:
        if epss > 0.5:
            score *= 1.5
        elif epss > 0.1:
            score *= 1.2

    if wild_exploited:
        score += 2.0
    elif has_poc:
        score += 1.0

    if not fix_available:
        score += 0.5

    return min(score, 10.0)


# ---------------------------------------------------------------------------
# Data extraction — Vulners
# ---------------------------------------------------------------------------
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


def extract_vulners_cves(filepath: str) -> dict:
    """Extract normalised vulnerability records from a Vulners audit JSON.

    Returns {vuln_id: {severity, cvss, epss, packages, ...}}.
    Includes both CVE-based and non-CVE advisories (e.g. GHSA).
    """
    with open(filepath) as f:
        raw = json.load(f)

    cve_map = {}  # normalised_id -> merged record

    for pkg in raw.get("data", []):
        pkg_name = f"{pkg.get('package', '?')}@{pkg.get('version', '?')}"

        for adv in pkg.get("applicableAdvisories", []):
            # Collect vulnerability IDs: CVEs if present, else advisory ID
            cve_ids = adv.get("cvelist", [])
            if not cve_ids:
                # Use advisory ID as the vulnerability identifier
                adv_id = adv.get("id", "")
                if adv_id:
                    cve_ids = [adv_id]
                else:
                    continue

            metrics = adv.get("metrics", {})
            cvss_info = metrics.get("cvss", {})
            cvss_score = cvss_info.get("score")
            severity = (cvss_info.get("severity") or "").upper()

            epss_data = adv.get("epss", [])
            epss_score = epss_data[0].get("epss") if epss_data else None

            exploitation = adv.get("exploitation", {})
            wild = exploitation.get("wildExploited", False)

            # Check for PoC references
            has_poc = False
            enchantments = adv.get("enchantments", {})
            deps = enchantments.get("dependencies", {})
            for ref in deps.get("references", []):
                if ref.get("type", "") in POC_REFERENCE_TYPES:
                    has_poc = True
                    break

            for raw_id in cve_ids:
                vuln_id = normalize_vuln_id(raw_id)
                if not vuln_id:
                    continue

                if vuln_id not in cve_map:
                    cve_map[vuln_id] = {
                        "cve_id": vuln_id,
                        "severity": severity,
                        "cvss": cvss_score,
                        "epss": epss_score,
                        "packages": set(),
                        "wild_exploited": False,
                        "has_poc": False,
                        "fix_available": False,
                        "fix_versions": [],
                    }

                entry = cve_map[vuln_id]
                entry["packages"].add(pkg_name)
                if wild:
                    entry["wild_exploited"] = True
                if has_poc:
                    entry["has_poc"] = True
                # Keep highest severity
                sev_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
                if sev_order.get(severity, 0) > sev_order.get(entry["severity"], 0):
                    entry["severity"] = severity
                    entry["cvss"] = cvss_score

    # Compute risk scores
    for entry in cve_map.values():
        entry["risk_score"] = compute_risk_score(
            entry["cvss"],
            entry["epss"],
            entry["wild_exploited"],
            entry["has_poc"],
            entry["fix_available"],
        )

    return cve_map


# ---------------------------------------------------------------------------
# Data extraction — Grype
# ---------------------------------------------------------------------------
def extract_grype_cves(filepath: str) -> dict:
    """Extract normalised vulnerability records from a grype JSON.

    Returns {vuln_id: {severity, cvss, epss, packages, ...}}.
    Handles both CVE and GHSA primary IDs.
    """
    with open(filepath) as f:
        raw = json.load(f)

    cve_map = {}

    for m in raw.get("matches", []):
        vuln = m.get("vulnerability", {})
        artifact = m.get("artifact", {})
        fix = vuln.get("fix", {})

        raw_id = vuln.get("id", "")
        if not raw_id:
            continue
        vuln_id = normalize_vuln_id(raw_id)

        sev = (vuln.get("severity") or "Unknown").upper()
        # Normalise severity
        if sev not in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
            sev = "UNKNOWN"

        cvss_list = vuln.get("cvss", [])
        cvss_score = None
        if cvss_list:
            cvss_score = cvss_list[0].get("metrics", {}).get("baseScore")

        epss_list = vuln.get("epss", [])
        epss_score = None
        if epss_list:
            epss_score = epss_list[0].get("epss")

        fix_state = fix.get("state", "unknown")
        fix_versions = fix.get("versions", [])
        fix_available = fix_state == "fixed"

        pkg_name = f"{artifact.get('name', '?')}@{artifact.get('version', '?')}"

        if vuln_id not in cve_map:
            cve_map[vuln_id] = {
                "cve_id": vuln_id,
                "severity": sev,
                "cvss": cvss_score,
                "epss": epss_score,
                "packages": set(),
                "wild_exploited": False,
                "has_poc": False,
                "fix_available": fix_available,
                "fix_versions": fix_versions,
            }

        entry = cve_map[vuln_id]
        entry["packages"].add(pkg_name)
        if fix_available:
            entry["fix_available"] = True
            if fix_versions:
                entry["fix_versions"] = list(set(entry["fix_versions"] + fix_versions))

        # Keep highest severity
        sev_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
        if sev_order.get(sev, 0) > sev_order.get(entry["severity"], 0):
            entry["severity"] = sev
            entry["cvss"] = cvss_score

    # Compute risk scores
    for entry in cve_map.values():
        entry["risk_score"] = compute_risk_score(
            entry["cvss"],
            entry["epss"],
            entry["wild_exploited"],
            entry["has_poc"],
            entry["fix_available"],
        )

    return cve_map


# ---------------------------------------------------------------------------
# Filename mapping
# ---------------------------------------------------------------------------
def find_grype_file(grype_dir: Path, vulners_stem: str) -> Path | None:
    """Map a vulners filename stem to its grype counterpart."""
    prefix = "package-analysis-report-"
    key = vulners_stem
    if key.startswith(prefix):
        key = key[len(prefix) :]

    grype_path = grype_dir / f"grype_{key}.json"
    return grype_path if grype_path.exists() else None


# ---------------------------------------------------------------------------
# Comparison logic
# ---------------------------------------------------------------------------
def compare_sources(vulners_cves: dict, grype_cves: dict) -> dict:
    """Cross-reference vulners and grype CVE maps.

    Returns a structured comparison dict.
    """
    v_ids = set(vulners_cves.keys())
    g_ids = set(grype_cves.keys())

    both = sorted(v_ids & g_ids)
    vulners_only = sorted(v_ids - g_ids)
    grype_only = sorted(g_ids - v_ids)
    all_ids = sorted(v_ids | g_ids)

    # Package coverage
    v_pkgs = set()
    for entry in vulners_cves.values():
        v_pkgs.update(entry["packages"])
    g_pkgs = set()
    for entry in grype_cves.values():
        g_pkgs.update(entry["packages"])

    # Build comparison records for shared CVEs
    shared_records = []
    for cve_id in both:
        v = vulners_cves[cve_id]
        g = grype_cves[cve_id]
        shared_records.append(
            {
                "cve_id": cve_id,
                "vulners": v,
                "grype": g,
                "severity_match": v["severity"] == g["severity"],
                "cvss_match": v["cvss"] == g["cvss"],
                "risk_delta": abs((v["risk_score"] or 0) - (g["risk_score"] or 0)),
            }
        )

    return {
        "total_vulners": len(v_ids),
        "total_grype": len(g_ids),
        "total_unique": len(all_ids),
        "overlap_count": len(both),
        "overlap_pct": round(len(both) / len(all_ids) * 100, 1) if all_ids else 0,
        "vulners_only_count": len(vulners_only),
        "grype_only_count": len(grype_only),
        "vulners_packages": sorted(v_pkgs),
        "grype_packages": sorted(g_pkgs),
        "packages_both": sorted(v_pkgs & g_pkgs),
        "packages_vulners_only": sorted(v_pkgs - g_pkgs),
        "packages_grype_only": sorted(g_pkgs - v_pkgs),
        "shared": shared_records,
        "vulners_only": [vulners_cves[c] for c in vulners_only],
        "grype_only": [grype_cves[c] for c in grype_only],
    }


# ---------------------------------------------------------------------------
# Risk label
# ---------------------------------------------------------------------------
def risk_label(score: float) -> str:
    """Convert numeric risk to a label."""
    if score >= 9.0:
        return "🔴 Critical"
    if score >= 7.0:
        return "🟠 High"
    if score >= 4.0:
        return "🟡 Medium"
    if score >= 0.1:
        return "🟢 Low"
    return "⚪ None"


# ---------------------------------------------------------------------------
# Markdown report generation
# ---------------------------------------------------------------------------
def generate_report(comparison: dict, sbom_name: str) -> str:
    """Generate a markdown comparison report."""
    lines = [f"# Source Comparison: {sbom_name}\n"]

    # Overview
    lines.append("## Overview\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Vulners CVEs | {comparison['total_vulners']} |")
    lines.append(f"| Grype CVEs | {comparison['total_grype']} |")
    lines.append(f"| Total unique CVEs | {comparison['total_unique']} |")
    lines.append(
        f"| Overlap | {comparison['overlap_count']} ({comparison['overlap_pct']}%) |"
    )
    lines.append(f"| Vulners-only | {comparison['vulners_only_count']} |")
    lines.append(f"| Grype-only | {comparison['grype_only_count']} |\n")

    # Package coverage
    lines.append("## Package Coverage\n")
    if comparison["packages_both"]:
        lines.append("**In both sources:**")
        for p in comparison["packages_both"]:
            lines.append(f"- {p}")
        lines.append("")
    if comparison["packages_vulners_only"]:
        lines.append("**Vulners only:**")
        for p in comparison["packages_vulners_only"]:
            lines.append(f"- {p}")
        lines.append("")
    if comparison["packages_grype_only"]:
        lines.append("**Grype only:**")
        for p in comparison["packages_grype_only"]:
            lines.append(f"- {p}")
        lines.append("")

    # CVEs in both sources
    if comparison["shared"]:
        lines.append("## CVEs Found in Both Sources\n")
        lines.append(
            "| CVE | Severity | Vulners CVSS | Grype CVSS | "
            "Vulners EPSS | Grype EPSS | Vulners Risk | Grype Risk | Match |"
        )
        lines.append(
            "|-----|----------|-------------|------------|"
            "-------------|------------|-------------|------------|-------|"
        )
        for rec in comparison["shared"]:
            v, g = rec["vulners"], rec["grype"]
            sev_icon = "✅" if rec["severity_match"] else "⚠️"
            match = "✅" if rec["severity_match"] and rec["cvss_match"] else "⚠️"
            lines.append(
                f"| {rec['cve_id']} "
                f"| {v['severity']}/{g['severity']} {sev_icon} "
                f"| {v['cvss'] or '—'} | {g['cvss'] or '—'} "
                f"| {v['epss'] or '—'} | {g['epss'] or '—'} "
                f"| {v['risk_score']:.1f} {risk_label(v['risk_score'])} "
                f"| {g['risk_score']:.1f} {risk_label(g['risk_score'])} "
                f"| {match} |"
            )
        lines.append("")

    # CVEs only in Vulners
    if comparison["vulners_only"]:
        lines.append("## CVEs Only in Vulners\n")
        lines.append(
            "| CVE | Severity | CVSS | EPSS | Package | Wild Exploited | PoC | Risk |"
        )
        lines.append(
            "|-----|----------|------|------|---------|---------------|-----|------|"
        )
        for entry in sorted(
            comparison["vulners_only"],
            key=lambda x: x["risk_score"],
            reverse=True,
        ):
            pkgs = ", ".join(sorted(entry["packages"]))
            lines.append(
                f"| {entry['cve_id']} | {entry['severity']} "
                f"| {entry['cvss'] or '—'} | {entry['epss'] or '—'} "
                f"| {pkgs} "
                f"| {'Yes' if entry['wild_exploited'] else 'No'} "
                f"| {'Yes' if entry['has_poc'] else 'No'} "
                f"| {entry['risk_score']:.1f} {risk_label(entry['risk_score'])} |"
            )
        lines.append("")

    # CVEs only in Grype
    if comparison["grype_only"]:
        lines.append("## CVEs Only in Grype\n")
        lines.append(
            "| CVE | Severity | CVSS | EPSS | Package | "
            "Fix Available | Fix Versions | Risk |"
        )
        lines.append(
            "|-----|----------|------|------|---------|"
            "--------------|-------------|------|"
        )
        for entry in sorted(
            comparison["grype_only"],
            key=lambda x: x["risk_score"],
            reverse=True,
        ):
            pkgs = ", ".join(sorted(entry["packages"]))
            fix_v = ", ".join(entry["fix_versions"]) if entry["fix_versions"] else "—"
            lines.append(
                f"| {entry['cve_id']} | {entry['severity']} "
                f"| {entry['cvss'] or '—'} | {entry['epss'] or '—'} "
                f"| {pkgs} "
                f"| {'Yes' if entry['fix_available'] else 'No'} "
                f"| {fix_v} "
                f"| {entry['risk_score']:.1f} {risk_label(entry['risk_score'])} |"
            )
        lines.append("")

    # Risk summary
    lines.append("## Risk Summary\n")

    lines.append(
        "| Source | CVEs | Avg Risk | Max Risk | Critical | High | Medium | Low |"
    )
    lines.append(
        "|--------|------|----------|----------|----------|------|--------|-----|"
    )

    for label, cves_data, source_key in [
        (
            "Vulners",
            comparison["vulners_only"] + [r["vulners"] for r in comparison["shared"]],
            None,
        ),
        (
            "Grype",
            comparison["grype_only"] + [r["grype"] for r in comparison["shared"]],
            None,
        ),
    ]:
        if not cves_data:
            lines.append(f"| {label} | 0 | — | — | 0 | 0 | 0 | 0 |")
            continue
        risks = [c["risk_score"] for c in cves_data]
        sevs = [c["severity"] for c in cves_data]
        lines.append(
            f"| {label} | {len(cves_data)} "
            f"| {sum(risks) / len(risks):.1f} "
            f"| {max(risks):.1f} "
            f"| {sevs.count('CRITICAL')} "
            f"| {sevs.count('HIGH')} "
            f"| {sevs.count('MEDIUM')} "
            f"| {sevs.count('LOW')} |"
        )

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Generate JSON summary (for judge consumption)
# ---------------------------------------------------------------------------
def generate_json_summary(comparison: dict) -> dict:
    """Generate a compact JSON summary for judge consumption."""

    def _entry_to_dict(e):
        return {
            "cve": e["cve_id"],
            "severity": e["severity"],
            "cvss": e["cvss"],
            "epss": e["epss"],
            "packages": sorted(e["packages"]),
            "risk_score": round(e["risk_score"], 1),
            "wild_exploited": e.get("wild_exploited", False),
            "has_poc": e.get("has_poc", False),
            "fix_available": e.get("fix_available", False),
        }

    shared = []
    for rec in comparison["shared"]:
        shared.append(
            {
                "cve": rec["cve_id"],
                "vulners": _entry_to_dict(rec["vulners"]),
                "grype": _entry_to_dict(rec["grype"]),
                "severity_match": rec["severity_match"],
            }
        )

    return {
        "overview": {
            "vulners_cves": comparison["total_vulners"],
            "grype_cves": comparison["total_grype"],
            "total_unique": comparison["total_unique"],
            "overlap": comparison["overlap_count"],
            "overlap_pct": comparison["overlap_pct"],
        },
        "packages": {
            "both": comparison["packages_both"],
            "vulners_only": comparison["packages_vulners_only"],
            "grype_only": comparison["packages_grype_only"],
        },
        "cves_in_both": shared,
        "cves_vulners_only": [_entry_to_dict(e) for e in comparison["vulners_only"]],
        "cves_grype_only": [_entry_to_dict(e) for e in comparison["grype_only"]],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Compare Grype and Vulners SBOM audit results"
    )
    parser.add_argument(
        "--vulners",
        default="vulners_results",
        help="Directory with Vulners audit JSON files (default: vulners_results/)",
    )
    parser.add_argument(
        "--grype",
        default="grype_results",
        help="Directory with Grype JSON results (default: grype_results/)",
    )
    parser.add_argument(
        "--output",
        default="comparisons",
        help="Output directory for comparison reports (default: comparisons/)",
    )

    args = parser.parse_args()
    vulners_dir = Path(args.vulners)
    grype_dir = Path(args.grype)
    output_dir = Path(args.output)

    vulners_files = sorted(vulners_dir.glob("*.json"))
    if not vulners_files:
        print(f"No JSON files found in {vulners_dir}")
        sys.exit(1)

    print(f"Found {len(vulners_files)} Vulners files")
    print(f"Grype directory: {grype_dir}")
    print(f"Output directory: {output_dir}\n")

    for vf in vulners_files:
        sbom_name = vf.stem
        # Strip package-analysis-report- prefix for display
        display_name = sbom_name
        prefix = "package-analysis-report-"
        if display_name.startswith(prefix):
            display_name = display_name[len(prefix) :]

        print(f"{'=' * 60}")
        print(f"Comparing: {display_name}")
        print(f"{'=' * 60}")

        # Find matching grype file
        gf = find_grype_file(grype_dir, sbom_name)
        if not gf:
            print("  WARNING: No grype file found, skipping")
            continue

        # Extract CVEs
        vulners_cves = extract_vulners_cves(str(vf))
        grype_cves = extract_grype_cves(str(gf))

        print(f"  Vulners: {len(vulners_cves)} CVEs")
        print(f"  Grype:   {len(grype_cves)} CVEs")

        # Compare
        comparison = compare_sources(vulners_cves, grype_cves)

        print(
            f"  Overlap: {comparison['overlap_count']} ({comparison['overlap_pct']}%)"
        )
        print(f"  Vulners-only: {comparison['vulners_only_count']}")
        print(f"  Grype-only: {comparison['grype_only_count']}")

        # Generate outputs
        sbom_dir = output_dir / display_name
        sbom_dir.mkdir(parents=True, exist_ok=True)

        # Markdown report
        report = generate_report(comparison, display_name)
        md_path = sbom_dir / "comparison.md"
        md_path.write_text(report)
        print(f"  Report: {md_path}")

        # JSON summary (for judge)
        json_summary = generate_json_summary(comparison)
        json_path = sbom_dir / "comparison.json"
        with open(json_path, "w") as f:
            json.dump(json_summary, f, indent=2)
        print(f"  JSON:   {json_path}")

    print(f"\nDone. Reports written to {output_dir}/")


if __name__ == "__main__":
    main()
