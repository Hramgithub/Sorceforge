import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_manifest_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_fixture_manifest_prep.json"
REPORT = OUT_ROOT / "gate_1_fixture_manifest_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_manifest_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-MANIFEST-PREP-001"
HUMAN_DECISION = (
    "proceed with fixture_manifest_prep; no fixture admission, no whole Gate 1 "
    "acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_manifest_prep_is_fail_closed():
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
            "proceed with fixture_manifest_prep",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_manifest_prep_consumes_readiness_refresh():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1FMP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_readiness_refresh"] == "G1FARR-G1-VIRAL-001"
    assert packet["human_decision"] == HUMAN_DECISION
    assert packet["page_complete_acceptance_scope"] == "pages_001_020_individual_page_complete_only"
    assert packet["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["review_question_count"] == 4


def test_fixture_manifest_prep_shape_and_sequence():
    packet = read_json(PACKET)

    assert packet["proposed_manifest_shape"]["positive_fixture_seed_scope"] == (
        "pages_001_020_page_complete_accepted_only"
    )
    assert packet["proposed_manifest_shape"]["admission_dependency"] == (
        "separate_fixture_admission_decision_required_after_manifest_review"
    )
    assert [row["group_id"] for row in packet["proposed_positive_fixture_groups"]] == [
        "positive_page_complete_seed_pages_001_020"
    ]
    assert [row["group_id"] for row in packet["proposed_negative_fixture_groups"]] == [
        "negative_unsupported_profile_claim",
        "negative_missing_or_unresolved_policy",
        "negative_stale_lineage_or_invalidation_trigger",
        "negative_page_021_plus_boundary_violation",
    ]
    assert [row["question_id"] for row in packet["review_questions"]] == [
        "positive_fixture_seed_manifest_shape",
        "negative_fixture_group_manifest_shape",
        "manifest_invalidation_shape",
        "manifest_admission_dependency",
    ]
    assert packet["next_possible_packets"][0] == "fixture_manifest_acceptance_record"


def test_fixture_manifest_prep_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    for payload in (packet, report):
        assert payload["creates_fixture_manifest"] is False
        assert payload["admits_fixture"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture manifest creation: `false`." in summary
    assert "Fixture admission: `false`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
