import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p013_method_registry_selector.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001"
ENTRY = OUT_ROOT / "method_registry_entries" / "page_013.json"
DRY_RUN = OUT_ROOT / "selector_dry_run" / "page_013_selection.json"
REPORT = OUT_ROOT / "p013_method_registry_selector_report.json"
SUMMARY = OUT_ROOT / "p013_method_registry_selector_summary.md"
MANIFEST = OUT_ROOT / "p013_method_registry_selector_manifest.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-METHOD-REGISTRY-SELECTOR-001"
HUMAN_DECISION = (
    "Следующий шаг по плану: оформить отдельный reviewed method-registry/selector шаг для P013 winner, "
    "потом встраивать в общий first-pass 001-020 selector loop без плохих версий в production output."
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs():
    if not REPORT.exists():
        pytest.skip("P013 method-registry selector candidate decision output has not been generated yet")


def test_p013_method_registry_selector_decision_is_fail_closed():
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
            HUMAN_DECISION,
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
            "пробуй",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_p013_method_registry_selector_entry_schema_and_hash_pins():
    require_outputs()
    entry = read_json(ENTRY)
    report = read_json(REPORT)

    assert entry["entry_id"] == "C01TEP013MRS-G1-VIRAL-001-P013"
    assert entry["decision_id"] == "C01TEP013MRS-G1-VIRAL-001"
    assert entry["authorization_id"] == AUTHORIZATION_ID
    assert entry["page"] == "013"
    assert entry["status"] == "candidate_selected_not_runtime"
    assert entry["source_lane_id"] == "C01TEP013SAC-G1-VIRAL-001"
    assert entry["selected_candidate_id"] == "p013_sac_d_noise_then_declared_seam_fracture"
    assert entry["metrics"]["sequence_similarity_ratio"] == 0.998915
    assert entry["metrics"]["token_recall"] == 0.993939
    assert entry["reference_dependency"]["label"] == "reference_text_map_not_ocr_verified"
    assert entry["reference_dependency"]["note"] == "scored_against_reference_text_map_not_independently_source_accepted_ocr_truth"

    verified = report["verified_inputs"]
    assert (
        verified["C01TEP013SAC-G1-VIRAL-001.report"]["sha256"]
        == "E5436DFC3839735D7544A072B8764E57D757D45EF8AED331CD23907AEAEC29D4"
    )
    assert (
        verified["C01TEP013SAC-G1-VIRAL-001.rankings"]["sha256"]
        == "613455DDA093EC5F7E01E4F993481D344AB37643257BF5259AC546D5A557D47A"
    )
    assert (
        entry["artifact_hashes"]["candidate_text_sha256"]
        == "E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4"
    )
    assert (
        entry["artifact_hashes"]["normalized_candidate_sha256"]
        == "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D"
    )


def test_p013_method_registry_selector_tie_break_selects_d_and_notes_e():
    require_outputs()
    entry = read_json(ENTRY)
    dry_run = read_json(DRY_RUN)

    assert entry["selected_candidate_id"] == "p013_sac_d_noise_then_declared_seam_fracture"
    assert entry["equivalent_candidate_not_selected"] == {
        "candidate_id": "p013_sac_e_paragraph_join_d",
        "reason": "same_normalized_hash_and_metrics_but_separator_only_variant",
        "candidate_text_sha256": "3150AEA9688A0D4333A708348D1E2F4A44AC1732EE9C266A14323BC631B46B61",
        "normalized_candidate_sha256": "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D",
        "assembly_mode": "source_region_paragraph_join",
    }
    assert entry["tie_break"]["rule"] == "prefer_line_join_over_separator_only_equivalent_when_normalized_hash_and_metrics_match"
    assert dry_run["selected_candidate_id"] == entry["selected_candidate_id"]
    assert dry_run["candidate_text_copied"] is False
    assert "tie_break_line_join_over_separator_only_equivalent" in dry_run["selection_basis"]


def test_p013_method_registry_selector_boundary_flags_remain_false():
    require_outputs()
    report = read_json(REPORT)
    entry = read_json(ENTRY)
    dry_run = read_json(DRY_RUN)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "selector_rule_created",
        "selector_enabled",
        "runtime_selector_integration",
        "runtime_implementation_created",
        "production_assembly_created",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "page_021_plus_included",
    ]
    for payload in (report, entry):
        for flag in false_flags:
            assert payload[flag] is False, flag
    for flag in [
        "selector_rule_created",
        "selector_enabled",
        "runtime_selector_integration",
        "production_assembly_created",
        "page_001_020_runtime_loop_created",
        "page_021_plus_included",
    ]:
        assert dry_run[flag] is False, flag

    assert report["page_001_020_runtime_loop_created"] is False
    assert report["reference_token_insertion_performed"] is False
    assert report["text_token_mutation_performed"] is False
    assert "not an enabled selector rule" in summary
    for key, value in report["negative_capability_matrix"].items():
        assert value is False, key


def test_p013_method_registry_selector_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`method_registry_entries/page_013.json`" in manifest
    assert "`selector_dry_run/page_013_selection.json`" in manifest
    assert "`p013_method_registry_selector_report.json`" in manifest
    assert "`p013_method_registry_selector_summary.md`" in manifest
    assert "production assembly" in manifest
