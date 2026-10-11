import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_004_context_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_004_context_decision_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_004_context_decision_report.json"
PACKET = OUT_ROOT / "page_004_context_decision_packet.md"
SUMMARY = OUT_ROOT / "page_004_context_decision_summary.md"
MANIFEST = OUT_ROOT / "page_004_context_decision_manifest.md"
AUTH = "BA-G1-VIRAL-PAGE-004-CONTEXT-DECISION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_004_context_decision_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT), "--page", "004"], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-MAP-READINESS-P004-001", "--page", "004"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_004_context_decision_allows_only_page_004():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--page", "003"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "profile exists only for page 004" in result.stderr


def test_page_004_context_decision_report_identity_and_inputs():
    report = read_json(REPORT)

    assert report["package_id"] == "P004CDP-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "ready_for_bogdan_page_004_context_only_decision"
    assert report["scope"] == "page_004_context_only_decision_packet_no_acceptance"
    assert report["page"] == "004"
    assert report["page_id"] == "PG-G1-VIRAL-P004"
    assert report["image_id"] == "IMG-G1-VIRAL-RENDER-001-P004"
    assert report["input_packages"] == ["SRCR-G1-VIRAL-004", "P004A-G1-VIRAL-004"]


def test_page_004_context_decision_records_full_tilted_inset_as_context_only():
    decision = read_json(REPORT)["context_decision"]

    assert decision["requires_bogdan_decision"] is True
    assert decision["context_region_id"] == "PRM-G1-VIRAL-001-P004-R01"
    assert decision["proposed_status"] == "context_only_not_peer_crop_record"
    assert decision["full_tilted_inset"] is True
    assert "overlap peer crops" in decision["reason"]
    assert [record["source_region_id"] for record in decision["accepted_peer_records"]] == [
        "PRM-G1-VIRAL-001-P004-R02",
        "PRM-G1-VIRAL-001-P004-R03",
    ]
    assert decision["display_normalization"] == {
        "scope": "review_asset_only",
        "rule": "body-only text blocks use text_body instead of none in human-facing structure labels",
        "predecessor_source_review_packet_mutated": False,
    }


def test_page_004_context_decision_has_review_assets():
    report = read_json(REPORT)
    assets = {asset["package_path"]: asset for asset in report["review_attachments"]}

    expected = {
        "review_assets/page_004.png",
        "review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png",
        "review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png",
        "review_assets/page_004_ocr_block_text.md",
    }
    assert set(assets) == expected
    for relpath, asset in assets.items():
        path = OUT_ROOT / relpath
        assert path.exists()
        assert path.stat().st_size > 0
        assert asset["sha256"]


def test_page_004_context_decision_packet_is_human_readable():
    packet = PACKET.read_text(encoding="utf-8-sig")
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "Page 004 Context-Only Decision Packet" in packet
    assert "PRM-G1-VIRAL-001-P004-R01" in packet
    assert "page 004 context-only ok" in packet
    assert "This packet itself creates no page-complete acceptance." in packet
    assert "Draft structure/semantics: `safety_warning_body` / `text_body`" in (OUT_ROOT / "review_assets" / "page_004_ocr_block_text.md").read_text(encoding="utf-8-sig")
    assert "Draft structure/semantics: `safety_warning_body` / `none`" not in (OUT_ROOT / "review_assets" / "page_004_ocr_block_text.md").read_text(encoding="utf-8-sig")
    assert "source page shot, 2 block shots, OCR/block text markdown" in summary
    assert "review_assets/page_004_ocr_block_text.md" in manifest


def test_page_004_context_decision_guardrails_stay_false():
    guardrails = read_json(REPORT)["guardrails"]

    assert guardrails["ocr_executed"] is False
    assert guardrails["pdf_opened_or_parsed"] is False
    assert guardrails["pdf_text_layer_used"] is False
    assert guardrails["render_executed"] is False
    assert guardrails["raw_artifacts_modified"] is False
    assert guardrails["source_acceptance_created_or_mutated"] is False
    assert guardrails["page_complete_acceptance_created"] is False
    assert guardrails["accepted_pages_as_complete"] == []
    assert guardrails["whole_gate_1_acceptance_created"] is False
    assert guardrails["fixture_admission"] is False
    assert guardrails["translation_authorized"] is False
    assert guardrails["proofreading_authorized"] is False
    assert guardrails["renderer_profile_acceptance"] is False
    assert guardrails["implementation_authorized"] is False
    assert guardrails["push_authorized"] is False
