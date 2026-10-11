from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
RUN_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_first_pass_runtime_selector_run_001_020_G1_VIRAL_001"
BRIDGE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEBRIDGEAUD020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-AUDIT-001-008-014-019-001"
HUMAN_DECISION = "Ок иди по плану, ты оркестратор, следи чтоб все было сделанл"
AUDIT_PAGES = ["001", "002", "003", "004", "005", "006", "007", "008", "014", "019"]
REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
NEXT_ROUTES = {
    "visual_only_no_text_rule",
    "fresh_ocr_route_possible",
    "fresh_ocr_assets_missing",
    "needs_source_asset_recovery",
}

INPUT_HASHES = {
    "C01TEFPSRUN020-G1-VIRAL-001.report": (
        RUN_ROOT / "first_pass_runtime_selector_run_001_020_report.json",
        "2896B6D682A38AACC713FEC4E60015A8840008B161D0364C2EEC825B4B85041B",
    ),
    "C01TEFPSRUN020-G1-VIRAL-001.manifest": (
        RUN_ROOT / "first_pass_runtime_selector_run_001_020_manifest.md",
        "9E931134745B8C1C6E898E3D451D3EE8F36A3C12BA9C9734C5FD300A0C07B5CD",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.selector_v4": (
        BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json",
        "A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries": (
        BRIDGE_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json",
        "D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_mutation",
    "raw_mutation",
    "fixture_admission",
    "production_assembly",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
    "promotion",
    "acceptance",
    "downstream_execution",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Audit bridge pages 001-008/014/019 for fresh first-pass route planning.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("bridge page audit is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"bridge page audit requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("bridge page audit requires the exact bounded human decision")


def latest_review_dir(page: str) -> Path | None:
    pattern = f"page_complete_review_p{page}_G1_VIRAL_*"
    dirs = [path for path in TRIAL_ROOT.glob(pattern) if path.is_dir()]
    if not dirs:
        return None

    def key(path: Path) -> int:
        match = re.search(r"_G1_VIRAL_(\d+)$", path.name)
        return int(match.group(1)) if match else 0

    return sorted(dirs, key=key)[-1]


def git_head() -> str:
    result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def pinned_file(path: Path) -> dict[str, str]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}


def pinned_files(paths: list[Path]) -> list[dict[str, str]]:
    return [pinned_file(path) for path in paths]


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict], list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if "Status: `first_pass_runtime_selector_output_surface_materialized_with_bridge_lineage`" not in ledger:
        raise SystemExit("predecessor runtime selector output materialization is not synced in ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    run_report = read_json(RUN_ROOT / "first_pass_runtime_selector_run_001_020_report.json")
    selector_v4 = read_json(BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json")
    bridge_entries = read_json(BRIDGE_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json")
    if sorted(run_report["bridge_lineage_pages"]) != AUDIT_PAGES:
        raise SystemExit(f"runtime bridge page set drifted: {run_report['bridge_lineage_pages']}")
    if sorted(entry["page"] for entry in bridge_entries) != AUDIT_PAGES:
        raise SystemExit("bridge entries page set drifted")
    return verified, run_report, selector_v4, bridge_entries


def classify_page(selector_item: dict) -> dict:
    page = selector_item["page"]
    report_path = ROOT / selector_item["acceptance_report_path"]
    report_hash = sha256_file(report_path)
    if report_hash != selector_item["acceptance_report_sha256"]:
        raise SystemExit(f"P{page} acceptance report hash mismatch: {report_hash}")
    acceptance_report = read_json(report_path)
    review_dir = latest_review_dir(page)
    assets = review_dir / "review_assets" if review_dir else None
    text_evidence = sorted(assets.glob("*text-evidence.png")) if assets and assets.exists() else []
    page_image = assets / f"page_{page}.png" if assets else None
    text_maps = sorted(assets.glob("*text_map.md")) if assets and assets.exists() else []
    ocr_maps = sorted(assets.glob("*ocr_verified_text_map.md")) if assets and assets.exists() else []
    semantic_maps = sorted(assets.glob("*semantic_text_map.md")) if assets and assets.exists() else []
    none_categories = (
        acceptance_report.get("page_complete_acceptance", {}).get("declared_none_categories")
        or acceptance_report.get("declared_none_categories")
        or []
    )
    declares_no_source_text = "source_text" in none_categories and "table" in none_categories
    if review_dir is None or assets is None or not assets.exists():
        next_route = "needs_source_asset_recovery"
        route_reason = "review_assets_missing"
        missing_assets = ["review_assets"]
    elif not text_evidence and not text_maps and not ocr_maps and declares_no_source_text:
        next_route = "visual_only_no_text_rule"
        route_reason = "page_complete_acceptance_declares_no_source_text_and_no_text_assets_found"
        missing_assets = []
    elif (page_image and page_image.exists()) or text_evidence:
        next_route = "fresh_ocr_route_possible"
        route_reason = "asset_availability_only_page_image_or_text_evidence_present"
        missing_assets = []
    else:
        next_route = "fresh_ocr_assets_missing"
        route_reason = "text_route_expected_but_no_page_image_or_text_evidence_found"
        missing_assets = ["page_image_or_text_evidence"]
    if next_route not in NEXT_ROUTES:
        raise SystemExit(f"P{page} unsupported next route: {next_route}")
    return {
        "page": page,
        "selector_decision": selector_item["selector_decision"],
        "source_lane_id": selector_item["source_lane_id"],
        "acceptance_report_path": selector_item["acceptance_report_path"],
        "acceptance_report_sha256": report_hash,
        "review_dir": review_dir.relative_to(ROOT).as_posix() if review_dir else None,
        "review_assets_dir": assets.relative_to(ROOT).as_posix() if assets and assets.exists() else None,
        "page_image_exists": bool(page_image and page_image.exists()),
        "page_image": pinned_file(page_image) if page_image and page_image.exists() else None,
        "text_evidence_crop_count": len(text_evidence),
        "text_evidence_crops": pinned_files(text_evidence),
        "text_map_count": len(text_maps),
        "text_maps": pinned_files(text_maps),
        "ocr_verified_text_map_count": len(ocr_maps),
        "ocr_verified_text_maps": pinned_files(ocr_maps),
        "semantic_text_map_count": len(semantic_maps),
        "semantic_text_maps": pinned_files(semantic_maps),
        "declares_no_source_text": declares_no_source_text,
        "asset_classification": "bridge_page_existing_asset_audit",
        "bridge_lineage_fresh_ocr": False,
        "recommended_next_route": next_route,
        "next_route": next_route,
        "route_reason": route_reason,
        "missing_assets": missing_assets,
        "fresh_ocr_success_created": False,
        "production_or_acceptance_created": False,
        "no_mutation_performed": True,
    }


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def write_summary(report: dict) -> None:
    lines = [
        "# Bridge Page Audit 001-008 014 019 - C01TEBRIDGEAUD020-G1-VIRAL-001",
        "",
        "Status: `bridge_page_audit_completed_no_ocr_no_mutation`",
        "",
        "| Page | Next route | Text crops | Text maps | OCR maps | Page image |",
        "|---|---|---:|---:|---:|---|",
    ]
    for page in report["page_audit"]:
        lines.append(
            f"| `{page['page']}` | `{page['recommended_next_route']}` | `{page['text_evidence_crop_count']}` | "
            f"`{page['text_map_count']}` | `{page['ocr_verified_text_map_count']}` | `{str(page['page_image_exists']).lower()}` |"
        )
    lines.extend(
        [
            "",
            "This audit does not execute OCR and does not count bridge lineage as fresh first-pass success.",
            "",
            f"Pages requiring visual-only/no-text rule: `{', '.join(report['visual_only_no_text_rule_pages']) or 'none'}`.",
            f"Pages with possible fresh OCR route: `{', '.join(report['fresh_ocr_route_possible_pages']) or 'none'}`.",
            f"Pages needing source asset recovery: `{', '.join(report['needs_source_asset_recovery_pages']) or 'none'}`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "bridge_page_audit_001_008_014_019_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Bridge Page Audit 001-008 014 019 Manifest - C01TEBRIDGEAUD020-G1-VIRAL-001",
        "",
        "Boundary: report-only audit; no OCR execution, no mutation, no page 021+.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "bridge_page_audit_001_008_014_019_manifest.md":
            lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    lines.append("")
    write_text(OUT_ROOT / "bridge_page_audit_001_008_014_019_manifest.md", "\n".join(lines))


def build() -> None:
    verified_inputs, run_report, selector_v4, _bridge_entries = verify_inputs()
    selector_by_page = {item["page"]: item for item in selector_v4}
    audit = [classify_page(selector_by_page[page]) for page in AUDIT_PAGES]
    route_groups: dict[str, list[str]] = {}
    for item in audit:
        route_groups.setdefault(item["recommended_next_route"], []).append(item["page"])
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "bridge_page_audit_completed_no_ocr_no_mutation",
        "base_commit": git_head(),
        "human_decision": HUMAN_DECISION,
        "input_lane_id": run_report["lane_id"],
        "requested_pages": REQUESTED_PAGES,
        "audit_pages": AUDIT_PAGES,
        "audited_bridge_pages": AUDIT_PAGES,
        "page_audit": audit,
        "visual_only_no_text_rule_pages": route_groups.get("visual_only_no_text_rule", []),
        "fresh_ocr_route_possible_pages": route_groups.get("fresh_ocr_route_possible", []),
        "fresh_ocr_assets_missing_pages": route_groups.get("fresh_ocr_assets_missing", []),
        "needs_source_asset_recovery_pages": route_groups.get("needs_source_asset_recovery", []),
        "all_bridge_pages_remain_non_fresh": True,
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "runtime_execution_performed": False,
        "production_ready": False,
        "production_assembly_authorized": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "fixture_admission_performed": False,
        "page_021_plus_included": False,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    write_json(OUT_ROOT / "bridge_page_audit_001_008_014_019_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
