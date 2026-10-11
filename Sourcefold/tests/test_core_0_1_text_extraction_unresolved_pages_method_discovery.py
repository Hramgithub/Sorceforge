from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_core_0_1_text_extraction_unresolved_pages_method_discovery import (  # noqa: E402
    AUTHORIZATION_ID,
    DISCOVERY_ID,
    EXPECTED_DISCOVERED,
    EXPECTED_STILL_UNRESOLVED,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    discover_entries,
    geometry_rows,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_unresolved_pages_method_discovery.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_unresolved_pages_method_discovery_G1_VIRAL_001"
REPORT = OUT_ROOT / "unresolved_pages_method_discovery_report.json"
SUMMARY = OUT_ROOT / "unresolved_pages_method_discovery_summary.md"
MANIFEST = OUT_ROOT / "unresolved_pages_method_discovery_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("unresolved-pages discovery output has not been generated yet")


def test_unresolved_pages_method_discovery_is_fail_closed():
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
            "давай",
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


def test_unresolved_pages_method_discovery_refuses_overwrite():
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
                "давай",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    finally:
        OUT_ROOT.rmdir()
    assert result.returncode != 0
    assert "refusing to overwrite existing output directory" in result.stderr


def test_unresolved_pages_pre_output_discovers_only_threshold_pages():
    _, selector_report, _selector_selections, p013_entry, geometry_report = verify_inputs()
    rows = geometry_rows(geometry_report)
    discovered, unresolved = discover_entries(rows)

    assert selector_report["unresolved_pages"] == ["012", "016", "017", "018", "020"]
    assert p013_entry["entry_id"] == "C01TEP013DISC-G1-VIRAL-001-P013"
    assert [entry["page"] for entry in discovered] == EXPECTED_DISCOVERED
    assert [item["page"] for item in unresolved] == EXPECTED_STILL_UNRESOLVED
    assert {entry["selected_candidate_id"] for entry in discovered} == {
        "full_page_bright_title_body_psm7_4_4",
        "full_page_expanded_overlap_psm4",
    }
    assert all(entry["metrics"]["sequence_similarity_ratio"] >= 0.997 for entry in discovered)
    assert all(item["metrics"]["sequence_similarity_ratio"] < 0.997 for item in unresolved)


def test_unresolved_pages_report_records_partial_selector_v2():
    require_outputs()
    report = read_json(REPORT)

    assert report["discovery_id"] == DISCOVERY_ID
    assert report["status"] == "unresolved_pages_method_discovery_partial_coverage"
    assert report["discovered_pages"] == ["017", "018"]
    assert report["still_unresolved_pages"] == ["012", "016", "020"]
    assert report["selected_pages_v2"] == ["009", "010", "011", "013", "015", "017", "018"]
    assert report["production_ready"] is False
    assert report["all_pages_first_pass_success"] is False
    assert report["selector_replay_v2"]["failed_or_superseded_candidates_selected"] is False


def test_unresolved_pages_entries_are_static_and_hash_pinned():
    require_outputs()
    report = read_json(REPORT)

    entries = {entry["page"]: entry for entry in report["discovered_entries"]}
    assert entries["017"]["entry_id"] == "C01TEUNRES020-G1-VIRAL-001-P017"
    assert entries["017"]["selected_candidate_id"] == "full_page_bright_title_body_psm7_4_4"
    assert entries["017"]["artifact_hashes"]["candidate_text_sha256"] == (
        "EE2C75BA5B7083F143EACF9B42862AB7DDBFDFE6C4AD87A66F0B18D833D4E0F2"
    )
    assert entries["018"]["entry_id"] == "C01TEUNRES020-G1-VIRAL-001-P018"
    assert entries["018"]["selected_candidate_id"] == "full_page_expanded_overlap_psm4"
    assert entries["018"]["artifact_hashes"]["candidate_text_sha256"] == (
        "047189E7340BFE706FCF705B01E50551FFC4EE015A39C4DE458F0E116C2933D4"
    )
    for entry in entries.values():
        assert entry["selector_rule_created"] is False
        assert entry["runtime_selector_integration"] is False
        assert entry["production_assembly_created"] is False


def test_unresolved_pages_selector_v2_routes_expected_pages():
    require_outputs()
    report = read_json(REPORT)
    groups = report["selector_replay_v2"]["groups"]

    assert groups["not_run_ineligible"] == ["001", "002", "003", "004", "005", "006", "007", "008"]
    assert groups["selected_frozen_baseline"] == ["009", "010", "011", "015"]
    assert groups["selected_p013_discovered_candidate"] == ["013"]
    assert groups["selected_unresolved_pages_discovered_candidate"] == ["017", "018"]
    assert groups["still_unresolved_needs_method_winner"] == ["012", "016", "020"]
    assert groups["parked_candidate_policy"] == ["014", "019"]


def test_unresolved_pages_boundaries_are_false():
    require_outputs()
    report = read_json(REPORT)
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
    assert "`production_assembly_created=false`" in summary
    assert "`page_021_plus_included=false`" in summary
    assert "`acceptance_performed=false`" in summary


def test_unresolved_pages_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`method_registry_entries/page_017.json`" in manifest
    assert "`method_registry_entries/page_018.json`" in manifest
    assert "`selector_replay_v2/selector_replay_v2_selections.json`" in manifest
    assert "`unresolved_pages_method_discovery_report.json`" in manifest
    assert "no production assembly" in manifest
