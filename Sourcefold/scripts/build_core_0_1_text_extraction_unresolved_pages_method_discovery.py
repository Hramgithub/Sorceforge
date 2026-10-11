from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SEL020_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001"
P013DISC_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_discovery_G1_VIRAL_001"
GEOMETRY_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_unresolved_pages_method_discovery_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

DISCOVERY_ID = "C01TEUNRES020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-UNRESOLVED-PAGES-METHOD-DISCOVERY-001"
HUMAN_DECISION = "давай"

PAGES = ["012", "016", "017", "018", "020"]
EXPECTED_DISCOVERED = ["017", "018"]
EXPECTED_STILL_UNRESOLVED = ["012", "016", "020"]
SELECTED_PAGES_V2 = ["009", "010", "011", "013", "015", "017", "018"]

INPUT_HASHES = {
    "C01TESEL020-G1-VIRAL-001.report": (
        SEL020_ROOT / "selector_replay_001_020_report.json",
        "5EF728BE91FA609C44591C104ACC21766F4F184217DF2E01FC151A3504BA75AF",
    ),
    "C01TESEL020-G1-VIRAL-001.selections": (
        SEL020_ROOT / "selector_replay_001_020_selections.json",
        "17EEE268DA1972CF89FFC643F1BCBEC35D56DE1D959C223D2E15E769D0A0372F",
    ),
    "C01TEP013DISC-G1-VIRAL-001.entry": (
        P013DISC_ROOT / "method_registry_entries" / "page_013.json",
        "9E92035A3411C4FDB32F523D9420CB34A17AB3449CD0EA34F57E30FF6295A494",
    ),
    "C01TEP013DISC-G1-VIRAL-001.report": (
        P013DISC_ROOT / "p013_method_discovery_report.json",
        "8DC4220677A7338A1BDF988D429CF4D4D1095596EAF334F3465F1E8325CC86F7",
    ),
    "C01TEGP012013016017018020-G1-VIRAL-001.report": (
        GEOMETRY_ROOT / "geometry_probe_012_013_016_017_018_020_report.json",
        "5A13578D917186A48ECDA8C13C5EE6998700386AA70FFF1913342FEDDB69DAFF",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "reference_guided_repair",
    "reference_token_insertion",
    "text_token_mutation",
    "source_mutation",
    "raw_mutation",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "selector_runtime_enablement",
    "runtime_selector_integration",
    "runtime_execution",
    "production_assembly",
    "clean_production_output_folder",
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


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build unresolved-pages method discovery report.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("unresolved-pages method discovery is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"unresolved-pages method discovery requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("unresolved-pages method discovery requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    selector_report = read_json(SEL020_ROOT / "selector_replay_001_020_report.json")
    selector_selections = read_json(SEL020_ROOT / "selector_replay_001_020_selections.json")
    p013_entry = read_json(P013DISC_ROOT / "method_registry_entries" / "page_013.json")
    geometry_report = read_json(GEOMETRY_ROOT / "geometry_probe_012_013_016_017_018_020_report.json")

    if selector_report["replay_id"] != "C01TESEL020-G1-VIRAL-001":
        raise SystemExit("selector replay input drifted")
    if selector_report["unresolved_pages"] != PAGES:
        raise SystemExit(f"unexpected unresolved pages: {selector_report['unresolved_pages']}")
    if p013_entry["entry_id"] != "C01TEP013DISC-G1-VIRAL-001-P013":
        raise SystemExit("P013 discovery entry drifted")
    if geometry_report["lane_id"] != "C01TEGP012013016017018020-G1-VIRAL-001":
        raise SystemExit("geometry probe input drifted")
    if geometry_report["pages"] != ["012", "013", "016", "017", "018", "020"]:
        raise SystemExit("geometry probe page set drifted")

    return verified, selector_report, selector_selections, p013_entry, geometry_report


def geometry_rows(geometry_report: dict) -> list[dict]:
    rows: list[dict] = []
    for page in PAGES:
        result = geometry_report["best_by_page"][page]
        metrics = result["metrics"]
        rows.append(
            {
                "page": page,
                "lane_id": geometry_report["lane_id"],
                "candidate_id": result["candidate_id"],
                "metrics": metrics,
                "diagnostic_threshold_met": bool(result["diagnostic_threshold_met"]),
                "candidate_text_sha256": result["candidate_text_sha256"],
                "normalized_candidate_sha256": metrics["candidate_normalized_sha256"],
                "reference_label": result["reference_label"],
                "reference_path": result["reference_path"],
                "reference_sha256": result["reference_sha256"],
                "candidate_text_path": result["candidate_text_path"],
                "source_page_image_sha256": result["source_page_image_sha256"],
            }
        )
    return rows


def discover_entries(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    discovered: list[dict] = []
    unresolved: list[dict] = []
    for row in rows:
        if row["diagnostic_threshold_met"]:
            discovered.append(build_entry(row))
        else:
            unresolved.append(
                {
                    "page": row["page"],
                    "status": "still_unresolved_no_threshold_winner",
                    "source_lane_id": row["lane_id"],
                    "best_candidate_id": row["candidate_id"],
                    "metrics": row["metrics"],
                    "candidate_text_sha256": row["candidate_text_sha256"],
                    "normalized_candidate_sha256": row["normalized_candidate_sha256"],
                    "reason": "best_available_evidence_does_not_meet_diagnostic_threshold",
                }
            )
    if [entry["page"] for entry in discovered] != EXPECTED_DISCOVERED:
        raise SystemExit(f"unexpected discovered pages: {[entry['page'] for entry in discovered]}")
    if [item["page"] for item in unresolved] != EXPECTED_STILL_UNRESOLVED:
        raise SystemExit(f"unexpected still-unresolved pages: {[item['page'] for item in unresolved]}")
    return discovered, unresolved


def build_entry(row: dict) -> dict:
    page = row["page"]
    return {
        "entry_id": f"C01TEUNRES020-G1-VIRAL-001-P{page}",
        "discovery_id": DISCOVERY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "page": page,
        "status": "method_discovered_not_runtime",
        "source_lane_id": row["lane_id"],
        "selected_candidate_id": row["candidate_id"],
        "selection_rule": "diagnostic_threshold_met_from_unresolved_pages_geometry_probe_then_similarity_then_token_recall",
        "metrics": row["metrics"],
        "reference_dependency": {
            "label": row["reference_label"],
            "path": row["reference_path"],
            "sha256": row["reference_sha256"],
            "note": "scored_against_reference_text_map_not_independently_source_accepted_ocr_truth",
        },
        "artifact_hashes": {
            "candidate_text_sha256": row["candidate_text_sha256"],
            "normalized_candidate_sha256": row["normalized_candidate_sha256"],
            "source_page_image_sha256": row["source_page_image_sha256"],
        },
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
    }


def selector_v2(selector_selections: list[dict], p013_entry: dict, discovered: list[dict], unresolved: list[dict]) -> list[dict]:
    by_page = {item["page"]: item for item in selector_selections}
    discovered_by_page = {entry["page"]: entry for entry in discovered}
    unresolved_by_page = {item["page"]: item for item in unresolved}
    selections: list[dict] = []
    for number in range(1, 21):
        page = f"{number:03d}"
        if page == "013":
            selections.append(p013_discovery_selection(p013_entry))
        elif page in discovered_by_page:
            selections.append(discovered_selection(discovered_by_page[page]))
        elif page in unresolved_by_page:
            base = by_page[page]
            item = dict(base)
            item["source_lane_id"] = unresolved_by_page[page]["source_lane_id"]
            item["best_available_candidate"] = unresolved_by_page[page]
            item["reason"] = "best_available_evidence_does_not_meet_diagnostic_threshold"
            selections.append(item)
        else:
            selections.append(by_page[page])
    return selections


def p013_discovery_selection(entry: dict) -> dict:
    return {
        "page": "013",
        "selector_decision": "selected_p013_discovered_candidate",
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": entry["discovery_id"],
        "method_entry_id": entry["entry_id"],
        "selected_candidate_id": entry["selected_candidate_id"],
        "selected_output_hashes": entry["artifact_hashes"],
        "metrics": entry["metrics"],
        "reference_label": entry["reference_dependency"]["label"],
        "reference_dependency": entry["reference_dependency"],
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def discovered_selection(entry: dict) -> dict:
    return {
        "page": entry["page"],
        "selector_decision": "selected_unresolved_pages_discovered_candidate",
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": entry["discovery_id"],
        "method_entry_id": entry["entry_id"],
        "selected_candidate_id": entry["selected_candidate_id"],
        "selected_output_hashes": entry["artifact_hashes"],
        "metrics": entry["metrics"],
        "reference_label": entry["reference_dependency"]["label"],
        "reference_dependency": entry["reference_dependency"],
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def summarize_groups(selections: list[dict]) -> dict[str, list[str]]:
    groups = {
        "not_run_ineligible": [],
        "selected_frozen_baseline": [],
        "selected_p013_discovered_candidate": [],
        "selected_unresolved_pages_discovered_candidate": [],
        "still_unresolved_needs_method_winner": [],
        "parked_candidate_policy": [],
    }
    for item in selections:
        decision = item["selector_decision"]
        if decision == "unresolved_needs_method_winner":
            groups["still_unresolved_needs_method_winner"].append(item["page"])
        elif decision in groups:
            groups[decision].append(item["page"])
        else:
            raise SystemExit(f"unexpected selector decision: {decision}")
    return groups


def build_report(verified_inputs: dict, rows: list[dict], discovered: list[dict], unresolved: list[dict], selections: list[dict]) -> dict:
    groups = summarize_groups(selections)
    selected_pages = [
        item["page"]
        for item in selections
        if item["selection_status"] == "selected_static_evidence_only"
    ]
    if selected_pages != SELECTED_PAGES_V2:
        raise SystemExit(f"unexpected selected pages v2: {selected_pages}")
    return {
        "discovery_id": DISCOVERY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "unresolved_pages_method_discovery_partial_coverage",
        "purpose": "discover_method_entries_for_unresolved_001_020_pages_when_existing_threshold_evidence_allows_it",
        "human_decision": HUMAN_DECISION,
        "input_selector_replay": "C01TESEL020-G1-VIRAL-001",
        "input_unresolved_pages": PAGES,
        "candidate_source_lanes": ["C01TEGP012013016017018020-G1-VIRAL-001"],
        "candidate_count": len(rows),
        "discovered_pages": [entry["page"] for entry in discovered],
        "still_unresolved_pages": [item["page"] for item in unresolved],
        "selected_pages_v2": selected_pages,
        "production_ready": False,
        "all_pages_first_pass_success": False,
        "discovered_entries": discovered,
        "still_unresolved": unresolved,
        "selector_replay_v2": {
            "scope": "static_001_020_selector_replay_v2_from_discovered_entries",
            "requested_pages": [f"{page:03d}" for page in range(1, 21)],
            "groups": groups,
            "failed_or_superseded_candidates_selected": False,
            "candidate_text_copied": False,
            "production_assembly_created": False,
            "clean_production_output_folder_created": False,
            "page_021_plus_included": False,
        },
        "selections": selections,
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "reference_guided_repair_used": False,
        "reference_token_insertion_performed": False,
        "text_token_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "selector_runtime_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "clean_production_output_folder_created": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
    }


def write_summary(report: dict) -> None:
    lines = [
        "# Unresolved Pages Method Discovery - C01TEUNRES020-G1-VIRAL-001",
        "",
        "Status: `unresolved_pages_method_discovery_partial_coverage`",
        "",
        "This dry-run opens method entries only for unresolved pages that already have threshold-passing sealed diagnostic evidence.",
        "",
        f"Input unresolved pages: `{', '.join(report['input_unresolved_pages'])}`.",
        f"Discovered pages: `{', '.join(report['discovered_pages'])}`.",
        f"Still unresolved: `{', '.join(report['still_unresolved_pages'])}`.",
        f"Selected pages v2: `{', '.join(report['selected_pages_v2'])}`.",
        "",
        "## Discovered Entries",
        "",
        "| Page | Entry | Candidate | Similarity | Token recall |",
        "|---|---|---|---:|---:|",
    ]
    for entry in report["discovered_entries"]:
        metrics = entry["metrics"]
        lines.append(
            f"| `{entry['page']}` | `{entry['entry_id']}` | `{entry['selected_candidate_id']}` | "
            f"`{metrics['sequence_similarity_ratio']}` | `{metrics['token_recall']}` |"
        )
    lines.extend(["", "## Still Unresolved", "", "| Page | Best candidate | Similarity | Token recall | Reason |", "|---|---|---:|---:|---|"])
    for item in report["still_unresolved"]:
        metrics = item["metrics"]
        lines.append(
            f"| `{item['page']}` | `{item['best_candidate_id']}` | "
            f"`{metrics['sequence_similarity_ratio']}` | `{metrics['token_recall']}` | `{item['reason']}` |"
        )
    lines.extend(
        [
            "",
            "## Boundary Flags",
            "",
            "- `ocr_execution_performed=false`.",
            "- `production_assembly_created=false`.",
            "- `accepted_text_mutation_performed=false`.",
            "- `page_001_020_runtime_loop_created=false`.",
            "- `page_021_plus_included=false`.",
            "- `promotion_performed=false`.",
            "- `acceptance_performed=false`.",
            "- `downstream_execution_performed=false`.",
            "",
            "Boundary: no OCR/render/PDF/text-layer execution, no reference-token insertion, no accepted/semantic/page-status/source/raw mutation, no runtime selector integration, no production assembly, no clean production output folder, no page 021+, no promotion, no acceptance, and no downstream execution.",
            "",
        ]
    )
    write_text(OUT_ROOT / "unresolved_pages_method_discovery_summary.md", "\n".join(lines))


def output_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "unresolved_pages_method_discovery_manifest.md":
            hashes[path.relative_to(OUT_ROOT).as_posix()] = sha256_file(path)
    return hashes


def write_manifest() -> None:
    lines = [
        "# Unresolved Pages Method Discovery Manifest - C01TEUNRES020-G1-VIRAL-001",
        "",
        "Boundary: method discovery and selector replay v2 report only; no production assembly.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, digest in output_hashes().items():
        lines.append(f"| `{rel_path}` | `{digest}` |")
    lines.append("")
    write_text(OUT_ROOT / "unresolved_pages_method_discovery_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, _selector_report, selector_selections, p013_entry, geometry_report = verify_inputs()
    rows = geometry_rows(geometry_report)
    discovered, unresolved = discover_entries(rows)
    selections = selector_v2(selector_selections, p013_entry, discovered, unresolved)
    report = build_report(verified_inputs, rows, discovered, unresolved, selections)

    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    for entry in discovered:
        write_json(OUT_ROOT / "method_registry_entries" / f"page_{entry['page']}.json", entry)
    write_json(OUT_ROOT / "selector_replay_v2" / "selector_replay_v2_selections.json", selections)
    write_json(OUT_ROOT / "unresolved_pages_method_discovery_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
