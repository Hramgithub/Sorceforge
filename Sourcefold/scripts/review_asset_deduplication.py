from __future__ import annotations

from pathlib import Path
from typing import Any


REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION = "sourcefold_review_asset_deduplication.v1"

IMAGE_REVIEW_ROLES = {
    "block_crop",
    "human_context_crop",
    "human_review_crop",
    "source_page_image",
    "text_evidence_crop",
}

DELIVERY_ROLE_ORDER = {
    "source_page_image": 10,
    "human_context_crop": 20,
    "human_review_crop": 20,
    "block_crop": 30,
    "text_evidence_crop": 40,
    "ocr_verified_text_map": 50,
    "semantic_text_map_markdown": 60,
    "semantic_text_map_json": 70,
}

CANONICAL_ROLE_PRIORITY = {
    "text_evidence_crop": 10,
    "source_page_image": 20,
    "block_crop": 30,
    "human_review_crop": 40,
    "human_context_crop": 50,
}


def is_review_image_asset(attachment: dict[str, Any]) -> bool:
    package_path = str(attachment.get("package_path", "")).lower()
    return attachment.get("role") in IMAGE_REVIEW_ROLES and package_path.endswith((".png", ".jpg", ".jpeg", ".webp"))


def canonical_sort_key(attachment: dict[str, Any]) -> tuple[int, str]:
    return (
        CANONICAL_ROLE_PRIORITY.get(attachment.get("role", ""), 100),
        attachment.get("package_path", ""),
    )


def same_crop_identity(a: dict[str, Any], b: dict[str, Any]) -> bool:
    if a.get("sha256") != b.get("sha256"):
        return False
    if "box_px" in a or "box_px" in b:
        return a.get("box_px") == b.get("box_px")
    return True


def build_review_asset_index(attachments: list[dict[str, Any]]) -> dict[str, Any]:
    physical_assets: dict[str, dict[str, Any]] = {}
    role_bindings: list[dict[str, Any]] = []
    duplicates: list[dict[str, Any]] = []
    by_sha: dict[str, list[dict[str, Any]]] = {}

    for attachment in attachments:
        if is_review_image_asset(attachment):
            by_sha.setdefault(attachment["sha256"], []).append(attachment)

    canonical_by_attachment_id: dict[str, dict[str, Any]] = {}
    for group in by_sha.values():
        canonical = sorted(group, key=canonical_sort_key)[0]
        for attachment in group:
            canonical_by_attachment_id[attachment["attachment_id"]] = canonical

    for attachment in attachments:
        canonical = canonical_by_attachment_id.get(attachment["attachment_id"], attachment)
        package_path = canonical["package_path"]
        asset = physical_assets.setdefault(
            package_path,
            {
                "asset_id": canonical["attachment_id"],
                "package_path": package_path,
                "sha256": canonical["sha256"],
                "roles": [],
            },
        )
        binding = {
            "attachment_id": attachment["attachment_id"],
            "role": attachment["role"],
            "package_path": package_path,
            "sha256": attachment["sha256"],
        }
        for optional_key in ("label", "covered_review_blocks", "box_px"):
            if optional_key in attachment:
                binding[optional_key] = attachment[optional_key]
        if attachment is not canonical:
            binding["deduplicated_with"] = canonical["attachment_id"]
            binding["original_package_path"] = attachment.get("original_package_path", attachment["package_path"])
            duplicates.append(binding)
        asset["roles"].append(binding)
        role_bindings.append(binding)

    return {
        "schema_version": REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION,
        "physical_assets": sorted(physical_assets.values(), key=lambda item: item["package_path"]),
        "role_bindings": role_bindings,
        "deduplicated_bindings": duplicates,
    }


def validate_review_asset_deduplication(attachments: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    index = build_review_asset_index(attachments)
    image_attachments = [attachment for attachment in attachments if is_review_image_asset(attachment)]
    by_sha: dict[str, list[dict[str, Any]]] = {}
    for attachment in image_attachments:
        by_sha.setdefault(attachment["sha256"], []).append(attachment)

    for sha256, group in by_sha.items():
        unique_paths = {attachment["package_path"] for attachment in group}
        if len(group) < 2 or len(unique_paths) < 2:
            continue
        canonical = sorted(group, key=canonical_sort_key)[0]
        for attachment in group:
            if attachment is canonical:
                continue
            if not same_crop_identity(canonical, attachment):
                findings.append(
                    {
                        "finding_id": "duplicate_hash_without_safe_crop_identity",
                        "sha256": sha256,
                        "canonical_attachment_id": canonical["attachment_id"],
                        "duplicate_attachment_id": attachment["attachment_id"],
                    }
                )

    delivery_assets = build_delivery_assets(attachments)
    if not delivery_assets:
        findings.append({"finding_id": "missing_delivery_assets"})

    return {
        "schema_version": REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "findings": findings,
        "physical_asset_count": len(index["physical_assets"]),
        "logical_attachment_count": len(attachments),
        "deduplicated_binding_count": len(index["deduplicated_bindings"]),
        "deduplicated_bindings": index["deduplicated_bindings"],
    }


def build_delivery_assets(attachments: list[dict[str, Any]], policy: str = "page_complete_review") -> list[dict[str, Any]]:
    if policy != "page_complete_review":
        raise ValueError(f"unsupported delivery asset policy: {policy}")
    index = build_review_asset_index(attachments)
    deduplicated_attachment_ids = {item["attachment_id"] for item in index["deduplicated_bindings"]}
    delivered_by_path: set[str] = set()
    delivery_assets: list[dict[str, Any]] = []

    for binding in sorted(index["role_bindings"], key=lambda item: (DELIVERY_ROLE_ORDER.get(item["role"], 100), item["package_path"])):
        if binding["attachment_id"] in deduplicated_attachment_ids:
            continue
        if binding["package_path"] in delivered_by_path:
            continue
        delivered_by_path.add(binding["package_path"])
        delivery_assets.append(
            {
                "attachment_id": binding["attachment_id"],
                "role": binding["role"],
                "package_path": binding["package_path"],
                "sha256": binding["sha256"],
            }
        )
    return delivery_assets


def apply_review_asset_deduplication(
    attachments: list[dict[str, Any]],
    *,
    out_root: Path,
) -> dict[str, Any]:
    index = build_review_asset_index(attachments)
    canonical_by_original_path = {
        binding["original_package_path"]: binding["package_path"]
        for binding in index["deduplicated_bindings"]
    }
    for attachment in attachments:
        original_package_path = attachment["package_path"]
        canonical_package_path = canonical_by_original_path.get(original_package_path)
        if not canonical_package_path:
            continue
        duplicate_path = out_root / original_package_path
        canonical_path = out_root / canonical_package_path
        if duplicate_path.exists() and duplicate_path != canonical_path:
            duplicate_path.unlink()
        attachment["deduplicated_with_package_path"] = canonical_package_path
        attachment["original_package_path"] = original_package_path
        attachment["package_path"] = canonical_package_path
    refreshed_index = build_review_asset_index(attachments)
    validation = validate_review_asset_deduplication(attachments)
    if validation["status"] != "passed":
        raise ValueError(f"review asset deduplication blocked: {validation['findings']}")
    return {
        "review_asset_deduplication": validation,
        "package_assets": refreshed_index["physical_assets"],
        "role_bindings": refreshed_index["role_bindings"],
        "delivery_assets": build_delivery_assets(attachments),
    }


def require_passed_review_asset_deduplication(packet_or_report: dict[str, Any]) -> dict[str, Any]:
    validation = packet_or_report.get("review_asset_deduplication")
    if not isinstance(validation, dict):
        raise ValueError("consumer requires review_asset_deduplication before using review package assets")
    if validation.get("schema_version") != REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION:
        raise ValueError(f"consumer requires {REVIEW_ASSET_DEDUPLICATION_SCHEMA_VERSION}")
    if validation.get("status") != "passed":
        raise ValueError(f"review asset deduplication blocked: {validation.get('findings')}")
    return validation
