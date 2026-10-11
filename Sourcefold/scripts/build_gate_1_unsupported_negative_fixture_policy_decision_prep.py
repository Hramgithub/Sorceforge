from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_unsupported_negative_fixture_policy_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_unsupported_negative_fixture_policy_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
FABRPREV_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-001"
PACKET_ID = "G1UNFPDP-G1-VIRAL-001"

INPUT_HASHES = {
    "G1FABRPREV-G1-VIRAL-001.review": (
        FABRPREV_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review.json",
        "FAD1AA01AB0AAB2E2B69B02BF101D788035E5C058920E33463800F9E351E3183",
    ),
    "G1FABRPREV-G1-VIRAL-001.summary": (
        FABRPREV_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_summary.md",
        "BA3AC1B0B7EE58EF2D65F1DB9EF391C00F0A77C4F961D60BBB54D0B0DE67616E",
    ),
    "G1FABRPREV-G1-VIRAL-001.manifest": (
        FABRPREV_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_manifest.md",
        "7B6AF4B28CC90BB7A8537BFD996C2DBACF32EAE3343CCDAF92DEAE9B86147745",
    ),
}

NEGATIVE_CAPABILITIES = [
    "policy_decision",
    "blocker_resolution",
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
    parser = argparse.ArgumentParser(description="Build unsupported/negative fixture policy decision prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Unsupported/negative fixture policy decision prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Unsupported/negative fixture policy decision prep requires {AUTHORIZATION_ID}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    review = read_json(INPUT_HASHES["G1FABRPREV-G1-VIRAL-001.review"][0])
    if review["review_id"] != "G1FABRPREV-G1-VIRAL-001":
        raise SystemExit("unexpected G1FABRPREV review")
    if review["next_candidate"] != "unsupported_negative_fixture_policy_decision_prep":
        raise SystemExit("G1FABRPREV did not select unsupported/negative fixture policy prep")
    if review["creates_blocker_resolution"] or review["admits_fixture"] or review["accepts_whole_gate_1"]:
        raise SystemExit("G1FABRPREV exceeds prep-only boundary")
    return verified, review


def build_packet(verified_inputs: dict[str, dict[str, str]], review: dict) -> dict:
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "unsupported_negative_fixture_policy_decision_prep_ready_for_review",
        "purpose": "policy_decision_prep_only_no_policy_decision",
        "source_review": review["review_id"],
        "creates_policy_decision": False,
        "creates_blocker_resolution": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "policy_questions": [
            {
                "question_id": "unsupported_profiles_scope",
                "status": "needs_human_decision",
                "decision_needed": "which source/profile families remain out of Core 0.1 scope",
                "candidate_default": "declare non-Viral-like/non-page-complete evidence profiles unsupported for Core 0.1",
            },
            {
                "question_id": "negative_fixture_obligations",
                "status": "needs_human_decision",
                "decision_needed": "which negative fixtures or counterexamples are required before fixture admission",
                "candidate_default": "require negative fixtures for unsupported profile claims before any fixture admission",
            },
            {
                "question_id": "invalidation_conditions",
                "status": "needs_human_decision",
                "decision_needed": "what invalidates a future unsupported/negative fixture policy",
                "candidate_default": "new page 021+ evidence, new OCR/render evidence, or user policy change invalidates",
            },
            {
                "question_id": "fixture_admission_dependency",
                "status": "needs_human_decision",
                "decision_needed": "whether fixture admission is blocked until policy questions are recorded",
                "candidate_default": "fixture admission remains blocked until this policy is accepted or explicitly parked",
            },
        ],
        "candidate_decision_text": (
            "prepare an unsupported/negative fixture policy record: declare unsupported Core 0.1 profiles, "
            "define required negative fixtures/counterexamples, attach invalidation conditions, and keep "
            "fixture admission plus whole Gate 1 blocked until a separate decision"
        ),
        "next_possible_packets": [
            "unsupported_negative_fixture_policy_record",
            "fixture_strategy_fit_decision_prep",
            "fixture_admission_readiness_refresh",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Decision Prep - G1UNFPDP-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_prep_ready_for_review`",
        "",
        "Purpose: decision prep only for unsupported profiles and negative fixture obligations.",
        "",
        "## Policy Questions",
        "",
    ]
    for row in packet["policy_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['status']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No policy decision.",
            "- No blocker resolution.",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, or implementation.",
            "- No push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "policy_question_count": len(packet["policy_questions"]),
            "creates_policy_decision": False,
            "creates_blocker_resolution": False,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_unsupported_negative_fixture_policy_decision_prep_manifest.md"
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Decision Prep Manifest - G1UNFPDP-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_prep_ready_for_review`",
        "",
        "Boundary: policy decision prep only; no policy decision, blocker resolution, fixture admission, fixture manifest creation, source-profile acceptance, page 021+, OCR/remediation, source/OCR/render/PDF/raw mutation, translation/proofreading/implementation, push, or whole Gate 1 acceptance.",
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
    verified_inputs, review = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, review)
    write_json(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
