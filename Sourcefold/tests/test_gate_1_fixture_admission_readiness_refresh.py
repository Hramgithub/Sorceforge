import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_admission_readiness_refresh.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_refresh_G1_VIRAL_001"
REFRESH = OUT_ROOT / "gate_1_fixture_admission_readiness_refresh.json"
REPORT = OUT_ROOT / "gate_1_fixture_admission_readiness_refresh_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_readiness_refresh_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-REFRESH-001"
HUMAN_DECISION = (
    "proceed with fixture_admission_readiness_refresh; no fixture admission, "
    "no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_admission_readiness_refresh_is_fail_closed():
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
            "proceed with fixture_admission_readiness_refresh",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_admission_readiness_refresh_consumes_current_acceptances():
    refresh = read_json(REFRESH)
    report = read_json(REPORT)

    assert refresh["refresh_id"] == "G1FARR-G1-VIRAL-001"
    assert refresh["authorization_id"] == AUTHORIZATION_ID
    assert refresh["source_status_packet"] == "G1SP-G1-VIRAL-017"
    assert refresh["previous_readiness_packet"] == "G1FARP-G1-VIRAL-001"
    assert refresh["source_policy_acceptance"] == "G1UNFPAR-G1-VIRAL-001"
    assert refresh["source_strategy_fit_acceptance"] == "G1FSFAR-G1-VIRAL-001"
    assert refresh["human_decision"] == HUMAN_DECISION
    assert refresh["readiness_inputs"]["pages_001_020_page_complete_accepted_only"] is True
    assert refresh["readiness_inputs"]["unsupported_negative_fixture_policy_decision_accepted"] is True
    assert refresh["readiness_inputs"]["fixture_strategy_fit_decision_accepted"] is True
    assert refresh["resolves_fixture_admission_readiness_refresh_blocker"] is True
    assert report["resolves_fixture_admission_readiness_refresh_blocker"] is True


def test_fixture_admission_readiness_refresh_rows_and_remaining_blockers():
    refresh = read_json(REFRESH)
    rows = {row["row_id"]: row for row in refresh["readiness_rows"]}

    assert rows["positive_fixture_seed_readiness"]["status"] == "ready_as_seed_material_for_future_manifest_prep"
    assert rows["negative_fixture_policy_readiness"]["status"] == "ready_policy_accepted_negative_fixtures_not_materialized"
    assert rows["fixture_strategy_fit_readiness"]["status"] == "ready_strategy_fit_accepted"
    assert rows["fixture_admission_readiness"]["status"] == "not_ready_requires_fixture_manifest_prep_and_admission_decision"
    assert rows["whole_gate_1_acceptance_readiness"]["status"] == "not_ready_requires_future_recheck_after_admission_path"
    assert refresh["remaining_blockers"] == [
        "fixture_manifest_prep",
        "fixture_admission_decision",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert refresh["next_possible_packets"][0] == "fixture_manifest_prep"


def test_fixture_admission_readiness_refresh_boundaries():
    refresh = read_json(REFRESH)
    report = read_json(REPORT)

    for payload in (refresh, report):
        assert payload["admits_fixture"] is False
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    for key, value in refresh["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture admission readiness refresh blocker resolved: `true`." in summary
    assert "Fixture admission: `false`." in summary
    assert "Fixture manifest creation: `false`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
