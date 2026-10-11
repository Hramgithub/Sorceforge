from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MATRIX_ROOT = TRIAL_ROOT / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-READINESS-MATRIX-REVIEW-001"
MATRIX_ID = "G1SPRM-G1-VIRAL-001"
REVIEW_ID = "G1SPRMREV-G1-VIRAL-001"
HUMAN_DECISION = "ok accepted with comments"
HUMAN_DECISION_SOURCE_TEXT = "ок принято с коментариями"
HUMAN_DECISION_MESSAGE_ID = "2182"

INPUT_HASHES = {
    "G1SPRM-G1-VIRAL-001.matrix": (
        MATRIX_ROOT / "gate_1_source_profile_readiness_parking_matrix.json",
        "49EFEF00F19ACA3D583EA5A2DB221023C54F9EA32C83609A0DD95988F9612466",
    ),
    "G1SPRM-G1-VIRAL-001.report": (
        MATRIX_ROOT / "gate_1_source_profile_readiness_parking_matrix_report.json",
        "1E5F1A6CEA99B4BB4C67D9126727FBBC5C855CDDCF3B0F98CA0AD9F1C6710577",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "creates_parking_decision",
    "ocr_execution",
    "ocr_remediation_execution",
    "page_021_plus_processing",
    "whole_gate_1_acceptance",
    "fixture_admission",
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 source-profile readiness matrix route review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source-profile readiness matrix review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source-profile readiness matrix review requires {AUTHORIZATION_ID}")
    if args.decision not in {HUMAN_DECISION, HUMAN_DECISION_SOURCE_TEXT}:
        raise SystemExit(
            "Gate 1 source-profile readiness matrix review requires decision: "
            f"{HUMAN_DECISION_SOURCE_TEXT}"
        )


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    matrix = read_json(INPUT_HASHES["G1SPRM-G1-VIRAL-001.matrix"][0])
    if matrix["matrix_id"] != MATRIX_ID:
        raise SystemExit("matrix id mismatch")
    if matrix["creates_acceptance"] is not False:
        raise SystemExit("matrix unexpectedly creates acceptance")
    if matrix["creates_parking_decision"] is not False:
        raise SystemExit("matrix unexpectedly creates parking decision")
    if matrix["starts_ocr_remediation"] is not False:
        raise SystemExit("matrix unexpectedly starts OCR remediation")
    if matrix["baseline"]["page_021_plus_state"] != "unprocessed_not_authorized":
        raise SystemExit("page 021+ is not blocked in matrix baseline")
    if matrix["baseline"]["whole_gate_1_acceptance"] is not False:
        raise SystemExit("whole Gate 1 is unexpectedly accepted")
    return verified, matrix


def disposition_counts(matrix: dict) -> dict[str, int]:
    counts = {status: 0 for status in matrix["allowed_dispositions"]}
    for row in matrix["rows"]:
        counts[row["disposition"]] += 1
    return counts


def build_record(verified_inputs: dict[str, dict[str, str]], matrix: dict) -> dict:
    counts = disposition_counts(matrix)
    expected_counts = {
        "ready_for_gate_review": 5,
        "parked_for_0.1": 0,
        "parked_pending_ocr_hardening": 2,
        "blocked_needs_decision": 3,
        "evidence_only_not_accepting": 2,
    }
    if counts != expected_counts:
        raise SystemExit(f"unexpected matrix disposition counts: {counts}")

    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "reviewed_matrix_id": MATRIX_ID,
        "status": "source_profile_readiness_matrix_route_review_accepted_with_comments",
        "human_decision": HUMAN_DECISION,
        "human_decision_source_text": HUMAN_DECISION_SOURCE_TEXT,
        "human_decision_source": {
            "platform": "telegram",
            "message_id": HUMAN_DECISION_MESSAGE_ID,
        },
        "accepts_route_review_artifact": True,
        "accepts_source_profile": False,
        "creates_parking_decision": False,
        "starts_ocr_remediation": False,
        "accepted_comments": [
            "ready_for_gate_review rows are accepted only as ready for Gate/route review, not acceptance.",
            "parked_pending_ocr_hardening rows proceed to the next OCR hardening branch, not parked for 0.1.",
            "blocked_needs_decision rows remain blocked: page 021+, unsupported/negative fixtures, and whole Gate 1.",
            "evidence_only_not_accepting rows remain evidence only and do not admit fixture/source/profile acceptance.",
        ],
        "disposition_counts": counts,
        "next_selected_branch": {
            "branch": "ocr_benchmark_remediation_methodology_hardening",
            "status": "selected_next_branch_requires_separate_bounded_authorization",
        },
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_manifest() -> None:
    manifest_name = "gate_1_source_profile_readiness_parking_matrix_review_manifest.md"
    lines = [
        "# Gate 1 Source Profile Readiness Parking Matrix Review Manifest - G1SPRMREV-G1-VIRAL-001",
        "",
        "Status: `source_profile_readiness_matrix_route_review_accepted_with_comments`",
        "",
        "Boundary: route-review artifact acceptance only; no source-profile acceptance, parking decision, OCR remediation, page 021+ authorization, or whole Gate 1 acceptance.",
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


def write_summary(record: dict) -> None:
    counts = record["disposition_counts"]
    lines = [
        "# Gate 1 Source Profile Readiness Parking Matrix Review - G1SPRMREV-G1-VIRAL-001",
        "",
        "Status: `source_profile_readiness_matrix_route_review_accepted_with_comments`",
        "",
        f"Human decision: `{record['human_decision_source_text']}`",
        "",
        "This accepts `G1SPRM-G1-VIRAL-001` as a route-review artifact only.",
        "",
        "## Accepted Matrix Counts",
        "",
    ]
    for status in record["disposition_counts"]:
        lines.append(f"- `{status}`: {counts[status]}")
    lines.extend(
        [
            "",
            "## Comments",
            "",
        ]
    )
    for comment in record["accepted_comments"]:
        lines.append(f"- {comment}")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No source-profile acceptance.",
            "- No parking decision.",
            "- No OCR remediation execution.",
            "- No page 021+ processing.",
            "- No whole Gate 1 acceptance.",
            "- Next selected branch requires a separate bounded authorization: `ocr_benchmark_remediation_methodology_hardening`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_review_summary.md", "\n".join(lines))


def build() -> None:
    verified_inputs, matrix = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    record = build_record(verified_inputs, matrix)
    write_json(OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_review.json", record)
    write_summary(record)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
