from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_p004_verified_review.py"
TEST_PATH = ROOT / "tests" / "test_p004_verified_review_acceptance.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRCR_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004"
SRCRV_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_004_verify_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001"
PACKAGE_ID = "P004A-G1-VIRAL-004"
SRCR_REPORT_SHA256 = "C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A"
SRCR_MANIFEST_SHA256 = "30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4"
SRCR_PACKET_SHA256 = "1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446"
SRCRV_REPORT_SHA256 = "95041F808A1C2F44A417245BF3E25318C9BDE36183CCE7C4E372DF9363812FBA"
SRCRV_MANIFEST_SHA256 = "21B3CE0135D4D8CF09C394C192D7976766DA9DA1E55DE5F9B3FE240380CC0AB0"
SRCRV_SUMMARY_SHA256 = "F342D7DA0CBB7245812B8B3291F2C5585D880DA67D6C24DCAFEC4FF8B86D9011"


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
    parser = argparse.ArgumentParser(description="Accept verified page 004 review records as a narrow source reconstruction slice.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("p004 verified review acceptance is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"p004 verified review acceptance requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> tuple[dict[str, object], dict[str, object]]:
    verify_authorization_ledger()
    if sha256_file(SRCR_ROOT / "source_reconstruction_next_slice_report.json") != SRCR_REPORT_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 report hash mismatch")
    if sha256_file(SRCR_ROOT / "source_reconstruction_next_slice_manifest.md") != SRCR_MANIFEST_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 manifest hash mismatch")
    if sha256_file(SRCR_ROOT / "human_review_packet.md") != SRCR_PACKET_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 human review packet hash mismatch")
    if sha256_file(SRCRV_ROOT / "source_reconstruction_next_slice_004_verify_report.json") != SRCRV_REPORT_SHA256:
        raise SystemExit("SRCRV-G1-VIRAL-004 verification report hash mismatch")
    if sha256_file(SRCRV_ROOT / "source_reconstruction_next_slice_004_verify_manifest.md") != SRCRV_MANIFEST_SHA256:
        raise SystemExit("SRCRV-G1-VIRAL-004 verification manifest hash mismatch")
    if sha256_file(SRCRV_ROOT / "page_004_human_verification_summary.md") != SRCRV_SUMMARY_SHA256:
        raise SystemExit("SRCRV-G1-VIRAL-004 verification summary hash mismatch")

    review_report = read_json(SRCR_ROOT / "source_reconstruction_next_slice_report.json")
    verification_report = read_json(SRCRV_ROOT / "source_reconstruction_next_slice_004_verify_report.json")
    if review_report["package_id"] != "SRCR-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 review packet id")
    if verification_report["verification_id"] != "SRCRV-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 verification id")
    if verification_report["status"] != "page_004_review_packet_human_verified_not_source_accepted":
        raise SystemExit("page 004 verification is not in the expected verification-only state")
    if verification_report["summary"]["human_verified_records"] != 2:
        raise SystemExit("page 004 verification does not cover exactly two records")
    if any(decision["decision"] != "ok" for decision in verification_report["user_decision"]["record_decisions"]):
        raise SystemExit("page 004 verification includes non-ok decisions")

    guardrail = review_report.get("crop_layout_guardrail")
    if not guardrail:
        raise SystemExit("SRCR-G1-VIRAL-004 missing crop layout guardrail evidence")
    if guardrail["guardrail_policy_id"] != "SRCG-GLOBAL-CROP-BOX-LAYOUT-001" or guardrail["status"] != "passed":
        raise SystemExit("SRCR-G1-VIRAL-004 crop layout guardrail did not pass")
    validated = {item["region_id"]: item["box_px"] for item in guardrail.get("validated_boxes", [])}
    review_records = {record["review_id"]: record for record in review_report["records"]}
    if set(review_records) != {"SRCR-G1-VIRAL-004-R01", "SRCR-G1-VIRAL-004-R02"}:
        raise SystemExit("page 004 review packet does not contain exactly the two expected peer records")
    for record in review_report["records"]:
        if validated.get(record["review_id"]) != record["box_px"]:
            raise SystemExit(f"SRCR-G1-VIRAL-004 crop layout guardrail mismatch for {record['review_id']}")
    for verified in verification_report["records"]:
        review = review_records.get(verified["input_review_id"])
        if not review:
            raise SystemExit(f"verified record has no matching review record: {verified['input_review_id']}")
        if verified["source_region_id"] != review["source_region_id"]:
            raise SystemExit(f"source region mismatch for {verified['verified_record_id']}")
        if verified["crop_reference_sha256"] != review["crop_reference_sha256"]:
            raise SystemExit(f"crop reference hash mismatch for {verified['verified_record_id']}")
        if verified["verified_draft_text_sha256"] != review["draft_text_sha256"]:
            raise SystemExit(f"draft text hash mismatch for {verified['verified_record_id']}")
        if verified["verified_structure"] != review["draft_structure"]:
            raise SystemExit(f"structure mismatch for {verified['verified_record_id']}")
    return review_report, verification_report


def build() -> None:
    review_report, verification_report = verify_predecessors()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    review_records = {record["review_id"]: record for record in review_report["records"]}
    accepted_records = []
    for index, verified in enumerate(verification_report["records"], start=1):
        review = review_records[verified["input_review_id"]]
        accepted_records.append(
            {
                "source_acceptance_record_id": f"SRSA-G1-VIRAL-004-R{index:02d}",
                "verified_record_id": verified["verified_record_id"],
                "review_id": verified["input_review_id"],
                "source_region_id": verified["source_region_id"],
                "page": "004",
                "crop_reference": verified["crop_reference"],
                "crop_reference_sha256": verified["crop_reference_sha256"],
                "accepted_text": verified["verified_draft_text"],
                "accepted_text_sha256": verified["verified_draft_text_sha256"],
                "accepted_structure": verified["verified_structure"],
                "review_box_px": review["box_px"],
                "human_verification_id": "SRCRV-G1-VIRAL-004",
                "bogdan_decision": verified["bogdan_decision"],
            }
        )

    predecessor_guardrail = review_report["crop_layout_guardrail"]
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p004_two_record_source_acceptance_ready",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_review_packet_id": "SRCR-G1-VIRAL-004",
        "input_review_report_sha256": SRCR_REPORT_SHA256,
        "input_review_manifest_sha256": SRCR_MANIFEST_SHA256,
        "input_human_review_packet_sha256": SRCR_PACKET_SHA256,
        "input_verification_id": "SRCRV-G1-VIRAL-004",
        "input_verification_report_sha256": SRCRV_REPORT_SHA256,
        "input_verification_manifest_sha256": SRCRV_MANIFEST_SHA256,
        "input_verification_summary_sha256": SRCRV_SUMMARY_SHA256,
        "user_authority": {
            "telegram_message_id": "538",
            "raw_text": "Ok, go with C1, commit allowed; call me at the end when I need to assess the result.",
        },
        "qa": {
            "qa_id": "SRCRQ-G1-VIRAL-004",
            "status": "passed",
            "records": 2,
            "verified_message_id": verification_report["user_decision"]["telegram_message_id"],
            "checks": [
                "exact_predecessor_hashes",
                "two_ok_human_verified_records",
                "draft_text_hashes_match_review_packet",
                "crop_reference_hashes_match_review_packet",
                "structure_semantics_match_review_packet",
                "predecessor_crop_guardrail_passed",
                "no_context_only_region_accepted_as_peer_record",
            ],
        },
        "crop_guardrail": {
            "guardrail_id": "SRCG-G1-VIRAL-004",
            "status": "passed",
            "predecessor_guardrail": predecessor_guardrail,
            "global_policy_id": predecessor_guardrail["guardrail_policy_id"],
            "policy_version": predecessor_guardrail["policy_version"],
            "accepted_validated_boxes": predecessor_guardrail["validated_boxes"],
            "context_region_policy": review_report["context_region"],
        },
        "source_acceptance": {
            "source_acceptance_id": "SRSA-G1-VIRAL-004",
            "status": "accepted_two_page_004_records_only",
            "accepted_records": accepted_records,
        },
        "rollup": {
            "rollup_id": "G1SRER-G1-VIRAL-004",
            "status": "fourth_source_reconstruction_slice_rolled_up",
            "prior_accepted_records": 11,
            "new_accepted_records": 2,
            "total_accepted_records": 13,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "fixture_admission": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "next_authorization_recommendation": "BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001",
    }
    write_json(OUT_ROOT / "p004_verified_review_acceptance_report.json", report)

    summary = [
        "# P004 Verified Review Acceptance Summary",
        "",
        "Status: `p004_two_record_source_acceptance_ready`",
        "",
        "- `SRCRQ-G1-VIRAL-004` passed QA for Bogdan-verified page-004 draft records.",
        "- `SRCG-G1-VIRAL-004` consumes predecessor global crop-layout guardrail evidence.",
        "- `SRSA-G1-VIRAL-004` accepts exactly two page-004 records as source reconstruction records.",
        "- `G1SRER-G1-VIRAL-004` rolls accepted source reconstruction records from 11 to 13.",
        "- Page 004 is not accepted as complete; whole Gate 1 is not accepted.",
        "",
    ]
    (OUT_ROOT / "p004_verified_review_acceptance_summary.md").write_text(
        "\n".join(summary), encoding="utf-8", newline="\n"
    )

    manifest = [
        "# P004 Verified Review Acceptance Manifest",
        "",
        f"Package: `{PACKAGE_ID}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p004_verified_review_acceptance_manifest.md":
            manifest.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest.append("")
    (OUT_ROOT / "p004_verified_review_acceptance_manifest.md").write_text(
        "\n".join(manifest), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
