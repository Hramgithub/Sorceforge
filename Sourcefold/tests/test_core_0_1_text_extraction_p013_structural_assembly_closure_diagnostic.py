from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic as sac


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001"
)
REPORT = OUT / "p013_structural_assembly_closure_diagnostic_report.json"
SUMMARY = OUT / "p013_structural_assembly_closure_diagnostic_summary.md"
MANIFEST = OUT / "p013_structural_assembly_closure_diagnostic_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-run P013 SAC diagnostic output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_p013_sac_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "C01TEP013SAC-G1-VIRAL-001" in source
    assert "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001" in source
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-ASSEMBLY-CLOSURE-DIAGNOSTIC-001" in source
    assert "Следующий ход" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "ocr_execution_performed" in source
    assert "reference_guided_repair_used" in source
    assert "method_registry_candidate" in source


def test_p013_sac_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        sac.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        sac.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", sac.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        sac.check_authorization(["--execute", "--authorization-id", sac.AUTHORIZATION_ID, "--decision", "wrong"])


def test_p013_sac_pins_ssp_and_raw_tsv_inputs() -> None:
    expected = set(sac.EXPECTED_INPUT_HASHES)
    assert {
        "ssp_report",
        "ssp_summary",
        "ssp_manifest",
        "ssp_a_candidate",
        "ssp_a_normalized_candidate",
        "ssp_a_retained_records",
        "ssp_a_suppression_ledger",
        "source_ranking",
        "p013_b001_tsv",
        "p013_b002_tsv",
        "p013_b003_tsv",
        "p013_b004_tsv",
        "p013_b005_tsv",
    }.issubset(expected)
    assert "source_reference" not in expected
    assert sac.EXPECTED_REFERENCE_HASH == "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67"


def test_p013_sac_variant_list_is_fixed() -> None:
    assert sac.VARIANTS == [
        "p013_sac_a0_ssp_best_baseline",
        "p013_sac_b_noise_after_ssp",
        "p013_sac_c_declared_seam_fracture_after_ssp",
        "p013_sac_d_noise_then_declared_seam_fracture",
        "p013_sac_e_paragraph_join_d",
    ]


def test_p013_sac_baseline_uses_ssp_best_records() -> None:
    records = sac.ssp_best_records()
    assert any(item["record_id"] == "P013-B001-TES:3.1.1" for item in records)
    assert any(item["record_id"] == "P013-B005-TES:1.1.1" for item in records)
    retained, ledgers, assembly_mode = sac.apply_variant(records, "p013_sac_a0_ssp_best_baseline")
    assert retained == records
    assert ledgers == []
    assert assembly_mode == "line_join"


def test_p013_sac_noise_deletion_is_low_confidence_geometry_only() -> None:
    records = sac.ssp_best_records()
    retained, ledgers, _ = sac.apply_variant(records, "p013_sac_b_noise_after_ssp")
    removed = {item["record_id"] for item in records} - {item["record_id"] for item in retained}
    assert removed == {"P013-B001-TES:3.1.1"}
    assert ledgers[0]["rule_id"] == "low_confidence_thin_noise_or_punctuation_fragment"
    assert ledgers[0]["suppressed_records"][0]["mean_confidence"] <= 50.0


def test_p013_sac_declared_seam_fracture_deletes_later_fragment_only() -> None:
    records = sac.ssp_best_records()
    retained, ledgers, _ = sac.apply_variant(records, "p013_sac_c_declared_seam_fracture_after_ssp")
    removed = {item["record_id"] for item in records} - {item["record_id"] for item in retained}
    assert removed == {"P013-B005-TES:1.1.1"}
    assert ledgers[0]["rule_id"] == "declared_seam_fractured_duplicate"
    assert ledgers[0]["parameters"]["text_literal_matching"] is False
    assert ledgers[0]["edges"][0]["boundary_position_proof"]["earlier_is_lower_boundary_record"] is True
    assert ledgers[0]["edges"][0]["token_containment_proof"]["bounded_fragment_drop"] is True


def test_p013_sac_non_declared_same_lane_tie_is_preserved() -> None:
    records = sac.ssp_best_records()
    left = next(item for item in records if item["record_id"] == "P013-B004-TES:1.1.13")
    right = {**left, "record_id": "P013-B099-TES:1.1.1", "source_region": "P013-B099-TES", "source_order": "99.001"}
    retained, ledger = sac.suppress_declared_seam_fractures([left, right])
    assert [item["record_id"] for item in retained] == [left["record_id"], right["record_id"]]
    assert ledger["suppressed_records"] == []


def test_p013_sac_declared_seam_preserves_novel_tokens() -> None:
    records = sac.ssp_best_records()
    earlier = next(item for item in records if item["record_id"] == "P013-B004-TES:1.1.13")
    later = next(item for item in records if item["record_id"] == "P013-B005-TES:1.1.1")
    novel_later = {
        **later,
        "text": "new him, he'll get them off the island by dawn.",
        "normalized_text": "new him he ll get them off the island by dawn",
    }
    retained, ledger = sac.suppress_declared_seam_fractures([earlier, novel_later])
    assert [item["record_id"] for item in retained] == [earlier["record_id"], later["record_id"]]
    assert ledger["suppressed_records"] == []


def test_p013_sac_declared_seam_preserves_non_boundary_records() -> None:
    records = sac.ssp_best_records()
    earlier = next(item for item in records if item["record_id"] == "P013-B004-TES:1.1.12")
    later = next(item for item in records if item["record_id"] == "P013-B005-TES:1.1.1")
    boundary_blocker = {
        **earlier,
        "record_id": "P013-B004-TES:9.9.9",
        "final_ordinal": earlier["final_ordinal"] + 1,
        "normalized_text": "unrelated boundary proof blocker",
        "text": "unrelated boundary proof blocker",
    }
    shifted_later = {
        **later,
        "page_center": earlier["page_center"],
        "page_bbox_half_open": earlier["page_bbox_half_open"],
        "normalized_text": earlier["normalized_text"],
    }
    retained, ledger = sac.suppress_declared_seam_fractures([earlier, boundary_blocker, shifted_later])
    assert [item["record_id"] for item in retained] == [
        earlier["record_id"],
        boundary_blocker["record_id"],
        later["record_id"],
    ]
    assert ledger["suppressed_records"] == []


def test_p013_sac_declared_seam_preserves_partial_overlaps() -> None:
    records = sac.ssp_best_records()
    earlier = next(item for item in records if item["record_id"] == "P013-B004-TES:1.1.13")
    later = next(item for item in records if item["record_id"] == "P013-B005-TES:1.1.1")
    partial_later = {**later, "page_bbox_half_open": [1900, 881, 2025, 910]}
    retained, ledger = sac.suppress_declared_seam_fractures([earlier, partial_later])
    assert [item["record_id"] for item in retained] == [earlier["record_id"], later["record_id"]]
    assert ledger["suppressed_records"] == []


def test_p013_sac_paragraph_join_changes_separators_only() -> None:
    records = sac.ssp_best_records()
    retained_d, _, mode_d = sac.apply_variant(records, "p013_sac_d_noise_then_declared_seam_fracture")
    retained_e, _, mode_e = sac.apply_variant(records, "p013_sac_e_paragraph_join_d")
    text_d, trace_d = sac.assemble_text(retained_d, mode_d)
    text_e, trace_e = sac.assemble_text(retained_e, mode_e)
    assert [item["record_id"] for item in retained_d] == [item["record_id"] for item in retained_e]
    assert trace_d["record_text_mutation_performed"] is False
    assert trace_e["record_text_mutation_performed"] is False
    assert trace_e["separator_only_change"] is True
    assert sac.overview.normalize_candidate_for_metrics(text_d) == sac.overview.normalize_candidate_for_metrics(text_e)


def test_p013_sac_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sac, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        sac.verify_inputs()


def test_p013_sac_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sac, "EXPECTED_INPUT_HASHES", {"ssp_report": (sac.SSP_REPORT, "BADHASH")})
    with pytest.raises(SystemExit, match="hash mismatch"):
        sac.verify_expected_inputs()


def test_p013_sac_report_boundaries_and_threshold_result() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert data["lane_id"] == "C01TEP013SAC-G1-VIRAL-001"
    assert data["page"] == "013"
    assert data["source_lane_id"] == "C01TEP013SSP-G1-VIRAL-001"
    assert data["ocr_execution_performed"] is False
    assert data["reference_guided_repair_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["all_candidate_hashes_sealed_before_reference_text_load"] is True
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
    baseline = next(item for item in data["results"] if item["candidate_id"] == "p013_sac_a0_ssp_best_baseline")
    assert baseline["metrics"]["sequence_similarity_ratio"] == pytest.approx(0.914027)
    assert baseline["metrics"]["token_recall"] == pytest.approx(0.993939)
    for result in data["results"]:
        assert result["candidate_hash_sealed_before_reference_scoring"] is True
        assert result["method_registry_candidate"] is result["diagnostic_threshold_met"]
