import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "record_source_reconstruction_human_review.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_human_review_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_human_review_report.json"
ACCEPTED_TEXT = OUT_ROOT / "source_review_accepted_text.md"
SRHP_REPORT = (
    TRIAL_ROOT
    / "source_reconstruction_human_package_G1_VIRAL_001"
    / "source_reconstruction_human_package_report.json"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def records_by_id(report):
    return {record["region_admission_id"]: record for record in report["human_review_records"]}


def test_human_review_recording_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001" in wrong_auth.stderr


def test_human_review_preserves_lineage_and_boundaries():
    report = read_json(REPORT)

    assert report["review_id"] == "SRHR-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001"
    assert report["status"] == "source_review_accepted_not_qa_accepted"
    assert report["input_package_id"] == "SRHP-G1-VIRAL-001"
    assert report["input_package_sha256"] == sha256_file(SRHP_REPORT)
    assert report["reviewer"] == "Bogdan D"
    assert report["review_channel"] == "telegram:150618017"
    assert report["packet_message_ids"] == [248, 253, 259, 262]
    assert report["user_response_message_ids"] == [251, 257, 260, 265]
    assert report["source_acceptance"] is True
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["fixture_creation"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_source_reconstruction_human_review.py")


def test_human_review_records_all_numbered_decisions():
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
        "source_text_accepted_records": 4,
        "visual_exclusion_accepted_records": 3,
        "blocked_records": 0,
        "qa_accepted_records": 0,
    }
    assert [records[key]["question_number"] for key in sorted(records)] == [1, 3, 4, 6, 7, 2, 5]

    text_record_ids = {
        "SRA-G1-VIRAL-001-R002",
        "SRA-G1-VIRAL-001-R003",
        "SRA-G1-VIRAL-001-R004",
        "SRA-G1-VIRAL-001-R005",
    }
    for region_id, record in records.items():
        assert record["qa_acceptance"] is False
        assert record["gate_1_advancement"] is False
        if region_id in text_record_ids:
            assert record["source_text_accepted"] is True
            assert record["visual_exclusion_accepted"] is False
            assert record["candidate_text"]
        else:
            assert record["source_text_accepted"] is False
            assert record["visual_exclusion_accepted"] is True
            assert record["candidate_text"] is None


def test_human_review_captures_corrected_full_crop_and_heading_hint():
    report = read_json(REPORT)
    record = records_by_id(report)["SRA-G1-VIRAL-001-R003"]

    assert record["question_number"] == 4
    assert record["packet_message_id"] == 259
    assert record["human_response_message_id"] == 260
    assert record["human_decision"] == "accepted_candidate_text_after_full_crop_resend"
    assert "full source crop was resent in message 259" in record["packet_correction_note"]
    assert record["semantic_heading_hint"] == [
        {"text": "Introduction", "level": "H1"},
        {"text": "Summary", "level": "H3"},
        {"text": "Overview", "level": "H3"},
        {"text": "The Spektral Krew", "level": "H2"},
    ]


def test_human_review_accepted_text_output_is_not_fixture_or_qa():
    text = ACCEPTED_TEXT.read_text(encoding="utf-8")

    assert "source_review_accepted_not_qa_accepted" in text
    assert "QA acceptance" in text
    assert "Introduction\nSummary\nOverview\nThe Spektral Krew" in text
    assert "We are the Spektral Krew" in text
    assert "H2" in text
    assert "The Spektral Krew" in text


def test_human_review_script_has_no_ocr_pdf_render_or_raw_mutation_dependencies():
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
