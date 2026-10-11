import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare_gate_1_review_decision_brief.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
G1RP_ROOT = TRIAL_ROOT / "gate_1_review_packet_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_decision_brief_G1_VIRAL_001"
REPORT = OUT_ROOT / "gate_1_review_decision_brief_report.json"
BRIEF_JSON = OUT_ROOT / "gate_1_review_decision_brief.json"
BRIEF_MD = OUT_ROOT / "gate_1_review_decision_brief.md"
G1RP_REPORT = G1RP_ROOT / "gate_1_review_packet_report.json"
G1RP_MANIFEST = G1RP_ROOT / "gate_1_review_packet_manifest.md"
G1RP_PACKET = G1RP_ROOT / "gate_1_review_packet.json"
G1RP_SUMMARY = G1RP_ROOT / "gate_1_review_packet_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_gate_1_review_decision_brief_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001" in wrong_auth.stderr


def test_gate_1_review_decision_brief_preserves_packet_lineage_and_boundaries():
    report = read_json(REPORT)

    assert report["brief_id"] == "G1RDB-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001"
    assert report["status"] == "gate_1_review_decision_brief_ready_requires_bogdan"
    assert report["input_packet_id"] == "G1RP-G1-VIRAL-001"
    assert report["accepted_protocol_revision"] == "5ee1760f"
    assert report["input_packet_report_sha256"] == sha256_file(G1RP_REPORT)
    assert report["input_packet_manifest_sha256"] == sha256_file(G1RP_MANIFEST)
    assert report["input_packet_sha256"] == sha256_file(G1RP_PACKET)
    assert report["input_packet_summary_sha256"] == sha256_file(G1RP_SUMMARY)
    assert report["requires_bogdan_review"] is True
    assert report["gate_1_decision_recorded"] is False
    assert report["gate_1_advancement"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_gate_1_review_decision_brief.py")


def test_gate_1_review_decision_brief_contains_one_numbered_question():
    brief = read_json(BRIEF_JSON)

    assert brief["brief_id"] == "G1RDB-G1-VIRAL-001"
    assert brief["status"] == "gate_1_review_decision_brief_ready_requires_bogdan"
    assert brief["gate_1_decision_recorded"] is False
    assert brief["gate_1_advancement"] is False
    assert brief["summary"] == {
        "decision_questions": 1,
        "packet_items": 7,
        "positive_source_text_items": 4,
        "negative_visual_exclusion_items": 3,
        "blocking_items": 0,
        "requires_bogdan_review": True,
    }
    question = brief["decision_questions"][0]
    assert question["question_number"] == 1
    assert question["subject"] == "G1RP-G1-VIRAL-001"
    assert question["acceptance_scope"] == "exact_G1RP_G1_VIRAL_001_source_reconstruction_evidence_slice_only"
    assert "whole_gate_1_acceptance" in question["not_authorized_by_acceptance"]
    assert "implementation" in question["not_authorized_by_acceptance"]
    assert brief["inherited_source_acceptance"] is True
    assert brief["inherited_qa_acceptance"] is True
    assert brief["upstream_qa_report_sha256"] == "A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0"
    assert brief["upstream_qa_summary_sha256"] == "C7C32A1D4E9A74DC3F086D4D355151BF6C89DBDE576775AC0F67312E98981EC3"
    assert len(brief["non_waivable_checklist"]) == 8
    assert "user_visible_gate_1_decision_record" in brief["if_accepted_requires"]
    assert "accepted_scope_revision" in brief["if_parked_requires"]


def test_gate_1_review_decision_brief_markdown_is_short_answer_ready():
    brief_md = BRIEF_MD.read_text(encoding="utf-8")

    assert "1 - `G1RP-G1-VIRAL-001`" in brief_md
    assert "`1 - принять`" in brief_md
    assert "`1 - hold: <blocker>`" in brief_md
    assert "`1 - reject: <reason>`" in brief_md
    assert "`1 - park: <exact scope/rationale>`" in brief_md
    assert "G1RP manifest SHA-256" in brief_md
    assert "SRFA fixtures SHA-256" in brief_md
    assert "no stale lineage" in brief_md
    assert "Gate 1 advanced: `false`" in brief_md


def test_gate_1_review_decision_brief_script_has_no_ocr_pdf_or_raw_mutation_dependencies():
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
