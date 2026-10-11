from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


BoxPx = Sequence[int]
GLOBAL_CROP_POLICY_ID = "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
GLOBAL_CROP_POLICY_VERSION = 1
DEFAULT_MIN_GUTTER_PX = 24
HISTORICAL_TIGHT_BOXES_BY_REGION = {
    "SRCR-G1-VIRAL-003-R01": [[590, 180, 1350, 700]],
    "SRCR-G1-VIRAL-003-R02": [[460, 860, 1650, 2050]],
}


@dataclass(frozen=True)
class CropBox:
    region_id: str
    left: int
    top: int
    width: int
    height: int

    @property
    def right(self) -> int:
        return self.left + self.width

    @property
    def bottom(self) -> int:
        return self.top + self.height


def crop_box(region_id: str, box_px: BoxPx) -> CropBox:
    if len(box_px) != 4:
        raise ValueError(f"{region_id} crop box must have four values")
    if any(type(value) is not int for value in box_px):
        raise ValueError(f"{region_id} crop box coordinates must be integers")
    left, top, width, height = box_px
    if min(left, top, width, height) < 0:
        raise ValueError(f"{region_id} crop box has negative coordinates")
    if width <= 0 or height <= 0:
        raise ValueError(f"{region_id} crop box must have positive size")
    return CropBox(region_id=region_id, left=left, top=top, width=width, height=height)


def validate_crop_layout(
    records: Iterable[Mapping[str, object]],
    *,
    image_size: tuple[int, int],
    min_gutter_px: int = DEFAULT_MIN_GUTTER_PX,
    blocked_boxes: Iterable[BoxPx] = (),
    blocked_boxes_by_region: Mapping[str, Iterable[BoxPx]] | None = None,
    approved_boxes_by_region: Mapping[str, BoxPx] | None = None,
    validated_at_stage: str,
) -> dict[str, object]:
    boxes = [
        crop_box(str(record.get("review_id") or record.get("slice_region_id") or record["source_region_id"]), record["box_px"])
        for record in records
    ]
    blocked = {tuple(box) for box in blocked_boxes}
    per_region_blocked = {
        region_id: {tuple(box) for box in boxes}
        for region_id, boxes in (blocked_boxes_by_region or HISTORICAL_TIGHT_BOXES_BY_REGION).items()
    }
    approved = {region_id: tuple(box) for region_id, box in (approved_boxes_by_region or {}).items()}
    image_width, image_height = image_size

    for box in boxes:
        box_tuple = (box.left, box.top, box.width, box.height)
        if box_tuple in blocked or box_tuple in per_region_blocked.get(box.region_id, set()):
            raise ValueError(f"{box.region_id} uses a blocked tight crop box")
        if approved and approved.get(box.region_id) != box_tuple:
            raise ValueError(f"{box.region_id} crop box is not the approved crop box")
        if box.right > image_width or box.bottom > image_height:
            raise ValueError(f"{box.region_id} crop box exceeds page bounds")

    for index, first in enumerate(boxes):
        for second in boxes[index + 1 :]:
            if _overlaps(first, second):
                raise ValueError(f"{first.region_id} crop box overlaps {second.region_id}")
            distance = _rectangle_distance(first, second)
            if distance < min_gutter_px:
                raise ValueError(
                    f"{first.region_id} crop box is too close to {second.region_id}: "
                    f"{distance}px gutter, expected at least {min_gutter_px}px"
                )

    return {
        "guardrail_policy_id": GLOBAL_CROP_POLICY_ID,
        "policy_version": GLOBAL_CROP_POLICY_VERSION,
        "policy_source_sha256": _policy_source_sha256(),
        "status": "passed",
        "validated_at_stage": validated_at_stage,
        "image_size": {"width": image_width, "height": image_height},
        "min_gutter_px": min_gutter_px,
        "checks": ["integer_geometry", "bounds", "historical_blocked_tight_boxes", "approved_boxes", "no_overlap", "min_gutter"],
        "validated_boxes": [
            {"region_id": box.region_id, "box_px": [box.left, box.top, box.width, box.height]} for box in boxes
        ],
    }


def crop_with_guardrail(image, box_px: BoxPx, target: Path) -> None:
    box = crop_box(str(target), box_px)
    image.crop((box.left, box.top, box.right, box.bottom)).save(target)


def _overlaps(first: CropBox, second: CropBox) -> bool:
    return first.left < second.right and second.left < first.right and first.top < second.bottom and second.top < first.bottom


def _rectangle_distance(first: CropBox, second: CropBox) -> int:
    dx = max(second.left - first.right, first.left - second.right, 0)
    dy = max(second.top - first.bottom, first.top - second.bottom, 0)
    return max(dx, dy)


def _policy_source_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
