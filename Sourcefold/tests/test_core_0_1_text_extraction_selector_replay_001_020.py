import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_selector_replay_001_020.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001"
REPORT = OUT_ROOT / "selector_replay_001_020_report.json"
SELECTIONS = OUT_ROOT / "selector_replay_001_020_selections.json"
SUMMARY = OUT_ROOT / "selector_replay_001_020_summary.md"
MANIFEST = OUT_ROOT / "selector_replay_001_020_manifest.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SELECTOR-REPLAY-001-020-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs():
    if not REPORT.exists():
        pytest.skip("001-020 selector replay output has not been generated yet")


def test_001_020_selector_replay_is_fail_closed():
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
            "делай",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            AUTHORIZATION_ID,
            "--decision",
            "production 001-020",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_001_020_selector_replay_exact_page_routing():
    require_outputs()
    report = read_json(REPORT)
    selections = {item["page"]: item for item in read_json(SELECTIONS)}

    assert report["replay_id"] == "C01TESEL020-G1-VIRAL-001"
    assert report["status"] == "static_selector_replay_completed_partial_coverage"
    assert report["requested_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert {page for page, item in selections.items() if item["selector_decision"] == "not_run_ineligible"} == {
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
    }
    assert {page for page, item in selections.items() if item["selector_decision"] == "selected_frozen_baseline"} == {
        "009",
        "010",
        "011",
        "015",
    }
    assert selections["013"]["selector_decision"] == "selected_p013_mrs_candidate"
    assert {page for page, item in selections.items() if item["selector_decision"] == "unresolved_needs_method_winner"} == {
        "012",
        "016",
        "017",
        "018",
        "020",
    }
    assert {page for page, item in selections.items() if item["selector_decision"] == "parked_candidate_policy"} == {
        "014",
        "019",
    }


def test_001_020_selector_replay_materializes_selected_hashes_without_text_copy():
    require_outputs()
    report = read_json(REPORT)
    selections = read_json(SELECTIONS)
    selected = [item for item in selections if item["selection_status"] == "selected_static_evidence_only"]

    assert report["selected_pages"] == ["009", "010", "011", "013", "015"]
    assert report["baseline_pages_materialized_with_output_hashes"] is True
    assert report["p013_mrs_selected"] is True
    for item in selected:
        assert item["selected_output_hashes"]
        assert all(isinstance(value, str) and len(value) == 64 for value in item["selected_output_hashes"].values())
        assert item["candidate_text_copied"] is False
        assert item["production_output_created"] is False
    p013 = {item["page"]: item for item in selections}["013"]
    assert p013["method_entry_id"] == "C01TEP013MRS-G1-VIRAL-001-P013"
    assert p013["selected_candidate_id"] == "p013_sac_d_noise_then_declared_seam_fracture"
    assert p013["excluded_equivalent_candidate"]["candidate_id"] == "p013_sac_e_paragraph_join_d"
    assert {item["candidate_id"] for item in p013["excluded_failed_variants"]} == {
        "p013_sac_a0_ssp_best_baseline",
        "p013_sac_b_noise_after_ssp",
        "p013_sac_c_declared_seam_fracture_after_ssp",
    }


def test_001_020_selector_replay_does_not_select_failed_or_unresolved_candidates():
    require_outputs()
    report = read_json(REPORT)
    selections = read_json(SELECTIONS)

    assert report["failed_or_superseded_candidates_selected"] is False
    assert report["all_pages_first_pass_success"] is False
    assert report["production_ready"] is False
    assert report["production_blocked_reason"] == "selector_coverage_is_partial_unresolved_pages_remain"
    for item in selections:
        if item["selector_decision"] in {"unresolved_needs_method_winner", "parked_candidate_policy"}:
            assert item["selection_status"] == "not_selected"
            assert item["failed_or_weak_candidate_selected"] is False
            assert item["candidate_text_copied"] is False


def test_001_020_selector_replay_boundary_flags_remain_false():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "ocr_execution_performed",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "reference_guided_repair_used",
        "reference_token_insertion_performed",
        "text_token_mutation_performed",
        "source_or_raw_mutation_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "selector_runtime_enabled",
        "runtime_selector_integration",
        "runtime_execution_performed",
        "production_assembly_created",
        "clean_production_output_folder_created",
        "page_021_plus_included",
        "translation_or_proofreading_performed",
        "push_performed",
        "promotion_performed",
        "acceptance_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    for key, value in report["negative_capability_matrix"].items():
        assert value is False, key
    assert report["negative_capability_matrix"]["promotion"] is False
    assert report["negative_capability_matrix"]["acceptance"] is False
    assert report["negative_capability_matrix"]["downstream_execution"] is False
    assert "no OCR/render/PDF/text-layer execution" in summary
    assert "no promotion, no acceptance, and no downstream execution" in summary
    assert "`promotion_performed=false`" in summary
    assert "`acceptance_performed=false`" in summary
    assert "`downstream_execution_performed=false`" in summary
    assert "`negative_capability_matrix.promotion=false`" in summary
    assert "`negative_capability_matrix.acceptance=false`" in summary
    assert "`negative_capability_matrix.downstream_execution=false`" in summary


def test_001_020_selector_replay_hash_pins_and_manifest():
    require_outputs()
    report = read_json(REPORT)
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert (
        report["verified_inputs"]["C01TEOR020-G1-VIRAL-001.report"]["sha256"]
        == "7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357"
    )
    assert (
        report["verified_inputs"]["C01TEP013MRS-G1-VIRAL-001.entry"]["sha256"]
        == "B09BF185510557CDAF3E757D381A416E2DEE52A8430B93E8293A348ACD6A56EC"
    )
    assert "`selector_replay_001_020_report.json`" in manifest
    assert "`selector_replay_001_020_selections.json`" in manifest
    assert "`selector_replay_001_020_summary.md`" in manifest
    assert "no production assembly" in manifest
