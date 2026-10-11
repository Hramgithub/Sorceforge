from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-REVIEW-001"
PREP_PACKET_ID = "G1UNFPDP-G1-VIRAL-001"
REVIEW_ID = "G1UNFPDPREV-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1unfpdp packet ok; proceed to prepare unsupported/negative fixture policy record over "
    "unsupported_profiles_scope, negative_fixture_obligations, invalidation_conditions, and "
    "fixture_admission_dependency; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push"
)
HUMAN_DECISION_MESSAGE_ID = "2315"

INPUT_HASHES = {
    "G1UNFPDP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep.json",
        "ACB7E596C63896C67CB4C93AB691DB5FE19B0B53ED56EBE87CA9D510D4771F58",
    ),
    "G1UNFPDP-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_report.json",
        "0FC376645E49B7E8323A25AA164ADA9C1E9B256C8B341FE73B07B6BB2776F571",
    ),
    "G1UNFPDP-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_summary.md",
        "378834F02FF862EA39B090F82D0A15D292F6359ED9249D2E435D618505F394D5",
    ),
    "G1UNFPDP-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_manifest.md",
        "2BA000A90B79D20201A1A71C32031C14250B91929BDA049E40876D81741C28F4",
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
    parser = argparse.ArgumentParser(description="Accept G1UNFPDP as unsupported/negative fixture policy prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("G1UNFPDP review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"G1UNFPDP review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"G1UNFPDP review requires decision: {HUMAN_DECISION}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    prep = read_json(INPUT_HASHES["G1UNFPDP-G1-VIRAL-001.packet"][0])
    if prep["packet_id"] != PREP_PACKET_ID:
        raise SystemExit("G1UNFPDP packet id mismatch")
    if prep["creates_policy_decision"]:
        raise SystemExit("G1UNFPDP unexpectedly creates a policy decision")
    if prep["creates_blocker_resolution"] or prep["admits_fixture"] or prep["creates_fixture_manifest"]:
        raise SystemExit("G1UNFPDP unexpectedly resolves blockers or admits fixtures")
    if prep["accepts_whole_gate_1"] or prep["accepts_source_profile"]:
        raise SystemExit("G1UNFPDP unexpectedly creates acceptance")
    if prep["processes_page_021_plus"] or prep["executes_ocr"]:
        raise SystemExit("G1UNFPDP unexpectedly processes page 021+ or OCR")
    return verified, prep


def build_review(verified_inputs: dict[str, dict[str, str]], prep: dict) -> dict:
    policy_question_ids = [row["question_id"] for row in prep["policy_questions"]]
    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "reviewed_packet_id": PREP_PACKET_ID,
        "status": "unsupported_negative_fixture_policy_decision_prep_accepted_for_policy_record",
        "human_decision": HUMAN_DECISION,
        "human_decision_source": {"platform": "telegram", "message_id": HUMAN_DECISION_MESSAGE_ID},
        "accepts_decision_prep_packet": True,
        "authorizes_policy_record_prep": True,
        "policy_record_scope": policy_question_ids,
        "creates_policy_decision": False,
        "creates_blocker_resolution": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "next_candidate": "unsupported_negative_fixture_policy_record",
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(review: dict) -> None:
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Decision Prep Review - G1UNFPDPREV-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_prep_accepted_for_policy_record`",
        "",
        f"Human decision: `{review['human_decision']}`",
        "",
        "## Accepted Scope",
        "",
    ]
    for question_id in review["policy_record_scope"]:
        lines.append(f"- `{question_id}`")
    lines.extend(
        [
            "",
            "## Next Candidate",
            "",
            f"- `{review['next_candidate']}`",
            "",
            "## Boundaries",
            "",
            "- No policy decision is created by this review.",
            "- No blocker resolution.",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, implementation, or push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_summary.md", "\n".join(lines))


def write_manifest() -> None:
    manifest_name = "gate_1_unsupported_negative_fixture_policy_decision_prep_review_manifest.md"
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Decision Prep Review Manifest - G1UNFPDPREV-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_prep_accepted_for_policy_record`",
        "",
        "Boundary: prep review only; no policy decision, no blocker resolution, no fixture admission, no page 021+, no push, and no whole Gate 1 acceptance.",
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
    review = build_review(verified_inputs, prep)
    write_json(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review.json", review)
    write_summary(review)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
