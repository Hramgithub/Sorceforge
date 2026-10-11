import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_whole_gate_acceptance_readiness_recheck.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_decision_G1_VIRAL_001"
ACCEPTANCE = OUT_ROOT / "gate_1_whole_gate_acceptance_decision.json"
REPORT = OUT_ROOT / "gate_1_whole_gate_acceptance_decision_report.json"
SUMMARY = OUT_ROOT / "gate_1_whole_gate_acceptance_decision_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-DECISION-RECORD-001"
HUMAN_DECISION = (
    "g1wgarr packet ok; proceed to prepare whole Gate 1 acceptance decision record limited to pages 001-020 "
    "and G1FADAR admitted fixture manifest groups; no page 021+, no source-profile acceptance beyond this "
    "Gate 1 record, no OCR/render/PDF/raw mutation, no translation/proofreading/implementation, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_whole_gate_acceptance_decision_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-WRONG",
            "--decision",
            HUMAN_DECISION,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            AUTHORIZATION_ID,
            "--decision",
            "g1wgarr packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_whole_gate_acceptance_decision_scope():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)
    scope = acceptance["whole_gate_1_acceptance_scope"]

    assert acceptance["acceptance_id"] == "G1WGADR-G1-VIRAL-001"
    assert acceptance["authorization_id"] == AUTHORIZATION_ID
    assert acceptance["source_readiness_recheck_packet"] == "G1WGARR-G1-VIRAL-001"
    assert acceptance["human_decision"] == HUMAN_DECISION
    assert acceptance["accepts_whole_gate_1"] is True
    assert report["accepts_whole_gate_1"] is True
    assert report["accepted_page_count"] == 20
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["accepted_decision_count"] == 4


def test_whole_gate_acceptance_decision_boundaries():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    for payload in (acceptance, report):
        assert payload["accepts_source_profile_beyond_gate_1_record"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False
        assert payload["executes_render"] is False
        assert payload["mutates_source_ocr_render_pdf_raw"] is False
        assert payload["creates_translation_or_proofreading"] is False
        assert payload["creates_implementation"] is False
        assert payload["push_performed"] is False

    for key, value in acceptance["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Whole Gate 1 acceptance: `true`." in summary
    assert "Source-profile acceptance beyond this Gate 1 record: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary
    assert "Translation/proofreading/implementation/push: `false`." in summary


def test_whole_gate_acceptance_decision_remaining_boundaries():
    acceptance = read_json(ACCEPTANCE)

    assert acceptance["remaining_blockers"] == [
        "page_021_plus_separate_bounded_authorization_if_selected",
        "source_profile_acceptance_beyond_gate_1_record_if_needed",
        "ocr_render_pdf_raw_translation_proofreading_implementation_requires_separate_authorization",
        "push_requires_separate_authorization",
    ]
    assert acceptance["next_possible_packets"][0] == "core_0_1_implementation_planning_if_separately_authorized"
