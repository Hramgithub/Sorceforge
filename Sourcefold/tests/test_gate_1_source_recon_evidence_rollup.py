import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "rollup_gate_1_source_reconstruction_evidence.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
DECISION_ROOT = TRIAL_ROOT / "gate_1_review_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_recon_evidence_rollup_G1_VIRAL_001"
ROLLUP = OUT_ROOT / "gate_1_source_recon_evidence_rollup.json"
REPORT = OUT_ROOT / "gate_1_source_recon_evidence_rollup_report.json"
SUMMARY = OUT_ROOT / "gate_1_source_recon_evidence_rollup_summary.md"
DECISION_REPORT = DECISION_ROOT / "gate_1_review_decision_report.json"
DECISION_RECORD = DECISION_ROOT / "gate_1_review_decision_record.json"
DECISION_MD = DECISION_ROOT / "gate_1_review_decision_record.md"
DECISION_SUMMARY = DECISION_ROOT / "gate_1_review_decision_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_gate_1_source_recon_rollup_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001" in wrong_auth.stderr


def test_gate_1_source_recon_rollup_preserves_decision_lineage():
    report = read_json(REPORT)

    assert report["rollup_id"] == "G1SRER-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001"
    assert report["input_decision_id"] == "G1RD-G1-VIRAL-001"
    assert report["input_decision_report_sha256"] == sha256_file(DECISION_REPORT)
    assert report["input_decision_record_sha256"] == sha256_file(DECISION_RECORD)
    assert report["input_decision_markdown_sha256"] == sha256_file(DECISION_MD)
    assert report["input_decision_summary_sha256"] == sha256_file(DECISION_SUMMARY)
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_gate_1_source_recon_evidence_rollup.py")


def test_gate_1_source_recon_rollup_carries_only_narrow_scope():
    rollup = read_json(ROLLUP)
    decision = read_json(DECISION_RECORD)

    assert rollup["input_packet_lineage"] == decision["direct_packet_lineage"]
    assert rollup["accepted_scope"] == "seven_reviewed_records_only_pages_not_complete"
    assert rollup["accepted_records"] == 7
    assert rollup["accepted_source_text_records"] == 4
    assert rollup["accepted_visual_exclusion_records"] == 3
    assert rollup["accepted_pages"] == ["001", "005", "006"]
    assert rollup["accepted_pages_as_complete"] is False
    assert rollup["whole_gate_1_acceptance"] is False
    assert rollup["page_complete_acceptance"] is False
    assert rollup["gate_1_source_reconstruction_evidence_slice_accepted"] is True
    assert rollup["gate_1_advancement"] is True
    assert rollup["gate_1_advancement_scope"] == "seven_reviewed_records_only_pages_not_complete"
    assert rollup["usable_as_higher_level_gate_1_status_input"] is True
    assert rollup["requires_explicit_scope_label_when_reused"] is True


def test_gate_1_source_recon_rollup_does_not_accept_forbidden_broader_work():
    rollup = read_json(ROLLUP)
    report = read_json(REPORT)

    for item in [
        "page_001_complete",
        "page_005_complete",
        "page_006_complete",
        "whole_viral_pdf",
        "whole_gate_1",
    ]:
        assert item in rollup["not_accepted"]

    for payload in [rollup, report]:
        assert payload["translation_authorized"] is False
        assert payload["proofreading_authorized"] is False
        assert payload["renderer_profile_acceptance"] is False
        assert payload["implementation_authorized"] is False
        assert payload["push_authorized"] is False
        assert payload["ocr_executed"] is False
        assert payload["pdf_opened_or_parsed"] is False
        assert payload["raw_ocr_outputs_modified"] is False


def test_gate_1_source_recon_rollup_summary_states_boundaries():
    summary = SUMMARY.read_text(encoding="utf-8")

    assert "Accepted records: `7`" in summary
    assert "Pages 001/005/006 as complete: `false`" in summary
    assert "Whole Gate 1: `false`" in summary
    assert "seven_reviewed_records_only_pages_not_complete" in summary


def test_gate_1_source_recon_rollup_script_has_no_ocr_pdf_or_raw_mutation_dependencies():
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
