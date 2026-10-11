from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image

from display_structure_labels import format_draft_structure_semantics
from source_reconstruction_crop_guardrails import crop_with_guardrail, validate_crop_layout


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_p002_completion_and_next_review.py"
TEST_PATH = ROOT / "tests" / "test_p002_completion_and_next_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRADV_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
NEXT_REF_ROOT = OUT_ROOT / "next_review_refs"

AUTHORIZATION_ID = "BA-G1-VIRAL-P002-QA-STRUCTURE-SOURCE-AND-NEXT-REVIEW-001"
PACKAGE_ID = "P002C-G1-VIRAL-002"
SRADV_REPORT_SHA256 = "BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52"
SRADV_MANIFEST_SHA256 = "B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A"
SRADV_SUMMARY_SHA256 = "225DC38D81F9BD4133D05823ACDDBED538E5CBA790DEF1A33A4E4AFCCBF7E13D"
PAGE_003_SHA256 = "B6B5A48D498FDEFB050B67E7155E85502010799D05CC10317C9E179CEB97A6BF"
TESSERACT = Path("D:/NRI/.tools/tesseract/tesseract.exe")

P002_STRUCTURE = [
    {
        "question_id": "1",
        "structure_record_id": "SRSS-G1-VIRAL-002-R01",
        "spans": [
            {"text": "Credits", "semantic_role": "credits_title", "heading_level": "h1", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "large", "confidence": "medium"},
            {"text": "Writing", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "Illustrations, Design & Layout", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "Editing", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "Additional Editing", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "Language Consultant", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "Play Testers", "semantic_role": "credit_role_label", "heading_level": "none", "bold": "likely", "italic": False, "underline": False, "centered": True, "font_scale": "normal", "confidence": "medium"},
            {"text": "credit names", "semantic_role": "credit_value_list", "heading_level": "none", "bold": "unknown", "italic": "unknown", "underline": "unknown", "centered": True, "font_scale": "normal", "confidence": "medium"},
        ],
    },
    {
        "question_id": "2",
        "structure_record_id": "SRSS-G1-VIRAL-002-R02",
        "spans": [
            {"text": "Special Thanks to Seth Skorkowsky.", "semantic_role": "special_thanks_sentence", "heading_level": "none", "bold": "unknown", "italic": "unknown", "underline": False, "centered": "unknown", "font_scale": "normal", "confidence": "high"},
            {"text": "In creating this unredacted version of Viral...", "semantic_role": "special_thanks_body", "heading_level": "none", "bold": False, "italic": False, "underline": False, "centered": "unknown", "font_scale": "normal", "confidence": "medium"},
            {"text": "(C) Copyright 2022 - Alex Guillotte, Buds RPG Review", "semantic_role": "copyright_notice", "heading_level": "none", "bold": False, "italic": False, "underline": False, "centered": "unknown", "font_scale": "small_or_normal", "confidence": "medium"},
            {"text": "Call of Cthulhu is a Trademark of Chaosium Inc.", "semantic_role": "trademark_notice", "heading_level": "none", "bold": False, "italic": False, "underline": False, "centered": "unknown", "font_scale": "small_or_normal", "confidence": "medium"},
            {"text": "www.Chaosium.com", "semantic_role": "publisher_url", "heading_level": "none", "bold": False, "italic": False, "underline": False, "centered": "unknown", "font_scale": "small_or_normal", "confidence": "medium"},
            {"text": "The Miskatonic Repository Logo is used under license.", "semantic_role": "logo_license_notice", "heading_level": "none", "bold": False, "italic": False, "underline": False, "centered": "unknown", "font_scale": "small_or_normal", "confidence": "medium"},
        ],
    },
]

NEXT_REVIEW_REGIONS = [
    {
        "review_id": "SRCR-G1-VIRAL-003-R01",
        "source_region_id": "PRM-G1-VIRAL-001-P003-R01",
        "box_px": [500, 130, 1550, 650],
        "draft_structure": [{"semantic_role": "title_heading_like", "heading_level": "h1_candidate", "bold": "unknown", "italic": "unknown", "underline": "unknown"}],
        "draft_text_override": "SPEKTRAL\nKREW",
        "draft_text_basis": "assistant_visual_transcription_draft_from_existing_page_image_after_crop_remediation",
    },
    {
        "review_id": "SRCR-G1-VIRAL-003-R02",
        "source_region_id": "PRM-G1-VIRAL-001-P003-R02",
        "box_px": [270, 860, 2050, 2240],
        "draft_structure": [{"semantic_role": "body_text", "heading_level": "none", "bold": "unknown", "italic": "unknown", "underline": "unknown"}],
        "draft_text_override": """OK guys, here's the thing. Get your passports ready because we are going to
Italy baby! The Old Country! So, according to Maya, we are just one live stream
away from hitting the one million sub mark. You know what that means? Better
sponsorship, getting on talk shows... maybe even a TV deal! More green on the table!
It's so close I can fucking TASTE it.

So Maya hits me up and tells me about this island, see, just off the west coast of Italy.
If you look on Google Maps, it's got nuthin' on it, but on this map she grabbed from
one of her people online it's got buildings and trees and what looks like a bombed-
out chapel. This island had this order of monks living on it... the Order of the Lamb
of the Living Jesus or some shit... anyway this island has been populated since the
Bronze Age. This order, they took in the sick when the plague punched Europe in the
face back in the day. I mean if anywhere is going to be haunted it's this place right?
This place makes Poveglia look like a frickin' kids movie!

So here's the plan. We fly out next week. I've got the gear being shipped over there
PRIORITY. When we arrive in the local town, Maya has arranged for someone to get
us to the island. From there we will set up and do a live broadcast right under the
dumb noses of the Eye-talian Navy. They'll never even know we were there.

Now Hyeon - I know, I know... you're going to mention signals and all that tech stuff. I
get it my man. We're screwed if we get there and can't broadcast. Don't worry brother
- I've got us covered. See, it turns out there is an old abandoned listening post from
the second World War there. Maya has paid for someone local to break in there and
hook it up with all the right cables and shit so we can spit out a signal! Should be A1
crystal clear baby!

OK - so any questions?""",
        "draft_text_basis": "assistant_visual_transcription_draft_from_existing_page_image_after_crop_remediation",
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build page 002 QA/structure/source rollup and next draft review packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("p002 completion and next review is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"p002 completion and next review requires {AUTHORIZATION_ID}")


def verify_predecessor() -> dict[str, object]:
    if sha256_file(SRADV_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json") != SRADV_REPORT_SHA256:
        raise SystemExit("SRADV report hash mismatch")
    if sha256_file(SRADV_ROOT / "source_reconstruction_p002_assisted_draft_verify_manifest.md") != SRADV_MANIFEST_SHA256:
        raise SystemExit("SRADV manifest hash mismatch")
    if sha256_file(SRADV_ROOT / "assisted_draft_human_verification_summary.md") != SRADV_SUMMARY_SHA256:
        raise SystemExit("SRADV summary hash mismatch")
    report = read_json(SRADV_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json")
    if report["verification_id"] != "SRADV-G1-VIRAL-002":
        raise SystemExit("unexpected SRADV verification id")
    if len(report["records"]) != 2:
        raise SystemExit("SRADV did not contain exactly two records")
    return report


def run_tesseract(path: Path) -> str:
    if not TESSERACT.exists():
        raise SystemExit("local tesseract executable missing")
    result = subprocess.run([str(TESSERACT), str(path), "stdout", "--psm", "6"], capture_output=True, check=True)
    return result.stdout.decode("utf-8", "replace").replace("\r\n", "\n").strip()


def crop_page(image: Image.Image, box_px: list[int], target: Path) -> None:
    crop_with_guardrail(image, box_px, target)


def build_next_review_packet() -> list[dict[str, object]]:
    page = TRIAL_ROOT / "images" / "page_003.png"
    if sha256_file(page) != PAGE_003_SHA256:
        raise SystemExit("page 003 image hash mismatch")
    crop_layout_guardrail = validate_crop_layout(
        NEXT_REVIEW_REGIONS,
        image_size=(2550, 3300),
        approved_boxes_by_region={
            "SRCR-G1-VIRAL-003-R01": [500, 130, 1550, 650],
            "SRCR-G1-VIRAL-003-R02": [270, 860, 2050, 2240],
        },
        validated_at_stage="SRCR-G1-VIRAL-003.review_crop_generation",
    )
    NEXT_REF_ROOT.mkdir(parents=True, exist_ok=True)
    records = []
    with Image.open(page) as image:
        for index, region in enumerate(NEXT_REVIEW_REGIONS, start=1):
            crop_path = NEXT_REF_ROOT / f"{index}_{region['review_id']}.png"
            crop_page(image, region["box_px"], crop_path)
            draft_text = region.get("draft_text_override") or run_tesseract(crop_path)
            records.append(
                {
                    **region,
                    "page": "003",
                    "page_image": page.relative_to(ROOT).as_posix(),
                    "page_image_sha256": PAGE_003_SHA256,
                    "crop_reference": crop_path.relative_to(ROOT).as_posix(),
                    "crop_reference_sha256": sha256_file(crop_path),
                    "draft_text": draft_text,
                    "draft_text_sha256": sha256_text(draft_text),
                    "draft_text_basis": region.get("draft_text_basis", "local_tesseract_ocr_draft_from_existing_page_image"),
                    "status": "draft_for_bogdan_review_not_accepted",
                    "source_acceptance": False,
                    "page_complete_acceptance": False,
                    "gate_1_advancement": False,
                }
            )
    return records, crop_layout_guardrail


def build() -> None:
    sradv = verify_predecessor()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    verified_records = sradv["records"]
    next_records, next_crop_layout_guardrail = build_next_review_packet()

    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_accepted_as_two_record_slice_next_review_packet_ready",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_verification_id": "SRADV-G1-VIRAL-002",
        "input_verification_report_sha256": SRADV_REPORT_SHA256,
        "input_verification_manifest_sha256": SRADV_MANIFEST_SHA256,
        "input_verification_summary_sha256": SRADV_SUMMARY_SHA256,
        "user_authority": {
            "telegram_message_id": "419",
            "raw_text": "Do the whole plan 1-6, use Sol/Terra and tests, commit, then prepare next review packet with text, structure, semantics, and crop.",
        },
        "qa": {
            "qa_id": "SRADQ-G1-VIRAL-002",
            "status": "passed",
            "records": 2,
            "verified_message_id": "377",
            "source_acceptance_created": False,
        },
        "structure_semantics": {
            "structure_id": "SRSS-G1-VIRAL-002",
            "status": "accepted_as_structure_metadata_for_two_records",
            "records": P002_STRUCTURE,
            "special_thanks_heading_level": "none",
        },
        "structure_qa": {
            "structure_qa_id": "SRSSQ-G1-VIRAL-002",
            "status": "passed",
            "renderer_profile_acceptance": False,
        },
        "source_acceptance_record": {
            "source_acceptance_id": "SRSA-G1-VIRAL-002",
            "status": "accepted_two_page_002_records_only",
            "accepted_records": 2,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "rollup": {
            "rollup_id": "G1SRER-G1-VIRAL-002",
            "status": "second_source_reconstruction_slice_rolled_up",
            "prior_accepted_records": 7,
            "new_accepted_records": 2,
            "total_accepted_records": 9,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "next_review_packet": {
            "review_packet_id": "SRCR-G1-VIRAL-003",
            "status": "draft_for_bogdan_review_not_accepted",
            "page": "003",
            "records": next_records,
            "crop_layout_guardrail": next_crop_layout_guardrail,
            "ocr_executed_for_draft": False,
            "draft_text_method": "assistant_visual_transcription_draft_after_crop_remediation",
            "remediation_note": "Telegram message 430 reported cropped text; page-003 crop boxes were expanded and the draft text layer was rebuilt for evaluation.",
            "source_acceptance": False,
            "page_complete_acceptance": False,
        },
        "next_review_human_verification": {
            "verification_id": "SRCRV-G1-VIRAL-003",
            "status": "human_verified_draft_packet_not_source_accepted",
            "telegram_message_id": "437",
            "records": [
                {"review_id": "SRCR-G1-VIRAL-003-R01", "decision": "ok"},
                {"review_id": "SRCR-G1-VIRAL-003-R02", "decision": "ok"},
            ],
            "source_acceptance": False,
            "qa_acceptance": False,
            "fixture_admission": False,
            "page_complete_acceptance": False,
            "whole_gate_1_acceptance": False,
        },
        "source_acceptance": True,
        "accepted_records": 2,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "gate_1_advancement": False,
        "gate_1_status_rollup_update": True,
        "fixture_admission": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
    }
    write_json(OUT_ROOT / "p002_completion_and_next_review_report.json", report)

    packet_lines = [
        "# Next Source Reconstruction Review Packet - SRCR-G1-VIRAL-003",
        "",
        "Status: `draft_for_bogdan_review_not_accepted`",
        "",
        "Boundary: this is the next review packet only. Text, structure, semantics, and crop refs are draft review inputs. Page 003 is not accepted as complete, source text is not accepted, QA is not accepted, and Gate 1 is not advanced.",
        "",
        "Bogdan review state: Telegram message `437` says `1 ок`, `2 ок`. This verifies the remediated draft packet for planning input only; it does not accept page 003 source text.",
        "",
        "Answer shape:",
        "",
        "```text",
        "1 - ok / правка / blocker",
        "2 - ok / правка / blocker",
        "```",
        "",
    ]
    for index, record in enumerate(next_records, start=1):
        packet_lines.append(f"## {index} - {record['source_region_id']}")
        packet_lines.append("")
        packet_lines.append(f"- Crop: `{record['crop_reference']}`")
        packet_lines.append(f"- Draft status: `{record['status']}`")
        packet_lines.append(
            f"- {format_draft_structure_semantics(record['draft_structure'][0]['semantic_role'], record['draft_structure'][0]['heading_level'])}"
        )
        packet_lines.append("")
        packet_lines.append("```text")
        packet_lines.append(record["draft_text"])
        packet_lines.append("```")
        packet_lines.append("")
    (OUT_ROOT / "next_review_packet_for_bogdan.md").write_text(
        "\n".join(packet_lines), encoding="utf-8", newline="\n"
    )

    manifest_lines = [
        "# P002 Completion and Next Review Manifest",
        "",
        f"Package: `{PACKAGE_ID}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p002_completion_and_next_review_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "p002_completion_and_next_review_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
