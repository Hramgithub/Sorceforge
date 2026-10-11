import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_015_aggressive_batch.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH = "BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001"

TRIAGE = TRIAL_ROOT / "page_015_triage_G1_VIRAL_001" / "page_015_triage_packet.json"
TEXT = TRIAL_ROOT / "page_015_text_extraction_G1_VIRAL_001" / "page_015_text_extraction_packet.json"
SEM = TRIAL_ROOT / "page_015_semantic_text_map_G1_VIRAL_001" / "page_015_semantic_text_map.json"
PCRP = TRIAL_ROOT / "page_complete_review_p015_G1_VIRAL_001" / "page_complete_review_report.json"
PCA = TRIAL_ROOT / "page_complete_acceptance_p015_G1_VIRAL_001" / "page_complete_acceptance_report.json"
STATUS = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_010" / "gate_1_status_packet.json"
BATCH = TRIAL_ROOT / "page_015_aggressive_batch_G1_VIRAL_001" / "page_015_aggressive_batch_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_015_aggressive_batch_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-015-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_015_preflight_materialized_exact_authorization():
    ledger = (ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md").read_text(encoding="utf-8-sig")

    assert ledger.count("## BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001") == 1
    assert "Lane: `P015BATCH-G1-VIRAL-001`" in ledger
    assert "page_015_image" in ledger


def test_internal_stages_record_skipped_human_review_and_sol_terra():
    for path in [TRIAGE, TEXT, SEM, PCRP, PCA, STATUS]:
        payload = read_json(path)
        gate = payload["review_gate"]
        assert gate["status"] == "passed"
        assert gate["human_review_state"] == "human_review_skipped_by_explicit_authorization"
        assert gate["delegated_review_state"] == "review_delegated_to_Sol_Terra"
        serialized = json.dumps(payload)
        assert "Bogdan approved" not in serialized
        assert "p015 triage ok" not in serialized
        assert "p015 semantic map ok" not in serialized


def test_page_015_scope_and_predecessors_are_hash_bound():
    triage = read_json(TRIAGE)
    text = read_json(TEXT)
    sem = read_json(SEM)
    pcrp = read_json(PCRP)
    pca = read_json(PCA)
    status = read_json(STATUS)

    predecessors = {item["name"]: item for item in triage["predecessors"]}
    assert predecessors["post_p014_status_route_packet"]["sha256"] == "E0F15FCA01D32C95D41EBCA87D87EDCEEEE59A2C503FF0965614169BF0159B54"
    assert predecessors["p014_final_batch_review"]["sha256"] == "FF8C193BB61A5D6A12F1E60EC7C853EB164CD1EC10A92A058A591200B430A76B"
    assert predecessors["page_015_image"]["sha256"] == "023836CD8DF8B77073F977E22F00CA87391F96855765D77B5C2826B0F00EDBBA"
    assert text["predecessor"]["package_id"] == "P015TR-G1-VIRAL-001"
    assert sem["predecessor"]["package_id"] == "P015TXT-G1-VIRAL-001"
    assert pcrp["predecessor"]["package_id"] == "P015SEM-G1-VIRAL-001"
    assert pca["predecessor"]["package_id"] == "PCRP-G1-VIRAL-P015-001"
    assert status["predecessor"]["package_id"] == "P015PCA-G1-VIRAL-001"


def test_page_015_text_evidence_and_visual_anchor_roles():
    triage = read_json(TRIAGE)
    blocks = {block["block_id"]: block for block in triage["review_blocks"]}

    assert len(blocks) == 2
    assert blocks["P015-B001"]["role"] == "timeline_text_panel"
    assert blocks["P015-B002"]["role"] == "history_text_visible_continuation"
    assert blocks["P015-B002"]["continues_to_next_page"] is True
    assert [block["block_id"] for block in triage["visual_only_blocks"]] == ["P015-V001"]
    for block in blocks.values():
        assert block["crop_contract"]["context_allowed"] is False


def test_page_015_semantic_map_keeps_timeline_labels_non_structural():
    sem = read_json(SEM)
    units = {unit["unit_id"]: unit for unit in sem["units"]}

    assert units["SU-P015-TIME-001"]["heading_level"] == "h2"
    assert units["SU-P015-TIME-002"]["heading_level"] == "h3"
    assert units["SU-P015-HIST-001"]["heading_level"] == "h2"
    timeline_entries = [unit for unit in sem["units"] if unit["unit_type"] == "timeline_entry"]
    assert timeline_entries
    for unit in timeline_entries:
        assert unit["heading_level"] is None
        assert unit["is_structural_heading"] is False
        assert unit["time_label"]
    assert units["SU-P015-HIST-005"]["continues_to_next_page"] is True
    assert sem["continuation"]["page_016_processed"] is False


def test_page_016_and_broad_capabilities_remain_blocked():
    status = read_json(STATUS)
    pca = read_json(PCA)
    batch = read_json(BATCH)

    assert status["page_complete_accepted_pages"] == [f"{i:03d}" for i in range(1, 16)]
    assert status["remaining_page_complete_pages_unstarted"] == ["016", "017", "018", "019", "020"]
    assert status["recommended_next_candidate"] == "page_016_triage_readiness_not_authorized"
    for payload in [status, pca, batch]:
        for key in [
            "whole_gate_1_acceptance",
            "fixture_admission",
            "source_acceptance_mutation",
            "ocr_execution",
            "render_execution",
            "pdf_parsing_or_text_layer_extraction",
            "raw_mutation",
            "translation",
            "proofreading",
            "renderer_profile_acceptance",
            "implementation",
            "push",
            "page_016_plus_processing",
        ]:
            assert payload["guardrails"][key] is False, key


def test_final_bundle_is_the_only_human_review_target():
    batch = read_json(BATCH)

    assert batch["status"] == "ready_for_bogdan_final_batch_review"
    assert batch["human_review_model"] == "final_bundle_and_post_p015_status_only"
    assert batch["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
    assert batch["decision_options"] == ["p015 aggressive batch ok", "hold p015 batch: <reason>"]
