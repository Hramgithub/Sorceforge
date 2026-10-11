from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scripts.run_core_0_1_text_extraction_p013_seam_dedupe_diagnostic as dedupe


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p013_seam_dedupe_diagnostic.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001"
)
REPORT = OUT / "p013_seam_dedupe_diagnostic_report.json"
SUMMARY = OUT / "p013_seam_dedupe_diagnostic_summary.md"
MANIFEST = OUT / "p013_seam_dedupe_diagnostic_manifest.md"


def report() -> dict:
    if not REPORT.exists():
        pytest.skip("post-run P013 seam dedupe diagnostic output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_p013_seam_dedupe_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-SEAM-DEDUPE-DIAGNOSTIC-001" in source
    assert "Работай по плану" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source
    assert "full_page_triage_boxes_expanded_psm4" in source
    assert "6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412" in source
    assert "INCOMPLETE_STALE_DO_NOT_USE.md" in source
    assert "reference_guided_repair_used" in source
    assert "ocr_execution_performed" in source
    assert "no-expansion" not in source
    assert "acceptance_effect" in source


def test_p013_seam_dedupe_authorization_gate_rejects_missing_or_wrong_args() -> None:
    with pytest.raises(SystemExit, match="pass --execute"):
        dedupe.check_authorization([])
    with pytest.raises(SystemExit, match="requires BA-G1"):
        dedupe.check_authorization(["--execute", "--authorization-id", "wrong", "--decision", dedupe.HUMAN_DECISION])
    with pytest.raises(SystemExit, match="exact bounded human decision"):
        dedupe.check_authorization(["--execute", "--authorization-id", dedupe.AUTHORIZATION_ID, "--decision", "wrong"])


def test_p013_seam_dedupe_rejects_stale_pinned_hash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        dedupe,
        "EXPECTED_INPUT_HASHES",
        {"source_p013_candidate": (dedupe.SOURCE_ROOT / "candidate_texts" / dedupe.SOURCE_CANDIDATE_ID / "page_013_candidate.md", "BADHASH")},
    )
    with pytest.raises(SystemExit, match="hash mismatch"):
        dedupe.verify_expected_inputs()


def test_p013_seam_dedupe_rejects_existing_output_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(dedupe, "OUT_ROOT", tmp_path)
    with pytest.raises(SystemExit, match="refusing to overwrite"):
        dedupe.verify_inputs()


def test_p013_seam_dedupe_exact_overlap_only() -> None:
    proof = dedupe.find_prefix_overlap(
        previous_text="alpha tail beta gamma",
        current_text="beta gamma delta",
        previous_tail_tokens=5,
        current_prefix_tokens=3,
        minimum_overlap_tokens=2,
    )
    assert proof is not None
    assert proof["match_basis"] == "exact_normalized_token_overlap"
    assert proof["deleted_text"] == "beta gamma"
    assert proof["previous_match_ends_at_boundary"] is True
    internal = dedupe.find_prefix_overlap(
        previous_text="alpha beta gamma tail noise",
        current_text="beta gamma delta",
        previous_tail_tokens=5,
        current_prefix_tokens=3,
        minimum_overlap_tokens=2,
    )
    assert internal is None
    fuzzy = dedupe.find_prefix_overlap(
        previous_text="realize that it is someone who knows far too much",
        current_text="realize that it is someone who knows tar too much",
        previous_tail_tokens=20,
        current_prefix_tokens=20,
        minimum_overlap_tokens=8,
    )
    assert fuzzy is None


def test_p013_seam_dedupe_apply_variant_ledgers_exact_boundary_deletion(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        dedupe,
        "BLOCKS",
        [
            {"id": "P013-B001", "expanded_page_space_box": [0, 0, 100, 100]},
            {"id": "P013-B002", "expanded_page_space_box": [0, 80, 100, 180]},
        ],
    )
    monkeypatch.setattr(dedupe, "SEAMS", [{"id": "P013-S001", "previous": "P013-B001", "current": "P013-B002"}])
    repaired, ledger = dedupe.apply_variant(
        {"P013-B001": "alpha tail beta gamma", "P013-B002": "beta gamma delta"},
        {
            "previous_tail_tokens": 5,
            "current_prefix_tokens": 3,
            "minimum_overlap_tokens": 2,
        },
    )
    assert repaired["P013-B002"] == "delta"
    assert ledger == [
        {
            "seam_id": "P013-S001",
            "source_block_pair": ["P013-B001", "P013-B002"],
            "deletion_performed": True,
            "current_source_span": [0, 10],
            "previous_match_span": [11, 21],
            "deleted_text": "beta gamma",
            "deleted_token_count": 2,
            "match_basis": "exact_normalized_token_overlap",
            "expanded_page_space_overlap": [0, 80, 100, 100],
        }
    ]


def test_p013_seam_dedupe_apply_variant_does_not_delete_internal_tail_repeat(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        dedupe,
        "BLOCKS",
        [
            {"id": "P013-B001", "expanded_page_space_box": [0, 0, 100, 100]},
            {"id": "P013-B002", "expanded_page_space_box": [0, 80, 100, 180]},
        ],
    )
    monkeypatch.setattr(dedupe, "SEAMS", [{"id": "P013-S001", "previous": "P013-B001", "current": "P013-B002"}])
    repaired, ledger = dedupe.apply_variant(
        {"P013-B001": "alpha beta gamma tail noise", "P013-B002": "beta gamma delta"},
        {
            "previous_tail_tokens": 5,
            "current_prefix_tokens": 3,
            "minimum_overlap_tokens": 2,
        },
    )
    assert repaired["P013-B002"] == "beta gamma delta"
    assert ledger == [
        {
            "seam_id": "P013-S001",
            "source_block_pair": ["P013-B001", "P013-B002"],
            "deletion_performed": False,
            "expanded_page_space_overlap": [0, 80, 100, 100],
            "match_basis": "no_exact_normalized_token_overlap",
        }
    ]


def test_p013_seam_dedupe_report_boundaries_and_metrics() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert data["lane_id"] == "C01TEP013SDD-G1-VIRAL-001"
    assert data["page"] == "013"
    assert data["scope"] == "P013-only sealed-candidate assembly repair; no OCR execution"
    assert data["source_geometry_probe"] == "C01TEGP012013016017018020-G1-VIRAL-001"
    assert data["ocr_execution_performed"] is False
    assert data["reference_guided_repair_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["diagnostic_thresholds"]["sequence_similarity"] == 0.997
    assert data["diagnostic_thresholds"]["token_recall_floor"] == 0.993939
    assert data["diagnostic_thresholds"]["acceptance_effect"] == "none"
    assert data["accepted_text_mutation_performed"] is False
    assert data["semantic_text_mutation_performed"] is False
    assert data["page_status_mutation_performed"] is False
    assert data["source_or_raw_mutation_performed"] is False
    assert data["runtime_implementation_created"] is False
    assert data["page_021_plus_included"] is False
    assert data["push_performed"] is False
    assert len(data["results"]) == 2
    for result in data["results"]:
        assert result["candidate_hash_sealed_before_reference_scoring"] is True
        assert result["candidate_text_sha256"]
        assert result["deletion_ledger_sha256"]
        assert "sequence_similarity_ratio" in result["metrics"]
        assert "token_recall" in result["metrics"]
        assert result["metrics"]["token_recall"] <= 1.0
        for deletion in result["deletion_ledger"]:
            if deletion["deletion_performed"]:
                assert deletion["match_basis"] == "exact_normalized_token_overlap"
                assert deletion["expanded_page_space_overlap"] is not None
                assert deletion["deleted_token_count"] >= 3
                assert deletion["previous_match_span"][1] > deletion["previous_match_span"][0]
