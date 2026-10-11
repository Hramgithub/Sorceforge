from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image

from source_reconstruction_crop_guardrails import crop_with_guardrail, validate_crop_layout


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "prepare_source_reconstruction_p002_assisted_draft.py"
TEST_PATH = ROOT / "tests" / "test_source_reconstruction_p002_assisted_draft.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRNS_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
REF_ROOT = OUT_ROOT / "corrected_region_refs"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001"
DRAFT_ID = "SRAD-G1-VIRAL-002"
SRNS_REPORT_SHA256 = "1A9A693883277635B02E02F143284280C1FBA1F928FF950843586B8A1C5EC224"
SRNS_MANIFEST_SHA256 = "B4D8E6AA3D08DFD78D16F72FD3774B57051F4AABCE32062C3B36E924466C6DCD"
PAGE_002_SHA256 = "ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9"

PAGE_IMAGE = TRIAL_ROOT / "images" / "page_002.png"

RECORDS = [
    {
        "question_id": "1",
        "assisted_record_id": "SRAD-G1-VIRAL-002-R01",
        "source_region_id": "PRM-G1-VIRAL-001-P002-R01",
        "srns_region_id": "SRNS-G1-VIRAL-002-R01",
        "corrected_crop_id": "SRAD-G1-VIRAL-002-R01-C01",
        "box_px": [180, 90, 2190, 1860],
        "initial_user_route": "text_present_but_too_long_for_manual_transcription",
        "crop_correction_note": "wider split crop; excludes lower footer/legal block overlap",
        "draft_text_basis": "assistant_visual_transcription_draft_from_corrected_crop",
        "draft_text": """Credits

Writing
Alex Guillotte, Buds RPG Review

Illustrations, Design & Layout
Alex Guillotte

Editing
Matthew Pook

Additional Editing
Keith Mageau

Language Consultant
Luca Alexander Volpino

Play Testers
Adrian Jones, Andy Simcock, Brendan Sharples, Christian Frost, Daniel Keegan,
Demonsamurai, DMH, Dragongirl174, Dr Ian "Griff" Griffiths, Fabio Vollono, Halsten Rust,
Ian Christiansen, James Cross, James Crosfield, Jim McCarthy, Keith Mageau, Lee Williams,
Ludovic Chabant, Mark Willoughby, Matthew Pook, Mehvish Ali (WishMoon), Michael Fryda,
Michalis Mandilaras, Molgars, Paul Baldowski, Paul Fricker, Renarion, Richard Marpole,
Scott "OrcusDorkus" Joest, Seth Skorkowsky, Stef1885, Symatt, Tristan Narbrough""",
    },
    {
        "question_id": "2",
        "assisted_record_id": "SRAD-G1-VIRAL-002-R02",
        "source_region_id": "PRM-G1-VIRAL-001-P002-R02",
        "srns_region_id": "SRNS-G1-VIRAL-002-R02",
        "corrected_crop_id": "SRAD-G1-VIRAL-002-R02-C01",
        "box_px": [200, 1980, 2150, 1220],
        "initial_user_route": "text_present_but_too_long_for_manual_transcription",
        "crop_correction_note": "taller lower split crop containing the special-thanks and legal/footer text",
        "draft_text_basis": "assistant_visual_transcription_draft_from_corrected_crop",
        "draft_text": """Special Thanks to Seth Skorkowsky.

In creating this unredacted version of Viral, we've taken some of your cool
ideas, filed off the serial numbers, and made them our own.

(C) Copyright 2022 - Alex Guillotte, Buds RPG Review

Call of Cthulhu is a Trademark of Chaosium Inc.
and is used with their permission via the
OBS Community Content program.

For more information please visit Chaosium's website:
www.Chaosium.com

The Miskatonic Repository Logo is used under license.""",
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
    parser = argparse.ArgumentParser(description="Prepare Viral page 002 assisted source reconstruction draft.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 002 assisted draft is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 002 assisted draft requires {AUTHORIZATION_ID}")


def verify_predecessors() -> dict[str, object]:
    report_path = SRNS_ROOT / "source_reconstruction_next_slice_report.json"
    manifest_path = SRNS_ROOT / "source_reconstruction_next_slice_manifest.md"
    if sha256_file(report_path) != SRNS_REPORT_SHA256:
        raise SystemExit("SRNS report hash mismatch")
    if sha256_file(manifest_path) != SRNS_MANIFEST_SHA256:
        raise SystemExit("SRNS manifest hash mismatch")
    if sha256_file(PAGE_IMAGE) != PAGE_002_SHA256:
        raise SystemExit("page 002 image hash mismatch")

    srns_report = read_json(report_path)
    if srns_report["package_id"] != "SRNS-G1-VIRAL-002":
        raise SystemExit("unexpected SRNS package id")
    if srns_report["candidate_text_created"] is not False if "candidate_text_created" in srns_report else False:
        raise SystemExit("unexpected SRNS candidate text state")
    if srns_report["source_acceptance"] is not False or srns_report["gate_1_advancement"] is not False:
        raise SystemExit("SRNS unexpectedly accepted source or advanced Gate 1")
    if len(srns_report["records"]) != 2:
        raise SystemExit("SRNS did not contain exactly two records")
    return srns_report


def crop_region(image: Image.Image, box_px: list[int], target: Path) -> None:
    crop_with_guardrail(image, box_px, target)


def build() -> None:
    verify_predecessors()
    crop_layout_guardrail = validate_crop_layout(
        RECORDS,
        image_size=(2550, 3300),
        approved_boxes_by_region={
            "PRM-G1-VIRAL-001-P002-R01": [180, 90, 2190, 1860],
            "PRM-G1-VIRAL-001-P002-R02": [200, 1980, 2150, 1220],
        },
        validated_at_stage="SRAD-G1-VIRAL-002.corrected_crop_generation",
    )

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    REF_ROOT.mkdir(parents=True, exist_ok=True)

    output_records = []
    with Image.open(PAGE_IMAGE) as image:
        if image.size != (2550, 3300):
            raise SystemExit("unexpected page 002 image dimensions")
        for record in RECORDS:
            crop_name = f"{record['question_id']}_{record['assisted_record_id']}__{record['corrected_crop_id']}.png"
            crop_path = REF_ROOT / crop_name
            crop_region(image, record["box_px"], crop_path)
            output_records.append(
                {
                    **record,
                    "page_image": PAGE_IMAGE.relative_to(ROOT).as_posix(),
                    "page_image_sha256": PAGE_002_SHA256,
                    "corrected_crop_reference": crop_path.relative_to(ROOT).as_posix(),
                    "corrected_crop_reference_sha256": sha256_file(crop_path),
                    "draft_text_sha256": sha256_text(record["draft_text"]),
                    "requires_bogdan_verification": True,
                    "source_acceptance": False,
                    "qa_acceptance": False,
                    "fixture_admission": False,
                    "gate_1_advancement": False,
                }
            )

    report = {
        "draft_id": DRAFT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "assisted_text_draft_ready_for_bogdan_verification_not_accepted",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_next_slice_id": "SRNS-G1-VIRAL-002",
        "input_next_slice_report_sha256": SRNS_REPORT_SHA256,
        "input_next_slice_manifest_sha256": SRNS_MANIFEST_SHA256,
        "user_review_messages": [
            {
                "telegram_message_id": "351",
                "raw_text": "1 текст, но кроп обрезал текст по ширине, если это важно 2 текст, обрезан по высоте, если важно",
            },
            {
                "telegram_message_id": "356",
                "raw_text": "1 текст, длинный для переписывания; Зацепили второй кроп, далеко вниз зашли; 2 текст, длинный для переписывания",
            },
        ],
        "selected_page": "002",
        "selected_page_image_sha256": PAGE_002_SHA256,
        "selected_scope": "page_002_two_record_assisted_draft_only",
        "records": output_records,
        "crop_layout_guardrail": crop_layout_guardrail,
        "summary": {
            "records": len(output_records),
            "draft_text_records": len(output_records),
            "accepted_records": 0,
            "blocked_for_bogdan_verification_records": len(output_records),
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "draft_text_created": True,
        "draft_text_is_source_accepted": False,
        "source_acceptance": False,
        "qa_acceptance": False,
        "fixture_admission": False,
        "gate_1_advancement": False,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_p002_assisted_draft_report.json", report)

    draft_lines = [
        "# Page 002 Assisted Source Reconstruction Draft - SRAD-G1-VIRAL-002",
        "",
        "Status: `ready_for_bogdan_verification_not_accepted`",
        "",
        "Boundary: this is assisted draft text only. It is not source acceptance, QA, fixture admission, page-complete acceptance, Gate 1 advancement, translation, proofreading, renderer/profile acceptance, implementation, or push.",
        "",
        "## Verification Questions",
        "",
    ]
    for record in output_records:
        draft_lines.append(f"### {record['question_id']} - {record['source_region_id']}")
        draft_lines.append("")
        draft_lines.append(f"- Corrected crop: `{record['corrected_crop_reference']}`")
        draft_lines.append(f"- Crop correction: {record['crop_correction_note']}")
        draft_lines.append("- Answer shape: `N - ok` or `N - правка: <corrected text>` or `N - blocker: <reason>`")
        draft_lines.append("")
        draft_lines.append("```text")
        draft_lines.append(record["draft_text"])
        draft_lines.append("```")
        draft_lines.append("")
    (OUT_ROOT / "assisted_text_draft_for_bogdan.md").write_text(
        "\n".join(draft_lines), encoding="utf-8", newline="\n"
    )

    manifest_lines = [
        "# Page 002 Assisted Draft Manifest - SRAD-G1-VIRAL-002",
        "",
        "Status: `assisted_text_draft_ready_for_bogdan_verification_not_accepted`",
        "",
        "Boundary: no source acceptance, QA, fixtures, Gate 1 advancement, OCR execution, PDF parsing/rendering, raw OCR mutation, translation, proofreading, implementation, or push.",
        "",
        "## Generator Hashes",
        "",
        f"- Script `{SCRIPT_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(SCRIPT_PATH)}`",
        f"- Test `{TEST_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(TEST_PATH)}`",
        "",
        "## Records",
        "",
        "| Question | Source region | Corrected crop SHA-256 | Draft text SHA-256 |",
        "|---:|---|---|---|",
    ]
    for record in output_records:
        manifest_lines.append(
            f"| {record['question_id']} | `{record['source_region_id']}` | `{record['corrected_crop_reference_sha256']}` | `{record['draft_text_sha256']}` |"
        )
    manifest_lines.extend(["", "## Output Hashes", "", "| Output | SHA-256 |", "|---|---|"])
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_p002_assisted_draft_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_p002_assisted_draft_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
