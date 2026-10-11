from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_unsupported_negative_fixture_policy_record.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_unsupported_negative_fixture_policy_record.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_G1_VIRAL_001"
REVIEW_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_record_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-RECORD-001"
RECORD_ID = "G1UNFPR-G1-VIRAL-001"

INPUT_HASHES = {
    "G1UNFPDP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep.json",
        "ACB7E596C63896C67CB4C93AB691DB5FE19B0B53ED56EBE87CA9D510D4771F58",
    ),
    "G1UNFPDPREV-G1-VIRAL-001.review": (
        REVIEW_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review.json",
        "3906CFB86519B0988E67B1DB681F817006493DD43F0209CE11E459C306BA8D72",
    ),
    "G1UNFPDPREV-G1-VIRAL-001.summary": (
        REVIEW_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_summary.md",
        "81B8CE5AC11222F561561FD5702DF603FCA29A6BBABF53EF1FC71203E3B158C3",
    ),
    "G1UNFPDPREV-G1-VIRAL-001.manifest": (
        REVIEW_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_manifest.md",
        "D3A0749BCB01E68C5D5FCE561F6BE6EABEF902D93D276F984C3F9B5D6E4911CF",
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
    parser = argparse.ArgumentParser(description="Build unsupported/negative fixture policy record.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Unsupported/negative fixture policy record is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Unsupported/negative fixture policy record requires {AUTHORIZATION_ID}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if expected is not None and actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    prep = read_json(INPUT_HASHES["G1UNFPDP-G1-VIRAL-001.packet"][0])
    review = read_json(INPUT_HASHES["G1UNFPDPREV-G1-VIRAL-001.review"][0])
    if prep["packet_id"] != "G1UNFPDP-G1-VIRAL-001":
        raise SystemExit("unexpected G1UNFPDP packet")
    if review["review_id"] != "G1UNFPDPREV-G1-VIRAL-001":
        raise SystemExit("unexpected G1UNFPDPREV review")
    if not review["authorizes_policy_record_prep"]:
        raise SystemExit("G1UNFPDPREV does not authorize policy record prep")
    if review["policy_record_scope"] != [row["question_id"] for row in prep["policy_questions"]]:
        raise SystemExit("G1UNFPDPREV scope differs from prep questions")
    for field in (
        "creates_policy_decision",
        "creates_blocker_resolution",
        "admits_fixture",
        "creates_fixture_manifest",
        "accepts_whole_gate_1",
        "accepts_source_profile",
        "processes_page_021_plus",
        "executes_ocr",
    ):
        if review[field]:
            raise SystemExit(f"G1UNFPDPREV boundary too broad: {field}")
    return verified, prep, review


def build_record(verified_inputs: dict[str, dict[str, str]], prep: dict, review: dict) -> dict:
    return {
        "record_id": RECORD_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "unsupported_negative_fixture_policy_record_ready_for_review",
        "purpose": "bounded_unsupported_negative_fixture_policy_record_candidate",
        "source_decision_prep_packet": prep["packet_id"],
        "source_review": review["review_id"],
        "creates_policy_decision": False,
        "resolves_unsupported_negative_fixture_policy_blocker": False,
        "creates_blocker_resolution": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "candidate_policy_decisions": [
            {
                "question_id": "unsupported_profiles_scope",
                "decision": "non_viral_like_or_non_page_complete_evidence_profiles_unsupported_for_core_0_1",
                "meaning": (
                    "Core 0.1 fixture planning remains scoped to Viral-like, page-complete accepted-only "
                    "evidence. Other source/profile families require a later explicit support decision."
                ),
            },
            {
                "question_id": "negative_fixture_obligations",
                "decision": "negative_fixtures_or_counterexamples_required_before_fixture_admission",
                "required_negative_fixture_classes": [
                    "unsupported_profile_claim",
                    "missing_or_unresolved_negative_fixture_policy",
                    "stale_lineage_or_invalidation_trigger",
                    "page_021_plus_boundary_violation",
                ],
            },
            {
                "question_id": "invalidation_conditions",
                "decision": "new_page_021_plus_evidence_new_ocr_render_evidence_or_user_policy_change_invalidates",
                "invalidation_conditions": [
                    "page 021+ evidence is authorized and contradicts the unsupported-profile boundary",
                    "new OCR, render, layout, or source-profile evidence changes accepted assumptions",
                    "fixture strategy or admission criteria change",
                    "Bogdan changes the policy or Core 0.1 support scope",
                ],
            },
            {
                "question_id": "fixture_admission_dependency",
                "decision": "fixture_admission_remains_blocked_until_separate_fixture_strategy_fit_and_admission_refresh",
                "meaning": (
                    "If accepted later, this policy record would close only the unsupported/negative fixture policy "
                    "decision. Fixture admission would still require separate fixture strategy fit review and admission "
                    "readiness refresh."
                ),
            },
        ],
        "remaining_blockers": [
            "fixture_strategy_fit_decision",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "unsupported_negative_fixture_policy_record_acceptance",
            "fixture_strategy_fit_decision_prep",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(record: dict) -> None:
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Record - G1UNFPR-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_record_ready_for_review`",
        "",
        "Purpose: prepare the unsupported/negative fixture policy record candidate over the four reviewed G1UNFPDP questions.",
        "",
        "## Candidate Policy Decisions",
        "",
    ]
    for row in record["candidate_policy_decisions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in record["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
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
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, implementation, or push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record_summary.md", "\n".join(lines))


def write_report(record: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record_report.json",
        {
            "record_id": RECORD_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": record["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "candidate_policy_decision_count": len(record["candidate_policy_decisions"]),
            "creates_policy_decision": False,
            "resolves_unsupported_negative_fixture_policy_blocker": False,
            "creates_blocker_resolution": False,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": record["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_unsupported_negative_fixture_policy_record_manifest.md"
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Record Manifest - G1UNFPR-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_record_ready_for_review`",
        "",
        "Boundary: unsupported/negative fixture policy record candidate only; no policy decision, no blocker resolution, no fixture admission, no fixture manifest, no page 021+, no push, and no whole Gate 1 acceptance.",
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
    verified_inputs, prep, review = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    record = build_record(verified_inputs, prep, review)
    write_json(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record.json", record)
    write_summary(record)
    write_report(record)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
