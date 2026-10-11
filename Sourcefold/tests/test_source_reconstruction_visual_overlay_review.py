import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "review_source_reconstruction_visual_overlay.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_visual_overlay_review_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_visual_overlay_review_report.json"
SRRB_REPORT = TRIAL_ROOT / "source_reconstruction_rebuild_G1_VIRAL_001" / "source_reconstruction_rebuild_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def records_by_id(report):
    return {
        record["region_admission_id"]: record
        for record in report["candidate_records"] + report["visual_qc_records"]
    }


def test_visual_overlay_review_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001" in wrong_auth.stderr


def test_visual_overlay_review_preserves_boundaries_and_lineage():
    report = read_json(REPORT)

    assert report["report_id"] == "SRVO-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001"
    assert report["status"] == "visual_overlay_blockers_closed_for_later_human_review"
    assert report["input_package_id"] == "SRRB-G1-VIRAL-001"
    assert report["input_package_sha256"] == sha256_file(SRRB_REPORT)
    assert report["source_acceptance"] is False
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["candidate_text_is_source_accepted"] is False
    assert report["human_review_ready"] is True
    assert report["human_review_blocked"] is False


def test_visual_overlay_review_closes_all_predecessor_blockers():
    report = read_json(REPORT)
    records = records_by_id(report)

    assert set(records) == {
        "SRA-G1-VIRAL-001-R001",
        "SRA-G1-VIRAL-001-R002",
        "SRA-G1-VIRAL-001-R003",
        "SRA-G1-VIRAL-001-R004",
        "SRA-G1-VIRAL-001-R005",
        "SRA-G1-VIRAL-001-R006",
        "SRA-G1-VIRAL-001-R007",
    }
    assert report["summary"]["remaining_blockers"] == []
    assert report["summary"]["human_review_ready_records"] == 7
    for record in records.values():
        assert record["human_review_ready"] is True
        assert record["remaining_blockers"] == []

    assert records["SRA-G1-VIRAL-001-R001"]["decision"] == "visual_only_component_excluded_from_source_text_candidate"
    assert records["SRA-G1-VIRAL-001-R002"]["candidate_text"] == "Contents"
    assert records["SRA-G1-VIRAL-001-R003"]["candidate_text"] == "Introduction\nSummary\nOverview\nThe Spektral Krew"
    assert records["SRA-G1-VIRAL-001-R003"]["candidate_text_basis"] == "manual_visual_review_of_full_source_crop"
    assert records["SRA-G1-VIRAL-001-R004"]["candidate_text"] == "Introduction"
    assert records["SRA-G1-VIRAL-001-R006"]["candidate_text"] is None
    assert records["SRA-G1-VIRAL-001-R007"]["decision"] == "non_source_layout_background_excluded"


def test_visual_overlay_review_reference_hashes_match_disk():
    report = read_json(REPORT)

    for record in records_by_id(report).values():
        reference = ROOT / record["visual_reference"]
        assert reference.exists()
        assert record["visual_reference_sha256"] == sha256_file(reference)
        if record["source_input_crop"] is not None:
            source_crop = ROOT / record["source_input_crop"]
            assert source_crop.exists()
            assert record["source_input_crop_sha256"] == sha256_file(source_crop)


def test_visual_overlay_review_script_has_no_ocr_pdf_or_render_dependencies():
    source = SCRIPT.read_text(encoding="utf-8").lower()

    forbidden = ["tesseract", "subprocess.run(", "pypdf", "pdfminer", "fitz", "pymupdf", "pdftotext", "pdftoppm"]
    for token in forbidden:
        assert token not in source

    out_files = [path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file()]
    assert not any("raw_outputs" in path for path in out_files)
    assert not any(path.endswith(".pdf") for path in out_files)
    assert not any(path.endswith(".tsv") for path in out_files)
