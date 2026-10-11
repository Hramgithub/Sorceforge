import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_runtime_source_profile_lock_or_parking_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_G1_VIRAL_001"
DECISION = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision.json"
REPORT = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_report.json"
SUMMARY = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-PARKING-DECISION-001"
HUMAN_DECISION = (
    "c01amtr packet ok; proceed to prepare runtime source-profile lock-or-parking decision for C01WP-01 "
    "from C01AMTR; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, "
    "no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_runtime_source_profile_decision_is_fail_closed():
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
            "c01amtr packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_runtime_source_profile_decision_scope():
    decision = read_json(DECISION)
    report = read_json(REPORT)
    scope = decision["accepted_gate_1_scope"]

    assert decision["decision_id"] == "C01RSPLP-G1-VIRAL-001"
    assert decision["authorization_id"] == AUTHORIZATION_ID
    assert decision["source_acceptance_matrix_trace_review"] == "C01AMTR-G1-VIRAL-001"
    assert decision["source_architecture_review_packet"] == "C01FSARP-G1-VIRAL-001"
    assert decision["source_profile_lock_or_parking_receipt"] == "C01SPLPR-G1-VIRAL-001"
    assert decision["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert decision["first_slice_id"] == "C01WP-01-phase-1-scaffold-contracts"
    assert decision["human_decision"] == HUMAN_DECISION
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20


def test_core_0_1_runtime_source_profile_decision_parks_runtime_profile():
    decision = read_json(DECISION)
    report = read_json(REPORT)
    disposition = decision["runtime_source_profile_disposition"]

    assert disposition["runtime_profile_disposition"] == "park_runtime_source_profile_lock_until_first_runtime_authorization"
    assert decision["runtime_source_profile_decision_created"] is True
    assert decision["runtime_source_profile_parking_recorded"] is True
    assert decision["runtime_source_profile_lock_created"] is False
    assert decision["runtime_source_profile_acceptance_created"] is False

    for payload in (decision, report):
        assert payload["runtime_implementation_authorized"] is False
        assert payload["creates_runtime_implementation"] is False
        assert payload["source_profile_lock_created"] is False
        assert payload["source_profile_acceptance_created"] is False
        assert payload["accepts_source_profile_beyond_c01splpr"] is False
        assert payload["executes_ocr"] is False
        assert payload["executes_render"] is False
        assert payload["mutates_source_ocr_render_pdf_raw"] is False
        assert payload["creates_translation_or_proofreading"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["push_performed"] is False

    for key, value in decision["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Runtime source-profile lock created: `false`." in summary
    assert "Runtime source-profile parking recorded: `true`." in summary
    assert "Runtime implementation: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary


def test_core_0_1_runtime_source_profile_decision_keeps_runtime_blocked():
    decision = read_json(DECISION)

    assert decision["remaining_blockers"][0] == "human_review_c01rsplp_required"
    assert "runtime_source_profile_lock_or_runtime_parking_decision_required" not in decision["remaining_blockers"]
    assert "first_slice_runtime_authorization_required" in decision["remaining_blockers"]
    assert decision["next_possible_packets"][0] == "human_review_c01rsplp_packet"
