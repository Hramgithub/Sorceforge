from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_p013_expanded_lane_order_diagnostic as lane


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p013_expanded_lane_order_diagnostic.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001"
)
REPORT = OUT / "p013_expanded_lane_order_diagnostic_report.json"
SUMMARY = OUT / "p013_expanded_lane_order_diagnostic_summary.md"
MANIFEST = OUT / "p013_expanded_lane_order_diagnostic_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-run P013 expanded lane-order diagnostic output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_p013_lane_order_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-EXPANDED-LANE-ORDER-DIAGNOSTIC-001" in source
    assert "пробуй" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "PREPARED_BORDER_PX = 24" in source
    assert "page_box[0] + left - PREPARED_BORDER_PX" in source
    assert "score_candidate(candidate_text)" in source
    assert "ocr_execution_performed" in source
    assert "method_registry_candidate" in source


def test_p013_lane_order_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        lane.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        lane.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", lane.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        lane.check_authorization(["--execute", "--authorization-id", lane.AUTHORIZATION_ID, "--decision", "wrong"])


def test_p013_lane_order_variants_and_thresholds_are_fixed() -> None:
    assert lane.PREPARED_BORDER_PX == 24
    assert lane.LANE_SPLIT_X == 1200
    assert lane.LINE_BAND_TOLERANCE_PX == 18
    assert lane.DIAGNOSTIC_SEQUENCE_SIMILARITY == 0.997
    assert lane.DIAGNOSTIC_TOKEN_RECALL == 0.993939
    assert [item["id"] for item in lane.VARIANTS] == [
        "p013_expanded_lane_order_source_region_baseline",
        "p013_expanded_lane_order_lane_then_y",
        "p013_expanded_lane_order_band_then_lane",
        "p013_expanded_lane_order_lane_then_y_exact_collapse",
    ]


def test_p013_lane_order_maps_tsv_crop_space_to_page_space() -> None:
    records = lane.line_records()
    first = records[0]
    assert first["source_region"] == "P013-B001-TES"
    assert first["tsv_box"] == [114, 69, 1134, 103]
    assert first["page_space_box"] == [226, 226, 1246, 260]
    assert first["lane_id"] == "left_lane"
    assert any(item["lane_id"] == "right_lane" for item in records)


def test_p013_lane_order_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(lane, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        lane.verify_inputs()


def test_p013_lane_order_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(lane, "EXPECTED_INPUT_HASHES", {"source_candidate": (lane.SOURCE_CANDIDATE, "BADHASH")})
    with pytest.raises(SystemExit, match="hash mismatch"):
        lane.verify_expected_inputs()


def test_p013_lane_order_report_boundaries_and_metrics() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert data["lane_id"] == "C01TEP013ELO-G1-VIRAL-001"
    assert data["page"] == "013"
    assert data["source_candidate_id"] == "full_page_triage_boxes_expanded_psm4"
    assert data["ocr_execution_performed"] is False
    assert data["reference_guided_repair_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["text_token_mutation_performed"] is False
    assert data["diagnostic_thresholds"]["method_registry_candidate_requires_threshold"] is True
    assert data["diagnostic_thresholds"]["acceptance_effect"] == "none"
    assert data["accepted_text_mutation_performed"] is False
    assert data["semantic_text_mutation_performed"] is False
    assert data["page_status_mutation_performed"] is False
    assert data["source_or_raw_mutation_performed"] is False
    assert data["runtime_implementation_created"] is False
    assert data["production_assembly_created"] is False
    assert data["page_021_plus_included"] is False
    assert len(data["results"]) == 4
    for result in data["results"]:
        assert result["candidate_hash_sealed_before_reference_scoring"] is True
        assert result["method_registry_candidate"] is result["diagnostic_threshold_met"]
        assert "line_order_trace_sha256" in result
        assert "duplicate_collapse_report_sha256" in result
