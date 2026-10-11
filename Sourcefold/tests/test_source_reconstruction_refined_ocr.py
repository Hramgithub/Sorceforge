import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_source_reconstruction_refined_ocr.py"
OUT_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "source_reconstruction_refined_ocr_G1_VIRAL_001"
)
REPORT = OUT_ROOT / "source_reconstruction_refined_ocr_report.json"
ROWS = OUT_ROOT / "source_reconstruction_refined_ocr_rows.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_refined_ocr_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001" in wrong_auth.stderr


def test_refined_ocr_preserves_boundaries():
    report = read_json(REPORT)

    assert report["run_id"] == "SRFO-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001"
    assert report["status"] == "refined_ocr_evidence_only"
    assert report["input_report_id"] == "SRCO-G1-VIRAL-001"
    assert report["input_report_sha256"] == "08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F"
    assert report["source_acceptance"] is False
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["ocr_executed"] is True
    assert report["summary"]["human_review_ready"] is False
    assert report["summary"]["human_review_blocked"] is True


def test_refined_ocr_target_is_exactly_one_srco_record():
    report = read_json(REPORT)
    rows = read_json(ROWS)
    inputs = report["inputs"]

    assert report["summary"]["refined_input_records"] == 1
    assert report["summary"]["matrix_rows"] == 16
    assert {row["region_admission_id"] for row in rows} == {"SRA-G1-VIRAL-001-R003"}
    assert {row["sample_id"] for row in rows} == {"GS-G1-VIRAL-003"}
    assert {row["page_id"] for row in rows} == {"PG-G1-VIRAL-P005"}
    assert {row["predecessor_zone_id"] for row in rows} == {"z01"}
    assert {row["psm"] for row in rows} == {1, 4, 8, 11}
    assert {3, 6}.isdisjoint({row["psm"] for row in rows})

    only = inputs[0]
    assert only["region_admission_id"] == "SRA-G1-VIRAL-001-R003"
    assert only["input_crop"].endswith("SRA-G1-VIRAL-001-R003__narrow_contents_candidate.png")
    assert only["input_crop_sha256"] == "A09B5848048C3BD20FEB71B0FC37FC55E108AA08454BCFB1156D3FAD62E5B40F"
    assert only["source_input_crop_sha256"] == "54E0E3B0A956EA0BA215987D25B242EED3A803100AD87C2E8949E3EA4592F66A"
    assert only["metric_scope"] == "refined_crop_visible_text_only"
    assert only["replaces_full_region_text"] is False


def test_refined_ocr_outputs_match_disk_hashes():
    report = read_json(REPORT)
    rows = read_json(ROWS)

    for item in report["inputs"]:
        input_crop = ROOT / item["input_crop"]
        source_input_crop = ROOT / item["source_input_crop"]
        assert item["input_crop_sha256"] == sha256_file(input_crop)
        assert item["source_input_crop_sha256"] == sha256_file(source_input_crop)

    for row in rows:
        assert row["prepared_input_sha256"] == sha256_file(ROOT / row["prepared_input"])
        assert row["raw_text_sha256"] == sha256_file(ROOT / row["raw_text"])
        assert row["raw_tsv_sha256"] == sha256_file(ROOT / row["raw_tsv"])


def test_refined_ocr_result_is_not_human_ready_by_score():
    report = read_json(REPORT)
    only = report["inputs"][0]

    assert report["summary"]["normalized_exact_records"] == 1
    assert only["normalized_exact"] is True
    assert only["token_recall"] == 1.0
    assert only["human_review_ready"] is False
    assert only["source_acceptance"] is False
    assert only["overlay_qc"]["status"] == "needs_visual_review"
    assert report["next_authorization_recommendation"] == "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001"


def test_refined_ocr_script_has_no_pdf_or_render_dependencies():
    source = SCRIPT.read_text(encoding="utf-8").lower()

    forbidden = ["pypdf", "pdfminer", "fitz", "pymupdf", "pdftotext", "pdftoppm"]
    for token in forbidden:
        assert token not in source
