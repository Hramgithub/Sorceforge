import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_review_packet.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
SRFA_ROOT = TRIAL_ROOT / "source_reconstruction_fixture_admission_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_packet_G1_VIRAL_001"
REPORT = OUT_ROOT / "gate_1_review_packet_report.json"
PACKET = OUT_ROOT / "gate_1_review_packet.json"
SUMMARY = OUT_ROOT / "gate_1_review_packet_summary.md"
SRFA_REPORT = SRFA_ROOT / "source_reconstruction_fixture_admission_report.json"
SRFA_FIXTURES = SRFA_ROOT / "source_reconstruction_admitted_fixtures.json"
SRFA_SUMMARY = SRFA_ROOT / "source_reconstruction_fixture_admission_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_gate_1_review_packet_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001" in wrong_auth.stderr


def test_gate_1_review_packet_preserves_lineage_and_boundaries():
    report = read_json(REPORT)

    assert report["packet_id"] == "G1RP-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001"
    assert report["status"] == "gate_1_review_packet_ready_not_advanced"
    assert report["input_fixture_admission_id"] == "SRFA-G1-VIRAL-001"
    assert report["input_fixture_admission_report_sha256"] == sha256_file(SRFA_REPORT)
    assert report["input_admitted_fixtures_sha256"] == sha256_file(SRFA_FIXTURES)
    assert report["input_fixture_admission_summary_sha256"] == sha256_file(SRFA_SUMMARY)
    assert report["source_acceptance"] is True
    assert report["qa_acceptance"] is True
    assert report["fixture_admission"] is True
    assert report["gate_1_review_packet_ready"] is True
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_gate_1_review_packet.py")


def test_gate_1_review_packet_covers_all_admitted_fixtures_without_advancing_gate():
    packet = read_json(PACKET)
    report = read_json(REPORT)
    items = packet["packet_items"]

    assert report["summary"] == {
        "packet_items": 7,
        "positive_source_text_items": 4,
        "negative_visual_exclusion_items": 3,
        "blocked_items": 0,
        "gate_1_advanced_items": 0,
    }
    assert len(items) == 7
    assert {item["fixture_id"] for item in items} == {
        "FX-G1-VIRAL-SOURCE-001",
        "FX-G1-VIRAL-SOURCE-002",
        "FX-G1-VIRAL-SOURCE-003",
        "FX-G1-VIRAL-SOURCE-004",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-001",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-002",
        "FX-G1-VIRAL-VISUAL-EXCLUSION-003",
    }
    for item in items:
        assert item["qa_acceptance"] is True
        assert item["fixture_admission"] is True
        assert item["included_for_gate_1_review"] is True
        assert item["gate_1_advancement"] is False


def test_gate_1_review_packet_preserves_r003_metadata():
    packet = read_json(PACKET)
    r003 = next(item for item in packet["packet_items"] if item["fixture_id"] == "FX-G1-VIRAL-SOURCE-002")

    assert r003["region_admission_id"] == "SRA-G1-VIRAL-001-R003"
    assert "full source crop was resent in message 259" in r003["packet_correction_note"]
    assert r003["semantic_heading_hint"] == [
        {"text": "Introduction", "level": "H1"},
        {"text": "Summary", "level": "H3"},
        {"text": "Overview", "level": "H3"},
        {"text": "The Spektral Krew", "level": "H2"},
    ]
    summary = SUMMARY.read_text(encoding="utf-8")
    assert "Packet items: `7`" in summary
    assert "Gate 1 advanced: `false`" in summary


def test_gate_1_review_packet_script_has_no_ocr_pdf_or_raw_mutation_dependencies():
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
