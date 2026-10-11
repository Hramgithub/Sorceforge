from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from PIL import Image


CROP_ROLE_CONTRACT_SCHEMA_VERSION = "sourcefold_crop_role_contract.v1"
TEXT_LIKE_CONTENT_KIND = "text_like_region"
ART_CONTENT_KIND = "art_anchor"


def rects_overlap(a: list[int], b: list[int]) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def default_is_ink(rgb: tuple[int, int, int]) -> bool:
    r, g, b = rgb
    black_text = r < 120 and g < 120 and b < 120
    red_text = r > 120 and g < 100 and b < 100
    green_text = r > 110 and g > 140 and b < 150
    return black_text or red_text or green_text


def edge_ink_ratios(path: Path, *, is_ink: Callable[[tuple[int, int, int]], bool] = default_is_ink) -> dict[str, float]:
    with Image.open(path).convert("RGB") as image:
        width, height = image.size
        margin = min(24, width // 8, height // 8)
        pixels = image.load()
        bands = {
            "left": [(x, y) for x in range(margin) for y in range(height)],
            "right": [(x, y) for x in range(width - margin, width) for y in range(height)],
            "top": [(x, y) for x in range(width) for y in range(margin)],
            "bottom": [(x, y) for x in range(width) for y in range(height - margin, height)],
        }
        return {edge: round(sum(1 for x, y in coords if is_ink(pixels[x, y])) / len(coords), 4) for edge, coords in bands.items()}


def iter_text_surfaces(block: dict[str, Any]) -> list[dict[str, Any]]:
    if "text_evidence_surfaces" in block:
        return block["text_evidence_surfaces"]
    required = {"ocr_candidate_crop_box_px", "text_evidence_crop_box_px", "ocr_candidate_asset", "text_evidence_asset"}
    if not required.issubset(block):
        return []
    return [
        {
            "surface_id": f"{block['block_id']}-TES",
            "role": block["role"],
            "ocr_candidate_crop_box_px": block["ocr_candidate_crop_box_px"],
            "text_evidence_crop_box_px": block["text_evidence_crop_box_px"],
            "ocr_candidate_asset": block["ocr_candidate_asset"],
            "text_evidence_asset": block["text_evidence_asset"],
        }
    ]


def validate_crop_role_contract(
    *,
    blocks: list[dict[str, Any]],
    output_root: Path,
    image_assets: dict[str, dict[str, str]],
    max_edge_ink_ratio: float,
    is_ink: Callable[[tuple[int, int, int]], bool] = default_is_ink,
    extra_fields: dict[str, Any] | None = None,
) -> dict[str, Any]:
    art_boxes = [
        block.get("visual_pollution_guard_box_px", block["source_region_box_px"])
        for block in blocks
        if block["content_kind"] == ART_CONTENT_KIND
    ]
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    represented_text_like_regions: list[str] = []
    text_evidence_surface_ids: list[str] = []
    text_evidence_crop_block_ids: list[str] = []
    text_blocks_by_source_region: dict[str, list[dict[str, Any]]] = {}

    for block in blocks:
        missing_roles = [key for key in ("source_region_box_px", "human_review_crop_box_px") if key not in block]
        if block["content_kind"] == TEXT_LIKE_CONTENT_KIND:
            text_blocks_by_source_region.setdefault(block["source_region_id"], []).append(block)
            if block["source_region_id"] not in represented_text_like_regions:
                represented_text_like_regions.append(block["source_region_id"])
            if block["block_id"] not in text_evidence_crop_block_ids:
                text_evidence_crop_block_ids.append(block["block_id"])
            surfaces = iter_text_surfaces(block)
            if not surfaces:
                missing_roles.append("text_evidence_surfaces")
            for surface in surfaces:
                text_evidence_surface_ids.append(surface["surface_id"])
                for key in ("ocr_candidate_crop_box_px", "text_evidence_crop_box_px"):
                    if key not in surface:
                        missing_roles.append(key)
        if missing_roles:
            findings.append({"block_id": block["block_id"], "finding_id": "missing_crop_role", "roles": sorted(set(missing_roles))})
        if block["content_kind"] != TEXT_LIKE_CONTENT_KIND:
            continue

        for surface in iter_text_surfaces(block):
            for role_key, asset_key in (
                ("ocr_candidate_crop_box_px", "ocr_candidate_asset"),
                ("text_evidence_crop_box_px", "text_evidence_asset"),
            ):
                box = surface[role_key]
                asset_path = output_root / surface[asset_key]
                ratios = edge_ink_ratios(asset_path, is_ink=is_ink)
                max_ratio = max(ratios.values())
                overlaps_art = any(rects_overlap(box, art_box) for art_box in art_boxes)
                status = "passed" if max_ratio <= max_edge_ink_ratio and not overlaps_art else "blocked"
                if max_ratio > max_edge_ink_ratio:
                    findings.append(
                        {
                            "block_id": block["block_id"],
                            "surface_id": surface["surface_id"],
                            "finding_id": "text_near_crop_boundary",
                            "role": role_key,
                            "edge_ink_ratios": ratios,
                        }
                    )
                if overlaps_art:
                    findings.append(
                        {
                            "block_id": block["block_id"],
                            "surface_id": surface["surface_id"],
                            "finding_id": "visual_pollution_in_text_crop",
                            "role": role_key,
                        }
                    )
                checks.append(
                    {
                        "block_id": block["block_id"],
                        "surface_id": surface["surface_id"],
                        "role": role_key,
                        "asset": image_assets[surface[asset_key]],
                        "status": status,
                        "edge_ink_ratios": ratios,
                        "maximum_allowed_edge_ink_ratio": max_edge_ink_ratio,
                        "overlaps_art_or_portrait_source_region": overlaps_art,
                        "source_region_box_is_lineage_not_ocr_boundary": True,
                    }
                )

    split_validation = validate_split_source_regions(text_blocks_by_source_region)
    findings.extend(split_validation["findings"])

    result = {
        "schema_version": CROP_ROLE_CONTRACT_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "findings": findings,
        "checks": checks,
        "page_map_reconciliation": {
            "represented_text_like_regions": represented_text_like_regions,
            "text_evidence_surface_ids": text_evidence_surface_ids,
            "text_evidence_crop_block_ids": text_evidence_crop_block_ids,
            "status": "passed" if represented_text_like_regions else "blocked",
        },
        "semantic_text_map_linkage": {
            "status": "contract_ready_not_materialized",
            "required_later_field": "text_evidence_crop_id",
            "human_review_crop_satisfies_text_evidence": False,
        },
        "split_source_region_validation": split_validation,
    }
    if extra_fields:
        result.update(extra_fields)
    return result


def validate_split_source_regions(text_blocks_by_source_region: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []
    for source_region_id, blocks in text_blocks_by_source_region.items():
        if len(blocks) < 2:
            continue
        split_values = [block.get("source_region_split") for block in blocks]
        asset_fields = ("human_review_asset", "ocr_candidate_asset", "text_evidence_asset")
        shared_assets = {
            field: [block.get(field) for block in blocks]
            for field in asset_fields
            if len([block.get(field) for block in blocks]) != len(set(block.get(field) for block in blocks))
        }
        missing_split_blocks = [block["block_id"] for block in blocks if not block.get("source_region_split")]
        duplicate_split_values = len(split_values) != len(set(split_values))
        if missing_split_blocks:
            findings.append(
                {
                    "finding_id": "missing_source_region_split",
                    "source_region_id": source_region_id,
                    "block_ids": missing_split_blocks,
                }
            )
        if duplicate_split_values:
            findings.append(
                {
                    "finding_id": "duplicate_source_region_split",
                    "source_region_id": source_region_id,
                    "split_values": split_values,
                }
            )
        if shared_assets:
            findings.append(
                {
                    "finding_id": "shared_split_source_region_crop_asset",
                    "source_region_id": source_region_id,
                    "shared_assets": shared_assets,
                }
            )
        checks.append(
            {
                "source_region_id": source_region_id,
                "block_ids": [block["block_id"] for block in blocks],
                "source_region_splits": split_values,
                "peer_blocks_required": True,
                "shared_context_crop_promoted_to_text_evidence": False,
                "status": "blocked" if missing_split_blocks or duplicate_split_values or shared_assets else "passed",
            }
        )
    return {
        "status": "passed" if not findings else "blocked",
        "findings": findings,
        "checks": checks,
    }
