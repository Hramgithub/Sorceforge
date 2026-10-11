from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRHP_ROOT = TRIAL_ROOT / "source_reconstruction_human_package_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_human_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001"
REVIEW_ID = "SRHR-G1-VIRAL-001"
SRHP_SHA256 = "2A5A475737BF6442B11DFB26CE6E62724978B9F797E37A8BAB843BF2534017CC"

PACKET_MESSAGE_IDS = [248, 253, 259, 262]
USER_RESPONSE_MESSAGE_IDS = [251, 257, 260, 265]
TELEGRAM_CHAT_ID = "telegram:150618017"

HUMAN_DECISIONS = {
    "SRA-G1-VIRAL-001-R001": {
        "question_number": 1,
        "packet_message_id": 248,
        "response_message_id": 251,
        "human_response": "1 ok",
        "human_decision": "accepted_visual_only_exclusion",
        "source_text_accepted": False,
        "visual_exclusion_accepted": True,
    },
    "SRA-G1-VIRAL-001-R002": {
        "question_number": 3,
        "packet_message_id": 253,
        "response_message_id": 257,
        "human_response": "3 ok",
        "human_decision": "accepted_candidate_text",
        "source_text_accepted": True,
        "visual_exclusion_accepted": False,
    },
    "SRA-G1-VIRAL-001-R003": {
        "question_number": 4,
        "packet_message_id": 259,
        "response_message_id": 260,
        "human_response": "4 ok",
        "human_decision": "accepted_candidate_text_after_full_crop_resend",
        "source_text_accepted": True,
        "visual_exclusion_accepted": False,
        "packet_correction_note": (
            "Initial narrow reference in message 253 did not show The Spektral Krew; "
            "full source crop was resent in message 259 before acceptance."
        ),
        "semantic_heading_hint": [
            {"text": "Introduction", "level": "H1"},
            {"text": "Summary", "level": "H3"},
            {"text": "Overview", "level": "H3"},
            {"text": "The Spektral Krew", "level": "H2"},
        ],
    },
    "SRA-G1-VIRAL-001-R004": {
        "question_number": 6,
        "packet_message_id": 262,
        "response_message_id": 265,
        "human_response": "6 ok",
        "human_decision": "accepted_candidate_text",
        "source_text_accepted": True,
        "visual_exclusion_accepted": False,
    },
    "SRA-G1-VIRAL-001-R005": {
        "question_number": 7,
        "packet_message_id": 262,
        "response_message_id": 265,
        "human_response": "7 ok",
        "human_decision": "accepted_candidate_text",
        "source_text_accepted": True,
        "visual_exclusion_accepted": False,
    },
    "SRA-G1-VIRAL-001-R006": {
        "question_number": 2,
        "packet_message_id": 248,
        "response_message_id": 251,
        "human_response": "2 ok",
        "human_decision": "accepted_visual_only_exclusion",
        "source_text_accepted": False,
        "visual_exclusion_accepted": True,
    },
    "SRA-G1-VIRAL-001-R007": {
        "question_number": 5,
        "packet_message_id": 253,
        "response_message_id": 257,
        "human_response": "5 ok",
        "human_decision": "accepted_visual_only_exclusion",
        "source_text_accepted": False,
        "visual_exclusion_accepted": True,
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Record Bogdan human source reconstruction review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction human review recording is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction human review recording requires {AUTHORIZATION_ID}")


def review_records(srhp: dict[str, object]) -> list[dict[str, object]]:
    output_records = []
    for package_record in srhp["human_review_records"]:
        region_id = str(package_record["region_admission_id"])
        decision = HUMAN_DECISIONS.get(region_id)
        if decision is None:
            raise SystemExit(f"missing human decision: {region_id}")
        if package_record["human_review_ready"] is not True:
            raise SystemExit(f"package record was not ready for human review: {region_id}")
        if package_record["source_acceptance"] is not False or package_record["qa_acceptance"] is not False:
            raise SystemExit(f"package record already had acceptance flags: {region_id}")

        accepted_text = bool(decision["source_text_accepted"])
        accepted_exclusion = bool(decision["visual_exclusion_accepted"])
        if accepted_text == accepted_exclusion:
            raise SystemExit(f"ambiguous human decision acceptance type: {region_id}")
        if accepted_text and package_record["candidate_text"] is None:
            raise SystemExit(f"source text accepted without candidate text: {region_id}")
        if accepted_exclusion and package_record["candidate_text"] is not None:
            raise SystemExit(f"visual-only exclusion accepted for text candidate: {region_id}")

        output = {
            "review_order": package_record["review_order"],
            "question_number": decision["question_number"],
            "region_admission_id": region_id,
            "record_kind": package_record["record_kind"],
            "sample_id": package_record["sample_id"],
            "page_id": package_record["page_id"],
            "region_id": package_record["region_id"],
            "route_class": package_record["route_class"],
            "review_class": package_record["review_class"],
            "candidate_text": package_record["candidate_text"],
            "source_input_crop": package_record["source_input_crop"],
            "source_input_crop_sha256": package_record["source_input_crop_sha256"],
            "visual_reference": package_record["visual_reference"],
            "visual_reference_sha256": package_record["visual_reference_sha256"],
            "packet_message_id": decision["packet_message_id"],
            "human_response_message_id": decision["response_message_id"],
            "human_response": decision["human_response"],
            "human_decision": decision["human_decision"],
            "source_text_accepted": accepted_text,
            "visual_exclusion_accepted": accepted_exclusion,
            "qa_acceptance": False,
            "gate_1_advancement": False,
        }
        if "packet_correction_note" in decision:
            output["packet_correction_note"] = decision["packet_correction_note"]
        if "semantic_heading_hint" in decision:
            output["semantic_heading_hint"] = decision["semantic_heading_hint"]
        output_records.append(output)
    return sorted(output_records, key=lambda record: int(record["review_order"]))


def accepted_source_text(records: list[dict[str, object]]) -> str:
    text_records = [record for record in records if record["source_text_accepted"]]
    lines = [
        "# Source Reconstruction Human-Accepted Text - SRHR-G1-VIRAL-001",
        "",
        "Status: `source_review_accepted_not_qa_accepted`",
        "",
        "Boundary: Bogdan accepted this source text during human review. It is not QA acceptance, fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Accepted Candidate Text",
        "",
    ]
    for record in text_records:
        lines.append(f"### {record['question_number']}. {record['region_admission_id']}")
        lines.append("")
        lines.append(f"- Source crop SHA-256: `{record['source_input_crop_sha256']}`")
        lines.append(f"- Human response message id: `{record['human_response_message_id']}`")
        lines.append("")
        lines.append("```text")
        lines.append(str(record["candidate_text"]))
        lines.append("```")
        lines.append("")
        if "semantic_heading_hint" in record:
            lines.append("Semantic heading hint:")
            for hint in record["semantic_heading_hint"]:
                lines.append(f"- `{hint['level']}`: `{hint['text']}`")
            lines.append("")
    return "\n".join(lines)


def build() -> None:
    srhp_report_path = SRHP_ROOT / "source_reconstruction_human_package_report.json"
    if sha256_file(srhp_report_path) != SRHP_SHA256:
        raise SystemExit("SRHP report hash mismatch")

    srhp = read_json(srhp_report_path)
    if srhp["package_id"] != "SRHP-G1-VIRAL-001":
        raise SystemExit("unexpected SRHP package id")
    if srhp["ready_for_bogdan_human_review"] is not True:
        raise SystemExit("SRHP is not ready for Bogdan human review")
    if srhp["source_acceptance"] is not False or srhp["qa_acceptance"] is not False:
        raise SystemExit("SRHP boundary flags are not safe")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    records = review_records(srhp)
    text_records = [record for record in records if record["source_text_accepted"]]
    visual_exclusion_records = [record for record in records if record["visual_exclusion_accepted"]]
    report = {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "source_review_accepted_not_qa_accepted",
        "input_package_id": "SRHP-G1-VIRAL-001",
        "input_package_sha256": SRHP_SHA256,
        "generator_script": "scripts/record_source_reconstruction_human_review.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_source_reconstruction_human_review.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_source_reconstruction_human_review.py")
        if (ROOT / "tests" / "test_source_reconstruction_human_review.py").exists()
        else None,
        "reviewer": "Bogdan D",
        "review_channel": TELEGRAM_CHAT_ID,
        "review_method": "page_by_page_telegram_packet_review",
        "packet_message_ids": PACKET_MESSAGE_IDS,
        "user_response_message_ids": USER_RESPONSE_MESSAGE_IDS,
        "source_acceptance": True,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "fixture_creation": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "human_review_records": records,
        "summary": {
            "records": len(records),
            "source_text_accepted_records": len(text_records),
            "visual_exclusion_accepted_records": len(visual_exclusion_records),
            "blocked_records": 0,
            "qa_accepted_records": 0,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-QA-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_human_review_report.json", report)

    accepted_text_path = OUT_ROOT / "source_review_accepted_text.md"
    accepted_text_path.write_text(accepted_source_text(records), encoding="utf-8")

    manifest_lines = [
        "# Source Reconstruction Human Review Manifest - SRHR-G1-VIRAL-001",
        "",
        "Status: `source_review_accepted_not_qa_accepted`",
        "",
        "Boundary: source review accepted by Bogdan; no QA acceptance, fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        f"- Records: `{report['summary']['records']}`",
        f"- Source text accepted records: `{report['summary']['source_text_accepted_records']}`",
        f"- Visual exclusion accepted records: `{report['summary']['visual_exclusion_accepted_records']}`",
        "- QA accepted: `false`",
        "- Gate 1 advanced: `false`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_human_review_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_human_review_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    check_authorization()
    build()
