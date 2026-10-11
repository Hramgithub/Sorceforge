import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_implementation_planning_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_implementation_planning_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "core_0_1_implementation_planning_prep.json"
REPORT = OUT_ROOT / "core_0_1_implementation_planning_prep_report.json"
SUMMARY = OUT_ROOT / "core_0_1_implementation_planning_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-PLANNING-PREP-001"
HUMAN_DECISION = (
    "proceed with core_0_1_implementation_planning_prep from G1WGADR; no implementation, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, "
    "no source-profile acceptance beyond G1WGADR, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_implementation_planning_prep_is_fail_closed():
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
            "proceed with core_0_1_implementation_planning_prep",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_implementation_planning_prep_scope():
    packet = read_json(PACKET)
    report = read_json(REPORT)
    scope = packet["accepted_gate_1_scope"]

    assert packet["packet_id"] == "C01IPP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert packet["human_decision"] == HUMAN_DECISION
    assert packet["status"] == "core_0_1_implementation_planning_prep_ready_for_review"
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["recommended_first_slice"] == "C01WP-01-phase-1-scaffold-contracts"


def test_core_0_1_implementation_planning_prep_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    for payload in (packet, report):
        assert payload["creates_implementation"] is False
        assert payload["creates_implementation_authorization_receipt"] is False
        assert payload["executes_ocr"] is False
        assert payload["executes_render"] is False
        assert payload["mutates_source_ocr_render_pdf_raw"] is False
        assert payload["creates_translation_or_proofreading"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["accepts_source_profile_beyond_g1wgadr"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["push_performed"] is False

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Runtime implementation: `false`." in summary
    assert "OCR/render/PDF/raw/source mutation: `false`." in summary
    assert "Translation/proofreading: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary


def test_core_0_1_implementation_planning_requires_future_authorization():
    packet = read_json(PACKET)
    planning = packet["implementation_planning"]

    assert planning["planning_only"] is True
    assert planning["first_slice_authorized"] is False
    assert all(row["may_start_now"] is False for row in planning["work_packages"])
    assert all(row["separate_authorization_required"] is True for row in planning["work_packages"])
    assert packet["remaining_blockers"][0] == "runtime_implementation_requires_separate_authorization"
    assert packet["next_possible_packets"][0] == "core_0_1_implementation_authorization_receipt_if_separately_authorized"
