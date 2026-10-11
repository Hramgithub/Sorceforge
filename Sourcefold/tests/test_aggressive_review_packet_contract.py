from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.aggressive_review_packet_contract import (
    SEQUENTIAL_RUN_AUTHORIZATION_ID,
    SEQUENTIAL_RUN_PAGE_IDS,
    assert_human_review_packet_policy,
    human_review_assets_for_page,
    human_review_packet_for_sequential_run,
    sequential_aggressive_run_pages,
)


def test_sequential_aggressive_run_is_bounded_to_pages_016_020():
    assert sequential_aggressive_run_pages() == SEQUENTIAL_RUN_PAGE_IDS

    with pytest.raises(ValueError):
        sequential_aggressive_run_pages("015", "020")
    with pytest.raises(ValueError):
        sequential_aggressive_run_pages("016", "021")


def test_human_review_packet_shows_only_source_art_and_semantic_map():
    packet = human_review_packet_for_sequential_run()

    assert packet["authorization_id"] == SEQUENTIAL_RUN_AUTHORIZATION_ID
    assert packet["human_review_policy"] == "source_page_art_and_semantic_text_map_only"
    assert packet["internal_evidence_policy"] == "crops_remain_internal_unless_blocker"
    assert_human_review_packet_policy(packet)

    roles = {(asset["page"], asset["role"]) for asset in packet["assets"]}
    for page in SEQUENTIAL_RUN_PAGE_IDS:
        assert (page, "source_page_art") in roles
        assert (page, "semantic_text_map_md") in roles

    serialized_paths = "\n".join(asset["path"] for asset in packet["assets"])
    assert "review_assets/" not in serialized_paths
    assert "crop" not in serialized_paths.lower()


def test_source_pages_and_semantic_maps_exist_before_human_packet():
    for page in SEQUENTIAL_RUN_PAGE_IDS:
        source_art, semantic_map = human_review_assets_for_page(page)

        assert source_art.path.exists()
        assert source_art.path.name == f"page_{page}.png"
        assert semantic_map.path.exists()
        assert semantic_map.path == (
            ROOT
            / "fixtures"
            / "candidate_inputs"
            / "viral"
            / "render_trials"
            / "RT-G1-VIRAL-RENDER-001"
            / f"page_{page}_semantic_text_map_G1_VIRAL_001"
            / f"page_{page}_semantic_text_map.md"
        )


def test_human_review_packet_fails_closed_when_required_asset_is_missing():
    packet = human_review_packet_for_sequential_run()
    packet["assets"][0]["path"] = "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/missing-page.png"

    with pytest.raises(AssertionError, match="required human review asset is missing"):
        assert_human_review_packet_policy(packet)
