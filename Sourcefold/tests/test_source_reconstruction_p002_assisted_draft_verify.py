import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_source_reconstruction_p002_assisted_draft.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
SRAD_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json"
MANIFEST = OUT_ROOT / "source_reconstruction_p002_assisted_draft_verify_manifest.md"
SUMMARY = OUT_ROOT / "assisted_draft_human_verification_summary.md"
SRAD_REPORT = SRAD_ROOT / "source_reconstruction_p002_assisted_draft_report.json"
SRAD_MANIFEST = SRAD_ROOT / "source_reconstruction_p002_assisted_draft_manifest.md"
SRAD_DRAFT = SRAD_ROOT / "assisted_text_draft_for_bogdan.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p002_assisted_draft_verify_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001" in wrong_auth.stderr


def test_p002_assisted_draft_verify_preserves_srad_lineage_and_generator_hashes():
    report = read_json(REPORT)

    assert report["verification_id"] == "SRADV-G1-VIRAL-002"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001"
    assert report["generator"]["script_sha256"] == sha256_file(SCRIPT)
    assert report["generator"]["test_sha256"] == sha256_file(Path(__file__))
    assert report["input_assisted_draft_id"] == "SRAD-G1-VIRAL-002"
    assert report["input_assisted_draft_report_sha256"] == sha256_file(SRAD_REPORT)
    assert report["input_assisted_draft_manifest_sha256"] == sha256_file(SRAD_MANIFEST)
    assert report["input_assisted_draft_markdown_sha256"] == sha256_file(SRAD_DRAFT)


def test_p002_assisted_draft_verify_records_bogdan_ok_decisions_only():
    report = read_json(REPORT)

    assert report["user_decision"]["telegram_message_id"] == "377"
    assert "1 ок" in report["user_decision"]["raw_text"]
    assert "Заголовки игнорирую" in report["user_decision"]["raw_text"]
    assert report["summary"]["records"] == 2
    assert report["summary"]["human_verified_records"] == 2
    assert report["summary"]["source_accepted_records"] == 0
    assert report["human_verification_recorded"] is True
    for record in report["records"]:
        assert record["bogdan_decision"] == "ok"
        assert record["verified_text_matches_crop"] is True
        assert record["heading_handling"] == "ignore_headings_for_this_decision"


def test_p002_assisted_draft_verify_reuses_exact_srad_text_and_crops():
    report = read_json(REPORT)
    srad = read_json(SRAD_REPORT)
    srad_records = {record["question_id"]: record for record in srad["records"]}

    assert {record["question_id"] for record in report["records"]} == {"1", "2"}
    for record in report["records"]:
        source = srad_records[record["question_id"]]
        assert record["verified_text"] == source["draft_text"]
        assert record["verified_text_sha256"] == sha256_text(source["draft_text"])
        assert record["corrected_crop_reference"] == source["corrected_crop_reference"]
        assert record["corrected_crop_reference_sha256"] == source["corrected_crop_reference_sha256"]


def test_p002_assisted_draft_verify_does_not_expand_gate_or_page_scope():
    report = read_json(REPORT)

    assert report["summary"]["accepted_pages_as_complete"] is False
    assert report["summary"]["whole_gate_1_acceptance"] is False
    for payload in [report, *report["records"]]:
        assert payload["source_acceptance"] is False
        assert payload["qa_acceptance"] is False
        assert payload["fixture_admission"] is False
        assert payload["gate_1_advancement"] is False
    assert report["page_complete_acceptance"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False


def test_p002_assisted_draft_verify_has_no_ocr_pdf_render_or_raw_mutation():
    report = read_json(REPORT)
    source = SCRIPT.read_text(encoding="utf-8").lower()

    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
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
        "raw_outputs",
    ]
    for token in forbidden:
        assert token not in source


def test_p002_assisted_draft_verify_summary_and_manifest_are_bounded():
    summary = SUMMARY.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert "assisted_draft_human_verified_not_source_accepted" in summary
    assert "Telegram message: `377`" in summary
    assert "not source acceptance" in summary
    assert "Generator Hashes" in manifest
    assert "no source acceptance, QA, fixtures, Gate 1 advancement" in manifest
