from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image

from source_reconstruction_crop_guardrails import crop_with_guardrail, validate_crop_layout


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_source_reconstruction_next_slice.py"
TEST_PATH = ROOT / "tests" / "test_source_reconstruction_next_slice.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002"
REF_ROOT = OUT_ROOT / "region_refs"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001"
PACKAGE_ID = "SRNS-G1-VIRAL-002"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-001"
STATUS_REPORT_SHA256 = "4F0AD3C7553863636B6FD15E329815EE26E62329D668C9FA8AC756CE04B24644"
STATUS_PACKET_SHA256 = "4C7EFAFDC60DF52A09F9358AB7F334FC5354B51E95A130F5BC86D42DC0C4BE68"
PRM_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
PAGE_002_SHA256 = "ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9"

PAGE_IMAGE = TRIAL_ROOT / "images" / "page_002.png"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"

REGIONS = [
    {
        "question_id": "1",
        "slice_region_id": "SRNS-G1-VIRAL-002-R01",
        "source_region_id": "PRM-G1-VIRAL-001-P002-R01",
        "page_id": "PG-G1-VIRAL-P002",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P002",
        "region_class": "text_like",
        "candidate_layer": "content_map_candidate",
        "box_px": [520, 350, 1500, 2100],
        "review_prompt": "Transcribe/confirm the centered credits/legal-like text block, or mark blocker.",
        "expected_answer_shape": "1 - text: <transcription> | 1 - blocker: <reason> | 1 - visual-only",
    },
    {
        "question_id": "2",
        "slice_region_id": "SRNS-G1-VIRAL-002-R02",
        "source_region_id": "PRM-G1-VIRAL-001-P002-R02",
        "page_id": "PG-G1-VIRAL-P002",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P002",
        "region_class": "mixed",
        "candidate_layer": "content_map_candidate",
        "box_px": [520, 2480, 1500, 420],
        "review_prompt": "Decide whether the boxed/footer legal-like block is source text and transcribe it if yes.",
        "expected_answer_shape": "2 - text: <transcription> | 2 - visual-only | 2 - blocker: <reason>",
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build the next Viral source reconstruction review slice.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction next-slice package is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction next-slice package requires {AUTHORIZATION_ID}")


def verify_predecessors() -> dict[str, object]:
    status_report_path = STATUS_ROOT / "gate_1_status_packet_report.json"
    status_packet_path = STATUS_ROOT / "gate_1_status_packet.json"
    if sha256_file(status_report_path) != STATUS_REPORT_SHA256:
        raise SystemExit("Gate 1 status packet report hash mismatch")
    if sha256_file(status_packet_path) != STATUS_PACKET_SHA256:
        raise SystemExit("Gate 1 status packet payload hash mismatch")
    if sha256_file(PRM_REPORT) != PRM_SHA256:
        raise SystemExit("provisional region map report hash mismatch")
    if sha256_file(PAGE_IMAGE) != PAGE_002_SHA256:
        raise SystemExit("page 002 image hash mismatch")

    status_report = read_json(status_report_path)
    status_packet = read_json(status_packet_path)
    if status_report["status_packet_id"] != STATUS_PACKET_ID or status_packet["status_packet_id"] != STATUS_PACKET_ID:
        raise SystemExit("unexpected Gate 1 status packet id")
    if status_packet["current_gate_1_state"] != "partial_narrow_source_reconstruction_evidence_accepted":
        raise SystemExit("unexpected Gate 1 status state")
    if status_packet["accepted_evidence"]["source_reconstruction_slice"]["accepted_pages_as_complete"] is not False:
        raise SystemExit("predecessor status packet accepted prior pages as complete")
    if status_packet["whole_gate_1_ready"] is not False:
        raise SystemExit("predecessor status packet says whole Gate 1 is ready")
    if "additional_source_reconstruction_slices" not in status_packet["pending"]:
        raise SystemExit("predecessor status packet does not permit next-slice planning")
    return status_packet


def verify_region_hints() -> None:
    prm_text = PRM_REPORT.read_text(encoding="utf-8")
    for region in REGIONS:
        if region["source_region_id"] not in prm_text:
            raise SystemExit(f"missing predecessor region hint {region['source_region_id']}")


def crop_region(image: Image.Image, box_px: list[int], target: Path) -> None:
    crop_with_guardrail(image, box_px, target)


def build() -> None:
    verify_predecessors()
    verify_region_hints()
    crop_layout_guardrail = validate_crop_layout(
        REGIONS,
        image_size=(2550, 3300),
        validated_at_stage="SRNS-G1-VIRAL-002.review_crop_generation",
    )

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    REF_ROOT.mkdir(parents=True, exist_ok=True)

    with Image.open(PAGE_IMAGE) as image:
        if image.size != (2550, 3300):
            raise SystemExit("unexpected page 002 image dimensions")
        output_records = []
        for region in REGIONS:
            crop_name = f"{region['question_id']}_{region['slice_region_id']}__{region['source_region_id']}.png"
            crop_path = REF_ROOT / crop_name
            crop_region(image, region["box_px"], crop_path)
            output_records.append(
                {
                    **region,
                    "page_image": PAGE_IMAGE.relative_to(ROOT).as_posix(),
                    "page_image_sha256": PAGE_002_SHA256,
                    "crop_reference": crop_path.relative_to(ROOT).as_posix(),
                    "crop_reference_sha256": sha256_file(crop_path),
                    "candidate_text": None,
                    "candidate_text_created": False,
                    "requires_bogdan_review": True,
                    "source_acceptance": False,
                    "qa_acceptance": False,
                    "fixture_admission": False,
                    "gate_1_advancement": False,
                }
            )

    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "next_source_reconstruction_slice_ready_for_bogdan_review_not_accepted",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_status_packet_id": STATUS_PACKET_ID,
        "input_status_packet_report_sha256": STATUS_REPORT_SHA256,
        "input_status_packet_payload_sha256": STATUS_PACKET_SHA256,
        "input_region_map_id": "PRM-G1-VIRAL-001",
        "input_region_map_sha256": PRM_SHA256,
        "selected_page": "002",
        "selected_page_image_sha256": PAGE_002_SHA256,
        "selected_scope": "page_002_two_region_review_packet_only",
        "records": output_records,
        "crop_layout_guardrail": crop_layout_guardrail,
        "summary": {
            "records": len(output_records),
            "source_text_candidate_records": 0,
            "requires_bogdan_review_records": len(output_records),
            "accepted_records": 0,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "previous_accepted_scope_preserved": "G1SP-G1-VIRAL-001 seven-record slice remains unchanged",
        "source_acceptance": False,
        "qa_acceptance": False,
        "fixture_admission": False,
        "gate_1_advancement": False,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-HUMAN-REVIEW-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_next_slice_report.json", report)

    review_lines = [
        "# Source Reconstruction Next Slice Review Packet - SRNS-G1-VIRAL-002",
        "",
        "Status: `ready_for_bogdan_review_not_accepted`",
        "",
        "Boundary: this packet contains page 002 visual crop references only. It creates no candidate text, source acceptance, QA acceptance, fixtures, Gate 1 advancement, OCR, PDF parsing, rendering, implementation, or push.",
        "",
        "Original page reference:",
        "",
        f"- `{PAGE_IMAGE.relative_to(ROOT).as_posix()}`",
        f"- SHA-256: `{PAGE_002_SHA256}`",
        "",
        "## Numbered Questions",
        "",
    ]
    for record in output_records:
        review_lines.append(f"### {record['question_id']} - {record['source_region_id']}")
        review_lines.append("")
        review_lines.append(f"- Crop: `{record['crop_reference']}`")
        review_lines.append(f"- Prompt: {record['review_prompt']}")
        review_lines.append(f"- Answer shape: `{record['expected_answer_shape']}`")
        review_lines.append("")
    (OUT_ROOT / "human_review_packet.md").write_text("\n".join(review_lines), encoding="utf-8", newline="\n")

    manifest_lines = [
        "# Source Reconstruction Next Slice Manifest - SRNS-G1-VIRAL-002",
        "",
        "Status: `next_source_reconstruction_slice_ready_for_bogdan_review_not_accepted`",
        "",
        "Boundary: page 002 two-region packet only; no source acceptance, QA, fixtures, Gate 1 advancement, OCR, PDF parsing, rendering, translation, proofreading, implementation, or push.",
        "",
        "## Generator Hashes",
        "",
        f"- Script `{SCRIPT_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(SCRIPT_PATH)}`",
        f"- Test `{TEST_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(TEST_PATH)}`",
        "",
        "## Records",
        "",
        "| Question | Region | Crop SHA-256 |",
        "|---:|---|---|",
    ]
    for record in output_records:
        manifest_lines.append(
            f"| {record['question_id']} | `{record['source_region_id']}` | `{record['crop_reference_sha256']}` |"
        )
    manifest_lines.extend(["", "## Output Hashes", "", "| Output | SHA-256 |", "|---|---|"])
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_next_slice_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_next_slice_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
