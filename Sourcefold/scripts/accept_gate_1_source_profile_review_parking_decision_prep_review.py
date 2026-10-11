from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-REVIEW-001"
PREP_PACKET_ID = "G1SPRPD-G1-VIRAL-001"
REVIEW_ID = "G1SPRPDREV-G1-VIRAL-001"
HUMAN_DECISION = (
    "G1SPRPD accepted as decision-prep only; proceed to prepare Gate 1 source-profile decision packet; "
    "no source-profile acceptance or parking yet"
)
HUMAN_DECISION_MESSAGE_ID = "2227"

INPUT_HASHES = {
    "G1SPRPD-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep.json",
        "3572FBB2A2A23DD9B4B3A2D9C518849F91AF60367A5165CA72AECE6E1AB7A06C",
    ),
    "G1SPRPD-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_report.json",
        "E31CFE5960F876EF483C5AEE8A65A8F4C5BD364D27201CC3ECC59E2E4DD94E44",
    ),
    "G1SPRPD-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_summary.md",
        "F9FEE23C6B5341E289C3776C590DA6918B82167AA9266942F4C47C8ED017C0B0",
    ),
    "G1SPRPD-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_source_profile_review_parking_decision_prep_manifest.md",
        "E310CC116A9DA41BE833770F69C3FC92FE2E7B3C53B3EFF3C0CAB9ABC1BF84A7",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "creates_parking_decision",
    "whole_gate_1_acceptance",
    "fixture_admission",
    "ocr_execution",
    "ocr_remediation_execution",
    "page_021_plus_processing",
    "source_mutation",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Accept G1SPRPD as decision-prep only.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("G1SPRPD review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"G1SPRPD review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"G1SPRPD review requires decision: {HUMAN_DECISION}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    prep = read_json(INPUT_HASHES["G1SPRPD-G1-VIRAL-001.packet"][0])
    if prep["packet_id"] != PREP_PACKET_ID:
        raise SystemExit("prep packet id mismatch")
    if prep["creates_acceptance"] or prep["creates_parking_decision"]:
        raise SystemExit("prep packet unexpectedly creates acceptance or parking")
    if prep["accepts_source_profile"] or prep["accepts_whole_gate_1"] or prep["admits_fixture"]:
        raise SystemExit("prep packet unexpectedly accepts source profile, Gate 1, or fixture")
    return verified, prep


def build_record(verified_inputs: dict[str, dict[str, str]], prep: dict) -> dict:
    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "reviewed_packet_id": PREP_PACKET_ID,
        "status": "source_profile_review_parking_decision_prep_accepted_for_next_packet",
        "human_decision": HUMAN_DECISION,
        "human_decision_source": {
            "platform": "telegram",
            "message_id": HUMAN_DECISION_MESSAGE_ID,
        },
        "accepts_decision_prep_packet": True,
        "authorizes_next_packet_prep": True,
        "accepts_source_profile": False,
        "creates_parking_decision": False,
        "accepts_whole_gate_1": False,
        "admits_fixture": False,
        "processes_page_021_plus": False,
        "decision_prep_counts": prep["decision_prep_counts"],
        "next_packet": "Gate 1 source-profile decision packet",
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(record: dict) -> None:
    lines = [
        "# Gate 1 Source-Profile Review / Parking Decision Prep Review - G1SPRPDREV-G1-VIRAL-001",
        "",
        "Status: `source_profile_review_parking_decision_prep_accepted_for_next_packet`",
        "",
        f"Human decision: `{record['human_decision']}`",
        "",
        "This accepts `G1SPRPD-G1-VIRAL-001` as decision-prep only and authorizes preparing the next source-profile decision packet.",
        "",
        "## Boundaries",
        "",
        "- No source-profile acceptance.",
        "- No parking decision.",
        "- No fixture admission.",
        "- No whole Gate 1 acceptance.",
        "- No page 021+ processing.",
        "- No OCR execution or remediation rerun.",
        "",
    ]
    write_text(OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_summary.md", "\n".join(lines))


def write_manifest() -> None:
    manifest_name = "gate_1_source_profile_review_parking_decision_prep_review_manifest.md"
    lines = [
        "# Gate 1 Source-Profile Review / Parking Decision Prep Review Manifest - G1SPRPDREV-G1-VIRAL-001",
        "",
        "Status: `source_profile_review_parking_decision_prep_accepted_for_next_packet`",
        "",
        "Boundary: prep review only; no source-profile acceptance, no parking decision, no page 021+ authorization, no fixture admission, and no whole Gate 1 acceptance.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / manifest_name, "\n".join(lines))


def build() -> None:
    verified_inputs, prep = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    record = build_record(verified_inputs, prep)
    write_json(OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_review.json", record)
    write_summary(record)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
