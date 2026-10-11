from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_discovery_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

DISCOVERY_ID = "C01TEP013DISC-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-DISCOVERY-001"
HUMAN_DECISION = "ну так делай"
PAGE = "013"

LANE_REPORTS = {
    "C01TEP013SDD-G1-VIRAL-001": (
        TRIAL_ROOT / "core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001" / "p013_seam_dedupe_diagnostic_report.json",
        "C99424139DBEBDC2F90025CC97CEB912B6E4D439820F3A68AE1281247C09E1E7",
    ),
    "C01TEP013GNO-G1-VIRAL-001": (
        TRIAL_ROOT / "core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001" / "p013_noexp_geometry_diagnostic_report.json",
        "E3DEE3400E3DE17530F6E7D2CEC90F98D0C33B192E13817125C0BD2B6EDF712E",
    ),
    "C01TEP013ELO-G1-VIRAL-001": (
        TRIAL_ROOT / "core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001" / "p013_expanded_lane_order_diagnostic_report.json",
        "C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB",
    ),
    "C01TEP013SSP-G1-VIRAL-001": (
        TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001" / "p013_structural_suppression_diagnostic_report.json",
        "712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B",
    ),
    "C01TEP013SAC-G1-VIRAL-001": (
        TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001" / "p013_structural_assembly_closure_diagnostic_report.json",
        "E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4",
    ),
}

EXPECTED_WINNER = "p013_sac_d_noise_then_declared_seam_fracture"
EXPECTED_EQUIVALENT = "p013_sac_e_paragraph_join_d"
SELECTION_RULE = (
    "highest_threshold_met_method_registry_candidate_then_similarity_then_token_recall_"
    "then_line_join_tie_break_then_candidate_id"
)

NEGATIVE_CAPABILITIES = [
    "mrs_registry_input_used",
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
    "page_001_020_runtime_loop",
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
    parser = argparse.ArgumentParser(description="Build P013 cold-start method discovery report.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 method discovery is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 method discovery requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 method discovery requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    reports: dict[str, dict] = {}
    for lane_id, (path, expected_hash) in LANE_REPORTS.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{lane_id} report hash mismatch: {actual}")
        report = read_json(path)
        if report.get("lane_id") != lane_id or report.get("page") != PAGE:
            raise SystemExit(f"{lane_id} report identity drifted")
        verified[f"{lane_id}.report"] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
        reports[lane_id] = report
    return verified, reports


def candidate_rows(reports: dict[str, dict]) -> list[dict]:
    rows: list[dict] = []
    for lane_id, report in reports.items():
        for result in report["results"]:
            metrics = result["metrics"]
            rows.append(
                {
                    "lane_id": lane_id,
                    "page": result.get("page", PAGE),
                    "candidate_id": result["candidate_id"],
                    "metrics": metrics,
                    "diagnostic_threshold_met": bool(result.get("diagnostic_threshold_met")),
                    "method_registry_candidate": bool(result.get("method_registry_candidate")),
                    "candidate_hash_sealed_before_reference_scoring": bool(
                        result.get("candidate_hash_sealed_before_reference_scoring", True)
                    ),
                    "reference_loaded_after_candidate_hashing": bool(result.get("reference_loaded_after_candidate_hashing", True)),
                    "candidate_text_sha256": result.get("candidate_text_sha256"),
                    "normalized_candidate_sha256": result.get("normalized_candidate_sha256")
                    or metrics.get("candidate_normalized_sha256"),
                    "reference_label": result.get("reference_label"),
                    "reference_sha256": result.get("reference_sha256"),
                    "source_result": result,
                }
            )
    return rows


def rank_key(row: dict) -> tuple[int, int, float, float, str]:
    metrics = row["metrics"]
    line_join_preferred = 1 if row["source_result"].get("assembly_mode") == "line_join" else 0
    return (
        1 if row["diagnostic_threshold_met"] else 0,
        1 if row["method_registry_candidate"] else 0,
        float(metrics["sequence_similarity_ratio"]),
        float(metrics["token_recall"]),
        line_join_preferred,
        row["candidate_id"],
    )


def discover_winner(rows: list[dict]) -> tuple[dict, list[dict]]:
    for row in rows:
        if not row["candidate_hash_sealed_before_reference_scoring"]:
            raise SystemExit(f"{row['candidate_id']} was not sealed before reference scoring")
        if not row["reference_loaded_after_candidate_hashing"]:
            raise SystemExit(f"{row['candidate_id']} loaded reference before candidate hash")
    ranked = sorted(rows, key=rank_key, reverse=True)
    winner = ranked[0]
    if winner["candidate_id"] != EXPECTED_WINNER:
        raise SystemExit(f"unexpected discovered winner: {winner['candidate_id']}")
    if not winner["diagnostic_threshold_met"] or not winner["method_registry_candidate"]:
        raise SystemExit("discovered winner does not meet registry threshold")
    return winner, ranked


def build_entry(winner: dict, ranked: list[dict]) -> dict:
    result = winner["source_result"]
    equivalent = next(row for row in ranked if row["candidate_id"] == EXPECTED_EQUIVALENT)
    failed = [row for row in ranked if row["candidate_id"] not in {EXPECTED_WINNER, EXPECTED_EQUIVALENT}]
    return {
        "entry_id": "C01TEP013DISC-G1-VIRAL-001-P013",
        "discovery_id": DISCOVERY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "page": PAGE,
        "status": "method_discovered_not_runtime",
        "discovered_without_mrs_registry_input": True,
        "source_lane_id": winner["lane_id"],
        "selected_candidate_id": winner["candidate_id"],
        "selection_rule": SELECTION_RULE,
        "metrics": winner["metrics"],
        "reference_dependency": {
            "label": result["reference_label"],
            "path": result["reference_path"],
            "sha256": result["reference_sha256"],
            "note": "scored_against_reference_text_map_not_independently_source_accepted_ocr_truth",
        },
        "artifact_hashes": {
            "candidate_text_sha256": result["candidate_text_sha256"],
            "normalized_candidate_sha256": result["normalized_candidate_sha256"],
            "retained_record_trace_sha256": result.get("retained_record_trace_sha256"),
            "suppression_ledger_sha256": result.get("suppression_ledger_sha256"),
            "assembly_trace_sha256": result.get("assembly_trace_sha256"),
        },
        "equivalent_candidate_not_selected": {
            "candidate_id": equivalent["candidate_id"],
            "reason": "same_normalized_hash_and_metrics_but_separator_only_variant",
            "metrics": equivalent["metrics"],
            "normalized_candidate_sha256": equivalent["normalized_candidate_sha256"],
        },
        "rejected_candidates": [
            {
                "lane_id": row["lane_id"],
                "candidate_id": row["candidate_id"],
                "metrics": row["metrics"],
                "diagnostic_threshold_met": row["diagnostic_threshold_met"],
                "method_registry_candidate": row["method_registry_candidate"],
            }
            for row in failed
        ],
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
    }


def build_report(verified_inputs: dict[str, dict[str, str]], rows: list[dict], ranked: list[dict], entry: dict) -> dict:
    return {
        "discovery_id": DISCOVERY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p013_method_discovered_without_mrs_registry_input",
        "purpose": "simulate_cold_start_p013_method_search_over_available_diagnostic_method_family_artifacts",
        "human_decision": HUMAN_DECISION,
        "page": PAGE,
        "mrs_registry_input_used": False,
        "diagnostic_lane_count": len(LANE_REPORTS),
        "candidate_count": len(rows),
        "ranking": [
            {
                "rank": index,
                "lane_id": row["lane_id"],
                "candidate_id": row["candidate_id"],
                "metrics": row["metrics"],
                "diagnostic_threshold_met": row["diagnostic_threshold_met"],
                "method_registry_candidate": row["method_registry_candidate"],
            }
            for index, row in enumerate(ranked, start=1)
        ],
        "discovered_entry": entry,
        "selector_dry_run": {
            "page": PAGE,
            "scope": "p013_static_selector_dry_run_from_discovered_entry_only",
            "selected_entry_id": entry["entry_id"],
            "selected_candidate_id": entry["selected_candidate_id"],
            "candidate_text_copied": False,
            "selector_rule_created": False,
            "selector_enabled": False,
            "runtime_selector_integration": False,
            "production_assembly_created": False,
            "page_001_020_runtime_loop_created": False,
            "page_021_plus_included": False,
        },
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
    entry = report["discovered_entry"]
    lines = [
        "# P013 Cold-Start Method Discovery - C01TEP013DISC-G1-VIRAL-001",
        "",
        "Status: `p013_method_discovered_without_mrs_registry_input`",
        "",
        "This discovery does not use the prior P013 MRS registry entry. It ranks available P013 diagnostic method-family artifacts and creates a fresh discovered entry for dry-run selector use.",
        "",
        f"Discovered entry: `{entry['entry_id']}`.",
        f"Selected lane: `{entry['source_lane_id']}`.",
        f"Selected candidate: `{entry['selected_candidate_id']}`.",
        f"Selection rule: `{entry['selection_rule']}`.",
        f"Similarity: `{entry['metrics']['sequence_similarity_ratio']}`.",
        f"Token recall: `{entry['metrics']['token_recall']}`.",
        "",
        "## Ranking",
        "",
        "| Rank | Lane | Candidate | Similarity | Token recall | Threshold | Registry candidate |",
        "|---:|---|---|---:|---:|---|---|",
    ]
    for item in report["ranking"]:
        metrics = item["metrics"]
        lines.append(
            f"| {item['rank']} | `{item['lane_id']}` | `{item['candidate_id']}` | "
            f"`{metrics['sequence_similarity_ratio']}` | `{metrics['token_recall']}` | "
            f"`{item['diagnostic_threshold_met']}` | `{item['method_registry_candidate']}` |"
        )
    lines.extend(
        [
            "",
            "## Boundary Flags",
            "",
            "- `mrs_registry_input_used=false`.",
            "- `ocr_execution_performed=false`.",
            "- `production_assembly_created=false`.",
            "- `accepted_text_mutation_performed=false`.",
            "- `page_001_020_runtime_loop_created=false`.",
            "- `page_021_plus_included=false`.",
            "- `promotion_performed=false`.",
            "- `acceptance_performed=false`.",
            "- `downstream_execution_performed=false`.",
            "",
            "Boundary: no OCR/render/PDF/text-layer execution, no reference-token insertion, no accepted/semantic/page-status/source/raw mutation, no runtime selector integration, no production assembly, no page 001-020 runtime loop, no page 021+, no promotion, no acceptance, and no downstream execution.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_method_discovery_summary.md", "\n".join(lines))


def output_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_method_discovery_manifest.md":
            hashes[path.relative_to(OUT_ROOT).as_posix()] = sha256_file(path)
    return hashes


def write_manifest() -> None:
    lines = [
        "# P013 Cold-Start Method Discovery Manifest - C01TEP013DISC-G1-VIRAL-001",
        "",
        "Boundary: method discovery/report only; no production assembly.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, digest in output_hashes().items():
        lines.append(f"| `{rel_path}` | `{digest}` |")
    lines.append("")
    write_text(OUT_ROOT / "p013_method_discovery_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, reports = verify_inputs()
    rows = candidate_rows(reports)
    winner, ranked = discover_winner(rows)
    entry = build_entry(winner, ranked)
    report = build_report(verified_inputs, rows, ranked, entry)
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    write_json(OUT_ROOT / "method_registry_entries" / "page_013.json", entry)
    write_json(OUT_ROOT / "selector_dry_run" / "page_013_selection.json", report["selector_dry_run"])
    write_json(OUT_ROOT / "p013_method_discovery_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
