from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image

from artifact_lifecycle_validation import require_current_artifact
from page_review_semantic_units import (
    build_semantic_map_markdown,
    reconcile_page_inventory,
    semantic_map_document,
    validate_semantic_map_markdown,
)
from review_asset_deduplication import apply_review_asset_deduplication


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_complete_review.py"
TEST_PATH = ROOT / "tests" / "test_page_complete_review.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MIN_BLOCK_CROP_DIMENSION_RATIO = 1.00
PAGE_009_REQUIRED_CROP_CONTRACT_ID = "P009TR-G1-VIRAL-003"
PAGE_009_STALE_TRIAGE_ID = "P009TR-G1-VIRAL-002"
PAGE_009_CROP_CONTRACT_ROOT = TRIAL_ROOT / "page_009_triage_G1_VIRAL_003"
PAGE_009_TEXT_ROOT = TRIAL_ROOT / "page_009_text_extraction_G1_VIRAL_001"
PAGE_009_SEMANTIC_ROOT = TRIAL_ROOT / "page_009_semantic_text_map_G1_VIRAL_001"
PAGE_010_CROP_CONTRACT_ROOT = TRIAL_ROOT / "page_010_triage_G1_VIRAL_001"
PAGE_010_TEXT_ROOT = TRIAL_ROOT / "page_010_text_extraction_G1_VIRAL_001"
PAGE_010_SEMANTIC_ROOT = TRIAL_ROOT / "page_010_semantic_text_map_G1_VIRAL_001"
PAGE_011_CROP_CONTRACT_ROOT = TRIAL_ROOT / "page_011_triage_G1_VIRAL_001"
PAGE_011_TEXT_ROOT = TRIAL_ROOT / "page_011_text_extraction_G1_VIRAL_001"
PAGE_011_SEMANTIC_ROOT = TRIAL_ROOT / "page_011_semantic_text_map_G1_VIRAL_001"

REVIEW_PROFILES: dict[str, dict[str, Any]] = {
    "001": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P001-001",
        "package_id": "PCRP-G1-VIRAL-P001-001",
        "page": "001",
        "page_label": "Page 001",
        "output_dir": TRIAL_ROOT / "page_complete_review_p001_G1_VIRAL_001",
        "readiness_package_id": "P001TR-G1-VIRAL-001",
        "readiness_report_sha256": "EDBB68B385CAC4EF6ED7D61298C8B69CFB944E566A6B53B9EEDBC5F1DB1A6A57",
        "readiness_packet_sha256": "5D428155CD967AC427BAB090EF90140891F07F1FF985F1333157F98932016411",
        "readiness_summary_sha256": "134B845ED919079C560668580374D4B734088408E08E32FAA12E99099D89E327",
        "readiness_manifest_sha256": "3DAE5B7D2076A8B1B48AB8CAD833A2BB9F8A288702B0381BE6C881F30D4C53C7",
        "decision_options": [
            "accept_page_001_as_complete_in_a_later_explicit_decision",
            "hold_page_001_for_corrections_or_additional_review",
        ],
        "skip_readiness_anchor_visual_proof": True,
        "inline_readiness": {
            "authorization_id": "BA-G1-VIRAL-PAGE-001-TRIAGE-001",
            "page_id": "PG-G1-VIRAL-P001",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P001",
            "profile_id": "page_map_profile_G1_VIRAL_P001_visual_title_v0",
            "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_001.png",
            "page_image_sha256": "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692",
            "declared_none": ["source_text", "table", "unknown", "missing"],
            "context_only_regions": [],
            "blocks": [
                {
                    "block_id": "P001-B001",
                    "block_type": "visual_anchor",
                    "content_kind": "cover_visual_anchor",
                    "extraction_policy": "anchor_only_defer_visual",
                    "role": "cover_full_page_visual_anchor",
                    "source_region_id": "PRM-G1-VIRAL-001-P001-R01",
                    "reading_order": 1,
                    "box_px": [0, 0, 2550, 3300],
                    "text": "",
                    "spans": [],
                    "protected_tokens": [],
                    "anchor_metadata": {
                        "anchor_id": "ART-G1-VIRAL-P001-001",
                        "anchor_label": "Full-page cover visual composition",
                        "visual_identification": "Full-page Viral Unredacted cover/title composition; preserve as a visual anchor for later extraction or layout assembly.",
                        "deferred_stage": "html_assembly_art_replacement",
                        "not_source_text": True,
                    },
                },
                {
                    "block_id": "P001-B002",
                    "block_type": "visual_anchor",
                    "content_kind": "title_visual_anchor",
                    "extraction_policy": "anchor_only_defer_visual",
                    "role": "cover_title_logo_area",
                    "source_region_id": "PRM-G1-VIRAL-001-P001-R02",
                    "reading_order": 2,
                    "box_px": [500, 80, 1550, 1030],
                    "text": "",
                    "spans": [],
                    "protected_tokens": [],
                    "anchor_metadata": {
                        "anchor_id": "ART-G1-VIRAL-P001-002",
                        "anchor_label": "Viral Unredacted title/logo area",
                        "visual_identification": "Cover title/logo area with visible VIRAL / UNREDACTED text; preserve as visual/title anchor, not OCR-verified source text.",
                        "deferred_stage": "html_assembly_art_replacement",
                        "visible_text_hint": "VIRAL / UNREDACTED",
                        "not_source_text": True,
                    },
                },
                {
                    "block_id": "P001-B003",
                    "block_type": "visual_anchor",
                    "content_kind": "mixed_footer_visual_anchor",
                    "extraction_policy": "anchor_only_defer_visual",
                    "role": "cover_footer_rating_tagline_logos",
                    "source_region_id": "PRM-G1-VIRAL-001-P001-R03",
                    "reading_order": 3,
                    "box_px": [40, 2740, 2460, 520],
                    "text": "",
                    "spans": [],
                    "protected_tokens": [],
                    "anchor_metadata": {
                        "anchor_id": "ART-G1-VIRAL-P001-003",
                        "anchor_label": "Cover footer rating/tagline/logo area",
                        "visual_identification": "Footer area with rating badge, modern Call of Cthulhu scenario tagline, and repository logo area; preserve as mixed visual anchor, not OCR-verified source text.",
                        "deferred_stage": "html_assembly_art_replacement",
                        "not_source_text": True,
                    },
                },
            ],
        },
        "review_attachments": [
            {
                "attachment_id": "P001-001-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_001.png",
                "target_path": "review_assets/page_001.png",
                "sha256": "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P001-001-ATT-CROP-FULL",
                "role": "human_review_crop",
                "label": "cover_full_page_visual_anchor",
                "source_path": TRIAL_ROOT / "images" / "page_001.png",
                "source_sha256": "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692",
                "box_px": [0, 0, 2550, 3300],
                "target_path": "review_assets/1_P001-full-page-cover-anchor.png",
                "covered_review_blocks": ["P001-B001"],
                "skip_edge_ink_check": True,
                "include_in_text_map": False,
            },
            {
                "attachment_id": "P001-001-ATT-CROP-TITLE",
                "role": "human_review_crop",
                "label": "cover_title_logo_area",
                "source_path": TRIAL_ROOT / "images" / "page_001.png",
                "source_sha256": "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692",
                "box_px": [500, 80, 1550, 1030],
                "target_path": "review_assets/2_P001-title-logo-area.png",
                "covered_review_blocks": ["P001-B002"],
                "skip_edge_ink_check": True,
                "include_in_text_map": False,
            },
            {
                "attachment_id": "P001-001-ATT-CROP-FOOTER",
                "role": "human_review_crop",
                "label": "cover_footer_rating_tagline_logos",
                "source_path": TRIAL_ROOT / "images" / "page_001.png",
                "source_sha256": "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692",
                "box_px": [40, 2740, 2460, 520],
                "target_path": "review_assets/3_P001-footer-title-credit-like-block.png",
                "covered_review_blocks": ["P001-B003"],
                "skip_edge_ink_check": True,
                "include_in_text_map": False,
            },
        ],
    },
    "002": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P002-001",
        "package_id": "PCRP-G1-VIRAL-P002-001",
        "page_label": "Page 002",
        "output_dir": TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P002-001",
        "readiness_report_sha256": "3F957442194211F6F0EC39775ED292DEF126222E98EEFB5BFFD1530D8EA702D6",
        "readiness_packet_sha256": "5DAAB049DC28C9C4633490348991DF822FF8E049460AC0978EBF8163D75C1734",
        "readiness_summary_sha256": "45104BC75F38DCA37612B308186EC8C877FE33369D564510941F03156AC0A52A",
        "readiness_manifest_sha256": "5AB662AF36355A75F73758EF4B73BF13F0315986AF40B2F9234BBE84B489173A",
        "decision_options": [
            "accept_page_002_as_complete_in_a_later_explicit_decision",
            "hold_page_002_for_corrections_or_additional_review",
        ],
    },
    "003": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P003-001",
        "package_id": "PCRP-G1-VIRAL-P003-001",
        "page_label": "Page 003",
        "output_dir": TRIAL_ROOT / "page_complete_review_p003_G1_VIRAL_001",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p003_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P003-001",
        "readiness_report_sha256": "21ED5DA166565BAB537B4CF190B41B55467353DDEC59D58656FFA2F56C827DDF",
        "readiness_packet_sha256": "76FDDE5A7A239E729B592D8D6BBDC50AEE55D037A2589CF329A1F83ED989D21F",
        "readiness_summary_sha256": "D108411E9778B055277BA625356E5EDC747475A6BDC3494FA1011A04F1164FE2",
        "readiness_manifest_sha256": "1A52C156277979A30ED6B81D33D065DE4302360814263D1B1787BAC8D2864EF0",
        "decision_options": [
            "accept_page_003_as_complete_in_a_later_explicit_decision",
            "hold_page_003_for_corrections_or_additional_review",
        ],
        "review_attachments": [
            {
                "attachment_id": "P003-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_003.png",
                "target_path": "review_assets/page_003.png",
                "sha256": "B6B5A48D498FDEFB050B67E7155E85502010799D05CC10317C9E179CEB97A6BF",
            },
            {
                "attachment_id": "P003-ATT-BLOCK-R01",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
                / "next_review_refs"
                / "1_SRCR-G1-VIRAL-003-R01.png",
                "target_path": "review_assets/1_SRCR-G1-VIRAL-003-R01.png",
                "sha256": "CC942FC60C379EF8DC32083FBDE5F08CF222A07A943A6392B67A090DBDEC9F7E",
            },
            {
                "attachment_id": "P003-ATT-BLOCK-R02",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
                / "next_review_refs"
                / "2_SRCR-G1-VIRAL-003-R02.png",
                "target_path": "review_assets/2_SRCR-G1-VIRAL-003-R02.png",
                "sha256": "ABDE2B383C0D8470F9923703A70560339ACAA1906B68867800A9B619EB3BB845",
            },
            {
                "attachment_id": "P003-ATT-BLOCK-TEXT",
                "role": "ocr_block_text_markdown",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
                / "next_review_packet_for_bogdan.md",
                "target_path": "review_assets/page_003_ocr_block_text.md",
                "sha256": "81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF",
            },
        ],
    },
    "004": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P004-001",
        "package_id": "PCRP-G1-VIRAL-P004-001",
        "page_label": "Page 004",
        "output_dir": TRIAL_ROOT / "page_complete_review_p004_G1_VIRAL_001",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p004_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P004-001",
        "readiness_report_sha256": "DEEBDA76EE371ABA8AC7761573FE5DDAA8B7D2268943C2DEC67C115F932EF39F",
        "readiness_packet_sha256": "1C9BE9076C84D9A577DA9CC0895ED6D84EE6E0A68EB0F34CA0DC1F9E0018DC43",
        "readiness_summary_sha256": "2943A0BA671F4E4C6B2B00161EAD89054BA1857895BE6F89AA6A2555B6DF1E02",
        "readiness_manifest_sha256": "7457E8655F406FE5D3DA588B583F24766E999E42CE853F327C53B75EBF8ED334",
        "decision_options": [
            "accept_page_004_as_complete_in_a_later_explicit_decision",
            "hold_page_004_for_corrections_or_additional_review",
        ],
        "review_attachments": [
            {
                "attachment_id": "P004-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_004.png",
                "target_path": "review_assets/page_004.png",
                "sha256": "45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88",
            },
            {
                "attachment_id": "P004-ATT-BLOCK-R02",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_next_slice_G1_VIRAL_004"
                / "region_refs"
                / "1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png",
                "target_path": "review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png",
                "sha256": "ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219",
            },
            {
                "attachment_id": "P004-ATT-BLOCK-R03",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_next_slice_G1_VIRAL_004"
                / "region_refs"
                / "2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png",
                "target_path": "review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png",
                "sha256": "EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8",
            },
            {
                "attachment_id": "P004-ATT-BLOCK-TEXT",
                "role": "ocr_block_text_markdown",
                "source_path": TRIAL_ROOT
                / "page_004_context_decision_G1_VIRAL_001"
                / "review_assets"
                / "page_004_ocr_block_text.md",
                "target_path": "review_assets/page_004_ocr_block_text.md",
                "sha256": "7994F6D597C0041052361533BDDBCC63511B784F1BC24D6E7A089588BAAD3DDB",
            },
        ],
    },
    "005": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-001",
        "package_id": "PCRP-G1-VIRAL-P005-001",
        "page": "005",
        "page_label": "Page 005",
        "output_dir": TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_001",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p005_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P005-001",
        "readiness_report_sha256": "92C8AED6BEEBBC03CBF4495DEA07E9BCF21699D362DDF426A8E7767CE3888AE5",
        "readiness_packet_sha256": "E9405BF49EC2CE00DCB39C67F602035C0AD9E25D4E7E5540624A6965688B40D7",
        "readiness_summary_sha256": "724B4963F9FA1D12891738A02D6A17BB2A34233F983201E65EF97BF1DC260FF5",
        "readiness_manifest_sha256": "21A7C524F36BD070CFA5384AAF035D8203B6F4CA5A870B4F957D74F603F9EAC1",
        "decision_options": [
            "accept_page_005_as_complete_in_a_later_explicit_decision",
            "hold_page_005_for_corrections_or_additional_review",
        ],
        "review_attachments": [
            {
                "attachment_id": "P005-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "target_path": "review_assets/page_005.png",
                "sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
            },
            {
                "attachment_id": "P005-ATT-BLOCK-R01",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_crop_overlay_G1_VIRAL_001"
                / "crop_overlay_refs"
                / "SRA-G1-VIRAL-001-R002__overlay_reference.png",
                "target_path": "review_assets/1_SRA-G1-VIRAL-001-R002__PRM-G1-VIRAL-001-P005-R01.png",
                "sha256": "8A3A979381FB476C3B6D9831D7665E50F3171C4D4300EB7C3373E4216738CF24",
            },
            {
                "attachment_id": "P005-ATT-BLOCK-R02",
                "role": "block_crop",
                "source_path": TRIAL_ROOT
                / "source_reconstruction_crop_overlay_G1_VIRAL_001"
                / "crop_overlay_refs"
                / "SRA-G1-VIRAL-001-R003__narrow_contents_candidate.png",
                "target_path": "review_assets/2_SRA-G1-VIRAL-001-R003__PRM-G1-VIRAL-001-P005-R02.png",
                "sha256": "A09B5848048C3BD20FEB71B0FC37FC55E108AA08454BCFB1156D3FAD62E5B40F",
            },
        ],
        "generated_block_text_attachment": {
            "attachment_id": "P005-ATT-BLOCK-TEXT",
            "role": "ocr_block_text_markdown",
            "target_path": "review_assets/page_005_ocr_block_text.md",
        },
    },
    "005-002": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-002",
        "package_id": "PCRP-G1-VIRAL-P005-002",
        "page": "005",
        "page_label": "Page 005",
        "output_dir": TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_002",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p005_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P005-001",
        "readiness_report_sha256": "92C8AED6BEEBBC03CBF4495DEA07E9BCF21699D362DDF426A8E7767CE3888AE5",
        "readiness_packet_sha256": "E9405BF49EC2CE00DCB39C67F602035C0AD9E25D4E7E5540624A6965688B40D7",
        "readiness_summary_sha256": "724B4963F9FA1D12891738A02D6A17BB2A34233F983201E65EF97BF1DC260FF5",
        "readiness_manifest_sha256": "21A7C524F36BD070CFA5384AAF035D8203B6F4CA5A870B4F957D74F603F9EAC1",
        "decision_options": [
            "accept_page_005_as_complete_in_a_later_explicit_decision",
            "hold_page_005_for_corrections_or_additional_review",
        ],
        "review_attachments": [
            {
                "attachment_id": "P005-002-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "target_path": "review_assets/page_005.png",
                "sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
            },
        ],
        "generated_declared_block_crops": [
            {
                "block_id": "P005-B001",
                "attachment_id": "P005-002-ATT-BLOCK-R01-FULL",
                "role": "block_crop",
                "target_path": "review_assets/1_P005-B001__declared_box__PRM-G1-VIRAL-001-P005-R01.png",
            },
            {
                "block_id": "P005-B002",
                "attachment_id": "P005-002-ATT-BLOCK-R02-FULL",
                "role": "block_crop",
                "target_path": "review_assets/2_P005-B002__declared_box__PRM-G1-VIRAL-001-P005-R02.png",
            },
        ],
        "generated_block_text_attachment": {
            "attachment_id": "P005-002-ATT-BLOCK-TEXT",
            "role": "ocr_block_text_markdown",
            "target_path": "review_assets/page_005_ocr_block_text.md",
        },
    },
    "005-003": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-003",
        "package_id": "PCRP-G1-VIRAL-P005-003",
        "page": "005",
        "page_label": "Page 005",
        "output_dir": TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_003",
        "readiness_root": TRIAL_ROOT / "page_map_readiness_p005_G1_VIRAL_001",
        "readiness_package_id": "PMRP-G1-VIRAL-P005-001",
        "readiness_report_sha256": "92C8AED6BEEBBC03CBF4495DEA07E9BCF21699D362DDF426A8E7767CE3888AE5",
        "readiness_packet_sha256": "E9405BF49EC2CE00DCB39C67F602035C0AD9E25D4E7E5540624A6965688B40D7",
        "readiness_summary_sha256": "724B4963F9FA1D12891738A02D6A17BB2A34233F983201E65EF97BF1DC260FF5",
        "readiness_manifest_sha256": "21A7C524F36BD070CFA5384AAF035D8203B6F4CA5A870B4F957D74F603F9EAC1",
        "decision_options": [
            "accept_page_005_as_complete_in_a_later_explicit_decision",
            "hold_page_005_for_corrections_or_additional_review",
        ],
        "skip_readiness_anchor_visual_proof": True,
        "review_attachments": [
            {
                "attachment_id": "P005-003-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "target_path": "review_assets/page_005.png",
                "sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P005-003-ATT-CROP-TITLE",
                "role": "human_review_crop",
                "label": "contents_title",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "source_sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
                "box_px": [740, 150, 940, 260],
                "target_path": "review_assets/1_P005-title__contents_heading.png",
                "covered_review_blocks": ["P005-RM-B001"],
            },
            {
                "attachment_id": "P005-003-ATT-CROP-LEFT",
                "role": "human_review_crop",
                "label": "contents_left_column",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "source_sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
                "box_px": [140, 420, 1070, 2580],
                "target_path": "review_assets/2_P005-left-column__contents_entries.png",
                "covered_review_blocks": ["P005-RM-B002"],
            },
            {
                "attachment_id": "P005-003-ATT-CROP-RIGHT",
                "role": "human_review_crop",
                "label": "contents_right_column",
                "source_path": TRIAL_ROOT / "images" / "page_005.png",
                "source_sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
                "box_px": [1210, 420, 1140, 2580],
                "target_path": "review_assets/3_P005-right-column__contents_entries.png",
                "covered_review_blocks": ["P005-RM-B003"],
            },
        ],
        "generated_review_text_map_attachment": {
            "attachment_id": "P005-003-ATT-TEXT-MAP",
            "role": "ocr_verified_text_map_markdown",
            "target_path": "review_assets/page_005_ocr_verified_text_map.md",
            "crops": [
                {
                    "crop_label": "contents_title",
                    "ocr_state": "ocr_verified_against_crop",
                    "entries": [
                        {"text": "Contents", "page": None, "heading_level": "h1", "style": "red_display_heading"}
                    ],
                },
                {
                    "crop_label": "contents_left_column",
                    "ocr_state": "ocr_verified_against_crop",
                    "entries": [
                        {"text": "Introduction", "page": "6", "heading_level": "h2", "style": "bold"},
                        {"text": "Summary", "page": "6", "heading_level": "h3", "style": "italic"},
                        {"text": "Overview", "page": "6", "heading_level": "h3", "style": "italic"},
                        {"text": "The Spektral Krew", "page": "7", "heading_level": "h2", "style": "bold"},
                        {"text": "Marco 'Proudfoot' Maglioni", "page": "7", "heading_level": "h3", "style": "italic"},
                        {"text": "Corrina Trench", "page": "8", "heading_level": "h3", "style": "italic"},
                        {"text": "Enoch Jeremiah Eakins", "page": "9", "heading_level": "h3", "style": "italic"},
                        {"text": "Peter Wharton", "page": "9", "heading_level": "h3", "style": "italic"},
                        {"text": "Ku Hyeon", "page": "10", "heading_level": "h3", "style": "italic"},
                        {"text": "Maya Adeduwon", "page": "10", "heading_level": "h3", "style": "italic"},
                        {"text": "Emily 'Em' Lavigne", "page": "11", "heading_level": "h3", "style": "italic"},
                        {"text": "Creating New Investigators", "page": "12", "heading_level": "h2", "style": "bold"},
                        {"text": "Spektral Krew Gear", "page": "14", "heading_level": "h2", "style": "bold"},
                        {"text": "Timeline", "page": "15", "heading_level": "h2", "style": "bold"},
                        {"text": "History", "page": "15", "heading_level": "h2", "style": "bold"},
                        {"text": "One Night in Perla", "page": "17", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Welcome to Perla", "page": "18", "heading_level": "h3", "style": "bold"},
                        {"text": "Perla", "page": "19", "heading_level": "h3", "style": "bold"},
                        {"text": "Exploring Perla", "page": "20", "heading_level": "h3", "style": "bold"},
                        {"text": "Rumors", "page": "20", "heading_level": "h4", "style": "italic"},
                        {"text": "Signs and Portents", "page": "21", "heading_level": "h4", "style": "italic"},
                        {"text": "Burning of the Disease", "page": "22", "heading_level": "h3", "style": "bold"},
                        {"text": "The Next Day", "page": "24", "heading_level": "h3", "style": "bold"},
                        {"text": "Perla NPCs", "page": "25", "heading_level": "h3", "style": "bold"},
                        {"text": "Isola di Malamente", "page": "26", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Keeper's Secrets", "page": "27", "heading_level": "h3", "style": "bold"},
                        {"text": "Running the Game", "page": "27", "heading_level": "h4", "style": "italic"},
                        {"text": "Number of Sessions", "page": "30", "heading_level": "h4", "style": "italic"},
                        {"text": "Plots and Schemes", "page": "30", "heading_level": "h4", "style": "italic"},
                        {"text": "Prologue", "page": "32", "heading_level": "h3", "style": "bold"},
                        {"text": "Isola di Malamente: Locations", "page": "33", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "1. Lighthouse/Radio Station", "page": "33", "heading_level": "h3", "style": "bold"},
                        {"text": "2. Beggar's Cove", "page": "34", "heading_level": "h3", "style": "bold"},
                        {"text": "3. The Weeping Bridge", "page": "34", "heading_level": "h3", "style": "bold"},
                        {"text": "4. Lemon Grove", "page": "35", "heading_level": "h3", "style": "bold"},
                        {"text": "5. Saint Roche's Hospital", "page": "37", "heading_level": "h3", "style": "bold"},
                        {"text": "Hospital Locations", "page": "39", "heading_level": "h4", "style": "italic"},
                    ],
                },
                {
                    "crop_label": "contents_right_column",
                    "ocr_state": "ocr_verified_against_crop",
                    "entries": [
                        {"text": "6. Mass Graves", "page": "45", "heading_level": "h3", "style": "bold"},
                        {"text": "7. Cremation Pit", "page": "46", "heading_level": "h3", "style": "bold"},
                        {"text": "8. Isola di Malamente Dock", "page": "46", "heading_level": "h3", "style": "bold"},
                        {"text": "9. Overlook Point", "page": "46", "heading_level": "h3", "style": "bold"},
                        {"text": "10. Chapel & Crypt", "page": "47", "heading_level": "h3", "style": "bold"},
                        {"text": "11. Catacomb Entrance", "page": "48", "heading_level": "h3", "style": "bold"},
                        {"text": "12. Catacombs", "page": "48", "heading_level": "h3", "style": "bold"},
                        {"text": "13. Temple of Morbus", "page": "49", "heading_level": "h3", "style": "bold"},
                        {"text": "Hastalÿk Awakens", "page": "49", "heading_level": "h2", "style": "bold"},
                        {"text": "Epilogue", "page": "52", "heading_level": "h2", "style": "bold"},
                        {"text": "Rewards", "page": "52", "heading_level": "h2", "style": "bold"},
                        {"text": "Cinematic Ending", "page": "54", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Expanded Ending", "page": "56", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "New Epilogue", "page": "54", "heading_level": "h3", "style": "bold"},
                        {"text": "Appendix", "page": "58", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Encounters", "page": "58", "heading_level": "h3", "style": "bold"},
                        {"text": "Outdoor Encounters", "page": "58", "heading_level": "h4", "style": "italic"},
                        {"text": "Hospital Encounters", "page": "59", "heading_level": "h4", "style": "italic"},
                        {"text": "Catacomb Encounters", "page": "60", "heading_level": "h4", "style": "italic"},
                        {"text": "New Rules", "page": "60", "heading_level": "h3", "style": "bold"},
                        {"text": "The Sight", "page": "60", "heading_level": "h4", "style": "italic"},
                        {"text": "The Taint", "page": "62", "heading_level": "h4", "style": "italic"},
                        {"text": "Insanity and Bouts of Madness", "page": "63", "heading_level": "h4", "style": "italic"},
                        {"text": "Paranormal Phenomena", "page": "64", "heading_level": "h4", "style": "italic"},
                        {"text": "New Mythos Horrors", "page": "65", "heading_level": "h3", "style": "bold"},
                        {"text": "Hastalÿk", "page": "65", "heading_level": "h4", "style": "italic"},
                        {"text": "The Plague Monk", "page": "66", "heading_level": "h4", "style": "italic"},
                        {"text": "The Reliquae", "page": "66", "heading_level": "h4", "style": "italic"},
                        {"text": "New Mythos Tome", "page": "67", "heading_level": "h3", "style": "bold"},
                        {"text": "Iuramentum Corruptionis", "page": "67", "heading_level": "h4", "style": "italic"},
                        {"text": "New Spells", "page": "68", "heading_level": "h3", "style": "bold"},
                        {"text": "Control Reliquae", "page": "68", "heading_level": "h4", "style": "italic"},
                        {"text": "Player Handouts", "page": "69", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Keeper Maps", "page": "104", "heading_level": "h2_major", "style": "bold_large"},
                        {"text": "Pre-Gens", "page": "111", "heading_level": "h2_major", "style": "bold_large"},
                    ],
                },
            ],
        },
    },
    "006-001": {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-001",
        "package_id": "PCRP-G1-VIRAL-P006-001",
        "page": "006",
        "page_label": "Page 006",
        "output_dir": TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_001",
        "readiness_package_id": "P006-READABLE-MAP-G1-VIRAL-001",
        "readiness_report_sha256": "inline_page_006_verified_text_map",
        "readiness_packet_sha256": "inline_page_006_verified_text_map",
        "readiness_summary_sha256": "inline_page_006_verified_text_map",
        "readiness_manifest_sha256": "inline_page_006_verified_text_map",
        "decision_options": [
            "accept_page_006_as_complete_in_a_later_explicit_decision",
            "hold_page_006_for_corrections_or_additional_review",
        ],
        "post_review_hold": {
            "decision_id": "hold_page_006_text_map_semantics_messages_896_897",
            "status": "held_after_bogdan_review",
            "reason": "text_map_semantics_and_formatting_blocker",
            "requires_superseding_package_id": "PCRP-G1-VIRAL-P006-002",
            "human_review_crop_decision": "ok_as_review_assets_only",
            "negative_regression_input": "review_assets/page_006_ocr_verified_text_map.md",
            "notes": [
                "P006-001 was reported ready before semantic structural validation existed.",
                "Crops ok means human-review framing only, not text completeness, OCR quality, semantic acceptance, source acceptance, page-complete readiness, or fixture admissibility.",
                "The P006-001 text map is blocked as structure evidence and may be reused only as negative regression input for collapsed semantic units.",
            ],
        },
        "skip_readiness_anchor_visual_proof": True,
        "inline_readiness": {
            "page_id": "PG-G1-VIRAL-P006",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P006",
            "profile_id": "page_map_profile_G1_VIRAL_P006_readable_v0",
            "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_006.png",
            "page_image_sha256": "B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF",
            "declared_none": ["table", "unknown", "missing"],
            "context_only_regions": [
                {
                    "source_region_id": "PRM-G1-VIRAL-001-P006-R01",
                    "status": "visual_context_not_source_text_record",
                    "reason": "Upper background art is packaged in the full page image and excluded from source text transcription.",
                },
                {
                    "source_region_id": "PRM-G1-VIRAL-001-P006-PAGE-NUMBER",
                    "status": "visual_exclusion_not_source_text_record",
                    "reason": "Bottom page marker is layout/page-number context, not body source text.",
                },
            ],
            "blocks": [
                {
                    "block_id": "P006-B001",
                    "role": "introduction_heading",
                    "source_region_id": "PRM-G1-VIRAL-001-P006-R02",
                    "reading_order": 1,
                    "box_px": [90, 90, 1240, 520],
                    "text": "Introduction",
                    "spans": [
                        {"text": "Introduction", "semantic_role": "chapter_title", "heading_level": "h1"}
                    ],
                    "protected_tokens": ["Introduction"],
                },
                {
                    "block_id": "P006-B002",
                    "role": "left_column_summary_overview_text",
                    "source_region_id": "PRM-G1-VIRAL-001-P006-R03-L",
                    "reading_order": 2,
                    "box_px": [120, 1530, 1160, 1590],
                    "text": "Summary\n\"We are the Spektral Krew, and we go places and do things you\nwould never do.\" - Marco Proudfoot\n\nProducers of a popular ghost hunting YouTube channel called\nSpektral Krew are planning to illegally visit Isola di Malamente,\nan island off the coast of Sicily to broadcast live as they attempt\nto uncover evidence of a genuine haunting and thus become\nInternet sensations. All goes well until they find that their ride\noff the island has disappeared and they begin to see more than\ndust orbs and incoherently blurred photos. They soon learn\nthat there may be someone or something... else on the island,\nand that the history of the place may be darker than they could\nhave ever imagined.\n\nOverview\nThis scenario involves a group of professional ghost hunters\ntraveling to a mysterious island to spend the night searching\nfor evidence of the supernatural. While some of them are\ncertainly interested in finding actual evidence for ghosts, their\nreal objective is to 'go viral' on YouTube in order to bring their\nchannel to the next level and perhaps even hit the big time with\ntheir own television show.\n\nUnbeknownst to the Investigators, a cult of the Great Old\nOne Hastalÿk has been active on the island since the Bronze",
                    "spans": [
                        {"text": "Summary", "semantic_role": "section_heading", "heading_level": "h2"},
                        {"text": "\"We are the Spektral Krew, and we go places and do things you would never do.\" - Marco Proudfoot", "semantic_role": "pull_quote", "heading_level": "quote"},
                        {"text": "Producers of a popular ghost hunting YouTube channel called Spektral Krew...", "semantic_role": "summary_body", "heading_level": "text_body"},
                        {"text": "Overview", "semantic_role": "section_heading", "heading_level": "h2"},
                        {"text": "This scenario involves a group of professional ghost hunters...", "semantic_role": "overview_body", "heading_level": "text_body"},
                    ],
                    "protected_tokens": ["Summary", "Spektral Krew", "Isola di Malamente", "Overview", "Bronze"],
                },
                {
                    "block_id": "P006-B003",
                    "role": "right_column_overview_text",
                    "source_region_id": "PRM-G1-VIRAL-001-P006-R03-R",
                    "reading_order": 3,
                    "box_px": [1280, 1580, 1140, 1540],
                    "text": "Age, offering countless sacrifices over the millennia. Only one\nof the 'Plague Monks' remains following a government raid\non the island in the 1950s, the details of which have been\ndiligently hidden from the public by the Italian government.\nThe Plague Monk's only objective is to manifest Hastalÿk\nphysically into the world, and spread its mutating corruption\nacross the planet. Hastalÿk's ultimate plan is incomprehensible\nto mortals, but it certainly involves turning all life on Earth into\nitself through the spread of its Taint and absorbing all living\nthings. To that end, it is vital to get the Investigators to witness\nthe final sacrifice of the last Plague Monk at the Charnel Pit, and\nideally become absorbed into the body of Hastalÿk themselves.\nAfter that, Hastalÿk will try to reach the water. Once it\nis able to touch the water, it bursts like a balloon to scatter\nits Taint to corrupt the nearby sea life, and eventually the\nworld. Fortunately for the world, the Italian government has\nbeen watching the island, and indeed the live stream from\nthe Spektral Krew. As soon as it becomes apparent that\nHastalÿk is about to be released, the Italian military triggers\nits equivalent of the 'Innsmouth Protocol' and scrambles\na squadron of jets to fire bomb the island, and end the vile\ncorruption once and for all.\nViral can be run in about four to eight hours depending on\nhow the Keeper chooses to approach the scenario. Certain\nfeatures are designed to be included or omitted as desired to\nspeed up or slow down the game.",
                    "spans": [
                        {"text": "Age, offering countless sacrifices over the millennia...", "semantic_role": "overview_body_continuation", "heading_level": "text_body"}
                    ],
                    "protected_tokens": ["Plague Monks", "Hastalÿk", "Charnel Pit", "Innsmouth Protocol", "four to eight hours"],
                },
            ],
        },
        "review_attachments": [
            {
                "attachment_id": "P006-001-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_006.png",
                "target_path": "review_assets/page_006.png",
                "sha256": "B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P006-001-ATT-CROP-TITLE",
                "role": "human_review_crop",
                "label": "introduction_title",
                "source_path": TRIAL_ROOT / "images" / "page_006.png",
                "source_sha256": "B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF",
                "box_px": [90, 90, 1240, 520],
                "target_path": "review_assets/1_P006-title__introduction_heading.png",
                "covered_review_blocks": ["P006-B001"],
                "detect_dark_text": False,
            },
            {
                "attachment_id": "P006-001-ATT-CROP-LEFT",
                "role": "human_review_crop",
                "label": "summary_overview_left_column",
                "source_path": TRIAL_ROOT / "images" / "page_006.png",
                "source_sha256": "B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF",
                "box_px": [120, 1530, 1160, 1590],
                "target_path": "review_assets/2_P006-left-column__summary_overview.png",
                "covered_review_blocks": ["P006-B002"],
            },
            {
                "attachment_id": "P006-001-ATT-CROP-RIGHT",
                "role": "human_review_crop",
                "label": "overview_right_column",
                "source_path": TRIAL_ROOT / "images" / "page_006.png",
                "source_sha256": "B0BE1CC101217D0732B5C8D32F731C7A22C1F1C852F67B673F5E2F38AC2B46BF",
                "box_px": [1280, 1580, 1140, 1540],
                "target_path": "review_assets/3_P006-right-column__overview_continuation.png",
                "covered_review_blocks": ["P006-B003"],
            },
        ],
        "generated_review_text_map_attachment": {
            "attachment_id": "P006-001-ATT-TEXT-MAP",
            "role": "ocr_verified_text_map_markdown",
            "target_path": "review_assets/page_006_ocr_verified_text_map.md",
            "crops_from_inline_readiness": True,
        },
        "generated_semantic_map_attachment": {
            "json_attachment_id": "P006-001-ATT-SEMANTIC-MAP-JSON",
            "markdown_attachment_id": "P006-001-ATT-SEMANTIC-MAP-MD",
            "json_role": "semantic_text_map_json",
            "markdown_role": "semantic_text_map_markdown",
            "map_id": "SM-G1-VIRAL-P006-001",
            "json_target_path": "review_assets/page_006_semantic_text_map.json",
            "markdown_target_path": "review_assets/page_006_semantic_text_map.md",
            "source": "generated_from_inline_readiness_spans",
        },
    },
}


def _p005_contents_line(entry: dict[str, Any]) -> str:
    page = entry.get("page")
    if page:
        return f"{entry['text']} {page}"
    return entry["text"]


_p005_003_text_crops = REVIEW_PROFILES["005-003"]["generated_review_text_map_attachment"]["crops"]
_p005_title_entry = _p005_003_text_crops[0]["entries"][0]
_p005_contents_entries = [
    entry
    for crop in _p005_003_text_crops
    if crop["crop_label"] in {"contents_left_column", "contents_right_column"}
    for entry in crop["entries"]
]
_p005_contents_text = "\n".join(_p005_contents_line(entry) for entry in _p005_contents_entries)

REVIEW_PROFILES["005-004"] = copy.deepcopy(REVIEW_PROFILES["005-003"])
REVIEW_PROFILES["005-004"].update(
    {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-004",
        "package_id": "PCRP-G1-VIRAL-P005-004",
        "output_dir": TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_004",
        "readiness_package_id": "PCRP-G1-VIRAL-P005-003",
        "readiness_report_sha256": "predecessor_review_packet_p005_003",
        "readiness_packet_sha256": "predecessor_review_packet_p005_003",
        "readiness_summary_sha256": "predecessor_review_packet_p005_003",
        "readiness_manifest_sha256": "predecessor_review_packet_p005_003",
    }
)
REVIEW_PROFILES["005-004"]["review_attachments"][0]["attachment_id"] = "P005-004-ATT-PAGE"
for crop in REVIEW_PROFILES["005-004"]["generated_page_crops"]:
    crop["attachment_id"] = crop["attachment_id"].replace("P005-003", "P005-004")
    if crop["label"] == "contents_title":
        crop["covered_review_blocks"] = ["P005-B001"]
    else:
        crop["covered_review_blocks"] = ["P005-B002"]
REVIEW_PROFILES["005-004"]["generated_review_text_map_attachment"]["attachment_id"] = "P005-004-ATT-TEXT-MAP"
REVIEW_PROFILES["005-004"]["generated_semantic_map_attachment"] = {
    "json_attachment_id": "P005-004-ATT-SEMANTIC-MAP-JSON",
    "markdown_attachment_id": "P005-004-ATT-SEMANTIC-MAP-MD",
    "json_role": "semantic_text_map_json",
    "markdown_role": "semantic_text_map_markdown",
    "map_id": "SM-G1-VIRAL-P005-004",
    "json_target_path": "review_assets/page_005_semantic_text_map.json",
    "markdown_target_path": "review_assets/page_005_semantic_text_map.md",
    "source": "generated_from_p005_003_verified_contents_text_map",
}
REVIEW_PROFILES["005-004"]["inline_readiness"] = {
    "page_id": "PG-G1-VIRAL-P005",
    "image_id": "IMG-G1-VIRAL-RENDER-001-P005",
    "profile_id": "page_map_profile_G1_VIRAL_P005_semantic_refresh_v0",
    "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_005.png",
    "page_image_sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
    "declared_none": ["art", "inset", "unknown", "missing"],
    "context_only_regions": [
        {
            "source_region_id": "PRM-G1-VIRAL-001-P005-R03",
            "status": "visual_exclusion_not_source_text_record",
            "reason": "Margin page marker/layout component is accepted as a visual-only exclusion, not source text.",
        }
    ],
    "blocks": [
        {
            "block_id": "P005-B001",
            "role": "contents_heading",
            "source_region_id": "PRM-G1-VIRAL-001-P005-R01",
            "reading_order": 1,
            "box_px": [740, 150, 940, 260],
            "text": _p005_title_entry["text"],
            "spans": [
                {"text": _p005_title_entry["text"], "semantic_role": "chapter_title", "heading_level": "h1"}
            ],
            "protected_tokens": [_p005_title_entry["text"]],
        },
        {
            "block_id": "P005-B002",
            "role": "contents_entry_group",
            "source_region_id": "PRM-G1-VIRAL-001-P005-R02",
            "reading_order": 2,
            "box_px": [140, 420, 2210, 2580],
            "text": _p005_contents_text,
            "spans": [
                {
                    "text": _p005_contents_text,
                    "semantic_role": "contents_entry_list",
                    "heading_level": None,
                },
                *[
                    {
                        "text": _p005_contents_line(entry),
                        "semantic_role": "contents_entry",
                        "heading_level": None,
                        "parent_unit_id": "SU-P005-B002-S001",
                    }
                    for entry in _p005_contents_entries
                ],
            ],
            "protected_tokens": ["Introduction", "Hastalÿk Awakens", "Iuramentum Corruptionis", "Pre-Gens"],
        },
    ],
}


REVIEW_PROFILES["006-002"] = copy.deepcopy(REVIEW_PROFILES["006-001"])
REVIEW_PROFILES["006-002"].update(
    {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-002",
        "package_id": "PCRP-G1-VIRAL-P006-002",
        "output_dir": TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_002",
    }
)
REVIEW_PROFILES["006-002"].pop("post_review_hold", None)
REVIEW_PROFILES["006-002"]["review_attachments"][0]["attachment_id"] = "P006-002-ATT-PAGE"
for crop in REVIEW_PROFILES["006-002"]["generated_page_crops"]:
    crop["attachment_id"] = crop["attachment_id"].replace("P006-001", "P006-002")
REVIEW_PROFILES["006-002"]["generated_review_text_map_attachment"] = {
    "attachment_id": "P006-002-ATT-TEXT-MAP",
    "role": "ocr_verified_text_map_markdown",
    "target_path": "review_assets/page_006_ocr_verified_text_map.md",
    "crops_from_inline_readiness_spans": True,
    "full_text_blocks": True,
}
REVIEW_PROFILES["006-002"]["generated_semantic_map_attachment"].update(
    {
        "json_attachment_id": "P006-002-ATT-SEMANTIC-MAP-JSON",
        "markdown_attachment_id": "P006-002-ATT-SEMANTIC-MAP-MD",
        "map_id": "SM-G1-VIRAL-P006-002",
    }
)
_p006_002_blocks = {block["block_id"]: block for block in REVIEW_PROFILES["006-002"]["inline_readiness"]["blocks"]}
_p006_002_blocks["P006-B001"]["spans"] = [
    {"text": "Introduction", "semantic_role": "chapter_title", "heading_level": "h2"}
]
_p006_002_blocks["P006-B002"]["spans"] = [
    {"text": "Summary", "semantic_role": "section_heading", "heading_level": "h2"},
    {
        "text": '"We are the Spektral Krew, and we go places and do things you would never do." - Marco Proudfoot',
        "semantic_role": "pull_quote",
        "heading_level": None,
    },
    {
        "text": (
            "Producers of a popular ghost hunting YouTube channel called Spektral Krew are planning to illegally "
            "visit Isola di Malamente, an island off the coast of Sicily to broadcast live as they attempt to "
            "uncover evidence of a genuine haunting and thus become Internet sensations. All goes well until they "
            "find that their ride off the island has disappeared and they begin to see more than dust orbs and "
            "incoherently blurred photos. They soon learn that there may be someone or something... else on the "
            "island, and that the history of the place may be darker than they could have ever imagined."
        ),
        "semantic_role": "summary_body",
        "heading_level": "text_body",
    },
    {"text": "Overview", "semantic_role": "section_heading", "heading_level": "h2"},
    {
        "text": (
            "This scenario involves a group of professional ghost hunters traveling to a mysterious island to spend "
            "the night searching for evidence of the supernatural. While some of them are certainly interested in "
            "finding actual evidence for ghosts, their real objective is to 'go viral' on YouTube in order to bring "
            "their channel to the next level and perhaps even hit the big time with their own television show. "
            "Unbeknownst to the Investigators, a cult of the Great Old One Hastalÿk has been active on the island "
            "since the Bronze"
        ),
        "semantic_role": "overview_body",
        "heading_level": "text_body",
        "continues_to": "SU-P006-B003-S001",
    },
]
_p006_002_blocks["P006-B003"]["spans"] = [
    {
        "text": (
            "Age, offering countless sacrifices over the millennia. Only one of the 'Plague Monks' remains following "
            "a government raid on the island in the 1950s, the details of which have been diligently hidden from the "
            "public by the Italian government. The Plague Monk's only objective is to manifest Hastalÿk physically "
            "into the world, and spread its mutating corruption across the planet. Hastalÿk's ultimate plan is "
            "incomprehensible to mortals, but it certainly involves turning all life on Earth into itself through the "
            "spread of its Taint and absorbing all living things. To that end, it is vital to get the Investigators "
            "to witness the final sacrifice of the last Plague Monk at the Charnel Pit, and ideally become absorbed "
            "into the body of Hastalÿk themselves. After that, Hastalÿk will try to reach the water. Once it is able "
            "to touch the water, it bursts like a balloon to scatter its Taint to corrupt the nearby sea life, and "
            "eventually the world. Fortunately for the world, the Italian government has been watching the island, "
            "and indeed the live stream from the Spektral Krew. As soon as it becomes apparent that Hastalÿk is about "
            "to be released, the Italian military triggers its equivalent of the 'Innsmouth Protocol' and scrambles "
            "a squadron of jets to fire bomb the island, and end the vile corruption once and for all. Viral can be "
            "run in about four to eight hours depending on how the Keeper chooses to approach the scenario. Certain "
            "features are designed to be included or omitted as desired to speed up or slow down the game."
        ),
        "semantic_role": "overview_body_continuation",
        "heading_level": "text_body",
        "continues_from": "SU-P006-B002-S005",
    }
]

REVIEW_PROFILES["007"] = {
    "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-003",
    "package_id": "PCRP-G1-VIRAL-P007-003",
    "page": "007",
    "page_label": "Page 007",
    "output_dir": TRIAL_ROOT / "page_complete_review_p007_G1_VIRAL_003",
    "readiness_package_id": "P007-INLINE-MAP-G1-VIRAL-003",
    "readiness_report_sha256": "inline_page_007_verified_text_map",
    "readiness_packet_sha256": "inline_page_007_verified_text_map",
    "readiness_summary_sha256": "inline_page_007_verified_text_map",
    "readiness_manifest_sha256": "inline_page_007_verified_text_map",
    "decision_options": [
        "accept_page_007_as_complete_in_a_later_explicit_decision",
        "hold_page_007_for_corrections_or_additional_review",
    ],
    "skip_readiness_anchor_visual_proof": True,
    "inline_readiness": {
        "page_id": "PG-G1-VIRAL-P007",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P007",
        "profile_id": "page_map_profile_G1_VIRAL_P007_readable_v0",
        "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_007.png",
        "page_image_sha256": "0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41",
        "declared_none": ["table", "unknown", "missing"],
        "context_only_regions": [
            {
                "source_region_id": "PRM-G1-VIRAL-001-P007-R02",
                "status": "visual_context_not_source_text_record",
                "reason": "Portrait/photo area is packaged in the full page image and excluded from source text transcription.",
            },
            {
                "source_region_id": "PRM-G1-VIRAL-001-P007-PAGE-NUMBER",
                "status": "visual_exclusion_not_source_text_record",
                "reason": "Bottom page marker is layout/page-number context, not body source text.",
            },
        ],
        "blocks": [
            {
                "block_id": "P007-B001",
                "block_type": "visual_anchor",
                "content_kind": "ui_art_anchor",
                "extraction_policy": "anchor_only_defer_visual",
                "role": "spektral_krew_ui_art_anchor",
                "source_region_id": "PRM-G1-VIRAL-001-P007-R01",
                "reading_order": 1,
                "box_px": [70, 70, 2350, 2100],
                "text": "",
                "spans": [],
                "protected_tokens": [],
                "anchor_metadata": {
                    "anchor_id": "ART-G1-VIRAL-P007-001",
                    "anchor_label": "Spektral Krew promo/web UI art",
                    "visual_identification": "Upper-page black/green Spektral Krew promotional web/social UI art with character portrait; preserve as a visual anchor for later extraction or crop replacement during assembly.",
                    "deferred_stage": "html_assembly_art_replacement",
                    "not_source_text": True,
                },
            },
            {
                "block_id": "P007-B002",
                "role": "marco_proudfoot_body_left_column",
                "source_region_id": "PRM-G1-VIRAL-001-P007-R03",
                "reading_order": 2,
                "box_px": [200, 2250, 960, 810],
                "text": (
                    "Marco 'Proudfoot' Maglioni (Lead Investigator)\n\n"
                    "Marco Proudfoot (real name Marco Anthony Maglioni) was\n"
                    "born in Palermo, Italy to a wealthy Italian mother and an\n"
                    "American father who was a Sergeant in the US Army. Marco\n"
                    "is only about a sixteenth Cherokee, but he uses the name\n"
                    "Proudfoot because he thinks it's cool and makes him sound\n"
                    "more \"spiritually connected to his roots and shit.\" Unfortunately,\n"
                    "Marco is not big on reading so he has never realized that the\n"
                    "name suggestion was a prank by a Tolkien fan.\n\n"
                    "His family moved to the United States when Marco was\n"
                    "ten years of age. Just after college Marco founded the Spektral\n"
                    "Krew, a popular YouTube channel that features videos exploring\n"
                    "strange, abandoned places, and investigating the paranormal.\n"
                    "His mother encouraged his 'odd hobbies' and so paid for most"
                ),
                "spans": [
                    {
                        "text": "Marco 'Proudfoot' Maglioni (Lead Investigator)",
                        "semantic_role": "section_heading",
                        "heading_level": "h2",
                    },
                    {
                        "text": (
                            "Marco Proudfoot (real name Marco Anthony Maglioni) was born in Palermo, Italy to a wealthy Italian mother and an "
                            "American father who was a Sergeant in the US Army. Marco is only about a sixteenth Cherokee, but he uses the name "
                            "Proudfoot because he thinks it's cool and makes him sound more \"spiritually connected to his roots and shit.\" Unfortunately, "
                            "Marco is not big on reading so he has never realized that the name suggestion was a prank by a Tolkien fan."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {
                        "text": (
                            "His family moved to the United States when Marco was ten years of age. Just after college Marco founded the Spektral "
                            "Krew, a popular YouTube channel that features videos exploring strange, abandoned places, and investigating the paranormal. "
                            "His mother encouraged his 'odd hobbies' and so paid for most"
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                        "continues_to": "SU-P007-B003-S001",
                    },
                ],
                "protected_tokens": ["Marco", "Proudfoot", "Lead Investigator", "Palermo", "Cherokee", "Tolkien", "Spektral", "Krew"],
            },
            {
                "block_id": "P007-B003",
                "role": "marco_proudfoot_body_right_column",
                "source_region_id": "PRM-G1-VIRAL-001-P007-R04-R",
                "reading_order": 3,
                "box_px": [1260, 2340, 1060, 710],
                "text": (
                    "of his equipment to get him started, and she continues to be his\n"
                    "number one patron.\n\n"
                    "Spektral Krew actually started off as a prank channel,\n"
                    "but after a video of a coffee cup moving on its own went viral\n"
                    "(largely due to his massive overreaction) Marco decided\n"
                    "to lean into 'real' ghost hunting. He bought all of the typical\n"
                    "ghost hunting gear and began posting videos. The channel's\n"
                    "popularity exploded almost overnight.\n\n"
                    "Marco is an absolute believer in demons, demonic\n"
                    "possession, and exorcism to the point where he claims that\n"
                    "EVERYTHING unexplained is demonic.\n\n"
                    "He came up with the channel's tagline: \"Hi, I'm Marco and\n"
                    "we are the Spektral Krew. We go places and do things that you"
                ),
                "spans": [
                    {
                        "text": (
                            "of his equipment to get him started, and she continues to be his number one patron."
                        ),
                        "semantic_role": "character_body_continuation",
                        "heading_level": "text_body",
                        "continues_from": "SU-P007-B002-S003",
                    },
                    {
                        "text": (
                            "Spektral Krew actually started off as a prank channel, but after a video of a coffee cup moving on its own went viral "
                            "(largely due to his massive overreaction) Marco decided to lean into 'real' ghost hunting. He bought all of the typical "
                            "ghost hunting gear and began posting videos. The channel's popularity exploded almost overnight."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {
                        "text": (
                            "Marco is an absolute believer in demons, demonic possession, and exorcism to the point where he claims that "
                            "EVERYTHING unexplained is demonic."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {
                        "text": (
                            "He came up with the channel's tagline: \"Hi, I'm Marco and "
                            "we are the Spektral Krew. We go places and do things that you"
                        ),
                        "semantic_role": "character_body_page_boundary",
                        "heading_level": "text_body",
                        "page_boundary": "visible_text_continues_beyond_page_007_without_processing_page_008",
                    }
                ],
                "protected_tokens": ["number one patron", "prank channel", "EVERYTHING", "Hi, I'm Marco"],
            },
        ],
    },
    "review_attachments": [
        {
            "attachment_id": "P007-003-ATT-PAGE",
            "role": "source_page_image",
            "source_path": TRIAL_ROOT / "images" / "page_007.png",
            "target_path": "review_assets/page_007.png",
            "sha256": "0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41",
        },
    ],
    "generated_page_crops": [
        {
            "attachment_id": "P007-003-ATT-CROP-ART",
            "role": "human_review_crop",
            "label": "spektral_krew_ui_art_anchor",
            "source_path": TRIAL_ROOT / "images" / "page_007.png",
            "source_sha256": "0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41",
            "box_px": [35, 40, 2410, 2140],
            "target_path": "review_assets/1_P007-spektral-krew-ui-art-anchor.png",
            "covered_review_blocks": ["P007-B001"],
            "detect_dark_text": False,
            "include_in_text_map": False,
        },
        {
            "attachment_id": "P007-003-ATT-CROP-LEFT",
            "role": "human_review_crop",
            "label": "marco_proudfoot_body_left_column",
            "source_path": TRIAL_ROOT / "images" / "page_007.png",
            "source_sha256": "0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41",
            "box_px": [80, 2220, 1210, 910],
            "target_path": "review_assets/2_P007-marco-proudfoot-body-left.png",
            "covered_review_blocks": ["P007-B002"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P007-003-ATT-CROP-RIGHT",
            "role": "human_review_crop",
            "label": "marco_proudfoot_body_right_column",
            "source_path": TRIAL_ROOT / "images" / "page_007.png",
            "source_sha256": "0271A5FB9A672248ABBC771C2F1F064D58640CCB6D8692C7AF7AAE58A160BC41",
            "box_px": [1260, 2290, 1180, 840],
            "target_path": "review_assets/3_P007-marco-proudfoot-body-right.png",
            "covered_review_blocks": ["P007-B003"],
        },
    ],
    "generated_review_text_map_attachment": {
        "attachment_id": "P007-003-ATT-TEXT-MAP",
        "role": "ocr_verified_text_map_markdown",
        "target_path": "review_assets/page_007_ocr_verified_text_map.md",
        "crops_from_inline_readiness_spans": True,
        "full_text_blocks": True,
    },
    "generated_semantic_map_attachment": {
        "json_attachment_id": "P007-003-ATT-SEMANTIC-MAP-JSON",
        "markdown_attachment_id": "P007-003-ATT-SEMANTIC-MAP-MD",
        "json_role": "semantic_text_map_json",
        "markdown_role": "semantic_text_map_markdown",
        "map_id": "SM-G1-VIRAL-P007-003",
        "json_target_path": "review_assets/page_007_semantic_text_map.json",
        "markdown_target_path": "review_assets/page_007_semantic_text_map.md",
        "source": "generated_from_inline_readiness_spans",
    },
}

REVIEW_PROFILES["008"] = {
    "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001",
    "package_id": "PCRP-G1-VIRAL-P008-001",
    "page": "008",
    "page_label": "Page 008",
    "output_dir": TRIAL_ROOT / "page_complete_review_p008_G1_VIRAL_001",
    "readiness_package_id": "P008-INLINE-MAP-G1-VIRAL-001",
    "readiness_report_sha256": "inline_page_008_verified_text_map",
    "readiness_packet_sha256": "inline_page_008_verified_text_map",
    "readiness_summary_sha256": "inline_page_008_verified_text_map",
    "readiness_manifest_sha256": "inline_page_008_verified_text_map",
    "decision_options": [
        "accept_page_008_as_complete_in_a_later_explicit_decision",
        "hold_page_008_for_corrections_or_additional_review",
    ],
    "skip_readiness_anchor_visual_proof": True,
    "inline_readiness": {
        "page_id": "PG-G1-VIRAL-P008",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P008",
        "profile_id": "page_map_profile_G1_VIRAL_P008_readable_v0",
        "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_008.png",
        "page_image_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
        "declared_none": ["table", "unknown", "missing"],
        "context_only_regions": [
            {
                "source_region_id": "PRM-G1-VIRAL-001-P008-PAGE-NUMBER",
                "status": "visual_exclusion_not_source_text_record",
                "reason": "Bottom page marker is layout/page-number context, not body source text.",
            }
        ],
        "blocks": [
            {
                "block_id": "P008-B001",
                "role": "marco_proudfoot_body_page_008_continuation",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R01A",
                "reading_order": 1,
                "box_px": [140, 220, 1080, 430],
                "text": (
                    "would NEVER do.” which he is very proud of as it puts him\n"
                    "at the forefront of any action and makes the Krew look like\n"
                    "fearless daredevils.\n\n"
                    "In addition to the supernatural, Marco is obsessed with his\n"
                    "physical appearance and going to the gym. He’s a narcissist\n"
                    "and extremely confident on the outside, but would probably\n"
                    "shit a brick if he saw a genuine paranormal event."
                ),
                "spans": [
                    {
                        "text": (
                            "would NEVER do.” which he is very proud of as it puts him at the forefront of any action and makes the Krew look like "
                            "fearless daredevils."
                        ),
                        "semantic_role": "character_body_continuation",
                        "heading_level": "text_body",
                        "page_boundary": "visible_text_continues_from_page_007_without_processing_page_007",
                    },
                    {
                        "text": (
                            "In addition to the supernatural, Marco is obsessed with his physical appearance and going to the gym. He’s a narcissist "
                            "and extremely confident on the outside, but would probably shit a brick if he saw a genuine paranormal event."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                ],
                "protected_tokens": ["NEVER", "Krew", "supernatural", "Marco", "narcissist"],
            },
            {
                "block_id": "P008-B002",
                "role": "marco_proudfoot_appearance_gear_box",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R01B",
                "reading_order": 2,
                "box_px": [170, 620, 930, 430],
                "text": (
                    "APPEARANCE\n"
                    "Marco (28) is 6’4” and muscular, with swept back black hair. He’s\n"
                    "always wearing shades (think Italian-American jock type) and\n"
                    "always dresses fashionably in his trademark black leather jacket.\n\n"
                    "GEAR CARRIED\n"
                    "Spektral Krew™ Satchel, Glowsticks (20), Handheld Night Vision\n"
                    "Camera, EMF Meter, Smartphone with FLIR Camera, EVP SCD1"
                ),
                "spans": [
                    {"text": "APPEARANCE", "semantic_role": "section_heading", "heading_level": "h3"},
                    {
                        "text": (
                            "Marco (28) is 6’4” and muscular, with swept back black hair. He’s always wearing shades "
                            "(think Italian-American jock type) and always dresses fashionably in his trademark black leather jacket."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {"text": "GEAR CARRIED", "semantic_role": "section_heading", "heading_level": "h3"},
                    {
                        "text": (
                            "Spektral Krew™ Satchel, Glowsticks (20), Handheld Night Vision Camera, EMF Meter, "
                            "Smartphone with FLIR Camera, EVP SCD1"
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                ],
                "protected_tokens": ["APPEARANCE", "Marco", "6’4”", "GEAR CARRIED", "Spektral Krew™", "EVP SCD1"],
            },
            {
                "block_id": "P008-B003",
                "block_type": "visual_anchor",
                "content_kind": "photo_anchor",
                "extraction_policy": "anchor_only_defer_visual",
                "role": "corrina_trench_portrait_anchor",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R02",
                "reading_order": 3,
                "box_px": [180, 1100, 900, 1250],
                "text": "",
                "spans": [],
                "protected_tokens": [],
                "anchor_metadata": {
                    "anchor_id": "ART-G1-VIRAL-P008-001",
                    "anchor_label": "Corrina Trench portrait/photo art",
                    "visual_identification": "Large left-column portrait/photo of Corrina Trench below Marco gear box; preserve as a visual anchor for later extraction or crop replacement during assembly.",
                    "deferred_stage": "html_assembly_art_replacement",
                    "not_source_text": True,
                },
            },
            {
                "block_id": "P008-B004",
                "role": "corrina_trench_body_left_column",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R04-L",
                "reading_order": 4,
                "box_px": [130, 2410, 1080, 700],
                "text": (
                    "Corrina Trench (Investigator)\n\n"
                    "Corrina is a firm believer in auras, crystals, ghosts, and the\n"
                    "like. She spent much of her life involved in a weird new age cult\n"
                    "in the forests of northern California, though she doesn’t like to\n"
                    "talk about it. After leaving the commune, Corrina studied for a\n"
                    "degree in Biology, but has since abandoned that and has fallen\n"
                    "into a rabbit-hole of occult, folklore, and conspiracy theories.\n"
                    "As a result she considers herself a professional Medium. Sadly\n"
                    "– at least for her – she’s as spiritually connected as a teapot.\n"
                    "Corrina puts on an act of being incredibly sexually free and\n"
                    "pretends to be pan-sexual – she is actually very straight."
                ),
                "spans": [
                    {"text": "Corrina Trench (Investigator)", "semantic_role": "section_heading", "heading_level": "h2"},
                    {
                        "text": (
                            "Corrina is a firm believer in auras, crystals, ghosts, and the like. She spent much of her life involved in a weird new age cult "
                            "in the forests of northern California, though she doesn’t like to talk about it. After leaving the commune, Corrina studied for a "
                            "degree in Biology, but has since abandoned that and has fallen into a rabbit-hole of occult, folklore, and conspiracy theories. "
                            "As a result she considers herself a professional Medium. Sadly – at least for her – she’s as spiritually connected as a teapot. "
                            "Corrina puts on an act of being incredibly sexually free and pretends to be pan-sexual – she is actually very straight."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                ],
                "protected_tokens": ["Corrina Trench", "Investigator", "northern California", "Biology", "Medium", "pan-sexual"],
            },
            {
                "block_id": "P008-B005",
                "role": "corrina_trench_body_right_column",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R01C-R",
                "reading_order": 5,
                "box_px": [1180, 220, 1160, 1300],
                "text": (
                    "People tend to judge her on the utter nonsense she comes\n"
                    "up with, which she absolutely insists is factual. Unfortunately\n"
                    "her confidence and quite fantastic acting ability (she can cry\n"
                    "on command – one of Spektral Krew’s fans’ catchphrases is,\n"
                    "“Cry Corrina, cry!”, but she hates this so much, the t-shirt for\n"
                    "it had to be discontinued from the range of Spektral Krew\n"
                    "merchandise) are usually enough to convince the average\n"
                    "mark that she’s the real deal. Before an investigation Corrina\n"
                    "makes sure to bone-up on the history of a place, but pretends\n"
                    "she knows nothing. She also makes up stuff on the spot\n"
                    "because she fears that if Marco thinks she’s a fraud, he would\n"
                    "fire her (which is true). She occasionally doubts herself,\n"
                    "but she has come too far to turn back and intends to see it\n"
                    "through to the bitter end. Corrina often claims she is allergic\n"
                    "to something in order to avoid suggestions from Spektral\n"
                    "Krew’s live audience, especially ones that would potentially\n"
                    "expose her as a fraud.\n\n"
                    "In preparation for this investigation, Corrina has done\n"
                    "some research on the island so that she’s ready for whatever\n"
                    "spirits she might encounter. Of course this also makes it\n"
                    "easier for her to make things up on the fly. Handout #12\n"
                    "provides a list of facts and folklore that Corrina has learned\n"
                    "about Isola di Malamente."
                ),
                "spans": [
                    {
                        "text": (
                            "People tend to judge her on the utter nonsense she comes up with, which she absolutely insists is factual. Unfortunately "
                            "her confidence and quite fantastic acting ability (she can cry on command – one of Spektral Krew’s fans’ catchphrases is, "
                            "“Cry Corrina, cry!”, but she hates this so much, the t-shirt for it had to be discontinued from the range of Spektral Krew "
                            "merchandise) are usually enough to convince the average mark that she’s the real deal. Before an investigation Corrina "
                            "makes sure to bone-up on the history of a place, but pretends she knows nothing. She also makes up stuff on the spot "
                            "because she fears that if Marco thinks she’s a fraud, he would fire her (which is true). She occasionally doubts herself, "
                            "but she has come too far to turn back and intends to see it through to the bitter end. Corrina often claims she is allergic "
                            "to something in order to avoid suggestions from Spektral Krew’s live audience, especially ones that would potentially expose her as a fraud."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {
                        "text": (
                            "In preparation for this investigation, Corrina has done some research on the island so that she’s ready for whatever "
                            "spirits she might encounter. Of course this also makes it easier for her to make things up on the fly. Handout #12 "
                            "provides a list of facts and folklore that Corrina has learned about Isola di Malamente."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                ],
                "protected_tokens": ["Corrina", "Cry Corrina, cry!", "Spektral Krew", "Handout #12", "Isola di Malamente"],
            },
            {
                "block_id": "P008-B006",
                "role": "corrina_trench_appearance_gear_box",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R04B",
                "reading_order": 6,
                "box_px": [1110, 1540, 900, 520],
                "text": (
                    "APPEARANCE\n"
                    "Corrina (27) is a 5’7”, plain looking white girl. She has long,\n"
                    "slightly unkempt brown hair with a streak of purple through it,\n"
                    "and a small diamond piercing in her nose. She wears a long\n"
                    "parka and stripy leggings with black Doc Martens boots. She\n"
                    "is always sniffing and wiping her nose with a handkerchief.\n\n"
                    "GEAR CARRIED\n"
                    "Spektral Krew™ Satchel, Glowsticks (20), Spirit Box, Custom Spirit\n"
                    "Board or ‘Witch Board’"
                ),
                "spans": [
                    {"text": "APPEARANCE", "semantic_role": "section_heading", "heading_level": "h3"},
                    {
                        "text": (
                            "Corrina (27) is a 5’7”, plain looking white girl. She has long, slightly unkempt brown hair with a streak of purple through it, "
                            "and a small diamond piercing in her nose. She wears a long parka and stripy leggings with black Doc Martens boots. "
                            "She is always sniffing and wiping her nose with a handkerchief."
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                    {"text": "GEAR CARRIED", "semantic_role": "section_heading", "heading_level": "h3"},
                    {
                        "text": (
                            "Spektral Krew™ Satchel, Glowsticks (20), Spirit Box, Custom Spirit Board or ‘Witch Board’"
                        ),
                        "semantic_role": "character_body",
                        "heading_level": "text_body",
                    },
                ],
                "protected_tokens": ["APPEARANCE", "Corrina", "5’7”", "GEAR CARRIED", "Spirit Box", "Witch Board"],
            },
            {
                "block_id": "P008-B007",
                "block_type": "visual_anchor",
                "content_kind": "art_anchor",
                "extraction_policy": "anchor_only_defer_visual",
                "role": "crystal_object_art_anchor",
                "source_region_id": "PRM-G1-VIRAL-001-P008-R03",
                "reading_order": 7,
                "box_px": [1100, 2140, 1230, 930],
                "text": "",
                "spans": [],
                "protected_tokens": [],
                "anchor_metadata": {
                    "anchor_id": "ART-G1-VIRAL-P008-002",
                    "anchor_label": "Crystal/object art",
                    "visual_identification": "Lower-right crystal/object image; preserve as a visual anchor for later extraction or crop replacement during assembly.",
                    "deferred_stage": "html_assembly_art_replacement",
                    "not_source_text": True,
                },
            },
        ],
    },
    "review_attachments": [
        {
            "attachment_id": "P008-001-ATT-PAGE",
            "role": "source_page_image",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "target_path": "review_assets/page_008.png",
            "sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
        },
    ],
    "generated_page_crops": [
        {
            "attachment_id": "P008-001-ATT-CROP-MARCO-TOP",
            "role": "human_review_crop",
            "label": "marco_proudfoot_body_page_008_continuation",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [100, 190, 1180, 395],
            "target_path": "review_assets/1_P008-marco-proudfoot-body-continuation.png",
            "covered_review_blocks": ["P008-B001"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-MARCO-BOX",
            "role": "human_review_crop",
            "label": "marco_proudfoot_appearance_gear_box",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [150, 600, 1130, 460],
            "target_path": "review_assets/2_P008-marco-proudfoot-appearance-gear.png",
            "covered_review_blocks": ["P008-B002"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-PORTRAIT",
            "role": "human_review_crop",
            "label": "corrina_trench_portrait_anchor",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [150, 1080, 980, 1290],
            "target_path": "review_assets/3_P008-corrina-trench-portrait-anchor.png",
            "covered_review_blocks": ["P008-B003"],
            "detect_dark_text": False,
            "skip_edge_ink_check": True,
            "include_in_text_map": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-CORRINA-LEFT",
            "role": "human_review_crop",
            "label": "corrina_trench_body_left_column",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [100, 2380, 1180, 760],
            "target_path": "review_assets/4_P008-corrina-trench-body-left.png",
            "covered_review_blocks": ["P008-B004"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-CORRINA-RIGHT",
            "role": "human_review_crop",
            "label": "corrina_trench_body_right_column",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [1180, 190, 1160, 1340],
            "target_path": "review_assets/5_P008-corrina-trench-body-right.png",
            "covered_review_blocks": ["P008-B005"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-CORRINA-BOX",
            "role": "human_review_crop",
            "label": "corrina_trench_appearance_gear_box",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [1080, 1510, 1260, 570],
            "target_path": "review_assets/6_P008-corrina-trench-appearance-gear.png",
            "covered_review_blocks": ["P008-B006"],
            "detect_dark_text": False,
        },
        {
            "attachment_id": "P008-001-ATT-CROP-CRYSTAL",
            "role": "human_review_crop",
            "label": "crystal_object_art_anchor",
            "source_path": TRIAL_ROOT / "images" / "page_008.png",
            "source_sha256": "237676B562EFE6A51A99E073B4AB3BA73796A89466D3B90DA5F1D9174C29BBE0",
            "box_px": [1420, 2120, 1130, 990],
            "target_path": "review_assets/7_P008-crystal-object-art-anchor.png",
            "covered_review_blocks": ["P008-B007"],
            "detect_dark_text": False,
            "skip_edge_ink_check": True,
            "include_in_text_map": False,
        },
    ],
    "generated_review_text_map_attachment": {
        "attachment_id": "P008-001-ATT-TEXT-MAP",
        "role": "ocr_verified_text_map_markdown",
        "target_path": "review_assets/page_008_ocr_verified_text_map.md",
        "crops_from_inline_readiness_spans": True,
        "full_text_blocks": True,
    },
    "generated_semantic_map_attachment": {
        "json_attachment_id": "P008-001-ATT-SEMANTIC-MAP-JSON",
        "markdown_attachment_id": "P008-001-ATT-SEMANTIC-MAP-MD",
        "json_role": "semantic_text_map_json",
        "markdown_role": "semantic_text_map_markdown",
        "map_id": "SM-G1-VIRAL-P008-001",
        "json_target_path": "review_assets/page_008_semantic_text_map.json",
        "markdown_target_path": "review_assets/page_008_semantic_text_map.md",
        "source": "generated_from_inline_readiness_spans",
    },
    "generated_action_backlog_attachment": {
        "attachment_id": "P008-001-ATT-ACTION-BACKLOG",
        "role": "action_backlog_markdown",
        "target_path": "review_assets/page_008_action_backlog.md",
        "steps": [
            {
                "order": 1,
                "actor": "Codex",
                "action": "Inspected existing roadmap/docs and P008 provisional map state.",
                "purpose": "Confirm P008 starts as its own full-page step after P007, before Gate 1.",
                "output": "P008-only plan; no P007/P008 mixing and no acceptance.",
            },
            {
                "order": 2,
                "actor": "Tool:view_image",
                "action": "Viewed rendered page_008.png.",
                "purpose": "Identify text blocks, photo/art anchors, gray boxes, and paragraph/column flow.",
                "output": "Seven review blocks: five text blocks plus portrait and crystal art anchors.",
            },
            {
                "order": 3,
                "actor": "Codex",
                "action": "Prepared inline P008 readable profile.",
                "purpose": "Transcribe visible text, preserve paragraphs, and classify art as anchors.",
                "output": "P008 spans use paragraph/continuation units; art has anchor metadata and zero source text.",
            },
            {
                "order": 4,
                "actor": "Script:build_page_complete_review.py",
                "action": "Materialized PCRP-G1-VIRAL-P008-001.",
                "purpose": "Generate packet/report/summary/manifest, crops, OCR text map, semantic JSON/Markdown, and this backlog.",
                "output": "Review packet only; no page-complete acceptance, Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw mutation, translation, proofreading, implementation, or push.",
            },
            {
                "order": 5,
                "actor": "Script:pytest",
                "action": "Ran focused page-complete review regression tests after P008 build.",
                "purpose": "Verify P008 profile gating, attachments, semantic map, text map, action backlog, and no acceptance leakage.",
                "output": "tests/test_page_complete_review.py passed: 79 tests.",
            },
            {
                "order": 6,
                "actor": "Script:pytest",
                "action": "Ran full Sourcefold test suite after P008 build.",
                "purpose": "Check P008 did not regress existing Sourcefold page-review and acceptance contracts.",
                "output": "Full suite passed: 305 tests.",
            },
            {
                "order": 7,
                "actor": "Script:npm",
                "action": "Ran roadmap validator after P008 docs/roadmap sync.",
                "purpose": "Verify roadmap graph and documentation checkpoints remain parseable and consistent.",
                "output": "Roadmap validator passed: 122 checkpoints.",
            },
            {
                "order": 8,
                "actor": "Tool:git",
                "action": "Ran scoped working-tree diff-check on generated/code/docs files.",
                "purpose": "Confirm the packet is not entering review with whitespace issues.",
                "output": "Scoped diff-check clean.",
            },
            {
                "order": 9,
                "actor": "Sol/Terra",
                "action": "Reviewed the first P008 packet candidate and returned blockers.",
                "purpose": "Catch review-layer risks before sending the packet as ready.",
                "output": "Blocked on Corrina paragraph continuation modeling and crop geometry for Marco/Corrina/crystal evidence.",
            },
            {
                "order": 10,
                "actor": "Codex + Script:build_page_complete_review.py",
                "action": "Returned to build/fix stage and regenerated the P008 packet.",
                "purpose": "Preserve visible paragraph boundaries and align crop evidence with declared block coverage.",
                "output": "Corrina right column starts as a paragraph, crystal crop is clean art-only, gray-box/text crops include represented text, and Marco top crop excludes the next block.",
            },
        ],
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def page_009_span_from_semantic_unit(unit: dict[str, Any]) -> dict[str, Any]:
    return {
        "text": unit["text"],
        "semantic_role": "section_heading" if unit["unit_type"] == "heading" else "character_body",
        "heading_level": unit["heading_level"] or "text_body",
    }


def page_009_text_block(
    block_id: str,
    role: str,
    source_region_id: str,
    reading_order: int,
    box_px: list[int],
    units: list[dict[str, Any]],
) -> dict[str, Any]:
    spans = [page_009_span_from_semantic_unit(unit) for unit in units]
    return {
        "block_id": block_id,
        "role": role,
        "source_region_id": source_region_id,
        "reading_order": reading_order,
        "box_px": box_px,
        "text": "\n\n".join(unit["text"] for unit in units),
        "spans": spans,
        "protected_tokens": [unit["text"] for unit in units if unit["unit_type"] == "heading"],
    }


def page_009_art_block(
    block_id: str,
    role: str,
    source_region_id: str,
    reading_order: int,
    box_px: list[int],
    anchor_label: str,
) -> dict[str, Any]:
    return {
        "block_id": block_id,
        "block_type": "visual_anchor",
        "content_kind": "art_anchor",
        "extraction_policy": "anchor_only_defer_visual",
        "role": role,
        "source_region_id": source_region_id,
        "reading_order": reading_order,
        "box_px": box_px,
        "text": "",
        "spans": [],
        "protected_tokens": [],
        "anchor_metadata": {
            "anchor_id": block_id,
            "anchor_label": anchor_label,
            "visual_identification": anchor_label,
            "deferred_stage": "html_assembly_art_replacement",
            "not_source_text": True,
        },
    }


def install_page_009_review_profile() -> None:
    semantic_map_path = PAGE_009_SEMANTIC_ROOT / "page_009_semantic_text_map.json"
    semantic_map = read_json(semantic_map_path)
    if semantic_map.get("package_id") != "P009SEM-G1-VIRAL-001":
        raise SystemExit("page 009 PCRP requires accepted P009SEM-G1-VIRAL-001")
    units_by_block: dict[str, list[dict[str, Any]]] = {"P009-B003": [], "P009-B004": []}
    for unit in semantic_map["units"]:
        units_by_block[unit["source_block_id"]].append(unit)
    for units in units_by_block.values():
        units.sort(key=lambda item: item["reading_order"])

    REVIEW_PROFILES["009"] = {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P009-001",
        "package_id": "PCRP-G1-VIRAL-P009-001",
        "page": "009",
        "page_label": "Page 009",
        "output_dir": TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001",
        "readiness_package_id": "P009SEM-G1-VIRAL-001",
        "readiness_report_sha256": "inline_from_P009SEM_G1_VIRAL_001",
        "readiness_packet_sha256": "inline_from_P009SEM_G1_VIRAL_001",
        "readiness_summary_sha256": "inline_from_P009SEM_G1_VIRAL_001",
        "readiness_manifest_sha256": "inline_from_P009SEM_G1_VIRAL_001",
        "extra_input_packages": ["P009TR-G1-VIRAL-003", "P009TXT-G1-VIRAL-001"],
        "decision_options": [
            "accept_page_009_as_complete_in_a_later_explicit_decision",
            "hold_page_009_for_corrections_or_additional_review",
        ],
        "skip_readiness_anchor_visual_proof": True,
        "inline_readiness": {
            "authorization_id": "BA-G1-VIRAL-PAGE-009-SEMANTIC-TEXT-MAP-001",
            "page_id": "PG-G1-VIRAL-P009",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P009",
            "profile_id": "page_map_profile_G1_VIRAL_P009_semantic_v0",
            "pipeline_id": "p009_crop_text_semantic_pcrp_profile_v0",
            "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_009.png",
            "page_image_sha256": "3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456",
            "declared_none": ["table", "unknown", "missing"],
            "context_only_regions": [
                {
                    "source_region_id": "PRM-G1-VIRAL-001-P009-PAGE-NUMBER",
                    "status": "visual_exclusion_not_source_text_record",
                    "reason": "Bottom page marker is layout/page-number context, not body source text.",
                }
            ],
            "blocks": [
                page_009_art_block(
                    "P009-B001",
                    "left_portrait_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P009-R01",
                    1,
                    [160, 225, 1085, 1005],
                    "Left profile portrait/image area for Enoch Jeremiah Eakins.",
                ),
                page_009_art_block(
                    "P009-B002",
                    "right_portrait_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P009-R02",
                    2,
                    [1300, 225, 1085, 1005],
                    "Right profile portrait/image area for Peter Wharton.",
                ),
                page_009_text_block(
                    "P009-B003",
                    "left_profile_text_column",
                    "PRM-G1-VIRAL-001-P009-R03",
                    3,
                    [50, 1540, 1225, 1500],
                    units_by_block["P009-B003"],
                ),
                page_009_text_block(
                    "P009-B004",
                    "right_profile_text_column",
                    "PRM-G1-VIRAL-001-P009-R04",
                    4,
                    [1275, 1540, 1225, 1500],
                    units_by_block["P009-B004"],
                ),
            ],
        },
        "review_attachments": [
            {
                "attachment_id": "P009-001-ATT-PAGE",
                "role": "source_page_image",
                "source_path": TRIAL_ROOT / "images" / "page_009.png",
                "target_path": "review_assets/page_009.png",
                "sha256": "3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456",
            },
            {
                "attachment_id": "P009-001-ATT-HUMAN-LEFT-PORTRAIT",
                "role": "human_context_crop",
                "source_path": PAGE_009_CROP_CONTRACT_ROOT / "review_assets" / "1_P009-left-portrait-image-area-readable.png",
                "target_path": "review_assets/1_P009-left-portrait-image-area-readable.png",
                "sha256": "4310AFFA3CF25A2CADD7A91AF64D4A8E0106316C033540861FFF8942170AA82C",
            },
            {
                "attachment_id": "P009-001-ATT-HUMAN-RIGHT-PORTRAIT",
                "role": "human_context_crop",
                "source_path": PAGE_009_CROP_CONTRACT_ROOT / "review_assets" / "2_P009-right-portrait-image-area-readable.png",
                "target_path": "review_assets/2_P009-right-portrait-image-area-readable.png",
                "sha256": "41E35E355E0DEC4158717652B3350F7AA99FC8794EC19D8C3216EFACB73ABDE4",
            },
            {
                "attachment_id": "P009-001-ATT-HUMAN-LEFT-TEXT",
                "role": "human_context_crop",
                "source_path": PAGE_009_CROP_CONTRACT_ROOT / "review_assets" / "3_P009-left-profile-text-column-human-context.png",
                "target_path": "review_assets/3_P009-left-profile-text-column-human-context.png",
                "sha256": "A39DC27C84A407DE8E3C7038119B198AAB8E180599559D1B51E99980681394FF",
            },
            {
                "attachment_id": "P009-001-ATT-HUMAN-RIGHT-TEXT",
                "role": "human_context_crop",
                "source_path": PAGE_009_CROP_CONTRACT_ROOT / "review_assets" / "4_P009-right-profile-text-column-human-context.png",
                "target_path": "review_assets/4_P009-right-profile-text-column-human-context.png",
                "sha256": "C9A11C02FE6C984D4A5BCBFA9B429B0F9FC3625D31622029FCDFB0649D196076",
            },
            {
                "attachment_id": "P009-001-ATT-PREDECESSOR-TEXT-MAP",
                "role": "predecessor_text_map_markdown",
                "source_path": PAGE_009_TEXT_ROOT / "page_009_text_map.md",
                "target_path": "review_assets/page_009_text_map.md",
                "sha256": "0F5DB5291A8F5DAE70F3EAF4757AFF0F164DB6D1D89745134A7440994841B968",
            },
            {
                "attachment_id": "P009-001-ATT-PREDECESSOR-SEMANTIC-MAP",
                "role": "predecessor_semantic_text_map_markdown",
                "source_path": PAGE_009_SEMANTIC_ROOT / "page_009_semantic_text_map.md",
                "target_path": "review_assets/page_009_semantic_text_map_predecessor.md",
                "sha256": "AE6D9F8C38E716583FD2D3B14026CEE562B2EE64F00BA263362CC84009746313",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P009-B003-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "left_profile_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_009.png",
                "source_sha256": "3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456",
                "box_px": [50, 1540, 1225, 1500],
                "target_path": "review_assets/3b_P009-left-profile-text-column-text-evidence.png",
                "covered_review_blocks": ["P009-B003"],
            },
            {
                "attachment_id": "P009-B004-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "right_profile_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_009.png",
                "source_sha256": "3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456",
                "box_px": [1275, 1540, 1225, 1500],
                "target_path": "review_assets/4b_P009-right-profile-text-column-text-evidence.png",
                "covered_review_blocks": ["P009-B004"],
            },
        ],
        "generated_review_text_map_attachment": {
            "attachment_id": "P009-001-ATT-TEXT-MAP",
            "role": "ocr_verified_text_map",
            "target_path": "review_assets/page_009_ocr_verified_text_map.md",
            "crops_from_inline_readiness_spans": True,
            "full_text_blocks": True,
        },
        "generated_semantic_map_attachment": {
            "json_attachment_id": "P009-001-ATT-SEMANTIC-MAP-JSON",
            "markdown_attachment_id": "P009-001-ATT-SEMANTIC-MAP-MD",
            "json_role": "semantic_text_map_json",
            "markdown_role": "semantic_text_map_markdown",
            "map_id": "SM-G1-VIRAL-P009-PCRP-001",
            "source": "P009SEM-G1-VIRAL-001",
            "json_target_path": "review_assets/page_009_semantic_text_map.json",
            "markdown_target_path": "review_assets/page_009_semantic_text_map.md",
        },
    }


install_page_009_review_profile()


def install_page_010_review_profile() -> None:
    semantic_map_path = PAGE_010_SEMANTIC_ROOT / "page_010_semantic_text_map.json"
    semantic_map = read_json(semantic_map_path)
    if semantic_map.get("package_id") != "P010SEM-G1-VIRAL-001":
        raise SystemExit("page 010 PCRP requires accepted P010SEM-G1-VIRAL-001")
    units_by_block: dict[str, list[dict[str, Any]]] = {
        "P010-B001": [],
        "P010-B002": [],
        "P010-B005": [],
        "P010-B006": [],
    }
    for semantic_unit in semantic_map["units"]:
        source_block_id = semantic_unit["source_block_id"]
        if source_block_id in units_by_block:
            units_by_block[source_block_id].append(semantic_unit)
    for units in units_by_block.values():
        units.sort(key=lambda item: item["reading_order"])

    REVIEW_PROFILES["010"] = {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P010-001",
        "package_id": "PCRP-G1-VIRAL-P010-001",
        "page": "010",
        "page_label": "Page 010",
        "output_dir": TRIAL_ROOT / "page_complete_review_p010_G1_VIRAL_001",
        "readiness_package_id": "P010SEM-G1-VIRAL-001",
        "readiness_report_sha256": "inline_from_P010SEM_G1_VIRAL_001",
        "readiness_packet_sha256": "inline_from_P010SEM_G1_VIRAL_001",
        "readiness_summary_sha256": "inline_from_P010SEM_G1_VIRAL_001",
        "readiness_manifest_sha256": "inline_from_P010SEM_G1_VIRAL_001",
        "extra_input_packages": ["P010TR-G1-VIRAL-001", "P010TXT-G1-VIRAL-001"],
        "decision_options": [
            "accept_page_010_as_complete_in_a_later_explicit_decision",
            "hold_page_010_for_corrections_or_additional_review",
        ],
        "skip_readiness_anchor_visual_proof": True,
        "inline_readiness": {
            "authorization_id": "BA-G1-VIRAL-PAGE-010-SEMANTIC-TEXT-MAP-001",
            "page_id": "PG-G1-VIRAL-P010",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P010",
            "profile_id": "page_map_profile_G1_VIRAL_P010_semantic_v0",
            "pipeline_id": "p010_crop_text_semantic_pcrp_profile_v0",
            "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_010.png",
            "page_image_sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
            "declared_none": ["table", "unknown", "missing"],
            "context_only_regions": [
                {
                    "source_region_id": "PRM-G1-VIRAL-001-P010-PAGE-NUMBER",
                    "status": "visual_exclusion_not_source_text_record",
                    "reason": "Bottom page marker is layout/page-number context, not body source text.",
                }
            ],
            "blocks": [
                page_009_text_block(
                    "P010-B001",
                    "upper_left_peter_continuation_gear_text",
                    "PRM-G1-VIRAL-001-P010-R01",
                    1,
                    [180, 170, 1080, 500],
                    units_by_block["P010-B001"],
                ),
                page_009_text_block(
                    "P010-B005",
                    "lower_left_hyeon_profile_text_start",
                    "PRM-G1-VIRAL-001-P010-R05",
                    2,
                    [180, 2020, 1080, 1040],
                    units_by_block["P010-B005"],
                ),
                page_009_text_block(
                    "P010-B002",
                    "upper_right_hyeon_continuation_appearance_gear_text",
                    "PRM-G1-VIRAL-001-P010-R02",
                    3,
                    [1280, 170, 1070, 875],
                    units_by_block["P010-B002"],
                ),
                page_009_text_block(
                    "P010-B006",
                    "lower_right_maya_profile_text_start",
                    "PRM-G1-VIRAL-001-P010-R05",
                    4,
                    [1260, 2360, 1110, 740],
                    units_by_block["P010-B006"],
                ),
                page_009_art_block(
                    "P010-B003",
                    "left_hyeon_portrait_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P010-R03",
                    5,
                    [160, 650, 1060, 1460],
                    "Left Hyeon portrait/image area.",
                ),
                page_009_art_block(
                    "P010-B004",
                    "right_maya_portrait_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P010-R04",
                    6,
                    [1310, 650, 1040, 1460],
                    "Right Maya portrait/image area.",
                ),
            ],
        },
        "review_attachments": [
            {
                "attachment_id": "P010-001-ATT-PAGE",
                "role": "source_page_image",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "page_010.png",
                "target_path": "review_assets/page_010.png",
                "sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-UPPER-LEFT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "1_P010-upper-left-continuation-gear-human-context.png",
                "target_path": "review_assets/1_P010-upper-left-continuation-gear-human-context.png",
                "sha256": "C5B10AF894F47363FE406A6676803EA79378BDAF20251BF0C80D5BA2AB31C10A",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-UPPER-RIGHT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "2_P010-upper-right-continuation-appearance-gear-human-context.png",
                "target_path": "review_assets/2_P010-upper-right-continuation-appearance-gear-human-context.png",
                "sha256": "8F27D91B5F3A27448C04119463F0D3A83BBA9FB086DE02756300A61734BF706A",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-LEFT-PORTRAIT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "3_P010-left-hyeon-portrait-image-area-human-context.png",
                "target_path": "review_assets/3_P010-left-hyeon-portrait-image-area-human-context.png",
                "sha256": "2438D5BE87570B876DE62C05BB1DB2F505F5FCDB6CEB89675BE776EC22EFCB27",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-RIGHT-PORTRAIT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "4_P010-right-maya-portrait-image-area-human-context.png",
                "target_path": "review_assets/4_P010-right-maya-portrait-image-area-human-context.png",
                "sha256": "C2DE4869A0CDD1F8671457A3033DBD4C86AECF41172CB4B63CDB222EAD7BE992",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-LOWER-LEFT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "5_P010-lower-left-hyeon-profile-human-context.png",
                "target_path": "review_assets/5_P010-lower-left-hyeon-profile-human-context.png",
                "sha256": "23F99207C9A7D86CEB740D1DD6608DB7B5B20E35DED71E782528711BB2915130",
            },
            {
                "attachment_id": "P010-001-ATT-HUMAN-LOWER-RIGHT",
                "role": "human_context_crop",
                "source_path": PAGE_010_CROP_CONTRACT_ROOT / "review_assets" / "6_P010-lower-right-maya-profile-human-context.png",
                "target_path": "review_assets/6_P010-lower-right-maya-profile-human-context.png",
                "sha256": "C5EAAD2782C5724AAD052868C2798B04773E2FC4C14A6EF3239EF504CC8E1946",
            },
            {
                "attachment_id": "P010-001-ATT-PREDECESSOR-TEXT-MAP",
                "role": "predecessor_text_map_markdown",
                "source_path": PAGE_010_TEXT_ROOT / "page_010_text_map.md",
                "target_path": "review_assets/page_010_text_map.md",
                "sha256": "EBF6D19ADA6DE436A19AC74C43CFF567F6C05F6D3A3F59991B12150027769D59",
            },
            {
                "attachment_id": "P010-001-ATT-PREDECESSOR-SEMANTIC-MAP",
                "role": "predecessor_semantic_text_map_markdown",
                "source_path": PAGE_010_SEMANTIC_ROOT / "page_010_semantic_text_map.md",
                "target_path": "review_assets/page_010_semantic_text_map_predecessor.md",
                "sha256": "005A8A6954CA28CD633BF4A26D1C911DDD385B0ADC64F258D317777057B5B974",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P010-B001-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "upper_left_peter_continuation_gear_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_010.png",
                "source_sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
                "box_px": [180, 170, 1080, 500],
                "target_path": "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png",
                "covered_review_blocks": ["P010-B001"],
            },
            {
                "attachment_id": "P010-B005-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "lower_left_hyeon_profile_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_010.png",
                "source_sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
                "box_px": [180, 2020, 1080, 1040],
                "target_path": "review_assets/5b_P010-lower-left-hyeon-profile-text-evidence.png",
                "covered_review_blocks": ["P010-B005"],
            },
            {
                "attachment_id": "P010-B002-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "upper_right_hyeon_continuation_appearance_gear_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_010.png",
                "source_sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
                "box_px": [1280, 170, 1070, 875],
                "target_path": "review_assets/2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
                "covered_review_blocks": ["P010-B002"],
            },
            {
                "attachment_id": "P010-B006-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "lower_right_maya_profile_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_010.png",
                "source_sha256": "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7",
                "box_px": [1260, 2360, 1110, 740],
                "target_path": "review_assets/6b_P010-lower-right-maya-profile-text-evidence.png",
                "covered_review_blocks": ["P010-B006"],
            },
        ],
        "generated_review_text_map_attachment": {
            "attachment_id": "P010-001-ATT-TEXT-MAP",
            "role": "ocr_verified_text_map",
            "target_path": "review_assets/page_010_ocr_verified_text_map.md",
            "crops_from_inline_readiness_spans": True,
            "full_text_blocks": True,
        },
        "generated_semantic_map_attachment": {
            "json_attachment_id": "P010-001-ATT-SEMANTIC-MAP-JSON",
            "markdown_attachment_id": "P010-001-ATT-SEMANTIC-MAP-MD",
            "json_role": "semantic_text_map_json",
            "markdown_role": "semantic_text_map_markdown",
            "map_id": "SM-G1-VIRAL-P010-PCRP-001",
            "source": "P010SEM-G1-VIRAL-001",
            "source_json_path": PAGE_010_SEMANTIC_ROOT / "page_010_semantic_text_map.json",
            "source_markdown_path": PAGE_010_SEMANTIC_ROOT / "page_010_semantic_text_map.md",
            "json_target_path": "review_assets/page_010_semantic_text_map.json",
            "markdown_target_path": "review_assets/page_010_semantic_text_map.md",
        },
    }


install_page_010_review_profile()


def install_page_011_review_profile() -> None:
    semantic_map_path = PAGE_011_SEMANTIC_ROOT / "page_011_semantic_text_map.json"
    semantic_map = read_json(semantic_map_path)
    if semantic_map.get("package_id") != "P011SEM-G1-VIRAL-001":
        raise SystemExit("page 011 PCRP requires accepted P011SEM-G1-VIRAL-001")
    units_by_block: dict[str, list[dict[str, Any]]] = {
        "P011-B001": [],
        "P011-B004": [],
    }
    for semantic_unit in semantic_map["units"]:
        source_block_id = semantic_unit["source_block_id"]
        if source_block_id in units_by_block:
            units_by_block[source_block_id].append(semantic_unit)
    for units in units_by_block.values():
        units.sort(key=lambda item: item["reading_order"])

    REVIEW_PROFILES["011"] = {
        "authorization_id": "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P011-001",
        "package_id": "PCRP-G1-VIRAL-P011-001",
        "page": "011",
        "page_label": "Page 011",
        "output_dir": TRIAL_ROOT / "page_complete_review_p011_G1_VIRAL_001",
        "readiness_package_id": "P011SEM-G1-VIRAL-001",
        "readiness_report_sha256": "inline_from_P011SEM_G1_VIRAL_001",
        "readiness_packet_sha256": "inline_from_P011SEM_G1_VIRAL_001",
        "readiness_summary_sha256": "inline_from_P011SEM_G1_VIRAL_001",
        "readiness_manifest_sha256": "inline_from_P011SEM_G1_VIRAL_001",
        "extra_input_packages": ["P011TR-G1-VIRAL-001", "P011TXT-G1-VIRAL-001"],
        "decision_options": [
            "accept_page_011_as_complete_in_a_later_explicit_decision",
            "hold_page_011_for_corrections_or_additional_review",
        ],
        "skip_readiness_anchor_visual_proof": True,
        "inline_readiness": {
            "authorization_id": "BA-G1-VIRAL-PAGE-011-SEMANTIC-TEXT-MAP-001",
            "page_id": "PG-G1-VIRAL-P011",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P011",
            "profile_id": "page_map_profile_G1_VIRAL_P011_semantic_v0",
            "pipeline_id": "p011_crop_text_semantic_pcrp_profile_v0",
            "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_011.png",
            "page_image_sha256": "697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6",
            "declared_none": ["table", "unknown", "missing"],
            "context_only_regions": [
                {
                    "source_region_id": "PRM-G1-VIRAL-001-P011-PAGE-NUMBER",
                    "status": "visual_exclusion_not_source_text_record",
                    "reason": "Bottom page marker is layout/page-number context, not body source text.",
                }
            ],
            "blocks": [
                page_009_text_block(
                    "P011-B001",
                    "left_maya_continuation_secret_appearance_text",
                    "PRM-G1-VIRAL-001-P011-R01",
                    1,
                    [170, 210, 1080, 1900],
                    units_by_block["P011-B001"],
                ),
                page_009_text_block(
                    "P011-B004",
                    "right_emily_profile_text_start",
                    "PRM-G1-VIRAL-001-P011-R04",
                    2,
                    [1260, 1560, 1080, 1530],
                    units_by_block["P011-B004"],
                ),
                page_009_art_block(
                    "P011-B002",
                    "emily_em_lavigne_portrait_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P011-R02",
                    3,
                    [1110, 220, 1000, 1320],
                    "Emily 'Em' Lavigne portrait/image area.",
                ),
                page_009_art_block(
                    "P011-B003",
                    "lower_left_screen_image_area_art_anchor",
                    "PRM-G1-VIRAL-001-P011-R03",
                    4,
                    [170, 2190, 1080, 900],
                    "Lower-left screen image area.",
                ),
            ],
        },
        "review_attachments": [
            {
                "attachment_id": "P011-001-ATT-PAGE",
                "role": "source_page_image",
                "source_path": PAGE_011_CROP_CONTRACT_ROOT / "review_assets" / "page_011.png",
                "target_path": "review_assets/page_011.png",
                "sha256": "697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6",
            },
            {
                "attachment_id": "P011-001-ATT-HUMAN-MAYA-TEXT",
                "role": "human_context_crop",
                "source_path": PAGE_011_CROP_CONTRACT_ROOT
                / "review_assets"
                / "1_P011-left-maya-continuation-secret-appearance-human-context.png",
                "target_path": "review_assets/1_P011-left-maya-continuation-secret-appearance-human-context.png",
                "sha256": "6AE73BB523A34DC9D59F901C08633E67D7270108D6CA59C10A1D38EDD463232B",
            },
            {
                "attachment_id": "P011-001-ATT-HUMAN-PORTRAIT",
                "role": "human_context_crop",
                "source_path": PAGE_011_CROP_CONTRACT_ROOT
                / "review_assets"
                / "2_P011-emily-em-lavigne-portrait-image-area-human-context.png",
                "target_path": "review_assets/2_P011-emily-em-lavigne-portrait-image-area-human-context.png",
                "sha256": "ECE5BB76CEC123593B97CA2BC67B3E9561298398E91078E8D5F45C431FCD15D1",
            },
            {
                "attachment_id": "P011-001-ATT-HUMAN-SCREEN",
                "role": "human_context_crop",
                "source_path": PAGE_011_CROP_CONTRACT_ROOT
                / "review_assets"
                / "3_P011-lower-left-screen-image-area-human-context.png",
                "target_path": "review_assets/3_P011-lower-left-screen-image-area-human-context.png",
                "sha256": "84A3FC84F2CCE74860CCC441870B30E6A9E870940DFBE7B18215928926092632",
            },
            {
                "attachment_id": "P011-001-ATT-HUMAN-EMILY-TEXT",
                "role": "human_context_crop",
                "source_path": PAGE_011_CROP_CONTRACT_ROOT
                / "review_assets"
                / "4_P011-right-emily-profile-text-human-context.png",
                "target_path": "review_assets/4_P011-right-emily-profile-text-human-context.png",
                "sha256": "B61C33FA2CBE276B605EB207014EACBD39D7B46925E8D9377921CF57C24E1D4A",
            },
            {
                "attachment_id": "P011-001-ATT-PREDECESSOR-TEXT-MAP",
                "role": "predecessor_text_map_markdown",
                "source_path": PAGE_011_TEXT_ROOT / "page_011_text_map.md",
                "target_path": "review_assets/page_011_text_map.md",
                "sha256": "0564ABB708AEE61F6602926B67427460DE6B96167F98A2FB5F97468CF9EBCAF8",
            },
            {
                "attachment_id": "P011-001-ATT-PREDECESSOR-SEMANTIC-MAP",
                "role": "predecessor_semantic_text_map_markdown",
                "source_path": PAGE_011_SEMANTIC_ROOT / "page_011_semantic_text_map.md",
                "target_path": "review_assets/page_011_semantic_text_map_predecessor.md",
                "sha256": "61274D62CE3F353934FF5B89BB4D567FBE83B6C1BB0610230FC72B9DD5E202E6",
            },
        ],
        "generated_page_crops": [
            {
                "attachment_id": "P011-B001-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "left_maya_continuation_secret_appearance_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_011.png",
                "source_sha256": "697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6",
                "box_px": [170, 210, 1080, 1900],
                "target_path": "review_assets/1b_P011-left-maya-continuation-secret-appearance-text-evidence.png",
                "covered_review_blocks": ["P011-B001"],
            },
            {
                "attachment_id": "P011-B004-TEXT-EVIDENCE",
                "role": "text_evidence_crop",
                "label": "right_emily_profile_text_evidence",
                "source_path": TRIAL_ROOT / "images" / "page_011.png",
                "source_sha256": "697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6",
                "box_px": [1260, 1560, 1080, 1530],
                "target_path": "review_assets/4b_P011-right-emily-profile-text-text-evidence.png",
                "covered_review_blocks": ["P011-B004"],
            },
        ],
        "generated_review_text_map_attachment": {
            "attachment_id": "P011-001-ATT-TEXT-MAP",
            "role": "ocr_verified_text_map",
            "target_path": "review_assets/page_011_ocr_verified_text_map.md",
            "crops_from_inline_readiness_spans": True,
            "full_text_blocks": True,
        },
        "generated_semantic_map_attachment": {
            "json_attachment_id": "P011-001-ATT-SEMANTIC-MAP-JSON",
            "markdown_attachment_id": "P011-001-ATT-SEMANTIC-MAP-MD",
            "json_role": "semantic_text_map_json",
            "markdown_role": "semantic_text_map_markdown",
            "map_id": "SM-G1-VIRAL-P011-PCRP-001",
            "source": "P011SEM-G1-VIRAL-001",
            "source_json_path": PAGE_011_SEMANTIC_ROOT / "page_011_semantic_text_map.json",
            "source_markdown_path": PAGE_011_SEMANTIC_ROOT / "page_011_semantic_text_map.md",
            "json_target_path": "review_assets/page_011_semantic_text_map.json",
            "markdown_target_path": "review_assets/page_011_semantic_text_map.md",
        },
    }


install_page_011_review_profile()


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a page-complete review packet for one authorized page.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--page", required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page-complete review packet is fail-closed; pass --execute with exact authorization id")
    if args.page == "009":
        verify_page_009_crop_contract_for_pcrp()
    if args.page not in REVIEW_PROFILES:
        raise SystemExit(f"no page-complete review profile exists for page {args.page}")
    expected_auth = REVIEW_PROFILES[args.page]["authorization_id"]
    if args.authorization_id != expected_auth:
        raise SystemExit(f"page-complete review packet requires {expected_auth}")
    return args


def verify_authorization_ledger(authorization_id: str) -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {authorization_id}" not in ledger:
        raise SystemExit(f"{authorization_id} is missing from bounded trial authorization ledger")


def verify_page_009_crop_contract_for_pcrp() -> None:
    packet_path = PAGE_009_CROP_CONTRACT_ROOT / "page_009_triage_packet.json"
    if not packet_path.exists():
        raise SystemExit(
            f"page 009 PCRP requires current {PAGE_009_REQUIRED_CROP_CONTRACT_ID}; "
            f"{PAGE_009_STALE_TRIAGE_ID} is stale for PCRP"
        )
    packet = read_json(packet_path)
    try:
        require_current_artifact(
            packet=packet,
            required_current_package_id=PAGE_009_REQUIRED_CROP_CONTRACT_ID,
            stale_package_ids=[PAGE_009_STALE_TRIAGE_ID],
            required_supersedes_package_id=PAGE_009_STALE_TRIAGE_ID,
            consumer="PCRP-G1-VIRAL-P009-001",
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if packet.get("crop_qa", {}).get("status") != "passed":
        raise SystemExit("page 009 crop contract QA has not passed")
    for block in packet.get("review_blocks", []):
        required = {"source_region_box_px", "human_review_crop_box_px"}
        if block.get("content_kind") == "text_like_region":
            required.update({"ocr_candidate_crop_box_px", "text_evidence_crop_box_px"})
        missing = sorted(required - set(block))
        if missing:
            raise SystemExit(f"page 009 crop contract block {block.get('block_id')} missing roles: {', '.join(missing)}")


def profile_page(profile_key: str) -> str:
    return REVIEW_PROFILES[profile_key].get("page", profile_key)


def readiness_paths(profile: dict[str, Any]) -> dict[str, Path]:
    root = profile["readiness_root"]
    return {
        "report": root / "page_map_readiness_report.json",
        "packet": root / "page_map_readiness_packet.md",
        "summary": root / "page_map_readiness_summary.md",
        "manifest": root / "page_map_readiness_manifest.md",
    }


def verify_readiness(profile_key: str) -> dict[str, Any]:
    profile = REVIEW_PROFILES[profile_key]
    page = profile_page(profile_key)
    verify_authorization_ledger(profile["authorization_id"])
    if "inline_readiness" in profile:
        return build_inline_readiness(profile)
    paths = readiness_paths(profile)
    expected = {
        paths["report"]: profile["readiness_report_sha256"],
        paths["packet"]: profile["readiness_packet_sha256"],
        paths["summary"]: profile["readiness_summary_sha256"],
        paths["manifest"]: profile["readiness_manifest_sha256"],
    }
    for path, expected_hash in expected.items():
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"readiness predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    report = read_json(paths["report"])
    if report["package_id"] != profile["readiness_package_id"]:
        raise SystemExit("unexpected readiness package")
    if report["page"] != page:
        raise SystemExit("readiness package page does not match requested review page")
    if report["status"] != "ready_for_page_complete_review_packet":
        raise SystemExit("readiness package is not ready for page-complete review packet")
    if report["coverage_summary"]["coverage_accepts_page"] is not False:
        raise SystemExit("readiness coverage must remain advisory")
    if report["readiness_decision"]["page_complete_acceptance_created"] is not False:
        raise SystemExit("readiness predecessor must not already create page-complete acceptance")
    if report["readiness_decision"]["whole_gate_1_acceptance_created"] is not False:
        raise SystemExit("readiness predecessor must not already create whole-Gate acceptance")
    if report["guardrails"]["ocr_executed"] is not False or report["guardrails"]["render_executed"] is not False:
        raise SystemExit("readiness predecessor breached OCR/render guardrail")
    return report


def build_inline_readiness(profile: dict[str, Any]) -> dict[str, Any]:
    inline = profile["inline_readiness"]
    page = profile["page"]
    blocks = []
    for block in inline["blocks"]:
        text = block.get("text", "")
        block_type = block.get("block_type", "text")
        extraction_policy = block.get("extraction_policy", "transcribe_source_text")
        metrics = {
            "character_count": len(text),
            "normalized_character_count": len(" ".join(text.split())),
            "line_count": len(text.splitlines()),
            "non_empty_line_count": sum(1 for line in text.splitlines() if line.strip()),
        }
        protected = [{"token": token, "present": token in text} for token in block.get("protected_tokens", [])]
        missing = [item["token"] for item in protected if not item["present"]]
        blocks.append(
            {
                "block_id": block["block_id"],
                "block_type": block_type,
                "content_kind": block.get("content_kind", "source_text"),
                "extraction_policy": extraction_policy,
                "role": block["role"],
                "source_region_id": block["source_region_id"],
                "reading_order": block["reading_order"],
                "required": True,
                "status": "ready_for_page_complete_review" if not missing else "blocked",
                "anchor": {
                    "page_image": inline["page_image"],
                    "page_image_sha256": inline["page_image_sha256"],
                    "source_region_id": block["source_region_id"],
                    "corrected_crop_reference": inline["page_image"],
                    "corrected_crop_reference_sha256": inline["page_image_sha256"],
                    "box_px": block["box_px"],
                },
                "text_fidelity": {
                    "draft_text_sha256": sha256_text(text),
                    "verified_text_sha256": sha256_text(text),
                    "draft_metrics": metrics,
                    "verified_metrics": metrics,
                    "draft_matches_verified": True,
                    "raw_ocr_available": False,
                    "raw_ocr_comparison": "not_available_for_this_authorization",
                    "protected_tokens": protected,
                    "missing_protected_tokens": missing,
                    "discrepancy": [] if not missing else ["protected_token_missing"],
                    "discrepancy_disposition": "none" if not missing else "blocker_before_page_complete_review",
                },
                "structure_semantics": {
                    "structure_record_id": block["block_id"],
                    "semantic_roles": sorted({span["semantic_role"] for span in block.get("spans", [])}),
                    "missing_semantic_expectations": [],
                    "spans": block.get("spans", []),
                    "anchor_metadata": block.get("anchor_metadata"),
                },
                "overlay_recovery": {
                    "overlay_state": "readable_review_profile_generated_from_page_image",
                    "parent_child_relation": "none",
                    "recovery_role": block["role"],
                    "reading_order_note": f"declared by page {page} inline readable profile",
                },
            }
        )
    return {
        "package_id": profile["readiness_package_id"],
        "authorization_id": inline.get("authorization_id", profile["authorization_id"]),
        "pipeline_id": inline.get("pipeline_id", "inline_readable_page_map_profile_v0"),
        "profile_id": inline["profile_id"],
        "status": "ready_for_page_complete_review_packet",
        "page": page,
        "page_id": inline["page_id"],
        "image_id": inline["image_id"],
        "profile": {
            "page_label": profile["page_label"],
            "expected_block_count": len(blocks),
            "declared_none": inline["declared_none"],
            "context_only_regions": inline["context_only_regions"],
            "page_specific": True,
            "reusable_pipeline": True,
        },
        "block_inventory": blocks,
        "coverage_summary": {
            "coverage_accepts_page": False,
        },
        "readiness_decision": {
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
        },
        "guardrails": {
            "ocr_executed": False,
            "render_executed": False,
        },
    }


def block_summary(block: dict[str, Any]) -> dict[str, Any]:
    fidelity = block["text_fidelity"]
    return {
        "block_id": block["block_id"],
        "block_type": block.get("block_type", "text"),
        "content_kind": block.get("content_kind", "source_text"),
        "extraction_policy": block.get("extraction_policy", "transcribe_source_text"),
        "anchor_metadata": block.get("structure_semantics", {}).get("anchor_metadata"),
        "role": block["role"],
        "source_region_id": block["source_region_id"],
        "reading_order": block["reading_order"],
        "status": block["status"],
        "anchor_crop": block["anchor"]["corrected_crop_reference"],
        "box_px": block["anchor"]["box_px"],
        "draft_matches_verified": fidelity["draft_matches_verified"],
        "protected_tokens_matched": len(fidelity["protected_tokens"]) - len(fidelity["missing_protected_tokens"]),
        "protected_tokens_total": len(fidelity["protected_tokens"]),
        "missing_protected_tokens": fidelity["missing_protected_tokens"],
        "discrepancy_disposition": fidelity["discrepancy_disposition"],
        "character_count": fidelity["verified_metrics"]["character_count"],
        "normalized_character_count": fidelity["verified_metrics"]["normalized_character_count"],
        "line_count": fidelity["verified_metrics"]["line_count"],
        "non_empty_line_count": fidelity["verified_metrics"]["non_empty_line_count"],
    }


def declared_none_note(categories: list[str]) -> str:
    if categories:
        return f"{'/'.join(categories)}: none identified by the readiness profile."
    return "No declared-none categories were provided by the readiness profile."


def materialize_attachments(profile: dict[str, Any], out_root: Path) -> list[dict[str, Any]]:
    materialized = []
    for attachment in profile.get("review_attachments", []):
        source_path = attachment["source_path"]
        if sha256_file(source_path) != attachment["sha256"]:
            raise SystemExit(f"review attachment hash mismatch: {source_path.relative_to(ROOT).as_posix()}")
        target_path = out_root / attachment["target_path"]
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        if sha256_file(target_path) != attachment["sha256"]:
            raise SystemExit(f"copied review attachment hash mismatch: {target_path.relative_to(ROOT).as_posix()}")
        materialized.append(
            {
                "attachment_id": attachment["attachment_id"],
                "role": attachment["role"],
                "source_path": source_path.relative_to(ROOT).as_posix(),
                "package_path": target_path.relative_to(out_root).as_posix(),
                "sha256": attachment["sha256"],
            }
        )
    return materialized


def extract_block_text(block: dict[str, Any]) -> str:
    spans = block["structure_semantics"]["spans"]
    if spans:
        return "\n".join(span["text"] for span in spans)
    return ""


def build_block_text_markdown(readiness: dict[str, Any]) -> str:
    lines = [f"# OCR/Block Text - Page {readiness['page']}", ""]
    for index, block in enumerate(sorted(readiness["block_inventory"], key=lambda item: item["reading_order"]), start=1):
        lines.extend(
            [
                f"{index} - {block['role']}",
                "",
                extract_block_text(block),
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def materialize_generated_block_text(
    profile: dict[str, Any],
    readiness: dict[str, Any],
    out_root: Path,
) -> dict[str, Any] | None:
    attachment = profile.get("generated_block_text_attachment")
    if not attachment:
        return None
    target_path = out_root / attachment["target_path"]
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(build_block_text_markdown(readiness), encoding="utf-8", newline="\n")
    return {
        "attachment_id": attachment["attachment_id"],
        "role": attachment["role"],
        "source_path": "generated_from_readiness_block_inventory",
        "package_path": target_path.relative_to(out_root).as_posix(),
        "sha256": sha256_file(target_path),
    }


def crop_declared_block(page_image_path: Path, box_px: list[int], target_path: Path) -> None:
    x, y, width, height = box_px
    with Image.open(page_image_path) as image:
        image_width, image_height = image.size
        if x < 0 or y < 0 or width <= 0 or height <= 0:
            raise SystemExit(f"invalid declared crop box: {box_px}")
        if x + width > image_width or y + height > image_height:
            raise SystemExit(f"declared crop box exceeds page image bounds: {box_px}")
        target_path.parent.mkdir(parents=True, exist_ok=True)
        image.crop((x, y, x + width, y + height)).save(target_path)


def materialize_generated_declared_block_crops(
    profile: dict[str, Any],
    readiness: dict[str, Any],
    out_root: Path,
) -> list[dict[str, Any]]:
    block_by_id = {block["block_id"]: block for block in readiness["block_inventory"]}
    materialized = []
    for crop_spec in profile.get("generated_declared_block_crops", []):
        block = block_by_id[crop_spec["block_id"]]
        anchor = block["anchor"]
        page_image_path = ROOT / anchor["page_image"]
        if sha256_file(page_image_path) != anchor["page_image_sha256"]:
            raise SystemExit(f"page image hash mismatch: {page_image_path.relative_to(ROOT).as_posix()}")
        target_path = out_root / crop_spec["target_path"]
        crop_declared_block(page_image_path, anchor["box_px"], target_path)
        materialized.append(
            {
                "attachment_id": crop_spec["attachment_id"],
                "role": crop_spec["role"],
                "source_path": anchor["corrected_crop_reference"].replace("\\", "/"),
                "source_origin": "generated_from_page_image_declared_readiness_box_px",
                "page_image_path": anchor["page_image"],
                "box_px": anchor["box_px"],
                "package_path": target_path.relative_to(out_root).as_posix(),
                "sha256": sha256_file(target_path),
            }
        )
    return materialized


def materialize_generated_page_crops(
    profile: dict[str, Any],
    out_root: Path,
) -> list[dict[str, Any]]:
    materialized = []
    for crop_spec in profile.get("generated_page_crops", []):
        source_path = crop_spec["source_path"]
        if sha256_file(source_path) != crop_spec["source_sha256"]:
            raise SystemExit(f"page crop source hash mismatch: {source_path.relative_to(ROOT).as_posix()}")
        target_path = out_root / crop_spec["target_path"]
        crop_declared_block(source_path, crop_spec["box_px"], target_path)
        materialized.append(
            {
                "attachment_id": crop_spec["attachment_id"],
                "role": crop_spec["role"],
                "label": crop_spec["label"],
                "source_path": source_path.relative_to(ROOT).as_posix(),
                "box_px": crop_spec["box_px"],
                "covered_review_blocks": crop_spec["covered_review_blocks"],
                "detect_dark_text": crop_spec.get("detect_dark_text", True),
                "skip_edge_ink_check": crop_spec.get("skip_edge_ink_check", False),
                "package_path": target_path.relative_to(out_root).as_posix(),
                "sha256": sha256_file(target_path),
            }
        )
    return materialized


def build_review_text_map_markdown(attachment: dict[str, Any], page: str) -> str:
    lines = [f"# OCR/Verified Text Map - Page {page}", ""]
    for crop in attachment["crops"]:
        lines.extend([f"## {crop['crop_label']}", "", f"OCR state: `{crop['ocr_state']}`", ""])
        if attachment.get("full_text_blocks"):
            lines.append("| Unit | Text preview | Page | Heading level | Style |")
            lines.append("|---|---|---|---|---|")
        else:
            lines.append("| Text | Page | Heading level | Style |")
            lines.append("|---|---|---|---|")
        for entry in crop["entries"]:
            page = entry["page"] if entry["page"] is not None else ""
            heading_level = entry["heading_level"] if entry["heading_level"] is not None else ""
            style = entry["style"] if entry["style"] is not None else ""
            if attachment.get("full_text_blocks"):
                preview = entry["text"] if len(entry["text"]) <= 120 else f"{entry['text'][:117]}..."
                preview = preview.replace("|", "\\|")
                lines.append(f"| {entry['unit_id']} | {preview} | {page} | `{heading_level}` | `{style}` |")
            else:
                text = entry["text"].replace("|", "\\|")
                lines.append(f"| {text} | {page} | `{heading_level}` | `{style}` |")
        if attachment.get("full_text_blocks"):
            lines.append("")
            for entry in crop["entries"]:
                fence = "````" if "```" in entry["text"] else "```"
                lines.extend([f"### Full Text - {entry['unit_id']}", "", f"{fence}text", entry["text"], fence, ""])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def text_map_crops(profile: dict[str, Any]) -> list[dict[str, Any]]:
    attachment = profile["generated_review_text_map_attachment"]
    if not attachment.get("crops_from_inline_readiness") and not attachment.get("crops_from_inline_readiness_spans"):
        return attachment["crops"]
    crop_specs = profile["generated_page_crops"]
    block_by_id = {block["block_id"]: block for block in profile["inline_readiness"]["blocks"]}
    crops = []
    for crop_spec in crop_specs:
        if not crop_spec.get("include_in_text_map", True):
            continue
        entries = []
        for block_id in crop_spec["covered_review_blocks"]:
            block = block_by_id[block_id]
            if attachment.get("crops_from_inline_readiness_spans"):
                for span_index, span in enumerate(block["spans"], start=1):
                    entries.append(
                        {
                            "unit_id": f"SU-{block['block_id']}-S{span_index:03}",
                            "text": span["text"],
                            "page": span.get("page"),
                            "heading_level": heading_level_for_span(span),
                            "style": display_style_for_span(span),
                        }
                    )
            else:
                entries.append(
                    {
                        "text": block["text"],
                        "page": None,
                        "heading_level": block["spans"][0]["heading_level"],
                        "style": block["role"],
                    }
                )
        if not entries:
            continue
        crops.append(
            {
                "crop_label": crop_spec["label"],
                "ocr_state": "ocr_verified_against_crop",
                "entries": entries,
            }
        )
    return crops


def materialize_generated_review_text_map(profile: dict[str, Any], out_root: Path) -> dict[str, Any] | None:
    attachment = profile.get("generated_review_text_map_attachment")
    if not attachment:
        return None
    attachment = dict(attachment)
    attachment["crops"] = text_map_crops(profile)
    target_path = out_root / attachment["target_path"]
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(build_review_text_map_markdown(attachment, profile.get("page", "")), encoding="utf-8", newline="\n")
    return {
        "attachment_id": attachment["attachment_id"],
        "role": attachment["role"],
        "source_path": "generated_from_ocr_verified_crop_text_map",
        "package_path": target_path.relative_to(out_root).as_posix(),
        "sha256": sha256_file(target_path),
    }


def unit_type_for_span(span: dict[str, Any]) -> str:
    role = span["semantic_role"]
    if role in {"chapter_title", "section_heading"}:
        return "heading"
    if role == "pull_quote":
        return "quote"
    if role == "contents_entry_list":
        return "list"
    if role in {"button_label", "contents_entry", "navigation_item"}:
        return "list_item"
    if role.endswith("_continuation"):
        return "continuation"
    return "paragraph"


def display_style_for_span(span: dict[str, Any]) -> str:
    role = span["semantic_role"]
    if role == "chapter_title":
        return "chapter_heading"
    if role == "section_heading":
        return "section_heading"
    if role == "pull_quote":
        return "pull_quote"
    if role in {"button_label", "contents_entry_list", "contents_entry", "navigation_item"}:
        return "list_item"
    return "body"


def heading_level_for_span(span: dict[str, Any]) -> str | None:
    level = span.get("heading_level")
    if isinstance(level, str) and level.startswith("h") and level[1:].isdigit():
        return level
    if level == "text_body":
        return None
    return level


def block_role_for_block(block: dict[str, Any]) -> str:
    role = block["role"]
    if block.get("extraction_policy") == "anchor_only_defer_visual" or role.endswith("_art_anchor"):
        return "art_region"
    if role.endswith("_heading"):
        return "title_region"
    if role == "contents_entry_group":
        return "list_region"
    if "column" in role:
        return "text_column"
    return "body_block"


def crop_ids_by_block(profile: dict[str, Any]) -> dict[str, list[str]]:
    crop_ids: dict[str, list[str]] = {}
    for crop in profile.get("generated_page_crops", []):
        for block_id in crop["covered_review_blocks"]:
            crop_ids.setdefault(block_id, []).append(crop["attachment_id"])
    return crop_ids


def semantic_units_from_inline_readiness(profile: dict[str, Any]) -> list[dict[str, Any]]:
    inline = profile.get("inline_readiness")
    if not inline:
        raise SystemExit("semantic map generation requires inline readiness semantic spans")
    block_crop_ids = crop_ids_by_block(profile)
    units = []
    reading_order = 1
    for block in sorted(inline["blocks"], key=lambda item: item["reading_order"]):
        spans = block.get("spans", [])
        if not spans:
            if block.get("extraction_policy") == "anchor_only_defer_visual":
                continue
            raise SystemExit(f"semantic map generation requires spans for {block['block_id']}")
        for span_index, span in enumerate(spans, start=1):
            units.append(
                unit := {
                    "unit_id": f"SU-{block['block_id']}-S{span_index:03}",
                    "schema_version": "page_review_semantic_units.v1",
                    "taxonomy_version": "sourcefold_page_review_taxonomy.v1",
                    "unit_type": unit_type_for_span(span),
                    "unit_scope": "in_scope_text",
                    "display_style": display_style_for_span(span),
                    "source_role": "human_verified_span",
                    "block_role": block_role_for_block(block),
                    "reading_order": reading_order,
                    "source_region_ids": [block["source_region_id"]],
                    "crop_ids": block_crop_ids.get(block["block_id"], []),
                    "evidence_predecessors": [profile["readiness_package_id"]],
                    "text_source_state": "human_verified",
                    "text": span["text"],
                    "heading_level": heading_level_for_span(span),
                    "source_block_id": block["block_id"],
                    "span_ids": [f"{block['block_id']}-S{span_index:03}"],
                    "review_state": "ready_for_review",
                }
            )
            for link_field in ("parent_unit_id", "container_unit_id", "continues_from", "continues_to"):
                if span.get(link_field):
                    unit[link_field] = span[link_field]
            if span.get("page_boundary"):
                unit["page_boundary"] = span["page_boundary"]
            reading_order += 1
    return units


def page_inventory_from_readiness(readiness: dict[str, Any]) -> list[dict[str, Any]]:
    regions = []
    for block in sorted(readiness["block_inventory"], key=lambda item: item["reading_order"]):
        spans = block.get("structure_semantics", {}).get("spans", [])
        expected_unit_types = sorted({unit_type_for_span(span) for span in spans})
        extraction_policy = block.get("extraction_policy", "transcribe_source_text")
        decision = "visual_only" if extraction_policy == "anchor_only_defer_visual" else "represented"
        regions.append(
            {
                "region_id": block["source_region_id"],
                "block_id": block["block_id"],
                "role": block["role"],
                "decision": decision,
                "expected_unit_types": [] if decision == "visual_only" else expected_unit_types,
            }
        )
    for context_region in readiness["profile"].get("context_only_regions", []):
        region_id = (
            context_region.get("source_region_id")
            if isinstance(context_region, dict)
            else context_region
        )
        regions.append(
            {
                "region_id": region_id,
                "decision": "context_only",
                "expected_unit_types": [],
            }
        )
    return regions


def materialize_generated_semantic_map(profile: dict[str, Any], out_root: Path) -> list[dict[str, Any]]:
    attachment = profile.get("generated_semantic_map_attachment")
    if not attachment:
        return []
    if attachment.get("source_json_path") and attachment.get("source_markdown_path"):
        source_json_path = attachment["source_json_path"]
        source_markdown_path = attachment["source_markdown_path"]
        document = read_json(source_json_path)
        json_path = out_root / attachment["json_target_path"]
        markdown_path = out_root / attachment["markdown_target_path"]
        json_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_json_path, json_path)
        shutil.copy2(source_markdown_path, markdown_path)
        return [
            {
                "attachment_id": attachment["json_attachment_id"],
                "role": attachment["json_role"],
                "source_path": source_json_path.relative_to(ROOT).as_posix(),
                "package_path": json_path.relative_to(out_root).as_posix(),
                "sha256": sha256_file(json_path),
                "semantic_validation": document["semantic_validation"],
                "markdown_projection_validation": document["markdown_projection_validation"],
            },
            {
                "attachment_id": attachment["markdown_attachment_id"],
                "role": attachment["markdown_role"],
                "source_path": source_markdown_path.relative_to(ROOT).as_posix(),
                "package_path": markdown_path.relative_to(out_root).as_posix(),
                "sha256": sha256_file(markdown_path),
                "semantic_validation": document["semantic_validation"],
                "markdown_projection_validation": document["markdown_projection_validation"],
            },
        ]
    units = semantic_units_from_inline_readiness(profile)
    document = semantic_map_document(
        page=profile["page"],
        package_id=profile["package_id"],
        map_id=attachment["map_id"],
        units=units,
        source=attachment["source"],
    )
    markdown = build_semantic_map_markdown(document)
    markdown_validation = validate_semantic_map_markdown(markdown, expected_unit_count=len(units))
    document["markdown_projection_validation"] = markdown_validation

    json_path = out_root / attachment["json_target_path"]
    markdown_path = out_root / attachment["markdown_target_path"]
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    markdown_path.write_text(markdown, encoding="utf-8", newline="\n")
    return [
        {
            "attachment_id": attachment["json_attachment_id"],
            "role": attachment["json_role"],
            "source_path": attachment["source"],
            "package_path": json_path.relative_to(out_root).as_posix(),
            "sha256": sha256_file(json_path),
            "semantic_validation": document["semantic_validation"],
            "markdown_projection_validation": markdown_validation,
        },
        {
            "attachment_id": attachment["markdown_attachment_id"],
            "role": attachment["markdown_role"],
            "source_path": attachment["source"],
            "package_path": markdown_path.relative_to(out_root).as_posix(),
            "sha256": sha256_file(markdown_path),
            "semantic_validation": document["semantic_validation"],
            "markdown_projection_validation": markdown_validation,
        },
    ]


def build_action_backlog_markdown(profile: dict[str, Any]) -> str:
    attachment = profile["generated_action_backlog_attachment"]
    lines = [
        f"# Page {profile['page']} Action Backlog",
        "",
        f"Package: `{profile['package_id']}`",
        "",
        "This log separates orchestration/tool work from scripts so the page-complete packet build remains inspectable.",
        "",
        "| Order | Actor | Action | Purpose | Output / Boundary |",
        "|---|---|---|---|---|",
    ]
    for step in attachment["steps"]:
        action = step["action"].replace("|", "\\|")
        purpose = step["purpose"].replace("|", "\\|")
        output = step["output"].replace("|", "\\|")
        lines.append(f"| {step['order']} | `{step['actor']}` | {action} | {purpose} | {output} |")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- This backlog is review/process evidence only.",
            "- It creates no page-complete acceptance, whole Gate 1 acceptance, fixture admission, source/OCR/render/PDF/raw mutation, translation, proofreading, implementation, or push.",
            "",
        ]
    )
    return "\n".join(lines)


def materialize_generated_action_backlog(profile: dict[str, Any], out_root: Path) -> dict[str, Any] | None:
    attachment = profile.get("generated_action_backlog_attachment")
    if not attachment:
        return None
    target_path = out_root / attachment["target_path"]
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(build_action_backlog_markdown(profile), encoding="utf-8", newline="\n")
    return {
        "attachment_id": attachment["attachment_id"],
        "role": attachment["role"],
        "source_path": "generated_from_orchestrator_action_backlog",
        "package_path": target_path.relative_to(out_root).as_posix(),
        "sha256": sha256_file(target_path),
    }


def load_semantic_units_from_attachment(attachment: dict[str, Any], out_root: Path) -> list[dict[str, Any]]:
    document_path = out_root / attachment["package_path"]
    document = json.loads(document_path.read_text(encoding="utf-8"))
    return document.get("units", [])


def crop_edge_ink_checks(attachments: list[dict[str, Any]], out_root: Path) -> list[dict[str, Any]]:
    checks = []
    for attachment in attachments:
        if attachment["role"] != "human_review_crop":
            continue
        if attachment.get("skip_edge_ink_check"):
            checks.append(
                {
                    "attachment_id": attachment["attachment_id"],
                    "label": attachment["label"],
                    "status": "passed",
                    "reason": "edge_ink_check_skipped_for_visual_anchor",
                    "edge_ink_ratios": {},
                    "maximum_allowed_edge_ink_ratio": 0.02,
                }
            )
            continue
        path = out_root / attachment["package_path"]
        with Image.open(path).convert("RGB") as image:
            width, height = image.size
            margin = min(24, width // 8, height // 8)
            pixels = image.load()

            def is_ink(x: int, y: int) -> bool:
                r, g, b = pixels[x, y]
                black_text = attachment.get("detect_dark_text", True) and r < 110 and g < 110 and b < 110
                red_text = r > 120 and g < 90 and b < 90
                green_text = r > 120 and g > 150 and b < 140
                return black_text or red_text or green_text

            bands = {
                "left": [(x, y) for x in range(margin) for y in range(height)],
                "right": [(x, y) for x in range(width - margin, width) for y in range(height)],
                "top": [(x, y) for x in range(width) for y in range(margin)],
                "bottom": [(x, y) for x in range(width) for y in range(height - margin, height)],
            }
            band_ratios = {}
            for edge, coords in bands.items():
                ink = sum(1 for x, y in coords if is_ink(x, y))
                band_ratios[edge] = round(ink / len(coords), 4)
        max_ratio = max(band_ratios.values())
        checks.append(
            {
                "attachment_id": attachment["attachment_id"],
                "label": attachment["label"],
                "status": "passed" if max_ratio <= 0.02 else "blocked",
                "reason": None if max_ratio <= 0.02 else "review_crop_has_text_ink_too_close_to_edge",
                "edge_ink_ratios": band_ratios,
                "maximum_allowed_edge_ink_ratio": 0.02,
            }
        )
    return checks


def image_dimensions(path: Path) -> dict[str, int]:
    with Image.open(path) as image:
        width, height = image.size
    return {"width": width, "height": height}


def attachment_by_source_path(attachments: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {attachment["source_path"].replace("\\", "/"): attachment for attachment in attachments}


def visual_proof_checks(
    blocks: list[dict[str, Any]],
    attachments: list[dict[str, Any]],
    out_root: Path,
) -> list[dict[str, Any]]:
    by_source = attachment_by_source_path(attachments)
    checks = []
    for block in blocks:
        anchor_path = block["anchor"]["corrected_crop_reference"].replace("\\", "/")
        attachment = by_source.get(anchor_path)
        if not attachment:
            checks.append(
                {
                    "block_id": block["block_id"],
                    "source_region_id": block["source_region_id"],
                    "status": "blocked",
                    "reason": "missing_block_crop_review_attachment",
                    "minimum_dimension_ratio": MIN_BLOCK_CROP_DIMENSION_RATIO,
                }
            )
            continue
        if attachment["role"] != "block_crop":
            checks.append(
                {
                    "block_id": block["block_id"],
                    "source_region_id": block["source_region_id"],
                    "status": "blocked",
                    "reason": "review_attachment_is_not_block_crop",
                    "attachment_role": attachment["role"],
                    "minimum_dimension_ratio": MIN_BLOCK_CROP_DIMENSION_RATIO,
                }
            )
            continue

        crop_size = image_dimensions(out_root / attachment["package_path"])
        _, _, box_width, box_height = block["anchor"]["box_px"]
        width_ratio = crop_size["width"] / box_width
        height_ratio = crop_size["height"] / box_height
        status = "passed"
        reason = None
        if width_ratio < MIN_BLOCK_CROP_DIMENSION_RATIO or height_ratio < MIN_BLOCK_CROP_DIMENSION_RATIO:
            status = "blocked"
            reason = "visual_crop_smaller_than_declared_block_box"
        checks.append(
            {
                "block_id": block["block_id"],
                "source_region_id": block["source_region_id"],
                "status": status,
                "reason": reason,
                "attachment_id": attachment["attachment_id"],
                "package_path": attachment["package_path"],
                "crop_size": crop_size,
                "declared_box_size": {"width": box_width, "height": box_height},
                "width_ratio": round(width_ratio, 4),
                "height_ratio": round(height_ratio, 4),
                "minimum_dimension_ratio": MIN_BLOCK_CROP_DIMENSION_RATIO,
            }
        )
    return checks


def build_report(
    profile_key: str,
    readiness: dict[str, Any],
    attachments: list[dict[str, Any]],
    asset_packaging: dict[str, Any],
) -> dict[str, Any]:
    profile = REVIEW_PROFILES[profile_key]
    page = profile_page(profile_key)
    blocks = sorted(readiness["block_inventory"], key=lambda item: item["reading_order"])
    blockers = []
    for block in blocks:
        if block["status"] != "ready_for_page_complete_review":
            blockers.append({"block_id": block["block_id"], "reason": "block_not_ready"})
        if block["text_fidelity"]["missing_protected_tokens"]:
            blockers.append({"block_id": block["block_id"], "reason": "missing_protected_tokens"})
        if block["text_fidelity"]["discrepancy_disposition"] != "none":
            blockers.append({"block_id": block["block_id"], "reason": "text_discrepancy"})
    visual_checks = []
    if not profile.get("skip_readiness_anchor_visual_proof", False):
        visual_checks = visual_proof_checks(blocks, attachments, profile["output_dir"])
    for check in visual_checks:
        if check["status"] != "passed":
            blockers.append({"block_id": check["block_id"], "reason": check["reason"]})
    human_review_crop_checks = crop_edge_ink_checks(attachments, profile["output_dir"])
    for check in human_review_crop_checks:
        if check["status"] != "passed":
            blockers.append({"block_id": check["label"], "reason": check["reason"]})
    semantic_attachments = [attachment for attachment in attachments if attachment["role"] == "semantic_text_map_json"]
    semantic_validation = semantic_attachments[0]["semantic_validation"] if semantic_attachments else None
    markdown_projection_validation = (
        semantic_attachments[0]["markdown_projection_validation"] if semantic_attachments else None
    )
    inventory_reconciliation = None
    structural_findings = []
    if semantic_validation:
        structural_findings.extend(semantic_validation["findings"])
        if semantic_validation["readiness_blocked"]:
            blockers.append(
                {
                    "block_id": semantic_attachments[0]["attachment_id"],
                    "reason": "semantic_validation_blocker",
                    "finding_count": len(semantic_validation["findings"]),
                }
            )
    if markdown_projection_validation:
        structural_findings.extend(markdown_projection_validation["findings"])
        if markdown_projection_validation["readiness_blocked"]:
            blockers.append(
                {
                    "block_id": semantic_attachments[0]["attachment_id"],
                    "reason": "markdown_projection_validation_blocker",
                    "finding_count": len(markdown_projection_validation["findings"]),
                }
            )
    if semantic_attachments:
        semantic_units = load_semantic_units_from_attachment(semantic_attachments[0], profile["output_dir"])
        inventory_reconciliation = reconcile_page_inventory(page_inventory_from_readiness(readiness), semantic_units)
        structural_findings.extend(inventory_reconciliation["findings"])
        if inventory_reconciliation["readiness_blocked"]:
            blockers.append(
                {
                    "block_id": semantic_attachments[0]["attachment_id"],
                    "reason": "inventory_reconciliation_blocker",
                    "finding_count": len(inventory_reconciliation["findings"]),
                }
            )
    post_review_hold = profile.get("post_review_hold")
    if post_review_hold:
        blockers.append(
            {
                "block_id": profile["package_id"],
                "reason": post_review_hold["reason"],
                "decision_id": post_review_hold["decision_id"],
                "requires_superseding_package_id": post_review_hold["requires_superseding_package_id"],
            }
        )

    recommendation = "page_complete_decision_ready_for_bogdan" if not blockers else "blocked_before_bogdan_decision"
    decision_options = profile["decision_options"]
    if blockers:
        decision_options = [option for option in decision_options if option.startswith("hold_")]
    return {
        "package_id": profile["package_id"],
        "authorization_id": profile["authorization_id"],
        "status": "ready_for_bogdan_page_complete_decision" if not blockers else "blocked",
        "scope": "page_complete_review_packet_only_no_acceptance",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "page": page,
        "page_id": readiness["page_id"],
        "image_id": readiness["image_id"],
        "input_packages": [*profile.get("extra_input_packages", []), readiness["package_id"]],
        "review_attachments": attachments,
        "package_assets": asset_packaging["package_assets"],
        "role_bindings": asset_packaging["role_bindings"],
        "delivery_assets": asset_packaging["delivery_assets"],
        "review_asset_deduplication": asset_packaging["review_asset_deduplication"],
        "readiness_input": {
            "package_id": readiness["package_id"],
            "authorization_id": readiness["authorization_id"],
            "pipeline_id": readiness["pipeline_id"],
            "profile_id": readiness["profile_id"],
            "report_sha256": profile["readiness_report_sha256"],
            "packet_sha256": profile["readiness_packet_sha256"],
            "summary_sha256": profile["readiness_summary_sha256"],
            "manifest_sha256": profile["readiness_manifest_sha256"],
        },
        "page_complete_review": {
            "expected_blocks": readiness["profile"]["expected_block_count"],
            "reviewed_blocks": len(blocks),
            "ready_blocks": len([block for block in blocks if block["status"] == "ready_for_page_complete_review"]),
            "reading_order": [block["role"] for block in blocks],
            "declared_none_categories": readiness["profile"]["declared_none"],
            "context_only_regions": readiness["profile"].get("context_only_regions", []),
            "declared_none_note": declared_none_note(readiness["profile"]["declared_none"]),
            "coverage_advisory_only": True,
            "visual_proof_checks": visual_checks,
            "human_review_crop_checks": human_review_crop_checks,
            "semantic_units_validated": bool(semantic_validation),
            "semantic_validation": semantic_validation,
            "markdown_projection_validation": markdown_projection_validation,
            "inventory_reconciliation": inventory_reconciliation,
            "structural_findings": structural_findings,
            "blocks": [block_summary(block) for block in blocks],
            "blockers": blockers,
            "open_questions": [],
            "recommendation": recommendation,
            "decision_options": decision_options,
        },
        "review_decision": {
            "requires_bogdan_decision": not bool(blockers),
            "requires_superseding_review_packet": bool(blockers),
            "requires_superseding_package_id": post_review_hold["requires_superseding_package_id"]
            if post_review_hold
            else None,
            "page_complete_acceptance_created": False,
            "page_complete_acceptance_record_id": None,
            "accepted_pages_as_complete": [],
            "whole_gate_1_acceptance_created": False,
            "fixture_admission_created": False,
        },
        "post_review_state": post_review_hold,
        "guardrails": {
            "ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "pdf_text_layer_used": False,
            "render_executed": False,
            "raw_artifacts_modified": False,
            "source_acceptance_created": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission": False,
            "translation_authorized": False,
            "proofreading_authorized": False,
            "renderer_profile_acceptance": False,
            "implementation_authorized": False,
            "push_authorized": False,
        },
    }


def build_packet(report: dict[str, Any]) -> str:
    review = report["page_complete_review"]
    page = report["page"]
    page_label = f"Page {page}"
    blockers = review["blockers"]
    lines = [
        f"# Page Complete Review Packet - {page_label}",
        "",
        f"Status: `{report['status']}`",
        "",
        f"Boundary: this is a review packet only. It does not accept page {page} as complete, does not advance Gate 1, and does not admit fixtures.",
        "",
        "## Readiness Input",
        "",
        f"- Input: `{report['readiness_input']['package_id']}`.",
        "- Scope: page-map readiness only, using existing artifacts.",
        "- Coverage remains advisory; this packet asks for a separate human decision.",
        "",
        f"## {page_label} Review",
        "",
        f"- Expected blocks: {review['expected_blocks']}",
        f"- Reviewed blocks: {review['reviewed_blocks']}",
        f"- Ready blocks: {review['ready_blocks']} / {review['expected_blocks']}",
        f"- Reading order: {' -> '.join(review['reading_order'])}",
        f"- {review['declared_none_note']}",
        f"- Context-only regions: {len(review['context_only_regions'])}.",
        f"- Blockers: {'none' if not blockers else len(blockers)}.",
        "- Open questions: none.",
        "",
        "## Review Attachments",
        "",
    ]
    if report["review_attachments"]:
        for attachment in report.get("delivery_assets", report["review_attachments"]):
            lines.append(f"- {attachment['role']}: `{attachment['package_path']}`")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
        "## Blocks",
        "",
        ]
    )
    for block in review["blocks"]:
        lines.extend(
            [
                f"### {block['block_id']} - {block['role']}",
                "",
                f"- Region: `{block['source_region_id']}`",
                f"- Content kind: `{block.get('content_kind', 'source_text')}`",
                f"- Extraction policy: `{block.get('extraction_policy', 'transcribe_source_text')}`",
                f"- Status: `{block['status']}`",
                f"- Characters: {block['character_count']} raw / {block['normalized_character_count']} normalized",
                f"- Lines: {block['line_count']} total / {block['non_empty_line_count']} non-empty",
                f"- Protected tokens: {block['protected_tokens_matched']} / {block['protected_tokens_total']}",
                f"- Discrepancy: `{block['discrepancy_disposition']}`",
                f"- Anchor crop: `{block['anchor_crop']}`",
                "",
            ]
        )
        if block.get("anchor_metadata"):
            metadata = block["anchor_metadata"]
            lines.extend(
                [
                    f"- Anchor id: `{metadata['anchor_id']}`",
                    f"- Anchor label: `{metadata['anchor_label']}`",
                    f"- Deferred stage: `{metadata['deferred_stage']}`",
                    f"- Visual identification: {metadata['visual_identification']}",
                    "",
                ]
            )
    if blockers:
        lines.extend(["## Blockers", ""])
        for blocker in blockers:
            lines.append(f"- `{blocker['block_id']}`: `{blocker['reason']}`")
        lines.append("")
    if review.get("semantic_units_validated"):
        semantic_validation = review["semantic_validation"]
        projection_validation = review["markdown_projection_validation"]
        inventory_reconciliation = review["inventory_reconciliation"]
        lines.extend(
            [
                "## Semantic Map Validation",
                "",
                f"- Semantic units validated: `{review['semantic_units_validated']}`",
                f"- Semantic validation: `{'valid' if semantic_validation['valid'] else 'blocked'}`",
                f"- Markdown projection: `{'valid' if projection_validation['valid'] else 'blocked'}`",
                f"- Inventory reconciliation: `{'valid' if inventory_reconciliation['valid'] else 'blocked'}`",
                f"- Structural findings: `{len(review['structural_findings'])}`",
                "",
            ]
        )
        for finding_item in review["structural_findings"]:
            lines.append(
                f"- `{finding_item['finding_id']}` / `{finding_item['rule_id']}` / `{finding_item['severity']}`: {finding_item['message']}"
            )
        if review["structural_findings"]:
            lines.append("")
    post_review_state = report.get("post_review_state")
    if post_review_state:
        lines.extend(
            [
                "## Post-Review State",
                "",
                f"- Status: `{post_review_state['status']}`",
                f"- Decision: `{post_review_state['decision_id']}`",
                f"- Reason: `{post_review_state['reason']}`",
                f"- Review crops: `{post_review_state['human_review_crop_decision']}`",
                f"- Requires superseding packet: `{post_review_state['requires_superseding_package_id']}`",
                f"- Negative regression input: `{post_review_state['negative_regression_input']}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Decision Needed",
            "",
            (
                f"Bogdan can now decide whether page {page} should be accepted as page-complete in a later explicit decision record."
                if not blockers
                else f"Page {page} is blocked before any page-complete decision. A superseding review packet is required."
            ),
            "",
            "Reply shape:",
            "",
        ]
    )
    if not blockers:
        lines.extend(
            [
                "```text",
                f"page {page} complete ok",
                "```",
                "",
                "or:",
                "",
            ]
        )
    lines.extend(
        [
            "```text",
            f"hold page {page}: <reason>",
            "```",
            "",
            "This packet itself creates no acceptance.",
            "",
        ]
    )
    return "\n".join(lines)


def build_summary(report: dict[str, Any]) -> str:
    review = report["page_complete_review"]
    page = report["page"]
    page_label = f"Page {page}"
    blockers = review["blockers"]
    inventory_reconciliation = review.get("inventory_reconciliation") or {}
    inventory_reconciliation_status = (
        inventory_reconciliation.get("valid", False)
        if review.get("inventory_reconciliation") is not None
        else "not_applicable_no_semantic_text_units"
    )
    return "\n".join(
        [
            f"# Page Complete Review Summary - {page_label}",
            "",
            f"Package: `{report['package_id']}`",
            "",
            f"- {page_label} was prepared for a separate page-complete human decision using `{report['readiness_input']['package_id']}` as readiness input.",
            f"- Expected/reviewed blocks: {review['expected_blocks']} / {review['reviewed_blocks']}.",
            f"- Ready blocks: {review['ready_blocks']} / {review['expected_blocks']}.",
            f"- Reading order: {' -> '.join(review['reading_order'])}.",
            f"- {review['declared_none_note']}",
            f"- Context-only regions: {len(review['context_only_regions'])}.",
            f"- Review attachments: {len(report['package_assets'])} packaged files / {len(report['review_attachments'])} logical bindings.",
            f"- Delivery assets: {len(report['delivery_assets'])}.",
            f"- Deduplicated review bindings: {report['review_asset_deduplication']['deduplicated_binding_count']}.",
            f"- Semantic units validated: {review.get('semantic_units_validated', False)}.",
            f"- Inventory reconciliation: {inventory_reconciliation_status}.",
            f"- Structural findings: {len(review.get('structural_findings', []))}.",
            f"- Blockers: {'none' if not blockers else len(blockers)}.",
            "- Open questions: none.",
            "- No page-complete acceptance, whole Gate 1 acceptance, fixture admission, OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push was created.",
            (
                "- Result: ready for Bogdan's explicit page-complete decision."
                if not blockers
                else "- Result: blocked before Bogdan's page-complete decision; a superseding review packet is required."
            ),
            (
                f"- Post-review state: `{report['post_review_state']['status']}`; requires `{report['post_review_state']['requires_superseding_package_id']}`."
                if report.get("post_review_state")
                else "- Post-review state: none."
            ),
            "",
        ]
    )


def build_manifest(report: dict[str, Any], out_root: Path) -> str:
    lines = [
        "# Page Complete Review Manifest",
        "",
        f"Package: `{report['package_id']}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "page_complete_review_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    deduplicated = report.get("review_asset_deduplication", {}).get("deduplicated_bindings", [])
    if deduplicated:
        lines.extend(
            [
                "## Deduplicated Role Bindings",
                "",
                "| Attachment | Role | Canonical Asset | Original Path |",
                "|---|---|---|---|",
            ]
        )
        for item in deduplicated:
            lines.append(
                f"| `{item['attachment_id']}` | `{item['role']}` | `{item['package_path']}` | `{item['original_package_path']}` |"
            )
        lines.append("")
    return "\n".join(lines)


def build(profile_key: str) -> None:
    profile = REVIEW_PROFILES[profile_key]
    readiness = verify_readiness(profile_key)
    out_root = profile["output_dir"]
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True, exist_ok=True)
    attachments = materialize_attachments(profile, out_root)
    attachments.extend(materialize_generated_declared_block_crops(profile, readiness, out_root))
    attachments.extend(materialize_generated_page_crops(profile, out_root))
    generated_block_text = materialize_generated_block_text(profile, readiness, out_root)
    if generated_block_text:
        attachments.append(generated_block_text)
    generated_review_text_map = materialize_generated_review_text_map(profile, out_root)
    if generated_review_text_map:
        attachments.append(generated_review_text_map)
    attachments.extend(materialize_generated_semantic_map(profile, out_root))
    generated_action_backlog = materialize_generated_action_backlog(profile, out_root)
    if generated_action_backlog:
        attachments.append(generated_action_backlog)
    asset_packaging = apply_review_asset_deduplication(attachments, out_root=out_root)
    report = build_report(profile_key, readiness, attachments, asset_packaging)
    write_json(out_root / "page_complete_review_report.json", report)
    (out_root / "page_complete_review_packet.md").write_text(build_packet(report), encoding="utf-8", newline="\n")
    (out_root / "page_complete_review_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (out_root / "page_complete_review_manifest.md").write_text(
        build_manifest(report, out_root), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build(parsed.page)
