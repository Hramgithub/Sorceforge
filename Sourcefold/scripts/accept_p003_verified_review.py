from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_p003_verified_review.py"
TEST_PATH = ROOT / "tests" / "test_p003_verified_review_acceptance.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P002C_ROOT = TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-P003-QA-SOURCE-ACCEPTANCE-001"
PACKAGE_ID = "P003A-G1-VIRAL-003"
P002C_REPORT_SHA256 = "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F"
P002C_MANIFEST_SHA256 = "8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6"
P002C_PACKET_SHA256 = "81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF"


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
    parser = argparse.ArgumentParser(description="Accept verified page 003 review records as a narrow source reconstruction slice.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("p003 verified review acceptance is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"p003 verified review acceptance requires {AUTHORIZATION_ID}")


def verify_predecessor() -> dict[str, object]:
    if sha256_file(P002C_ROOT / "p002_completion_and_next_review_report.json") != P002C_REPORT_SHA256:
        raise SystemExit("P002C report hash mismatch")
    if sha256_file(P002C_ROOT / "p002_completion_and_next_review_manifest.md") != P002C_MANIFEST_SHA256:
        raise SystemExit("P002C manifest hash mismatch")
    if sha256_file(P002C_ROOT / "next_review_packet_for_bogdan.md") != P002C_PACKET_SHA256:
        raise SystemExit("P002C next review packet hash mismatch")
    report = read_json(P002C_ROOT / "p002_completion_and_next_review_report.json")
    if report["next_review_human_verification"]["verification_id"] != "SRCRV-G1-VIRAL-003":
        raise SystemExit("P002C does not include verified SRCRV-G1-VIRAL-003")
    guardrail = report["next_review_packet"].get("crop_layout_guardrail")
    if not guardrail:
        raise SystemExit("P002C missing crop layout guardrail evidence")
    if guardrail["guardrail_policy_id"] != "SRCG-GLOBAL-CROP-BOX-LAYOUT-001" or guardrail["status"] != "passed":
        raise SystemExit("P002C crop layout guardrail did not pass")
    validated = {
        item["region_id"]: item["box_px"]
        for item in guardrail.get("validated_boxes", [])
    }
    for record in report["next_review_packet"]["records"]:
        if validated.get(record["review_id"]) != record["box_px"]:
            raise SystemExit(f"P002C crop layout guardrail mismatch for {record['review_id']}")
    return report


def build() -> None:
    predecessor = verify_predecessor()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    records = predecessor["next_review_packet"]["records"]
    predecessor_guardrail = predecessor["next_review_packet"]["crop_layout_guardrail"]
    accepted_records = [
        {
            "source_acceptance_record_id": f"SRSA-G1-VIRAL-003-R{index:02d}",
            "review_id": record["review_id"],
            "page": "003",
            "crop_reference": record["crop_reference"],
            "crop_reference_sha256": record["crop_reference_sha256"],
            "accepted_text_sha256": record["draft_text_sha256"],
            "accepted_structure": record["draft_structure"],
            "human_verification_id": "SRCRV-G1-VIRAL-003",
        }
        for index, record in enumerate(records, start=1)
    ]
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p003_two_record_source_acceptance_ready",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_package_id": "P002C-G1-VIRAL-002",
        "input_report_sha256": P002C_REPORT_SHA256,
        "input_manifest_sha256": P002C_MANIFEST_SHA256,
        "input_next_review_packet_sha256": P002C_PACKET_SHA256,
        "user_authority": {
            "telegram_message_id": "441",
            "raw_text": "Commit, then QA acceptance, then fix crop.",
        },
        "qa": {
            "qa_id": "SRCRQ-G1-VIRAL-003",
            "status": "passed",
            "records": 2,
            "verified_message_id": "437",
        },
        "crop_guardrail": {
            "guardrail_id": "SRCG-G1-VIRAL-003",
            "status": "passed",
            "predecessor_guardrail": predecessor_guardrail,
            "global_policy_id": predecessor_guardrail["guardrail_policy_id"],
            "policy_version": predecessor_guardrail["policy_version"],
            "accepted_validated_boxes": predecessor_guardrail["validated_boxes"],
            "debt": "Future review packet generators must reject unapproved page/region boxes that cut readable text at crop edges, overlap another crop, or violate the minimum gutter.",
        },
        "source_acceptance": {
            "source_acceptance_id": "SRSA-G1-VIRAL-003",
            "status": "accepted_two_page_003_records_only",
            "accepted_records": accepted_records,
        },
        "rollup": {
            "rollup_id": "G1SRER-G1-VIRAL-003",
            "status": "third_source_reconstruction_slice_rolled_up",
            "prior_accepted_records": 9,
            "new_accepted_records": 2,
            "total_accepted_records": 11,
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
    }
    write_json(OUT_ROOT / "p003_verified_review_acceptance_report.json", report)

    summary = [
        "# P003 Verified Review Acceptance Summary",
        "",
        "Status: `p003_two_record_source_acceptance_ready`",
        "",
        "- `SRCRQ-G1-VIRAL-003` passed QA for Bogdan-verified remediated draft records.",
        "- `SRCG-G1-VIRAL-003` records the crop guardrail: old tight boxes are blocked; padded boxes are required.",
        "- `SRSA-G1-VIRAL-003` accepts exactly two page-003 records as source reconstruction records.",
        "- Page 003 is not accepted as complete; whole Gate 1 is not accepted.",
        "",
    ]
    (OUT_ROOT / "p003_verified_review_acceptance_summary.md").write_text(
        "\n".join(summary), encoding="utf-8", newline="\n"
    )

    manifest = [
        "# P003 Verified Review Acceptance Manifest",
        "",
        f"Package: `{PACKAGE_ID}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p003_verified_review_acceptance_manifest.md":
            manifest.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest.append("")
    (OUT_ROOT / "p003_verified_review_acceptance_manifest.md").write_text(
        "\n".join(manifest), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
