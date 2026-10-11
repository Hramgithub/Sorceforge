import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "rebuild_source_reconstruction_candidate.py"
OUT_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "source_reconstruction_rebuild_G1_VIRAL_001"
)
REPORT = OUT_ROOT / "source_reconstruction_rebuild_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_rebuild_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001" in wrong_auth.stderr


def test_rebuild_preserves_boundaries_and_lineage():
    report = read_json(REPORT)

    assert report["package_id"] == "SRRB-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001"
    assert report["status"] == "rebuilt_candidate_blocked_for_visual_overlay_review"
    assert report["inputs"]["srco_report_sha256"] == "08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F"
    assert report["inputs"]["srfo_report_sha256"] == "531B61BE0C826E94427320C3CDEBEC1F2459043097ACF8FD9B456B0A0C4AA687"
    assert report["source_acceptance"] is False
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["human_review_ready"] is False
    assert report["human_review_blocked"] is True


def test_rebuild_keeps_visual_and_overlay_blockers():
    report = read_json(REPORT)
    candidates = {record["region_admission_id"]: record for record in report["candidate_records"]}
    visuals = {record["region_admission_id"]: record for record in report["visual_qc_records"]}

    assert set(candidates) == {
        "SRA-G1-VIRAL-001-R001",
        "SRA-G1-VIRAL-001-R002",
        "SRA-G1-VIRAL-001-R003",
        "SRA-G1-VIRAL-001-R004",
        "SRA-G1-VIRAL-001-R005",
    }
    assert set(visuals) == {"SRA-G1-VIRAL-001-R006", "SRA-G1-VIRAL-001-R007"}
    assert candidates["SRA-G1-VIRAL-001-R003"]["candidate_text"] is None
    assert candidates["SRA-G1-VIRAL-001-R003"]["normalized_exact"] is True
    assert candidates["SRA-G1-VIRAL-001-R003"]["replaces_full_region_text"] is False
    assert candidates["SRA-G1-VIRAL-001-R005"]["human_review_ready"] is True
    assert report["summary"]["later_human_ready_records"] == 1
    assert len(report["summary"]["blocking_records"]) == 6
    assert report["next_authorization_recommendation"] == "BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001"


def test_rebuild_crop_references_match_disk_hashes():
    report = read_json(REPORT)

    for record in report["candidate_records"] + report["visual_qc_records"]:
        path = ROOT / record["crop_reference"]
        assert path.exists()
        assert record["crop_reference_sha256"] == sha256_file(path)


def test_rebuild_script_has_no_ocr_pdf_or_render_dependencies():
    source = SCRIPT.read_text(encoding="utf-8").lower()

    forbidden = ["tesseract", "subprocess.run(", "pypdf", "pdfminer", "fitz", "pymupdf", "pdftotext", "pdftoppm"]
    for token in forbidden:
        assert token not in source
