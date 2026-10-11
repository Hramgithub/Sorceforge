from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_012_016_020_method_family import (  # noqa: E402
    AUTHORIZATION_ID,
    EXPECTED_SELECTED_PAGES_V3,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    PAGES,
    candidate_specs,
    normalize_p020_table,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_012_016_020_method_family.py"
REPORT = OUT_ROOT / "012_016_020_method_family_report.json"
SUMMARY = OUT_ROOT / "012_016_020_method_family_summary.md"
MANIFEST = OUT_ROOT / "012_016_020_method_family_manifest.md"
SELECTIONS = OUT_ROOT / "selector_replay_v3" / "selector_replay_v3_selections.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("P012/P016/P020 method-family output has not been generated yet")


def test_012_016_020_method_family_is_fail_closed():
    no_args = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_args.returncode != 0
    assert "--execute" in no_args.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "wrong",
            "--decision",
            "ок, комит и делай 12,16,20 что планировал",
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
            "wrong",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_012_016_020_method_family_refuses_overwrite():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; overwrite refusal is covered by generated-output state")
    OUT_ROOT.mkdir(parents=True)
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--execute",
                "--authorization-id",
                AUTHORIZATION_ID,
                "--decision",
                "ок, комит и делай 12,16,20 что планировал",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    finally:
        OUT_ROOT.rmdir()
    assert result.returncode != 0
    assert "refusing to overwrite existing output directory" in result.stderr


def test_012_016_020_pre_output_scope_and_pins():
    verified_inputs, unres_report, selector_v2 = verify_inputs()
    specs = candidate_specs()

    assert sorted(specs) == PAGES
    assert unres_report["still_unresolved_pages"] == ["012", "016", "020"]
    assert unres_report["production_ready"] is False
    assert len(selector_v2) == 20
    assert all(value["sha256"] for value in verified_inputs.values())
    assert specs["012"]["candidate_id"] == "p012_full_columns_scale2_psm6"
    assert specs["016"]["candidate_id"] == "p016_expanded_bottom_conf60_scale2_psm6"
    assert specs["020"]["candidate_id"] == "p020_table_normalized_scale2_threshold180_psm6"
    assert {region["postprocess"] for region in specs["016"]["regions"]} == {"confidence_60"}
    assert specs["020"]["threshold"] == 180
    assert specs["020"]["regions"][1]["postprocess"] == "p020_table_normalization"


def test_p020_table_normalization_is_source_derived_not_reference_insertion():
    source_ocr = "\n".join(
        [
            "Rumors",
            "Roll Rumor",
            "1 The real reason the island was raided back in the 1950s",
            "3 __ The hospital was just a front, and that the government",
            "5 Parents will sometimes take a boat out to the island if",
            "their child is particularly ill to leave on offering on the",
        ]
    )
    normalized = normalize_p020_table(source_ocr)

    assert "Roll Rumor" not in normalized
    assert "Roll 1: The real reason" in normalized
    assert "Roll 3: The hospital" in normalized
    assert "leave on offering" in normalized
    assert "Roll 2:" not in normalized


def test_012_016_020_report_records_threshold_winners_and_selector_v3():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "method_family_candidates_selected_static_evidence_only"
    assert report["input_unresolved_pages"] == ["012", "016", "020"]
    assert report["selected_pages"] == ["012", "016", "020"]
    assert report["still_unresolved_pages"] == []
    assert report["selected_pages_v3"] == EXPECTED_SELECTED_PAGES_V3
    assert report["production_ready"] is False
    assert report["all_pages_first_pass_success"] is False
    assert report["reference_token_insertion_performed"] is False
    assert report["selector_replay_v3"]["failed_or_superseded_candidates_selected"] is False
    assert report["selector_replay_v3"]["production_assembly_created"] is False
    assert all(candidate["diagnostic_threshold_met"] is True for candidate in report["method_candidates"])


def test_012_016_020_entries_are_static_hash_pinned_and_not_runtime():
    require_outputs()
    report = read_json(REPORT)
    entries = {entry["page"]: entry for entry in report["method_registry_entries"]}

    assert entries["012"]["entry_id"] == "C01TEMF012016020-G1-VIRAL-001-P012"
    assert entries["012"]["selected_candidate_id"] == "p012_full_columns_scale2_psm6"
    assert entries["016"]["entry_id"] == "C01TEMF012016020-G1-VIRAL-001-P016"
    assert entries["016"]["selected_candidate_id"] == "p016_expanded_bottom_conf60_scale2_psm6"
    assert entries["020"]["entry_id"] == "C01TEMF012016020-G1-VIRAL-001-P020"
    assert entries["020"]["selected_candidate_id"] == "p020_table_normalized_scale2_threshold180_psm6"
    for entry in entries.values():
        assert entry["artifact_hashes"]["candidate_text_sha256"]
        assert entry["artifact_hashes"]["normalized_candidate_sha256"]
        assert entry["selector_rule_created"] is False
        assert entry["runtime_selector_integration"] is False
        assert entry["production_assembly_created"] is False
        assert entry["accepted_text_mutation_performed"] is False
        assert entry["source_or_raw_mutation_performed"] is False


def test_012_016_020_selector_v3_routes_expected_pages():
    require_outputs()
    report = read_json(REPORT)
    selections = read_json(SELECTIONS)
    groups = report["selector_replay_v3"]["groups"]

    assert len(selections) == 20
    assert groups["not_run_ineligible"] == ["001", "002", "003", "004", "005", "006", "007", "008"]
    assert groups["selected_frozen_baseline"] == ["009", "010", "011", "015"]
    assert groups["selected_p013_discovered_candidate"] == ["013"]
    assert groups["selected_unresolved_pages_discovered_candidate"] == ["017", "018"]
    assert groups["selected_012_016_020_method_family_candidate"] == ["012", "016", "020"]
    assert groups["parked_candidate_policy"] == ["014", "019"]


def test_012_016_020_boundaries_are_false_except_bounded_ocr():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert report["ocr_execution_performed"] is True
    assert report["ocr_execution_scope"] == "bounded_candidate_generation_for_pages_012_016_020_only"
    false_flags = [
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "reference_guided_repair_used",
        "reference_token_insertion_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
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
    assert set(report["negative_capability_matrix"]) == set(NEGATIVE_CAPABILITIES)
    for capability, value in report["negative_capability_matrix"].items():
        assert value is False, capability
    assert "`ocr_execution_performed=true`" in summary
    assert "`reference_token_insertion_performed=false`" in summary
    assert "`production_assembly_created=false`" in summary
    assert "`acceptance_performed=false`" in summary


def test_012_016_020_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`method_registry_entries/page_012.json`" in manifest
    assert "`method_registry_entries/page_016.json`" in manifest
    assert "`method_registry_entries/page_020.json`" in manifest
    assert "`selector_replay_v3/selector_replay_v3_selections.json`" in manifest
    assert "`012_016_020_method_family_report.json`" in manifest
    assert "no production assembly" in manifest
