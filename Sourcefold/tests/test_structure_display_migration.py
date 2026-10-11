import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_structure_display_migration.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "structure_display_normalization_G1_VIRAL_001"
REPORT = OUT_ROOT / "structure_display_normalization_report.json"
SUMMARY = OUT_ROOT / "structure_display_normalization_summary.md"
MANIFEST = OUT_ROOT / "structure_display_normalization_manifest.md"
AUTH = "BA-G1-VIRAL-STRUCTURE-DISPLAY-NORMALIZATION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_structure_display_normalization_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P004-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_structure_display_normalization_records_display_only_scope():
    report = read_json(REPORT)

    assert report["package_id"] == "SDN-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "human_facing_structure_display_normalized"
    assert report["scope"] == "display_only_normalized_copies_for_prior_and_future_review_packets"
    assert report["display_rule"]["display_as"] == "text_body"
    assert report["display_rule"]["raw_predecessor_evidence_mutated"] is False
    assert set(report["display_rule"]["updated_generators"]) == {
        "scripts/build_p002_completion_and_next_review.py",
        "scripts/build_source_reconstruction_next_slice_004.py",
        "scripts/build_page_004_context_decision.py",
    }


def test_structure_display_normalization_outputs_prior_packet_copies():
    report = read_json(REPORT)
    packets = report["normalized_packets"]

    assert len(packets) == 3
    assert all(packet["source_mutated"] is False for packet in packets)
    assert all(packet["normalizations_applied"] is True for packet in packets)
    for packet in packets:
        source = ROOT / packet["source_path"]
        normalized = ROOT / packet["normalized_path"]
        assert source.exists()
        assert normalized.exists()
        text = normalized.read_text(encoding="utf-8-sig")
        assert "/ `text_body`" in text
        assert "Draft structure/semantics: `body_text` / `none`" not in text
        assert "Draft structure/semantics: `safety_warning_body` / `none`" not in text


def test_structure_display_normalization_keeps_original_predecessors_unchanged():
    report = read_json(REPORT)

    for packet in report["normalized_packets"]:
        source = ROOT / packet["source_path"]
        assert packet["source_sha256"]
        assert packet["normalized_sha256"]
        assert packet["source_sha256"] != packet["normalized_sha256"]
        assert "/ `none`" in source.read_text(encoding="utf-8-sig")


def test_structure_display_normalization_guardrails_stay_false():
    guardrails = read_json(REPORT)["guardrails"]

    assert guardrails["source_acceptance_created_or_mutated"] is False
    assert guardrails["page_complete_acceptance_created"] is False
    assert guardrails["accepted_pages_as_complete"] == []
    assert guardrails["whole_gate_1_acceptance_created"] is False
    assert guardrails["fixture_admission"] is False
    assert guardrails["ocr_executed"] is False
    assert guardrails["pdf_opened_or_parsed"] is False
    assert guardrails["pdf_text_layer_used"] is False
    assert guardrails["render_executed"] is False
    assert guardrails["raw_artifacts_modified"] is False
    assert guardrails["translation_authorized"] is False
    assert guardrails["proofreading_authorized"] is False
    assert guardrails["renderer_profile_acceptance"] is False
    assert guardrails["implementation_authorized"] is False
    assert guardrails["push_authorized"] is False


def test_structure_display_normalization_summary_and_manifest_are_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "Body/text-only" in summary
    assert "Original predecessor evidence files are not mutated." in summary
    assert "structure_display_normalization_report.json" in manifest


def test_future_generators_use_display_helper():
    for relpath in [
        "scripts/build_p002_completion_and_next_review.py",
        "scripts/build_source_reconstruction_next_slice_004.py",
        "scripts/build_page_004_context_decision.py",
    ]:
        source = (ROOT / relpath).read_text(encoding="utf-8")
        assert "display_structure_labels" in source
        assert "format_draft_structure_semantics" in source or "normalize_draft_structure_lines" in source
