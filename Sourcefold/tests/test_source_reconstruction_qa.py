import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "qa_source_reconstruction_human_review.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
SRHR_ROOT = TRIAL_ROOT / "source_reconstruction_human_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_qa_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_qa_report.json"
SUMMARY = OUT_ROOT / "source_reconstruction_qa_summary.md"
SRHR_REPORT = SRHR_ROOT / "source_reconstruction_human_review_report.json"
SRHR_ACCEPTED_TEXT = SRHR_ROOT / "source_review_accepted_text.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def records_by_id(report):
    return {record["region_admission_id"]: record for record in report["qa_records"]}


def test_source_reconstruction_qa_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-QA-001" in wrong_auth.stderr


def test_source_reconstruction_qa_preserves_lineage_and_boundaries():
    report = read_json(REPORT)

    assert report["qa_id"] == "SRQA-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-QA-001"
    assert report["status"] == "source_reconstruction_qa_passed_not_fixture_or_gate"
    assert report["input_review_id"] == "SRHR-G1-VIRAL-001"
    assert report["input_review_sha256"] == sha256_file(SRHR_REPORT)
    assert report["input_accepted_text_sha256"] == sha256_file(SRHR_ACCEPTED_TEXT)
    assert report["source_acceptance"] is True
    assert report["qa_acceptance"] is True
    assert report["gate_1_advancement"] is False
    assert report["fixture_creation"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_source_reconstruction_qa.py")


def test_source_reconstruction_qa_records_all_review_decisions():
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
    assert report["summary"] == {
        "records": 7,
        "source_text_qa_passed_records": 4,
        "visual_exclusion_qa_passed_records": 3,
        "blocked_records": 0,
        "gate_1_advanced_records": 0,
    }

    text_records = {"SRA-G1-VIRAL-001-R002", "SRA-G1-VIRAL-001-R003", "SRA-G1-VIRAL-001-R004", "SRA-G1-VIRAL-001-R005"}
    for region_id, record in records.items():
        assert record["qa_acceptance"] is True
        assert record["gate_1_advancement"] is False
        if region_id in text_records:
            assert record["qa_result"] == "source_text_qa_passed"
            assert record["source_text_accepted"] is True
            assert record["visual_exclusion_accepted"] is False
        else:
            assert record["qa_result"] == "visual_exclusion_qa_passed"
            assert record["source_text_accepted"] is False
            assert record["visual_exclusion_accepted"] is True


def test_source_reconstruction_qa_preserves_r003_correction_and_heading_hint():
    report = read_json(REPORT)
    record = records_by_id(report)["SRA-G1-VIRAL-001-R003"]

    assert record["question_number"] == 4
    assert "full source crop was resent in message 259" in record["packet_correction_note"]
    assert record["semantic_heading_hint"] == [
        {"text": "Introduction", "level": "H1"},
        {"text": "Summary", "level": "H3"},
        {"text": "Overview", "level": "H3"},
        {"text": "The Spektral Krew", "level": "H2"},
    ]
    summary = SUMMARY.read_text(encoding="utf-8")
    assert "Corrected full-crop packet: `true`" in summary
    assert "Semantic heading hint preserved as metadata: `true`" in summary


def test_source_reconstruction_qa_script_has_no_ocr_pdf_render_or_raw_mutation_dependencies():
    source = SCRIPT.read_text(encoding="utf-8").lower()

    forbidden = [
        "tesseract",
        "subprocess.run(",
        "pypdf",
        "pdfminer",
        "fitz",
        "pymupdf",
        "pdftotext",
        "pdftoppm",
        "render_page(",
        "render_pdf",
        "page_render",
        "raw_outputs",
    ]
    for token in forbidden:
        assert token not in source

    out_files = [path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file()]
    assert not any("raw_outputs" in path for path in out_files)
    assert not any(path.endswith(".pdf") for path in out_files)
    assert not any(path.endswith(".tsv") for path in out_files)
