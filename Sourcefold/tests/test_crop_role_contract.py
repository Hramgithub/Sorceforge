from pathlib import Path
import shutil
import sys

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
TEST_TMP = ROOT / ".test_tmp" / "crop_role_contract"

from scripts.crop_role_contract import (
    CROP_ROLE_CONTRACT_SCHEMA_VERSION,
    validate_crop_role_contract,
)


def reset_test_tmp(name: str) -> Path:
    path = TEST_TMP / name
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    return path


def make_asset(path: Path, *, color: tuple[int, int, int] = (255, 255, 255)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (40, 40), color).save(path)


def test_crop_role_contract_accepts_role_separated_text_crop():
    tmp_path = reset_test_tmp("accepts")
    make_asset(tmp_path / "text.png")
    blocks = [
        {
            "block_id": "B001",
            "content_kind": "text_like_region",
            "role": "body_text",
            "source_region_id": "R01",
            "source_region_box_px": [0, 0, 100, 100],
            "human_review_crop_box_px": [0, 0, 100, 100],
            "ocr_candidate_crop_box_px": [10, 10, 40, 40],
            "text_evidence_crop_box_px": [10, 10, 40, 40],
            "ocr_candidate_asset": "text.png",
            "text_evidence_asset": "text.png",
        }
    ]
    assets = {"text.png": {"path": "text.png", "sha256": "sha"}}

    result = validate_crop_role_contract(
        blocks=blocks,
        output_root=tmp_path,
        image_assets=assets,
        max_edge_ink_ratio=0.02,
    )

    assert result["schema_version"] == CROP_ROLE_CONTRACT_SCHEMA_VERSION
    assert result["status"] == "passed"
    assert result["semantic_text_map_linkage"]["human_review_crop_satisfies_text_evidence"] is False
    assert result["page_map_reconciliation"]["represented_text_like_regions"] == ["R01"]
    assert result["page_map_reconciliation"]["text_evidence_surface_ids"] == ["B001-TES"]


def test_crop_role_contract_blocks_missing_text_evidence_role():
    tmp_path = reset_test_tmp("missing")
    blocks = [
        {
            "block_id": "B001",
            "content_kind": "text_like_region",
            "role": "body_text",
            "source_region_id": "R01",
            "source_region_box_px": [0, 0, 100, 100],
            "human_review_crop_box_px": [0, 0, 100, 100],
        }
    ]

    result = validate_crop_role_contract(
        blocks=blocks,
        output_root=tmp_path,
        image_assets={},
        max_edge_ink_ratio=0.02,
    )

    assert result["status"] == "blocked"
    assert any(finding["finding_id"] == "missing_crop_role" for finding in result["findings"])


def test_crop_role_contract_blocks_visual_pollution_in_text_crop():
    tmp_path = reset_test_tmp("pollution")
    make_asset(tmp_path / "text.png")
    blocks = [
        {
            "block_id": "ART",
            "content_kind": "art_anchor",
            "role": "portrait",
            "source_region_id": "R02",
            "source_region_box_px": [0, 0, 100, 100],
            "human_review_crop_box_px": [0, 0, 100, 100],
        },
        {
            "block_id": "TEXT",
            "content_kind": "text_like_region",
            "role": "body_text",
            "source_region_id": "R01",
            "source_region_box_px": [100, 0, 100, 100],
            "human_review_crop_box_px": [100, 0, 100, 100],
            "ocr_candidate_crop_box_px": [10, 10, 40, 40],
            "text_evidence_crop_box_px": [10, 10, 40, 40],
            "ocr_candidate_asset": "text.png",
            "text_evidence_asset": "text.png",
        },
    ]
    assets = {"text.png": {"path": "text.png", "sha256": "sha"}}

    result = validate_crop_role_contract(
        blocks=blocks,
        output_root=tmp_path,
        image_assets=assets,
        max_edge_ink_ratio=0.02,
    )

    assert result["status"] == "blocked"
    assert any(finding["finding_id"] == "visual_pollution_in_text_crop" for finding in result["findings"])


def test_crop_role_contract_accepts_peer_split_source_region_blocks():
    tmp_path = reset_test_tmp("split_accepts")
    for name in ("left.png", "right.png"):
        make_asset(tmp_path / name)
    blocks = [
        {
            "block_id": "LEFT",
            "content_kind": "text_like_region",
            "role": "left_body_text",
            "source_region_id": "R05",
            "source_region_split": "left_derived_from_R05",
            "source_region_box_px": [0, 0, 200, 100],
            "human_review_crop_box_px": [0, 0, 100, 100],
            "ocr_candidate_crop_box_px": [0, 0, 100, 100],
            "text_evidence_crop_box_px": [0, 0, 100, 100],
            "human_review_asset": "left.png",
            "ocr_candidate_asset": "left.png",
            "text_evidence_asset": "left.png",
        },
        {
            "block_id": "RIGHT",
            "content_kind": "text_like_region",
            "role": "right_body_text",
            "source_region_id": "R05",
            "source_region_split": "right_derived_from_R05",
            "source_region_box_px": [0, 0, 200, 100],
            "human_review_crop_box_px": [100, 0, 100, 100],
            "ocr_candidate_crop_box_px": [100, 0, 100, 100],
            "text_evidence_crop_box_px": [100, 0, 100, 100],
            "human_review_asset": "right.png",
            "ocr_candidate_asset": "right.png",
            "text_evidence_asset": "right.png",
        },
    ]
    assets = {name: {"path": name, "sha256": "sha"} for name in ("left.png", "right.png")}

    result = validate_crop_role_contract(
        blocks=blocks,
        output_root=tmp_path,
        image_assets=assets,
        max_edge_ink_ratio=0.02,
    )

    assert result["status"] == "passed"
    assert result["split_source_region_validation"]["status"] == "passed"
    assert result["split_source_region_validation"]["checks"][0]["source_region_splits"] == [
        "left_derived_from_R05",
        "right_derived_from_R05",
    ]


def test_crop_role_contract_blocks_split_source_region_without_peer_contract():
    tmp_path = reset_test_tmp("split_blocks")
    make_asset(tmp_path / "shared.png")
    blocks = [
        {
            "block_id": "LEFT",
            "content_kind": "text_like_region",
            "role": "left_body_text",
            "source_region_id": "R05",
            "source_region_box_px": [0, 0, 200, 100],
            "human_review_crop_box_px": [0, 0, 100, 100],
            "ocr_candidate_crop_box_px": [0, 0, 100, 100],
            "text_evidence_crop_box_px": [0, 0, 100, 100],
            "human_review_asset": "shared.png",
            "ocr_candidate_asset": "shared.png",
            "text_evidence_asset": "shared.png",
        },
        {
            "block_id": "RIGHT",
            "content_kind": "text_like_region",
            "role": "right_body_text",
            "source_region_id": "R05",
            "source_region_box_px": [0, 0, 200, 100],
            "human_review_crop_box_px": [100, 0, 100, 100],
            "ocr_candidate_crop_box_px": [100, 0, 100, 100],
            "text_evidence_crop_box_px": [100, 0, 100, 100],
            "human_review_asset": "shared.png",
            "ocr_candidate_asset": "shared.png",
            "text_evidence_asset": "shared.png",
        },
    ]
    assets = {"shared.png": {"path": "shared.png", "sha256": "sha"}}

    result = validate_crop_role_contract(
        blocks=blocks,
        output_root=tmp_path,
        image_assets=assets,
        max_edge_ink_ratio=0.02,
    )

    assert result["status"] == "blocked"
    finding_ids = {finding["finding_id"] for finding in result["split_source_region_validation"]["findings"]}
    assert "missing_source_region_split" in finding_ids
    assert "shared_split_source_region_crop_asset" in finding_ids
