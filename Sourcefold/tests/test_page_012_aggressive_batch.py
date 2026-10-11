import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_012_aggressive_batch.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH = "BA-G1-VIRAL-PAGE-012-AGGRESSIVE-BATCH-001"

TRIAGE = TRIAL_ROOT / "page_012_triage_G1_VIRAL_001" / "page_012_triage_packet.json"
TEXT = TRIAL_ROOT / "page_012_text_extraction_G1_VIRAL_001" / "page_012_text_extraction_packet.json"
SEM = TRIAL_ROOT / "page_012_semantic_text_map_G1_VIRAL_001" / "page_012_semantic_text_map.json"
PCRP = TRIAL_ROOT / "page_complete_review_p012_G1_VIRAL_001" / "page_complete_review_report.json"
PCA = TRIAL_ROOT / "page_complete_acceptance_p012_G1_VIRAL_001" / "page_complete_acceptance_report.json"
STATUS = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_007" / "gate_1_status_packet.json"
BATCH = TRIAL_ROOT / "page_012_aggressive_batch_G1_VIRAL_001" / "page_012_aggressive_batch_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_012_aggressive_batch_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-012-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_internal_stages_record_skipped_human_review_and_sol_terra():
    for path in [TRIAGE, TEXT, SEM, PCRP, PCA, STATUS]:
        payload = read_json(path)
        gate = payload["review_gate"]
        assert gate["status"] == "passed"
        assert gate["human_review_state"] == "human_review_skipped_by_explicit_authorization"
        assert gate["delegated_review_state"] == "review_delegated_to_Sol_Terra"
        assert gate["sol"]["status"] == "OK"
        assert gate["terra"]["status"] == "OK"
        serialized = json.dumps(payload)
        assert "Bogdan approved" not in serialized
        assert "p012 triage ok" not in serialized
        assert "p012 text ok" not in serialized
        assert "p012 semantic map ok" not in serialized


def test_page_012_scope_and_sequence_are_hash_bound():
    triage = read_json(TRIAGE)
    text = read_json(TEXT)
    sem = read_json(SEM)
    pcrp = read_json(PCRP)
    pca = read_json(PCA)
    status = read_json(STATUS)

    assert triage["predecessors"][0]["name"] == "post_p011_status_route_packet"
    assert text["predecessor"]["package_id"] == "P012TR-G1-VIRAL-001"
    assert sem["predecessor"]["package_id"] == "P012TXT-G1-VIRAL-001"
    assert pcrp["predecessor"]["package_id"] == "P012SEM-G1-VIRAL-001"
    assert pca["predecessor"]["package_id"] == "PCRP-G1-VIRAL-P012-001"
    assert status["predecessor"]["package_id"] == "P012PCA-G1-VIRAL-001"
    assert pca["accepted_pages"] == ["012"]


def test_semantic_map_preserves_inline_option_headings():
    sem = read_json(SEM)
    units = {unit["unit_id"]: unit for unit in sem["units"]}

    assert units["SU-P012-EMILY-004"]["text"] == "Another Ghost Hunter Option."
    assert units["SU-P012-EMILY-004"]["layout_role"] == "inline_heading"
    assert units["SU-P012-EMILY-005"]["text"].startswith("Em is from a rival ghost hunting channel")
    assert not units["SU-P012-EMILY-005"]["text"].startswith("Option. ")

    assert units["SU-P012-CNI-007"]["text"] == "Mythos Investigators"
    assert units["SU-P012-CNI-007"]["heading_level"] == "h4"
    assert units["SU-P012-CNI-007"]["layout_role"] == "inline_heading"
    assert units["SU-P012-CNI-007"]["text_decoration"] == "underline"
    assert units["SU-P012-CNI-007"]["continues_inline_to"] == "SU-P012-CNI-008"
    assert units["SU-P012-CNI-008"]["external_continues_to"] == "P013 inert continuation metadata only"

    assert units["SU-P012-KEEPER-001"]["text"] == "Keeper's Notes"
    assert units["SU-P012-KEEPER-001"]["heading_level"] == "h4"
    assert units["SU-P012-KEEPER-001"]["layout_role"] == "block_heading"
    assert units["SU-P012-KEEPER-001"]["display_style"] == "callout_heading"
    assert units["SU-P012-KEEPER-002"]["display_style"] == "callout_body"
    assert units["SU-P012-KEEPER-002"]["semantic_split_contract"]["boundary_kind"] == "callout_extends_to_text_block_end"
    assert sem["semantic_split_validation"]["valid"] is True


def test_page_012_text_evidence_crops_have_explicit_contracts():
    triage = read_json(TRIAGE)
    blocks = {block["block_id"]: block for block in triage["review_blocks"]}

    assert len(blocks) == 7
    for block in blocks.values():
        assert block["crop_contract"]["context_allowed"] is False
        assert block["crop_contract"]["coverage"] in {"full_text_box", "full_text_region", "full_text_region_part"}

    keeper = blocks["P012-B006"]
    assert keeper["role"] == "keepers_notes_box"
    assert keeper["crop_box_px"] == [1305, 790, 1100, 400]
    assert keeper["crop_contract"]["neighbor_text_exclusion"] == ["PRM-G1-VIRAL-001-P012-R03"]
    assert keeper["crop_box_px"][0] >= 1250

    right_upper = blocks["P012-B004"]
    assert right_upper["role"] == "another_ghost_hunter_option_body_right_upper"
    assert right_upper["crop_contract"]["coverage"] == "full_text_region_part"


def test_page_013_and_broad_capabilities_remain_blocked():
    status = read_json(STATUS)
    pca = read_json(PCA)
    batch = read_json(BATCH)

    assert status["page_complete_accepted_pages"] == [
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
        "009",
        "010",
        "011",
        "012",
    ]
    assert status["remaining_page_complete_pages_unstarted"] == ["013", "014", "015", "016", "017", "018", "019", "020"]
    assert status["recommended_next_candidate"] == "page_013_triage_readiness_not_authorized"
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
            "page_013_processing",
        ]:
            assert payload["guardrails"][key] is False, key


def test_final_bundle_is_the_only_human_review_target():
    batch = read_json(BATCH)

    assert batch["status"] == "ready_for_bogdan_final_batch_review"
    assert batch["human_review_model"] == "final_bundle_and_post_p012_status_only"
    assert batch["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
    assert batch["decision_options"] == ["p012 aggressive batch ok", "hold p012 batch: <reason>"]
