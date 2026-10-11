from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_gate_1_unsupported_negative_fixture_policy_record.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_unsupported_negative_fixture_policy_acceptance.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
RECORD_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_record_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-ACCEPTANCE-001"
ACCEPTANCE_ID = "G1UNFPAR-G1-VIRAL-001"
SOURCE_RECORD_ID = "G1UNFPR-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1unfpr candidate ok; proceed to prepare unsupported/negative fixture policy acceptance record; "
    "no fixture admission, no whole Gate 1 acceptance, no page 021+, no push"
)

INPUT_HASHES = {
    "G1UNFPR-G1-VIRAL-001.record": (
        RECORD_ROOT / "gate_1_unsupported_negative_fixture_policy_record.json",
        "37CBDCFE0D9D715E3BCBA639F295C5609BBBB92F4678948BDF8747024E6D73F2",
    ),
    "G1UNFPR-G1-VIRAL-001.report": (
        RECORD_ROOT / "gate_1_unsupported_negative_fixture_policy_record_report.json",
        "F9CA1E06E77E273CA3C94D656D7FF6BD1BB09B6E733947739428A3C8F9127133",
    ),
    "G1UNFPR-G1-VIRAL-001.summary": (
        RECORD_ROOT / "gate_1_unsupported_negative_fixture_policy_record_summary.md",
        "97E18C7483F9D89D9417CCEAED5E6D34783B708FFB42D66D8681B4246BF2F651",
    ),
    "G1UNFPR-G1-VIRAL-001.manifest": (
        RECORD_ROOT / "gate_1_unsupported_negative_fixture_policy_record_manifest.md",
        "0FCA5F00EAC6FFE0A477F8EEA551E17B9AA2AF0F66B35D6FE2C35D612F6304E7",
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 unsupported/negative fixture policy record.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Unsupported/negative fixture policy acceptance is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Unsupported/negative fixture policy acceptance requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("unsupported/negative fixture policy acceptance requires the exact bounded human decision")


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

    source_record = read_json(INPUT_HASHES["G1UNFPR-G1-VIRAL-001.record"][0])
    if source_record["record_id"] != SOURCE_RECORD_ID:
        raise SystemExit("unexpected G1UNFPR source record")
    if source_record["status"] != "unsupported_negative_fixture_policy_record_ready_for_review":
        raise SystemExit("G1UNFPR is not ready for review")
    if source_record["creates_policy_decision"]:
        raise SystemExit("G1UNFPR unexpectedly already creates a policy decision")
    if source_record["admits_fixture"] or source_record["accepts_whole_gate_1"] or source_record["processes_page_021_plus"]:
        raise SystemExit("G1UNFPR boundary is too broad")
    if {row["question_id"] for row in source_record["candidate_policy_decisions"]} != {
        "unsupported_profiles_scope",
        "negative_fixture_obligations",
        "invalidation_conditions",
        "fixture_admission_dependency",
    }:
        raise SystemExit("G1UNFPR does not contain the expected four candidate decisions")
    return verified, source_record


def build_acceptance(verified_inputs: dict[str, dict[str, str]], source_record: dict) -> dict:
    accepted_decisions = []
    for row in source_record["candidate_policy_decisions"]:
        accepted = dict(row)
        accepted["accepted_as_policy"] = True
        accepted_decisions.append(accepted)

    return {
        "acceptance_id": ACCEPTANCE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "unsupported_negative_fixture_policy_decision_accepted",
        "purpose": "bounded_unsupported_negative_fixture_policy_acceptance_record",
        "human_decision": HUMAN_DECISION,
        "source_policy_record_candidate": source_record["record_id"],
        "source_decision_prep_packet": source_record["source_decision_prep_packet"],
        "source_review": source_record["source_review"],
        "creates_policy_decision": True,
        "accepted_policy_scope": [
            "unsupported_profiles_scope",
            "negative_fixture_obligations",
            "invalidation_conditions",
            "fixture_admission_dependency",
        ],
        "accepted_policy_decisions": accepted_decisions,
        "resolves_unsupported_negative_fixture_policy_blocker": True,
        "resolved_blocker": "unsupported_negative_fixture_policy_decision",
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_strategy_fit_decision",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_strategy_fit_decision_prep",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(acceptance: dict) -> None:
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Acceptance - G1UNFPAR-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_accepted`",
        "",
        "Decision: Bogdan accepted `G1UNFPR-G1-VIRAL-001` as the unsupported/negative fixture policy record.",
        "",
        "## Accepted Policy Scope",
        "",
    ]
    for item in acceptance["accepted_policy_scope"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Accepted Policy Decisions",
            "",
        ]
    )
    for row in acceptance["accepted_policy_decisions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Unsupported/negative fixture policy decision accepted: `true`.",
            "- Unsupported/negative fixture policy blocker resolved: `true`.",
            "- Fixture admission: `false`.",
            "- Fixture manifest creation: `false`.",
            "- Whole Gate 1 acceptance: `false`.",
            "- Source-profile acceptance: `false`.",
            "- Page 021+ processing: `false`.",
            "- OCR/remediation/render/PDF/raw mutation: `false`.",
            "- Translation/proofreading/implementation/push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in acceptance["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_summary.md", "\n".join(lines))


def write_report(acceptance: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_report.json",
        {
            "acceptance_id": ACCEPTANCE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": acceptance["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "accepted_policy_decision_count": len(acceptance["accepted_policy_decisions"]),
            "creates_policy_decision": True,
            "resolves_unsupported_negative_fixture_policy_blocker": True,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": acceptance["negative_capability_matrix"],
            "remaining_blockers": acceptance["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_unsupported_negative_fixture_policy_acceptance_manifest.md"
    lines = [
        "# Gate 1 Unsupported / Negative Fixture Policy Acceptance Manifest - G1UNFPAR-G1-VIRAL-001",
        "",
        "Status: `unsupported_negative_fixture_policy_decision_accepted`",
        "",
        "Boundary: unsupported/negative fixture policy acceptance only; no fixture admission, no fixture manifest, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, source_record = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    acceptance = build_acceptance(verified_inputs, source_record)
    write_json(OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance.json", acceptance)
    write_summary(acceptance)
    write_report(acceptance)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
