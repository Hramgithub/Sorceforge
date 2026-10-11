from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_p013_method_registry_selector.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_p013_method_registry_selector.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SAC_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-REGISTRY-SELECTOR-001"
DECISION_ID = "C01TEP013MRS-G1-VIRAL-001"
ENTRY_ID = "C01TEP013MRS-G1-VIRAL-001-P013"
HUMAN_DECISION = (
    "Следующий шаг по плану: оформить отдельный reviewed method-registry/selector шаг для P013 winner, "
    "потом встраивать в общий first-pass 001-020 selector loop без плохих версий в production output."
)
PAGE = "013"
SELECTED_CANDIDATE_ID = "p013_sac_d_noise_then_declared_seam_fracture"
EQUIVALENT_CANDIDATE_ID = "p013_sac_e_paragraph_join_d"

INPUT_HASHES = {
    "C01TEP013SAC-G1-VIRAL-001.report": (
        SAC_ROOT / "p013_structural_assembly_closure_diagnostic_report.json",
        "E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4",
    ),
    "C01TEP013SAC-G1-VIRAL-001.summary": (
        SAC_ROOT / "p013_structural_assembly_closure_diagnostic_summary.md",
        "353CA98438634BA64347B9FE8F545D3BFE3A8E8FAC002677A2A9D0073A065898",
    ),
    "C01TEP013SAC-G1-VIRAL-001.manifest": (
        SAC_ROOT / "p013_structural_assembly_closure_diagnostic_manifest.md",
        "46343B13144DFBD3C074F7E369A4DDE97F4D2F6540F60341120B5E3DE7CF7212",
    ),
    "C01TEP013SAC-G1-VIRAL-001.rankings": (
        SAC_ROOT / "rankings" / "page_013_candidate_rankings.json",
        "613455DDA093EC5F7E01E4F993481D344AB37643257BF5259AC546D5A557D47A",
    ),
    "C01TEP013SAC-G1-VIRAL-001.selected_candidate_text": (
        SAC_ROOT / "candidate_texts" / SELECTED_CANDIDATE_ID / "page_013_candidate.md",
        "E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4",
    ),
    "C01TEP013SAC-G1-VIRAL-001.selected_normalized_candidate": (
        SAC_ROOT / "normalized_candidate_texts" / SELECTED_CANDIDATE_ID / "page_013_candidate_normalized.txt",
        "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D",
    ),
    "C01TEP013SAC-G1-VIRAL-001.selected_retained_records": (
        SAC_ROOT / "retained_record_traces" / SELECTED_CANDIDATE_ID / "page_013_retained_records.json",
        "4B0628DE7BC5EF395DAAB107F6B6448A230C2E08FA24C0B4005F37FE90389A19",
    ),
    "C01TEP013SAC-G1-VIRAL-001.selected_suppression_ledger": (
        SAC_ROOT / "suppression_ledgers" / SELECTED_CANDIDATE_ID / "page_013_suppression_ledger.json",
        "4A54B31E63C66AE28939FAF9A9A63A8F131F19B2E1AD2E0BBA61B29DD96B5F03",
    ),
    "C01TEP013SAC-G1-VIRAL-001.selected_assembly_trace": (
        SAC_ROOT / "assembly_traces" / SELECTED_CANDIDATE_ID / "page_013_assembly_trace.json",
        "EC9A97A032A1562C25839AFCD46B15792A6498AAC3FB3D5B14A7B0FEC471C62D",
    ),
    "C01TEP013SAC-G1-VIRAL-001.equivalent_candidate_text": (
        SAC_ROOT / "candidate_texts" / EQUIVALENT_CANDIDATE_ID / "page_013_candidate.md",
        "3150AEA9688A0D4333A708348D1E2F4A44AC1732EE9C266A14323BC631B46B61",
    ),
    "C01TEP013SAC-G1-VIRAL-001.equivalent_normalized_candidate": (
        SAC_ROOT / "normalized_candidate_texts" / EQUIVALENT_CANDIDATE_ID / "page_013_candidate_normalized.txt",
        "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D",
    ),
    "C01TEP013SAC-G1-VIRAL-001.equivalent_retained_records": (
        SAC_ROOT / "retained_record_traces" / EQUIVALENT_CANDIDATE_ID / "page_013_retained_records.json",
        "4B0628DE7BC5EF395DAAB107F6B6448A230C2E08FA24C0B4005F37FE90389A19",
    ),
    "C01TEP013SAC-G1-VIRAL-001.equivalent_suppression_ledger": (
        SAC_ROOT / "suppression_ledgers" / EQUIVALENT_CANDIDATE_ID / "page_013_suppression_ledger.json",
        "4A54B31E63C66AE28939FAF9A9A63A8F131F19B2E1AD2E0BBA61B29DD96B5F03",
    ),
    "C01TEP013SAC-G1-VIRAL-001.equivalent_assembly_trace": (
        SAC_ROOT / "assembly_traces" / EQUIVALENT_CANDIDATE_ID / "page_013_assembly_trace.json",
        "635529A3A53AB7D52E547C6609A8B9AD61E1BD63ADB713AE8E01BD8AD95A9F14",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "image_processing",
    "reference_guided_repair",
    "reference_token_insertion",
    "spelling_correction",
    "text_token_mutation",
    "source_mutation",
    "raw_mutation",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_acceptance",
    "page_complete_acceptance",
    "method_registry_runtime_update",
    "selector_rule_creation",
    "selector_enablement",
    "runtime_selector_integration",
    "runtime_implementation",
    "runtime_execution",
    "production_assembly",
    "page_family_generalization",
    "page_001_020_runtime_loop",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
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
    parser = argparse.ArgumentParser(description="Build P013 method-registry selector candidate decision record.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 method-registry selector candidate decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 method-registry selector candidate decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 method-registry selector candidate decision requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if HUMAN_DECISION not in ledger:
        raise SystemExit("exact human decision missing from authorization ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    report = read_json(SAC_ROOT / "p013_structural_assembly_closure_diagnostic_report.json")
    rankings = read_json(SAC_ROOT / "rankings" / "page_013_candidate_rankings.json")
    if report["lane_id"] != "C01TEP013SAC-G1-VIRAL-001" or report["page"] != PAGE:
        raise SystemExit("unexpected SAC report input")
    if report["best_candidate"]["candidate_id"] != SELECTED_CANDIDATE_ID:
        raise SystemExit("SAC report best candidate drifted")
    if not report["best_candidate"]["diagnostic_threshold_met"]:
        raise SystemExit("SAC best candidate no longer meets the diagnostic threshold")
    if not report["best_candidate"]["method_registry_candidate"]:
        raise SystemExit("SAC best candidate no longer qualifies as candidate evidence")
    if report["best_candidate"]["reference_label"] != "reference_text_map_not_ocr_verified":
        raise SystemExit("P013 reference label must remain non-OCR-verified")
    for key in [
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "runtime_implementation_created",
        "production_assembly_created",
        "page_021_plus_included",
        "push_performed",
    ]:
        if report[key]:
            raise SystemExit(f"SAC report violates boundary flag {key}")
    if [item["candidate_id"] for item in rankings[:2]] != [SELECTED_CANDIDATE_ID, EQUIVALENT_CANDIDATE_ID]:
        raise SystemExit("SAC candidate ordering drifted")
    if rankings[0]["metrics"] != rankings[1]["metrics"]:
        raise SystemExit("SAC D/E tie metrics drifted")
    if rankings[0]["normalized_candidate_sha256"] != rankings[1]["normalized_candidate_sha256"]:
        raise SystemExit("SAC D/E normalized hash tie drifted")
    return verified, report, rankings


def selected_result(report: dict, candidate_id: str) -> dict:
    for item in report["results"]:
        if item["candidate_id"] == candidate_id:
            return item
    raise SystemExit(f"{candidate_id} missing from SAC report")


def build_registry_entry(verified_inputs: dict[str, dict[str, str]], report: dict, rankings: list[dict]) -> dict:
    selected = selected_result(report, SELECTED_CANDIDATE_ID)
    equivalent = selected_result(report, EQUIVALENT_CANDIDATE_ID)
    failed = [item for item in rankings if item["candidate_id"] not in {SELECTED_CANDIDATE_ID, EQUIVALENT_CANDIDATE_ID}]
    return {
        "entry_id": ENTRY_ID,
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "page": PAGE,
        "status": "candidate_selected_not_runtime",
        "source_lane_id": "C01TEP013SAC-G1-VIRAL-001",
        "selected_candidate_id": SELECTED_CANDIDATE_ID,
        "equivalent_candidate_not_selected": {
            "candidate_id": EQUIVALENT_CANDIDATE_ID,
            "reason": "same_normalized_hash_and_metrics_but_separator_only_variant",
            "candidate_text_sha256": equivalent["candidate_text_sha256"],
            "normalized_candidate_sha256": equivalent["normalized_candidate_sha256"],
            "assembly_mode": equivalent["assembly_mode"],
        },
        "tie_break": {
            "rule": "prefer_line_join_over_separator_only_equivalent_when_normalized_hash_and_metrics_match",
            "selected_assembly_mode": selected["assembly_mode"],
            "excluded_equivalent_assembly_mode": equivalent["assembly_mode"],
        },
        "metrics": selected["metrics"],
        "thresholds": report["diagnostic_thresholds"],
        "reference_dependency": {
            "label": selected["reference_label"],
            "path": selected["reference_path"],
            "sha256": selected["reference_sha256"],
            "note": "scored_against_reference_text_map_not_independently_source_accepted_ocr_truth",
        },
        "algorithm_contract": {
            "inputs": ["sealed_ssp_retained_records", "sealed_sac_suppression_ledger", "sealed_sac_assembly_trace"],
            "steps": [
                "start_from_sealed_ssp_best_retained_set",
                "apply_low_confidence_thin_noise_suppression",
                "apply_declared_seam_fracture_duplicate_suppression",
                "assemble_with_line_join",
            ],
            "no_text_literal_matching": True,
            "no_token_substitution_or_insertion": True,
            "seam_fracture_parameters": report["seam_fracture_parameters"],
        },
        "artifact_hashes": {
            "sac_report_sha256": verified_inputs["C01TEP013SAC-G1-VIRAL-001.report"]["sha256"],
            "sac_rankings_sha256": verified_inputs["C01TEP013SAC-G1-VIRAL-001.rankings"]["sha256"],
            "candidate_text_sha256": selected["candidate_text_sha256"],
            "normalized_candidate_sha256": selected["normalized_candidate_sha256"],
            "retained_record_trace_sha256": selected["retained_record_trace_sha256"],
            "suppression_ledger_sha256": selected["suppression_ledger_sha256"],
            "assembly_trace_sha256": selected["assembly_trace_sha256"],
        },
        "excluded_variants": [
            {
                "candidate_id": item["candidate_id"],
                "reason": "failed_threshold_or_superseded_by_combined_structural_candidate",
                "diagnostic_threshold_met": item["diagnostic_threshold_met"],
                "method_registry_candidate": item["method_registry_candidate"],
            }
            for item in failed
        ],
        "invalidation_triggers": [
            "any_pinned_sac_hash_drift",
            "sac_lane_rerun_or_supersession",
            "threshold_policy_change",
            "selector_schema_change",
            "reference_status_or_evidence_status_change",
            "future_source_acceptance_changes_page_013_ground_truth",
        ],
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "runtime_implementation_created": False,
        "production_assembly_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
    }


def build_selector_dry_run(entry: dict) -> dict:
    return {
        "decision_id": DECISION_ID,
        "page": PAGE,
        "scope": "page_013_static_selector_dry_run_only",
        "selected_entry_id": entry["entry_id"],
        "selected_candidate_id": entry["selected_candidate_id"],
        "selection_basis": [
            "diagnostic_threshold_met",
            "method_registry_candidate_evidence_true",
            "highest_sac_metric_pair",
            "tie_break_line_join_over_separator_only_equivalent",
        ],
        "candidate_text_copied": False,
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "production_assembly_created": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
    }


def build_report(verified_inputs: dict[str, dict[str, str]], report: dict, entry: dict, dry_run: dict) -> dict:
    return {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p013_method_registry_candidate_decision_recorded",
        "purpose": "record_p013_sac_winner_as_method_registry_candidate_decision_without_runtime_selector_or_production_output",
        "human_decision": HUMAN_DECISION,
        "sol_gate": {
            "status": "ok_with_scope",
            "scope": "p013_candidate_method_registry_selector_contract_only",
            "selected_candidate_id": SELECTED_CANDIDATE_ID,
        },
        "terra_gate": {
            "status": "ok_with_scope_after_tightening",
            "scope": "p013_method_registry_candidate_decision_record_not_enabled_selector_integration",
            "required_false_flags": [
                "selector_rule_created",
                "selector_enabled",
                "runtime_selector_integration",
                "production_assembly_created",
                "page_021_plus_included",
            ],
        },
        "page": PAGE,
        "selected_candidate_id": SELECTED_CANDIDATE_ID,
        "method_registry_candidate_decision_recorded": True,
        "method_registry_candidate_entry_created": True,
        "selector_dry_run_created": True,
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "runtime_implementation_created": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "reference_guided_repair_used": False,
        "reference_token_insertion_performed": False,
        "text_token_mutation_performed": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "registry_entry": entry,
        "selector_dry_run": dry_run,
        "sac_best_candidate": report["best_candidate"],
        "reference_dependency": entry["reference_dependency"],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
        "next_possible_packets": [
            "p013_selector_integration_prep_if_separately_authorized",
            "core_0_1_first_pass_001_020_selector_loop_prep_if_separately_authorized",
        ],
        "remaining_blockers": [
            "enabled_selector_rule_requires_separate_review_and_authorization",
            "runtime_selector_integration_requires_separate_review_and_authorization",
            "production_output_folder_requires_separate_review_and_authorization",
            "accepted_text_or_page_status_mutation_requires_separate_review_and_authorization",
            "page_family_or_001_020_generalization_requires_separate_review_and_authorization",
            "reference_map_is_not_independently_source_accepted_ocr_truth",
            "page_021_plus_remains_excluded",
            "push_requires_separate_authorization",
        ],
    }


def write_summary(report: dict) -> None:
    entry = report["registry_entry"]
    lines = [
        "# P013 Method-Registry Selector Candidate Decision - C01TEP013MRS-G1-VIRAL-001",
        "",
        "Status: `p013_method_registry_candidate_decision_recorded`",
        "",
        "`p013_sac_d_noise_then_declared_seam_fracture` is recorded as the P013 method-registry candidate decision from sealed SAC evidence.",
        "",
        "This is not an enabled selector rule, runtime selector integration, production assembly, accepted text mutation, semantic map mutation, or page-status acceptance.",
        "",
        "## Selected Candidate",
        "",
        f"- Page: `{PAGE}`.",
        f"- Entry: `{entry['entry_id']}`.",
        f"- Selected candidate: `{entry['selected_candidate_id']}`.",
        f"- Similarity: `{entry['metrics']['sequence_similarity_ratio']}`.",
        f"- Token recall: `{entry['metrics']['token_recall']}`.",
        "- Threshold: `>=0.997 / >=0.993939`.",
        "- Reference dependency: `reference_text_map_not_ocr_verified`.",
        "",
        "## Tie Break",
        "",
        f"- Equivalent candidate noted but not selected: `{EQUIVALENT_CANDIDATE_ID}`.",
        "- Reason: same normalized hash and metrics, but the selected D variant uses simpler `line_join`.",
        "",
        "## Boundary",
        "",
        "- Selector rule created: `false`.",
        "- Selector enabled: `false`.",
        "- Runtime selector integration: `false`.",
        "- Production assembly created: `false`.",
        "- Candidate text copied to production: `false`.",
        "- Accepted text / semantic map / page status mutation: `false`.",
        "- Page 001-020 runtime loop created: `false`.",
        "- Page 021+ included: `false`.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in report["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "p013_method_registry_selector_summary.md", "\n".join(lines))


def write_manifest() -> None:
    manifest_name = "p013_method_registry_selector_manifest.md"
    lines = [
        "# P013 Method-Registry Selector Candidate Decision Manifest - C01TEP013MRS-G1-VIRAL-001",
        "",
        "Status: `p013_method_registry_candidate_decision_recorded`",
        "",
        "Boundary: P013 candidate decision artifacts only; no enabled selector, runtime selector integration, production assembly, accepted text mutation, semantic map mutation, page status mutation, source/raw mutation, page 001-020 runtime loop, page 021+, translation/proofreading, push, or downstream execution.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / manifest_name, "\n".join(lines))


def build() -> None:
    verified_inputs, sac_report, rankings = verify_inputs()
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    entry = build_registry_entry(verified_inputs, sac_report, rankings)
    dry_run = build_selector_dry_run(entry)
    report = build_report(verified_inputs, sac_report, entry, dry_run)
    write_json(OUT_ROOT / "method_registry_entries" / "page_013.json", entry)
    write_json(OUT_ROOT / "selector_dry_run" / "page_013_selection.json", dry_run)
    write_json(OUT_ROOT / "p013_method_registry_selector_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
