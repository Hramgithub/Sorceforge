from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image

from display_structure_labels import format_draft_structure_semantics
from source_reconstruction_crop_guardrails import crop_with_guardrail, validate_crop_layout


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_source_reconstruction_next_slice_004.py"
TEST_PATH = ROOT / "tests" / "test_source_reconstruction_next_slice_004.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P003A_ROOT = TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004"
REF_ROOT = OUT_ROOT / "region_refs"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004"
PACKAGE_ID = "SRCR-G1-VIRAL-004"
P003A_REPORT_SHA256 = "9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B"
P003A_MANIFEST_SHA256 = "F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87"
P003A_SUMMARY_SHA256 = "860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2"
PRM_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
PAGE_004_SHA256 = "45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88"

PAGE_IMAGE = TRIAL_ROOT / "images" / "page_004.png"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"

P004_RECORDS = [
    {
        "question_id": "1",
        "review_id": "SRCR-G1-VIRAL-004-R01",
        "source_region_id": "PRM-G1-VIRAL-001-P004-R02",
        "page_id": "PG-G1-VIRAL-P004",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P004",
        "region_class": "title_heading_like",
        "candidate_layer": "content_map_candidate",
        "box_px": [720, 330, 1100, 270],
        "draft_structure": [
            {
                "semantic_role": "warning_title",
                "heading_level": "h1_candidate",
                "bold": "yes",
                "italic": False,
                "underline": False,
                "font_scale": "large",
                "confidence": "medium",
            }
        ],
        "draft_text": "WARNING",
        "draft_text_basis": "assistant_visual_transcription_draft_from_existing_page_image",
    },
    {
        "question_id": "2",
        "review_id": "SRCR-G1-VIRAL-004-R02",
        "source_region_id": "PRM-G1-VIRAL-001-P004-R03",
        "page_id": "PG-G1-VIRAL-P004",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P004",
        "region_class": "text_like",
        "candidate_layer": "content_map_candidate",
        "box_px": [330, 630, 1950, 2520],
        "draft_structure": [
            {
                "semantic_role": "safety_warning_body",
                "heading_level": "none",
                "bold": False,
                "italic": False,
                "underline": False,
                "font_scale": "normal",
                "confidence": "medium",
            }
        ],
        "draft_text": """Viral is intended for mature audiences. The Keeper and players should
be aware that this scenario contains situations, scenes, and imagery that
some might find intense, particularly if they have experienced any real
life trauma.

That being said, there is no substitute for good old-fashioned
communication between everyone involved in the game. Before beginning
this scenario, the Keeper should sit down and talk with their players,
making the nature and content of this material very clear. Encourage
the players to ask questions, voice concerns, and vote on whether or not
the scenario is right for the group. It may even be a good idea to have a
secret vote for the sake of personal privacy.

If everyone agrees to play, it is suggested that the Keeper give players
some way to end a scene that they find too intense. This can be done
using a token or safe word of some kind, but however it's done, there
should be no explanation required. The Keeper should simply end the
scene and have the group take a break so that they can resolve the
situation. Possible resolutions could include taking the scene in a
different direction, replaying things differently, or simply 'fading
to black' with a narrative description added by the Keeper.

The Keeper should avoid punishing the player when this happens. So there
should be no significant damage or Sanity loss when the game resumes.

In an extreme case where someone cannot continue the scenario, the session
should end immediately. At that point, the group can discuss options. The
Keeper may be able to rework the scenario, but it's also possible that the
player will have to bow out of the game for the remainder of the story,
or the scenario may have to be set aside altogether.

Remember that roleplaying games are ultimately about having fun. If
anything in this scenario would detract from that fun, it should be
changed or eliminated as the Keeper sees fit.""",
        "draft_text_basis": "assistant_visual_transcription_draft_from_existing_page_image",
    },
]

APPROVED_BOXES_BY_REGION = {
    "SRCR-G1-VIRAL-004-R01": [720, 330, 1100, 270],
    "SRCR-G1-VIRAL-004-R02": [330, 630, 1950, 2520],
}


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
    parser = argparse.ArgumentParser(description="Build page 004 source reconstruction review packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 004 source reconstruction next-slice package is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 004 source reconstruction next-slice package requires {AUTHORIZATION_ID}")


def verify_predecessors() -> dict[str, object]:
    if sha256_file(P003A_ROOT / "p003_verified_review_acceptance_report.json") != P003A_REPORT_SHA256:
        raise SystemExit("P003A report hash mismatch")
    if sha256_file(P003A_ROOT / "p003_verified_review_acceptance_manifest.md") != P003A_MANIFEST_SHA256:
        raise SystemExit("P003A manifest hash mismatch")
    if sha256_file(P003A_ROOT / "p003_verified_review_acceptance_summary.md") != P003A_SUMMARY_SHA256:
        raise SystemExit("P003A summary hash mismatch")
    if sha256_file(PRM_REPORT) != PRM_SHA256:
        raise SystemExit("provisional region map report hash mismatch")
    if sha256_file(PAGE_IMAGE) != PAGE_004_SHA256:
        raise SystemExit("page 004 image hash mismatch")

    report = read_json(P003A_ROOT / "p003_verified_review_acceptance_report.json")
    if report["package_id"] != "P003A-G1-VIRAL-003":
        raise SystemExit("unexpected P003A package id")
    if report["rollup"]["total_accepted_records"] != 11:
        raise SystemExit("P003A does not roll up 11 accepted source reconstruction records")
    if report["page_complete_acceptance"] is not False or report["whole_gate_1_acceptance"] is not False:
        raise SystemExit("P003A unexpectedly broadened page or Gate acceptance")
    return report


def verify_region_hints() -> None:
    prm_text = PRM_REPORT.read_text(encoding="utf-8")
    required = [
        "PRM-G1-VIRAL-001-P004-R01",
        "PRM-G1-VIRAL-001-P004-R02",
        "PRM-G1-VIRAL-001-P004-R03",
    ]
    for region_id in required:
        if region_id not in prm_text:
            raise SystemExit(f"missing predecessor region hint {region_id}")


def build() -> None:
    verify_predecessors()
    verify_region_hints()
    crop_layout_guardrail = validate_crop_layout(
        P004_RECORDS,
        image_size=(2550, 3300),
        approved_boxes_by_region=APPROVED_BOXES_BY_REGION,
        validated_at_stage="SRCR-G1-VIRAL-004.review_crop_generation",
    )

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    REF_ROOT.mkdir(parents=True, exist_ok=True)

    with Image.open(PAGE_IMAGE) as image:
        if image.size != (2550, 3300):
            raise SystemExit("unexpected page 004 image dimensions")
        records = []
        for region in P004_RECORDS:
            crop_name = f"{region['question_id']}_{region['review_id']}__{region['source_region_id']}.png"
            crop_path = REF_ROOT / crop_name
            crop_with_guardrail(image, region["box_px"], crop_path)
            draft_text = str(region["draft_text"])
            records.append(
                {
                    **region,
                    "page": "004",
                    "page_image": PAGE_IMAGE.relative_to(ROOT).as_posix(),
                    "page_image_sha256": PAGE_004_SHA256,
                    "crop_reference": crop_path.relative_to(ROOT).as_posix(),
                    "crop_reference_sha256": sha256_file(crop_path),
                    "draft_text_sha256": sha256_text(draft_text),
                    "status": "draft_for_bogdan_review_not_accepted",
                    "requires_bogdan_review": True,
                    "source_acceptance": False,
                    "qa_acceptance": False,
                    "fixture_admission": False,
                    "page_complete_acceptance": False,
                    "whole_gate_1_acceptance": False,
                    "gate_1_advancement": False,
                }
            )

    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_004_review_packet_ready_for_bogdan_review_not_accepted",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_package_id": "P003A-G1-VIRAL-003",
        "input_report_sha256": P003A_REPORT_SHA256,
        "input_manifest_sha256": P003A_MANIFEST_SHA256,
        "input_summary_sha256": P003A_SUMMARY_SHA256,
        "input_region_map_id": "PRM-G1-VIRAL-001",
        "input_region_map_sha256": PRM_SHA256,
        "selected_page": "004",
        "selected_page_image_sha256": PAGE_004_SHA256,
        "selected_scope": "page_004_two_record_review_packet_only",
        "context_region": {
            "source_region_id": "PRM-G1-VIRAL-001-P004-R01",
            "status": "context_only_not_peer_crop_record",
            "reason": "Full tilted inset contains the title/body regions and would overlap peer crops under the global crop layout guardrail.",
        },
        "records": records,
        "crop_layout_guardrail": crop_layout_guardrail,
        "summary": {
            "records": len(records),
            "draft_text_records": len(records),
            "requires_bogdan_review_records": len(records),
            "accepted_records": 0,
            "prior_accepted_records_preserved": 11,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "source_acceptance": False,
        "qa_acceptance": False,
        "fixture_admission": False,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "gate_1_advancement": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "next_stop": "present SRCR-G1-VIRAL-004 to Bogdan for numbered review; no source acceptance until separate authorization",
    }
    write_json(OUT_ROOT / "source_reconstruction_next_slice_report.json", report)

    packet_lines = [
        "# Source Reconstruction Page 004 Review Packet - SRCR-G1-VIRAL-004",
        "",
        "Status: `draft_for_bogdan_review_not_accepted`",
        "",
        "Boundary: this packet contains page 004 draft text, structure/semantics, and crop references for Bogdan review only. It creates no source acceptance, QA acceptance, fixture admission, page-complete acceptance, whole-Gate acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push.",
        "",
        "Original page reference:",
        "",
        f"- `{PAGE_IMAGE.relative_to(ROOT).as_posix()}`",
        f"- SHA-256: `{PAGE_004_SHA256}`",
        "",
        "Context note: `PRM-G1-VIRAL-001-P004-R01` is the full tilted inset/document field. It is context only here because it contains the title/body regions and would overlap them as a peer crop record.",
        "",
        "Answer shape:",
        "",
        "```text",
        "1 - ok / correction / blocker",
        "2 - ok / correction / blocker",
        "```",
        "",
    ]
    for record in records:
        structure = record["draft_structure"][0]
        packet_lines.append(f"## {record['question_id']} - {record['source_region_id']}")
        packet_lines.append("")
        packet_lines.append(f"- Crop: `{record['crop_reference']}`")
        packet_lines.append(f"- Draft status: `{record['status']}`")
        packet_lines.append(f"- {format_draft_structure_semantics(structure['semantic_role'], structure['heading_level'])}")
        packet_lines.append("")
        packet_lines.append("```text")
        packet_lines.append(record["draft_text"])
        packet_lines.append("```")
        packet_lines.append("")
    (OUT_ROOT / "human_review_packet.md").write_text("\n".join(packet_lines), encoding="utf-8", newline="\n")

    manifest_lines = [
        "# Source Reconstruction Page 004 Review Manifest - SRCR-G1-VIRAL-004",
        "",
        "Status: `page_004_review_packet_ready_for_bogdan_review_not_accepted`",
        "",
        "Boundary: review-only page 004 packet; no source acceptance, QA acceptance, fixtures, Gate 1 advancement, page-complete acceptance, OCR, PDF parsing, rendering, translation, proofreading, implementation, or push.",
        "",
        "## Generator Hashes",
        "",
        f"- Script `{SCRIPT_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(SCRIPT_PATH)}`",
        f"- Test `{TEST_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(TEST_PATH)}`",
        "",
        "## Records",
        "",
        "| Question | Region | Crop SHA-256 | Draft text SHA-256 |",
        "|---:|---|---|---|",
    ]
    for record in records:
        manifest_lines.append(
            f"| {record['question_id']} | `{record['source_region_id']}` | `{record['crop_reference_sha256']}` | `{record['draft_text_sha256']}` |"
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
