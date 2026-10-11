import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_core_0_1_text_extraction_p013_method_discovery import (  # noqa: E402
    EXPECTED_EQUIVALENT,
    EXPECTED_WINNER,
    candidate_rows,
    discover_winner,
    verify_inputs,
)

SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p013_method_discovery.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_discovery_G1_VIRAL_001"
REPORT = OUT_ROOT / "p013_method_discovery_report.json"
ENTRY = OUT_ROOT / "method_registry_entries" / "page_013.json"
SUMMARY = OUT_ROOT / "p013_method_discovery_summary.md"
MANIFEST = OUT_ROOT / "p013_method_discovery_manifest.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-DISCOVERY-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs():
    if not REPORT.exists():
        pytest.skip("P013 method discovery output has not been generated yet")


def test_p013_method_discovery_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-WRONG",
            "--decision",
            "ну так делай",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_p013_method_discovery_pre_output_ranking_selects_d_over_equivalent_e():
    _, reports = verify_inputs()
    rows = candidate_rows(reports)
    winner, ranked = discover_winner(rows)

    assert winner["candidate_id"] == EXPECTED_WINNER
    assert ranked[0]["candidate_id"] == EXPECTED_WINNER
    assert ranked[1]["candidate_id"] == EXPECTED_EQUIVALENT
    assert ranked[0]["metrics"] == ranked[1]["metrics"]
    assert ranked[0]["normalized_candidate_sha256"] == ranked[1]["normalized_candidate_sha256"]
    assert ranked[0]["source_result"]["assembly_mode"] == "line_join"


def test_p013_method_discovery_selects_sac_winner_without_mrs_input():
    require_outputs()
    report = read_json(REPORT)
    entry = read_json(ENTRY)

    assert report["discovery_id"] == "C01TEP013DISC-G1-VIRAL-001"
    assert report["mrs_registry_input_used"] is False
    assert report["diagnostic_lane_count"] == 5
    assert report["candidate_count"] >= 16
    assert report["ranking"][0]["lane_id"] == "C01TEP013SAC-G1-VIRAL-001"
    assert report["ranking"][0]["candidate_id"] == "p013_sac_d_noise_then_declared_seam_fracture"
    assert report["ranking"][0]["diagnostic_threshold_met"] is True
    assert report["ranking"][0]["method_registry_candidate"] is True
    assert entry["entry_id"] == "C01TEP013DISC-G1-VIRAL-001-P013"
    assert entry["discovered_without_mrs_registry_input"] is True
    assert entry["selected_candidate_id"] == "p013_sac_d_noise_then_declared_seam_fracture"
    assert entry["selection_rule"] == (
        "highest_threshold_met_method_registry_candidate_then_similarity_then_token_recall_"
        "then_line_join_tie_break_then_candidate_id"
    )
    assert entry["metrics"]["sequence_similarity_ratio"] == 0.998915
    assert entry["metrics"]["token_recall"] == 0.993939


def test_p013_method_discovery_records_tie_and_rejections():
    require_outputs()
    entry = read_json(ENTRY)

    assert entry["equivalent_candidate_not_selected"]["candidate_id"] == "p013_sac_e_paragraph_join_d"
    assert entry["equivalent_candidate_not_selected"]["normalized_candidate_sha256"] == (
        entry["artifact_hashes"]["normalized_candidate_sha256"]
    )
    rejected_ids = {item["candidate_id"] for item in entry["rejected_candidates"]}
    assert "p013_ssp_a_near_overlap_confidence" in rejected_ids
    assert "p013_expanded_lane_order_lane_then_y_exact_collapse" in rejected_ids
    assert "p013_geo_noexp_5box_triage_order" in rejected_ids
    assert "sealed_raw_v1_max_tail_prefix_exact_dedupe" in rejected_ids


def test_p013_method_discovery_hash_pins_and_selector_dry_run():
    require_outputs()
    report = read_json(REPORT)

    assert report["verified_inputs"]["C01TEP013SAC-G1-VIRAL-001.report"]["sha256"] == (
        "E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4"
    )
    entry = report["discovered_entry"]
    assert entry["artifact_hashes"]["candidate_text_sha256"] == (
        "E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4"
    )
    assert entry["artifact_hashes"]["normalized_candidate_sha256"] == (
        "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D"
    )
    dry_run = report["selector_dry_run"]
    assert dry_run["selected_entry_id"] == entry["entry_id"]
    assert dry_run["selected_candidate_id"] == entry["selected_candidate_id"]
    assert dry_run["candidate_text_copied"] is False
    assert dry_run["production_assembly_created"] is False


def test_p013_method_discovery_boundaries_are_false():
    require_outputs()
    report = read_json(REPORT)
    entry = read_json(ENTRY)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "ocr_execution_performed",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "reference_guided_repair_used",
        "reference_token_insertion_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "selector_runtime_enabled",
        "runtime_selector_integration",
        "runtime_execution_performed",
        "production_assembly_created",
        "clean_production_output_folder_created",
        "page_001_020_runtime_loop_created",
        "page_021_plus_included",
        "push_performed",
        "promotion_performed",
        "acceptance_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    for flag in [
        "runtime_selector_integration",
        "production_assembly_created",
        "accepted_text_mutation_performed",
        "page_001_020_runtime_loop_created",
        "page_021_plus_included",
        "promotion_performed",
        "acceptance_performed",
        "downstream_execution_performed",
    ]:
        assert entry[flag] is False, flag
    assert report["negative_capability_matrix"]["mrs_registry_input_used"] is False
    assert report["negative_capability_matrix"]["promotion"] is False
    assert report["negative_capability_matrix"]["acceptance"] is False
    assert report["negative_capability_matrix"]["downstream_execution"] is False
    assert "`mrs_registry_input_used=false`" in summary
    assert "then_line_join_tie_break_then_candidate_id" in summary
    assert "`promotion_performed=false`" in summary
    assert "`acceptance_performed=false`" in summary
    assert "`downstream_execution_performed=false`" in summary


def test_p013_method_discovery_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`method_registry_entries/page_013.json`" in manifest
    assert "`selector_dry_run/page_013_selection.json`" in manifest
    assert "`p013_method_discovery_report.json`" in manifest
    assert "`p013_method_discovery_summary.md`" in manifest
    assert "no production assembly" in manifest
