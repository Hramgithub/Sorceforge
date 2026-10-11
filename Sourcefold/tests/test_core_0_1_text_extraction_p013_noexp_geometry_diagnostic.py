from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_p013_noexp_geometry_diagnostic as noexp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p013_noexp_geometry_diagnostic.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001"
)
REPORT = OUT / "p013_noexp_geometry_diagnostic_report.json"
SUMMARY = OUT / "p013_noexp_geometry_diagnostic_summary.md"
MANIFEST = OUT / "p013_noexp_geometry_diagnostic_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-run P013 no-expansion geometry diagnostic output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_p013_noexp_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-NOEXP-GEOMETRY-DIAGNOSTIC-001" in source
    assert "Работай по плану" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "eng_oem1_psm4" in source
    assert "p013_geo_noexp_4unit_triage_logical_order" in source
    assert "reference_order" not in source
    assert "padding_px" in source
    assert "dedupe_enabled" in source
    assert "method_registry_candidate" in source


def test_p013_noexp_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        noexp.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        noexp.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", noexp.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        noexp.check_authorization(["--execute", "--authorization-id", noexp.AUTHORIZATION_ID, "--decision", "wrong"])


def test_p013_noexp_clips_half_open_boxes_without_overlap() -> None:
    records = noexp.clipped_boxes()
    assert records["P013-B001"]["original_half_open"] == [160, 205, 1260, 645]
    assert records["P013-B001"]["clipped_half_open"] == [160, 205, 1260, 625]
    assert records["P013-B002"]["original_half_open"] == [210, 625, 1270, 965]
    assert records["P013-B002"]["clipped_half_open"] == [210, 625, 1270, 960]
    assert records["P013-B003"]["clipped_half_open"] == [210, 960, 1270, 1100]
    assert records["P013-B004"]["clipped_half_open"] == [1290, 205, 2410, 905]
    assert records["P013-B005"]["clipped_half_open"] == [1335, 905, 2395, 1095]
    blocks = [key for key in records if key.startswith("P013-B")]
    for left in blocks:
        for right in blocks:
            if left >= right:
                continue
            assert noexp.boxes_overlap(records[left]["clipped_half_open"], records[right]["clipped_half_open"]) is False


def test_p013_noexp_assemblies_are_fixed_and_p013_only() -> None:
    assert [item["id"] for item in noexp.ASSEMBLIES] == [
        "p013_geo_noexp_5box_triage_order",
        "p013_geo_noexp_4unit_triage_logical_order",
        "p013_geo_noexp_4unit_column_order_control",
    ]
    assert noexp.ASSEMBLIES[1]["units"] == [["P013-B001"], ["P013-B002"], ["P013-B003", "P013-B004"], ["P013-B005"]]
    assert noexp.ASSEMBLIES[2]["units"] == [["P013-B001"], ["P013-B002"], ["P013-B004", "P013-B003"], ["P013-B005"]]
    assert noexp.PAGE == "013"
    assert noexp.PSM == 4
    assert noexp.DIAGNOSTIC_SEQUENCE_SIMILARITY == 0.997
    assert noexp.DIAGNOSTIC_TOKEN_RECALL == 0.993939


def test_p013_noexp_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(noexp, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        noexp.verify_inputs()


def test_p013_noexp_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(noexp, "EXPECTED_INPUT_HASHES", {"p013_reference_text_map": (noexp.P013_REFERENCE, "BADHASH")})
    with pytest.raises(SystemExit, match="hash mismatch"):
        noexp.verify_expected_inputs()


def test_p013_noexp_report_boundaries_and_metrics() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert data["lane_id"] == "C01TEP013GNO-G1-VIRAL-001"
    assert data["page"] == "013"
    assert data["no_expansion"] is True
    assert data["padding_px"] == 0
    assert data["dedupe_enabled"] is False
    assert data["ocr_engine_profile"] == "eng_oem1_psm4"
    assert data["candidate_generation_previous_ocr_text_used"] is False
    assert data["reference_guided_repair_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["diagnostic_thresholds"]["registry_candidate_requires_threshold"] is True
    assert data["diagnostic_thresholds"]["acceptance_effect"] == "none"
    assert data["accepted_text_mutation_performed"] is False
    assert data["semantic_text_mutation_performed"] is False
    assert data["page_status_mutation_performed"] is False
    assert data["source_or_raw_mutation_performed"] is False
    assert data["runtime_implementation_created"] is False
    assert data["production_assembly_created"] is False
    assert data["page_021_plus_included"] is False
    assert len(data["results"]) == 3
    for result in data["results"]:
        assert result["candidate_hash_sealed_before_reference_scoring"] is True
        assert result["method_registry_candidate"] is result["diagnostic_threshold_met"]
        assert "sequence_similarity_ratio" in result["metrics"]
        assert "token_recall" in result["metrics"]
