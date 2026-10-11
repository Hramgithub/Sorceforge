import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "admit_source_reconstruction_fixtures.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
SRQA_ROOT = TRIAL_ROOT / "source_reconstruction_qa_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_fixture_admission_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_fixture_admission_report.json"
FIXTURES = OUT_ROOT / "source_reconstruction_admitted_fixtures.json"
SUMMARY = OUT_ROOT / "source_reconstruction_fixture_admission_summary.md"
SRQA_REPORT = SRQA_ROOT / "source_reconstruction_qa_report.json"
SRQA_SUMMARY = SRQA_ROOT / "source_reconstruction_qa_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def fixtures_by_id():
    return {fixture["fixture_id"]: fixture for fixture in read_json(FIXTURES)["fixtures"]}


def test_fixture_admission_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-QA-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001" in wrong_auth.stderr


def test_fixture_admission_preserves_lineage_and_boundaries():
    report = read_json(REPORT)

    assert report["admission_id"] == "SRFA-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001"
    assert report["status"] == "source_reconstruction_fixtures_admitted_not_gate"
    assert report["input_qa_id"] == "SRQA-G1-VIRAL-001"
    assert report["input_qa_report_sha256"] == sha256_file(SRQA_REPORT)
    assert report["input_qa_summary_sha256"] == sha256_file(SRQA_SUMMARY)
    assert report["source_acceptance"] is True
    assert report["qa_acceptance"] is True
    assert report["fixture_admission"] is True
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_source_reconstruction_fixture_admission.py")


def test_fixture_admission_contains_positive_and_negative_fixtures():
    report = read_json(REPORT)
    fixtures = fixtures_by_id()

    assert report["summary"] == {
        "fixtures": 7,
        "positive_source_text_fixtures": 4,
        "negative_visual_exclusion_fixtures": 3,
        "blocked_fixtures": 0,
        "gate_1_advanced_fixtures": 0,
    }
    assert set(fixtures) == {
        "FX-G1-VIRAL-SOURCE-001",
        "FX-G1-VIRAL-SOURCE-002",
        "FX-G1-VIRAL-SOURCE-003",
        "FX-G1-VIRAL-SOURCE-004",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-001",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-002",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-003",
    }
    for fixture in fixtures.values():
        assert fixture["source_qa_id"] == "SRQA-G1-VIRAL-001"
        assert fixture["qa_acceptance"] is True
        assert fixture["fixture_admitted"] is True
        assert fixture["gate_1_advancement"] is False
        if fixture["fixture_kind"] == "positive_source_text":
            assert fixture["expected_behavior"] == "candidate_text_must_match_exact_source_review_text"
            assert fixture["source_text_accepted"] is True
            assert fixture["visual_exclusion_accepted"] is False
        else:
            assert fixture["expected_behavior"] == "visual_only_region_must_not_create_source_text"
            assert fixture["source_text_accepted"] is False
            assert fixture["visual_exclusion_accepted"] is True


def test_fixture_admission_preserves_r003_metadata():
    fixtures = fixtures_by_id()
    r003 = fixtures["FX-G1-VIRAL-SOURCE-002"]

    assert r003["region_admission_id"] == "SRA-G1-VIRAL-001-R003"
    assert "full source crop was resent in message 259" in r003["packet_correction_note"]
    assert r003["semantic_heading_hint"] == [
        {"text": "Introduction", "level": "H1"},
        {"text": "Summary", "level": "H3"},
        {"text": "Overview", "level": "H3"},
        {"text": "The Spektral Krew", "level": "H2"},
    ]
    summary = SUMMARY.read_text(encoding="utf-8")
    assert "Positive source-text fixtures: `4`" in summary
    assert "Negative visual-exclusion fixtures: `3`" in summary


def test_fixture_admission_script_has_no_ocr_pdf_render_or_raw_mutation_dependencies():
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
