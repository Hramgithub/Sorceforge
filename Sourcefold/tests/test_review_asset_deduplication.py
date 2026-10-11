import pytest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.review_asset_deduplication import (  # noqa: E402
    REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION,
    apply_review_asset_deduplication,
    build_delivery_assets,
    build_review_asset_index,
    require_passed_review_asset_deduplication,
    validate_review_asset_deduplication,
)


def attachment(attachment_id: str, role: str, package_path: str, sha256: str, **extra):
    payload = {
        "attachment_id": attachment_id,
        "role": role,
        "package_path": package_path,
        "sha256": sha256,
    }
    payload.update(extra)
    return payload


def test_review_asset_deduplication_aliases_identical_text_context_crops(tmp_path: Path):
    canonical = tmp_path / "review_assets" / "1b_text.png"
    duplicate = tmp_path / "review_assets" / "1_human.png"
    canonical.parent.mkdir(parents=True)
    canonical.write_bytes(b"same-crop")
    duplicate.write_bytes(b"same-crop")
    attachments = [
        attachment(
            "P010-001-ATT-HUMAN-UPPER-LEFT",
            "human_context_crop",
            "review_assets/1_human.png",
            "HASH",
            box_px=[180, 170, 1080, 500],
        ),
        attachment(
            "P010-B001-TEXT-EVIDENCE",
            "text_evidence_crop",
            "review_assets/1b_text.png",
            "HASH",
            box_px=[180, 170, 1080, 500],
        ),
    ]

    result = apply_review_asset_deduplication(attachments, out_root=tmp_path)

    assert result["review_asset_deduplication"]["schema_version"] == REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION
    assert result["review_asset_deduplication"]["status"] == "passed"
    assert result["review_asset_deduplication"]["deduplicated_binding_count"] == 1
    assert result["package_assets"] == [
        {
            "asset_id": "P010-B001-TEXT-EVIDENCE",
            "package_path": "review_assets/1b_text.png",
            "sha256": "HASH",
            "roles": [
                {
                    "attachment_id": "P010-001-ATT-HUMAN-UPPER-LEFT",
                    "role": "human_context_crop",
                    "package_path": "review_assets/1b_text.png",
                    "sha256": "HASH",
                    "box_px": [180, 170, 1080, 500],
                    "deduplicated_with": "P010-B001-TEXT-EVIDENCE",
                    "original_package_path": "review_assets/1_human.png",
                },
                {
                    "attachment_id": "P010-B001-TEXT-EVIDENCE",
                    "role": "text_evidence_crop",
                    "package_path": "review_assets/1b_text.png",
                    "sha256": "HASH",
                    "box_px": [180, 170, 1080, 500],
                },
            ],
        }
    ]
    assert attachments[0]["package_path"] == "review_assets/1b_text.png"
    assert attachments[0]["original_package_path"] == "review_assets/1_human.png"
    assert not duplicate.exists()
    assert canonical.exists()


def test_review_asset_deduplication_blocks_duplicate_hash_with_different_crop_identity():
    validation = validate_review_asset_deduplication(
        [
            attachment("A", "human_context_crop", "review_assets/a.png", "HASH", box_px=[0, 0, 10, 10]),
            attachment("B", "text_evidence_crop", "review_assets/b.png", "HASH", box_px=[0, 0, 20, 20]),
        ]
    )

    assert validation["status"] == "blocked"
    assert validation["findings"][0]["finding_id"] == "duplicate_hash_without_safe_crop_identity"


def test_review_asset_deduplication_keeps_distinct_human_context_assets():
    index = build_review_asset_index(
        [
            attachment("HUMAN", "human_context_crop", "review_assets/human.png", "HUMAN", box_px=[0, 0, 20, 20]),
            attachment("TEXT", "text_evidence_crop", "review_assets/text.png", "TEXT", box_px=[2, 2, 10, 10]),
        ]
    )

    assert len(index["physical_assets"]) == 2
    assert index["deduplicated_bindings"] == []


def test_review_asset_delivery_excludes_alias_only_duplicate_crops():
    delivery_assets = build_delivery_assets(
        [
            attachment("PAGE", "source_page_image", "review_assets/page.png", "PAGE"),
            attachment("HUMAN", "human_context_crop", "review_assets/human.png", "HASH", box_px=[0, 0, 10, 10]),
            attachment("TEXT", "text_evidence_crop", "review_assets/text.png", "HASH", box_px=[0, 0, 10, 10]),
            attachment("PORTRAIT", "human_context_crop", "review_assets/portrait.png", "PORTRAIT"),
            attachment("MAP", "ocr_verified_text_map", "review_assets/text_map.md", "MAP"),
        ]
    )

    assert [item["package_path"] for item in delivery_assets] == [
        "review_assets/page.png",
        "review_assets/portrait.png",
        "review_assets/text.png",
        "review_assets/text_map.md",
    ]


def test_review_asset_consumer_requires_passed_deduplication():
    packet = {"review_asset_deduplication": {"schema_version": REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION, "status": "passed"}}

    assert require_passed_review_asset_deduplication(packet)["status"] == "passed"
    with pytest.raises(ValueError, match="requires review_asset_deduplication"):
        require_passed_review_asset_deduplication({})
    with pytest.raises(ValueError, match="blocked"):
        require_passed_review_asset_deduplication(
            {"review_asset_deduplication": {"schema_version": REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION, "status": "blocked"}}
        )
