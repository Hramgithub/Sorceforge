from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
FARP_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-PREP-REVIEW-001"
PACKET_ID = "G1FARP-G1-VIRAL-001"
REVIEW_ID = "G1FARPREV-G1-VIRAL-001"
HUMAN_DECISION = (
    "G1FARP accepted as readiness/blocker packet only; proceed to prepare fixture admission "
    "blocker resolution prep; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push"
)
HUMAN_DECISION_MESSAGE_ID = "2255"

INPUT_HASHES = {
    "G1FARP-G1-VIRAL-001.packet": (
        FARP_ROOT / "gate_1_fixture_admission_readiness_prep.json",
        "A6AB9B1CD40EDAC6D2A83B24306920743D5B6039410B1188FA5D6DB433A52CEC",
    ),
    "G1FARP-G1-VIRAL-001.report": (
        FARP_ROOT / "gate_1_fixture_admission_readiness_prep_report.json",
        "0BBED96C4E0D41054AE1FA8AB1FA27430DD330580DA04A5B74C1EBC39CDE5EC8",
    ),
    "G1FARP-G1-VIRAL-001.summary": (
        FARP_ROOT / "gate_1_fixture_admission_readiness_prep_summary.md",
        "E8962C044123C9ADFA59C58F066C166C5675312D27DBE278FE91D0F30DFF6753",
    ),
    "G1FARP-G1-VIRAL-001.manifest": (
        FARP_ROOT / "gate_1_fixture_admission_readiness_prep_manifest.md",
        "51073752A2BD86B96233BE000A21C4A029E027E98B6F646C7C0545C256870780",
    ),
}

NEGATIVE_CAPABILITIES = [
    "fixture_admission",
    "fixture_manifest_creation",
    "whole_gate_1_acceptance",
    "source_profile_acceptance",
    "page_021_plus_processing",
    "ocr_execution",
    "ocr_remediation_execution",
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
    parser = argparse.ArgumentParser(description="Accept G1FARP as readiness/blocker packet only.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("G1FARP review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"G1FARP review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"G1FARP review requires decision: {HUMAN_DECISION}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    packet = read_json(INPUT_HASHES["G1FARP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != PACKET_ID:
        raise SystemExit("G1FARP packet id mismatch")
    if packet["admits_fixture"] or packet["creates_fixture_manifest"]:
        raise SystemExit("G1FARP unexpectedly admits fixtures")
    if packet["accepts_whole_gate_1"] or packet["accepts_source_profile"]:
        raise SystemExit("G1FARP unexpectedly creates acceptance")
    if packet["processes_page_021_plus"] or packet["executes_ocr"]:
        raise SystemExit("G1FARP unexpectedly processes page 021+ or OCR")
    return verified, packet


def build_review(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    readiness = {row["row_id"]: row["status"] for row in packet["readiness_rows"]}
    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "reviewed_packet_id": PACKET_ID,
        "status": "fixture_admission_readiness_prep_accepted_for_blocker_resolution_prep",
        "human_decision": HUMAN_DECISION,
        "human_decision_source": {"platform": "telegram", "message_id": HUMAN_DECISION_MESSAGE_ID},
        "accepts_readiness_blocker_packet": True,
        "authorizes_next_packet_prep": True,
        "next_packet": "fixture_admission_blocker_resolution_prep",
        "readiness_statuses": readiness,
        "accepted_counts": {
            "gate_review_candidate_rows": len(packet["accepted_gate_review_candidate_rows"]),
            "parked_ocr_methodology_rows": len(packet["parked_ocr_methodology_rows"]),
            "evidence_only_rows": len(packet["evidence_only_rows"]),
            "blocked_rows": len(packet["blocked_rows"]),
            "page_021_plus_separate_ba_rows": len(packet["page_021_plus_boundary"]["rows"]),
        },
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(review: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Readiness Prep Review - G1FARPREV-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_readiness_prep_accepted_for_blocker_resolution_prep`",
        "",
        f"Human decision: `{review['human_decision']}`",
        "",
        "This accepts `G1FARP-G1-VIRAL-001` as a readiness/blocker packet only and authorizes preparing a fixture admission blocker resolution prep packet.",
        "",
        "## Readiness Statuses",
        "",
    ]
    for row_id, status in review["readiness_statuses"].items():
        lines.append(f"- `{row_id}`: `{status}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_fixture_admission_readiness_prep_review_summary.md", "\n".join(lines))


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_admission_readiness_prep_review_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Readiness Prep Review Manifest - G1FARPREV-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_readiness_prep_accepted_for_blocker_resolution_prep`",
        "",
        "Boundary: readiness/blocker packet review only; no fixture admission, no fixture manifest, no page 021+, no push, and no whole Gate 1 acceptance.",
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
    verified_inputs, packet = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    review = build_review(verified_inputs, packet)
    write_json(OUT_ROOT / "gate_1_fixture_admission_readiness_prep_review.json", review)
    write_summary(review)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
