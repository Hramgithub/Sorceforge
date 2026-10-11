from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_p013_structural_suppression_diagnostic as ssp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p013_structural_suppression_diagnostic.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001"
)
REPORT = OUT / "p013_structural_suppression_diagnostic_report.json"
SUMMARY = OUT / "p013_structural_suppression_diagnostic_summary.md"
MANIFEST = OUT / "p013_structural_suppression_diagnostic_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-run P013 SSP diagnostic output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_p013_ssp_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "C01TEP013SSP-G1-VIRAL-001" in source
    assert "core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001" in source
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-SUPPRESSION-DIAGNOSTIC-001" in source
    assert "пробуй" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "ocr_execution_performed" in source
    assert "reference_guided_repair_used" in source
    assert "method_registry_candidate" in source


def test_p013_ssp_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        ssp.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        ssp.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", ssp.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        ssp.check_authorization(["--execute", "--authorization-id", ssp.AUTHORIZATION_ID, "--decision", "wrong"])


def test_p013_ssp_pins_elo_and_raw_tsv_inputs() -> None:
    expected = set(ssp.EXPECTED_INPUT_HASHES)
    assert {
        "elo_report",
        "elo_manifest",
        "elo_line_records_raw",
        "elo_best_trace",
        "elo_best_collapse_report",
        "source_ranking",
        "p013_b001_tsv",
        "p013_b002_tsv",
        "p013_b003_tsv",
        "p013_b004_tsv",
        "p013_b005_tsv",
    }.issubset(expected)
    assert "source_reference" not in expected
    assert ssp.EXPECTED_REFERENCE_HASH == "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67"


def test_p013_ssp_record_schema_and_confidence_are_derived_from_tsv() -> None:
    records = ssp.elo_best_records()
    first = records[0]
    assert first["record_id"] == "P013-B001-TES:1.1.1"
    assert first["source_order"] == "01.001"
    assert first["tsv_line_key"] == first["record_id"]
    assert first["page_bbox_half_open"] == [226, 226, 1246, 260]
    assert first["confidence"]["mean_confidence"] > 90
    assert any(item["record_id"] == "P013-B001-TES:3.1.1" for item in records)


def test_p013_ssp_variant_list_starts_with_elo_baseline() -> None:
    assert ssp.VARIANTS == [
        "p013_ssp_a0_elo_exact_collapse_baseline",
        "p013_ssp_a_near_overlap_confidence",
        "p013_ssp_b_noise_from_a0",
        "p013_ssp_c_floor_guarded_near_overlap_then_noise",
    ]


def test_p013_ssp_near_overlap_multiway_cluster_tie_preserves_all() -> None:
    base = {
        "lane_id": "left_lane",
        "page_center": [100, 100],
        "page_bbox_half_open": [0, 0, 100, 20],
        "normalized_text": "alpha beta gamma",
        "text": "alpha beta gamma",
        "source_order": "01.001",
        "tsv_line_key": "A:1.1.1",
    }
    records = [
        {**base, "record_id": "A:1.1.1", "final_ordinal": 1, "confidence": {"mean_confidence": 90.0}},
        {**base, "record_id": "A:1.1.2", "final_ordinal": 2, "confidence": {"mean_confidence": 89.5}},
        {**base, "record_id": "A:1.1.3", "final_ordinal": 3, "confidence": {"mean_confidence": 89.2}},
    ]
    retained, ledger = ssp.suppress_near_overlap_confidence(records)
    assert [item["record_id"] for item in retained] == ["A:1.1.1", "A:1.1.2", "A:1.1.3"]
    assert ledger["components"][0]["decision"] == "preserved_ambiguous_confidence_tie"


def test_p013_ssp_near_overlap_multiway_cluster_removes_lower_confidence() -> None:
    base = {
        "lane_id": "left_lane",
        "page_center": [100, 100],
        "page_bbox_half_open": [0, 0, 100, 20],
        "normalized_text": "alpha beta gamma",
        "text": "alpha beta gamma",
        "source_order": "01.001",
        "tsv_line_key": "A:1.1.1",
    }
    records = [
        {**base, "record_id": "A:1.1.1", "final_ordinal": 1, "confidence": {"mean_confidence": 92.0}},
        {**base, "record_id": "A:1.1.2", "final_ordinal": 2, "confidence": {"mean_confidence": 88.0}},
        {**base, "record_id": "A:1.1.3", "final_ordinal": 3, "confidence": {"mean_confidence": 87.0}},
    ]
    retained, ledger = ssp.suppress_near_overlap_confidence(records)
    assert [item["record_id"] for item in retained] == ["A:1.1.1"]
    assert set(ledger["components"][0]["suppressed_record_ids"]) == {"A:1.1.2", "A:1.1.3"}


def test_p013_ssp_near_overlap_transitive_chain_preserves_component() -> None:
    base = {
        "lane_id": "left_lane",
        "page_center": [100, 100],
        "normalized_text": "alpha beta gamma",
        "text": "alpha beta gamma",
        "source_order": "01.001",
        "tsv_line_key": "A:1.1.1",
    }
    records = [
        {
            **base,
            "record_id": "A:1.1.1",
            "final_ordinal": 1,
            "page_bbox_half_open": [0, 0, 100, 20],
            "confidence": {"mean_confidence": 99.0},
        },
        {
            **base,
            "record_id": "A:1.1.2",
            "final_ordinal": 2,
            "page_bbox_half_open": [20, 0, 120, 20],
            "confidence": {"mean_confidence": 80.0},
        },
        {
            **base,
            "record_id": "A:1.1.3",
            "final_ordinal": 3,
            "page_bbox_half_open": [40, 0, 140, 20],
            "confidence": {"mean_confidence": 70.0},
        },
    ]
    retained, ledger = ssp.suppress_near_overlap_confidence(records)
    assert [item["record_id"] for item in retained] == ["A:1.1.1", "A:1.1.2", "A:1.1.3"]
    assert ledger["components"][0]["decision"] == "preserved_non_clique_transitive_component"


def test_p013_ssp_elo_floor_guard_fails_closed() -> None:
    with pytest.raises(SystemExit, match="failed ELO floor guard"):
        ssp.assert_elo_floor(
            "p013_ssp_a0_elo_exact_collapse_baseline",
            {"sequence_similarity_ratio": 0.1, "token_recall": ssp.ELO_BEST_TOKEN_RECALL},
        )


def test_p013_ssp_noise_rule_uses_exact_geometry_and_simultaneous_neighbors() -> None:
    records = ssp.elo_best_records()
    noise = next(item for item in records if item["record_id"] == "P013-B001-TES:3.1.1")
    should_suppress, proof = ssp.is_noise_line(noise, records)
    assert should_suppress is True
    assert proof["height_px"] == 10
    assert proof["nearest_same_lane_neighbor"]["vertical_edge_gap_px"] <= ssp.LOW_CONF_NOISE_NEIGHBOR_Y_GAP_PX


def test_p013_ssp_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ssp, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        ssp.verify_inputs()


def test_p013_ssp_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ssp, "EXPECTED_INPUT_HASHES", {"elo_report": (ssp.ELO_REPORT, "BADHASH")})
    with pytest.raises(SystemExit, match="hash mismatch"):
        ssp.verify_expected_inputs()


def test_p013_ssp_report_boundaries_and_metrics() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert data["lane_id"] == "C01TEP013SSP-G1-VIRAL-001"
    assert data["page"] == "013"
    assert data["source_lane_id"] == "C01TEP013ELO-G1-VIRAL-001"
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
    baseline = next(item for item in data["results"] if item["candidate_id"] == "p013_ssp_a0_elo_exact_collapse_baseline")
    assert baseline["metrics"]["sequence_similarity_ratio"] == pytest.approx(0.433325)
    assert baseline["metrics"]["token_recall"] == pytest.approx(0.993939)
    guarded = next(item for item in data["results"] if item["candidate_id"] == "p013_ssp_c_floor_guarded_near_overlap_then_noise")
    assert guarded["metrics"]["sequence_similarity_ratio"] >= 0.433325
    assert guarded["metrics"]["token_recall"] >= 0.993939
    for result in data["results"]:
        assert result["candidate_hash_sealed_before_reference_scoring"] is True
        assert result["method_registry_candidate"] is result["diagnostic_threshold_met"]
