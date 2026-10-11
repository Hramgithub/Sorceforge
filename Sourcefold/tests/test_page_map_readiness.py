import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_map_readiness.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_map_readiness_report.json"
PACKET = OUT_ROOT / "page_map_readiness_packet.md"
AUTH = "BA-G1-VIRAL-PAGE-MAP-READINESS-PIPELINE-PILOT-002-001"
P003_OUT_ROOT = TRIAL_ROOT / "page_map_readiness_p003_G1_VIRAL_001"
P003_REPORT = P003_OUT_ROOT / "page_map_readiness_report.json"
P003_PACKET = P003_OUT_ROOT / "page_map_readiness_packet.md"
P003_AUTH = "BA-G1-VIRAL-PAGE-MAP-READINESS-P003-001"
P004_OUT_ROOT = TRIAL_ROOT / "page_map_readiness_p004_G1_VIRAL_001"
P004_REPORT = P004_OUT_ROOT / "page_map_readiness_report.json"
P004_PACKET = P004_OUT_ROOT / "page_map_readiness_packet.md"
P004_AUTH = "BA-G1-VIRAL-PAGE-MAP-READINESS-P004-001"
P005_OUT_ROOT = TRIAL_ROOT / "page_map_readiness_p005_G1_VIRAL_001"
P005_REPORT = P005_OUT_ROOT / "page_map_readiness_report.json"
P005_PACKET = P005_OUT_ROOT / "page_map_readiness_packet.md"
P005_AUTH = "BA-G1-VIRAL-PAGE-MAP-READINESS-P005-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_readiness_pipeline_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT), "--page", "002"], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001", "--page", "002"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_readiness_pipeline_is_profile_gated():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--page", "006"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "no page_map profile exists for page 006" in result.stderr


def test_page_002_inventory_and_coverage_are_ready_but_not_acceptance():
    report = read_json(REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert report["package_id"] == "PMRP-G1-VIRAL-P002-001"
    assert report["pipeline_id"] == "page_map_readiness_pipeline_v0"
    assert report["profile"]["reusable_pipeline"] is True
    assert report["status"] == "ready_for_page_complete_review_packet"
    assert set(blocks) == {"P002-B001", "P002-B002"}
    assert blocks["P002-B001"]["role"] == "credits"
    assert blocks["P002-B002"]["role"] == "boxed_legal_footer"
    assert [blocks["P002-B001"]["reading_order"], blocks["P002-B002"]["reading_order"]] == [1, 2]
    assert report["coverage_summary"]["inventory_coverage"]["count"] == 2
    assert report["coverage_summary"]["inventory_coverage"]["expected"] == 2
    assert report["coverage_summary"]["inventory_coverage"]["percent"] == 100.0
    assert report["coverage_summary"]["source_ready_in_scope_text_blocks"]["count"] == 2
    assert report["coverage_summary"]["source_ready_in_scope_text_blocks"]["expected"] == 2
    assert report["coverage_summary"]["coverage_accepts_page"] is False
    assert report["readiness_decision"]["page_complete_acceptance_created"] is False
    assert report["readiness_decision"]["whole_gate_1_acceptance_created"] is False


def test_page_002_text_fidelity_and_protected_tokens_are_declared():
    report = read_json(REPORT)
    for block in report["block_inventory"]:
        fidelity = block["text_fidelity"]
        assert fidelity["draft_matches_verified"] is True
        assert fidelity["raw_ocr_available"] is False
        assert fidelity["raw_ocr_comparison"] == "not_available_for_this_authorization"
        assert fidelity["missing_protected_tokens"] == []
        assert fidelity["discrepancy_disposition"] == "none"
        assert fidelity["verified_metrics"]["character_count"] > 100
        assert fidelity["verified_metrics"]["non_empty_line_count"] > 1


def test_readiness_guardrails_stay_false():
    for path in [REPORT, P003_REPORT, P004_REPORT, P005_REPORT]:
        report = read_json(path)
        for key in [
            "ocr_executed",
            "pdf_opened_or_parsed",
            "pdf_text_layer_used",
            "render_executed",
            "raw_artifacts_modified",
            "fixture_admission",
            "translation_authorized",
            "proofreading_authorized",
            "renderer_profile_acceptance",
            "implementation_authorized",
            "push_authorized",
        ]:
            assert report["guardrails"][key] is False


def test_human_packet_hides_internal_hashes_and_keeps_boundary():
    packet = PACKET.read_text(encoding="utf-8-sig")

    forbidden = ["SHA", "sha", "pytest", "test key", "diff-check", "stale scan"]
    assert all(item not in packet for item in forbidden)
    assert "Coverage is advisory only" in packet
    assert "does not accept page 002 as complete" in packet


def test_page_003_inventory_uses_accepted_source_records_without_page_acceptance():
    report = read_json(P003_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert report["package_id"] == "PMRP-G1-VIRAL-P003-001"
    assert report["authorization_id"] == P003_AUTH
    assert report["profile_id"] == "page_map_profile_G1_VIRAL_P003_v0"
    assert report["input_packages"] == ["PRM-G1-VIRAL-001", "P002C-G1-VIRAL-002", "P003A-G1-VIRAL-003"]
    assert report["status"] == "ready_for_page_complete_review_packet"
    assert set(blocks) == {"P003-B001", "P003-B002"}
    assert blocks["P003-B001"]["role"] == "title_heading_like"
    assert blocks["P003-B002"]["role"] == "main_body_text"
    assert [blocks["P003-B001"]["reading_order"], blocks["P003-B002"]["reading_order"]] == [1, 2]
    assert report["coverage_summary"]["inventory_coverage"]["count"] == 2
    assert report["coverage_summary"]["coverage_accepts_page"] is False
    assert report["readiness_decision"]["page_complete_acceptance_created"] is False
    assert report["readiness_decision"]["whole_gate_1_acceptance_created"] is False


def test_page_003_text_fidelity_and_profile_tokens_are_ready():
    report = read_json(P003_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert blocks["P003-B001"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P003-B001"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P003-B001"]["structure_semantics"]["semantic_roles"] == ["title_heading_like"]
    assert blocks["P003-B002"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P003-B002"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P003-B002"]["text_fidelity"]["verified_metrics"]["character_count"] > 1000
    assert blocks["P003-B002"]["structure_semantics"]["semantic_roles"] == ["body_text"]


def test_page_003_packet_keeps_readiness_boundary():
    packet = P003_PACKET.read_text(encoding="utf-8-sig")

    assert "Page Map Readiness Packet - Page 003" in packet
    assert "title_heading_like" in packet
    assert "main_body_text" in packet
    assert "Coverage is advisory only" in packet
    assert "does not accept page 003 as complete" in packet


def test_page_004_inventory_uses_context_only_confirmation_without_page_acceptance():
    report = read_json(P004_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert report["package_id"] == "PMRP-G1-VIRAL-P004-001"
    assert report["authorization_id"] == P004_AUTH
    assert report["profile_id"] == "page_map_profile_G1_VIRAL_P004_v0"
    assert report["input_packages"] == ["PRM-G1-VIRAL-001", "P004A-G1-VIRAL-004", "P004COD-G1-VIRAL-001"]
    assert report["status"] == "ready_for_page_complete_review_packet"
    assert set(blocks) == {"P004-B001", "P004-B002"}
    assert blocks["P004-B001"]["role"] == "warning_title"
    assert blocks["P004-B002"]["role"] == "safety_warning_body"
    assert [blocks["P004-B001"]["reading_order"], blocks["P004-B002"]["reading_order"]] == [1, 2]
    assert report["profile"]["context_only_regions"] == [
        {
            "source_region_id": "PRM-G1-VIRAL-001-P004-R01",
            "status": "context_only_not_peer_crop_record",
            "reason": "Full tilted inset contains the accepted title/body regions and would overlap peer crops.",
        }
    ]
    assert report["coverage_summary"]["inventory_coverage"]["count"] == 2
    assert report["coverage_summary"]["coverage_accepts_page"] is False
    assert report["readiness_decision"]["page_complete_acceptance_created"] is False
    assert report["readiness_decision"]["whole_gate_1_acceptance_created"] is False


def test_page_004_text_fidelity_and_profile_tokens_are_ready():
    report = read_json(P004_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert blocks["P004-B001"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P004-B001"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P004-B001"]["structure_semantics"]["semantic_roles"] == ["warning_title"]
    assert blocks["P004-B002"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P004-B002"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P004-B002"]["text_fidelity"]["verified_metrics"]["character_count"] > 1500
    assert blocks["P004-B002"]["structure_semantics"]["semantic_roles"] == ["safety_warning_body"]


def test_page_004_packet_keeps_context_only_and_readiness_boundary():
    packet = P004_PACKET.read_text(encoding="utf-8-sig")

    assert "Page Map Readiness Packet - Page 004" in packet
    assert "warning_title" in packet
    assert "safety_warning_body" in packet
    assert "Context-only regions: 1" in packet
    assert "Coverage is advisory only" in packet
    assert "does not accept page 004 as complete" in packet


def test_page_005_inventory_uses_human_qa_fixture_slice_without_page_acceptance():
    report = read_json(P005_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert report["package_id"] == "PMRP-G1-VIRAL-P005-001"
    assert report["authorization_id"] == P005_AUTH
    assert report["profile_id"] == "page_map_profile_G1_VIRAL_P005_v0"
    assert report["input_packages"] == ["PRM-G1-VIRAL-001", "SRHR-G1-VIRAL-001", "SRQA-G1-VIRAL-001", "SRFA-G1-VIRAL-001"]
    assert report["status"] == "ready_for_page_complete_review_packet"
    assert set(blocks) == {"P005-B001", "P005-B002"}
    assert blocks["P005-B001"]["role"] == "contents_heading"
    assert blocks["P005-B002"]["role"] == "contents_entry_group"
    assert [blocks["P005-B001"]["reading_order"], blocks["P005-B002"]["reading_order"]] == [1, 2]
    assert report["profile"]["context_only_regions"] == [
        {
            "source_region_id": "PRM-G1-VIRAL-001-P005-R03",
            "status": "visual_exclusion_not_source_text_record",
            "reason": "Margin page marker/layout component is accepted as a visual-only exclusion, not source text.",
        }
    ]
    assert report["coverage_summary"]["inventory_coverage"]["count"] == 2
    assert report["coverage_summary"]["coverage_accepts_page"] is False
    assert report["readiness_decision"]["page_complete_acceptance_created"] is False
    assert report["readiness_decision"]["whole_gate_1_acceptance_created"] is False


def test_page_005_text_fidelity_and_profile_tokens_are_ready():
    report = read_json(P005_REPORT)
    blocks = {block["block_id"]: block for block in report["block_inventory"]}

    assert blocks["P005-B001"]["region_admission_id"] == "SRA-G1-VIRAL-001-R002"
    assert blocks["P005-B001"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P005-B001"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P005-B001"]["structure_semantics"]["semantic_roles"] == ["heading"]
    assert blocks["P005-B002"]["region_admission_id"] == "SRA-G1-VIRAL-001-R003"
    assert blocks["P005-B002"]["text_fidelity"]["draft_matches_verified"] is True
    assert blocks["P005-B002"]["text_fidelity"]["missing_protected_tokens"] == []
    assert blocks["P005-B002"]["text_fidelity"]["verified_metrics"]["non_empty_line_count"] == 4
    assert blocks["P005-B002"]["structure_semantics"]["semantic_roles"] == ["table_list_entry_group"]


def test_page_005_packet_keeps_visual_exclusion_and_readiness_boundary():
    packet = P005_PACKET.read_text(encoding="utf-8-sig")

    assert "Page Map Readiness Packet - Page 005" in packet
    assert "contents_heading" in packet
    assert "contents_entry_group" in packet
    assert "Context-only regions: 1" in packet
    assert "Coverage is advisory only" in packet
    assert "does not accept page 005 as complete" in packet
