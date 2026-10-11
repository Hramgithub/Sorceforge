from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020 as probe


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
)
REPORT = OUT / "geometry_probe_012_013_016_017_018_020_report.json"
SUMMARY = OUT / "geometry_probe_012_013_016_017_018_020_summary.md"
MANIFEST = OUT / "geometry_probe_012_013_016_017_018_020_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-OCR geometry probe output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_geometry_probe_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-GEOMETRY-PROBE-012-013-016-017-018-020-001" in source
    assert "коммит затем делай 1-5 план" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "014" in source and "019" in source
    assert "validate_ocr_input_surface" in source
    assert "diagnostic_threshold_met" in source
    assert "ok_level" + "_candidate" not in source
    assert "OK" + "_" not in source
    assert "ok_" + "thresholds" not in source


def test_geometry_probe_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        probe.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        probe.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", probe.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        probe.check_authorization(["--execute", "--authorization-id", probe.AUTHORIZATION_ID, "--decision", "wrong"])


def test_geometry_probe_rejects_parked_and_page_021_plus() -> None:
    with pytest.raises(SystemExit, match="parked"):
        probe.validate_page_id("014")
    with pytest.raises(SystemExit, match="page 021\\+ is blocked"):
        probe.validate_page_id("021")
    with pytest.raises(SystemExit, match="not authorized"):
        probe.validate_page_id("015")


def test_geometry_probe_rejects_malformed_boxes_and_forbidden_roles() -> None:
    class DummyImage:
        width = 100
        height = 100

    image = DummyImage()
    with pytest.raises(SystemExit, match="invalid crop_box_px"):
        probe.validate_box([1, 2, 3], image)  # type: ignore[arg-type]
    with pytest.raises(SystemExit, match="invalid crop_box_px order"):
        probe.validate_box([10, 10, 0, 20], image)  # type: ignore[arg-type]
    with pytest.raises(SystemExit, match="out of page bounds"):
        probe.validate_box([10, 10, 150, 20], image)  # type: ignore[arg-type]
    with pytest.raises(SystemExit, match="forbidden role"):
        probe.reject_forbidden_role("acceptance_evidence")


def test_geometry_probe_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        probe,
        "EXPECTED_INPUT_HASHES",
        {"router_script": (ROOT / "scripts" / "ocr_input_surface_policy.py", "BADHASH")},
    )
    with pytest.raises(SystemExit, match="hash mismatch"):
        probe.verify_expected_inputs()


def test_geometry_probe_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(probe, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        probe.verify_inputs()


def test_geometry_probe_exact_scope_and_no_leak_boundary() -> None:
    data = report()
    assert data["lane_id"] == "C01TEGP012013016017018020-G1-VIRAL-001"
    assert data["source_router"] == "C01TEISP-G1-VIRAL-001"
    assert data["pages"] == ["012", "013", "016", "017", "018", "020"]
    assert data["parked_pages_not_included"] == ["014", "019"]
    assert data["candidate_generation_reference_text_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["reference_guided_repair_used"] is False
    assert data["independent_ocr_candidate"] is True


def test_geometry_probe_outputs_metrics_and_boundaries() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert set(data["best_by_page"]) == {"012", "013", "016", "017", "018", "020"}
    for page, best in data["best_by_page"].items():
        assert (OUT / "rankings" / f"page_{page}_candidate_rankings.json").exists()
        assert best["candidate_text_path"]
        assert best["source_page_image_path"].endswith(".png")
        assert best["reference_label"] in {"reference_text_map_not_ocr_verified", "reference_ocr_verified_text_map"}
        assert "sequence_similarity_ratio" in best["metrics"]
        assert "token_recall" in best["metrics"]
        assert "similarity_delta_from_p018_control" in best["metrics"]
        assert "token_recall_delta_from_p018_control" in best["metrics"]
        assert "diagnostic_threshold_met" in best
        assert data["diagnostic_thresholds"]["acceptance_effect"] == "none"
        for item in best["region_results"]:
            assert item["page_space_box"]
            assert item["ocr_input_surface"]["surface_class"] == "full_page_region"
            assert item["ocr_input_surface_validation"]["status"] == "passed"
            assert item["ocr_result"]["prepared_region_path"]
            assert item["ocr_result"]["raw_ocr_text_path"]
            assert item["ocr_result"]["raw_ocr_tsv_path"]
    assert data["accepted_text_mutation_performed"] is False
    assert data["semantic_text_mutation_performed"] is False
    assert data["page_status_mutation_performed"] is False
    assert data["source_or_raw_mutation_performed"] is False
    assert data["pdf_text_layer_extraction_performed"] is False
    assert data["render_execution_performed"] is False
    assert data["runtime_implementation_created"] is False
    assert data["runtime_start_performed"] is False
    assert data["page_021_plus_included"] is False
    assert data["push_performed"] is False
