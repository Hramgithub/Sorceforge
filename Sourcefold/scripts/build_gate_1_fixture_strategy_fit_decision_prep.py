from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_strategy_fit_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_strategy_fit_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
POLICY_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_decision_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
FIXTURE_STRATEGY = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "fixture_strategy.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-DECISION-PREP-001"
PACKET_ID = "G1FSFDP-G1-VIRAL-001"

INPUT_HASHES = {
    "G1UNFPAR-G1-VIRAL-001.acceptance": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance.json",
        "FD4D704EFE18EEA6BF33C82E6C106AF67268E7AEA5924CD4FFB150A4ACDE408C",
    ),
    "G1UNFPAR-G1-VIRAL-001.report": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_report.json",
        "9AE4141BC8824BA7B3F494222C2C45C5C32C2151742D5C6B8830EEF09909D232",
    ),
    "G1UNFPAR-G1-VIRAL-001.summary": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_summary.md",
        "C19E40A907688639C6BE286A149A8DF24CD16AC4F5150F430C7106A3AA874F35",
    ),
    "G1UNFPAR-G1-VIRAL-001.manifest": (
        POLICY_ROOT / "gate_1_unsupported_negative_fixture_policy_acceptance_manifest.md",
        "1A3F8DC8FEBD2721BC0C2FB2330BB12193010BA6866EDD2AC211ECA0E2FCB3B9",
    ),
    "fixture_strategy.md": (
        FIXTURE_STRATEGY,
        "7EF38F8B31F3EF58D275FDEC003A00CC996449B9BD062F76BC79B7B1F55A966F",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 fixture strategy fit decision prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture strategy fit decision prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture strategy fit decision prep requires {AUTHORIZATION_ID}")


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

    policy = read_json(INPUT_HASHES["G1UNFPAR-G1-VIRAL-001.acceptance"][0])
    if policy["acceptance_id"] != "G1UNFPAR-G1-VIRAL-001":
        raise SystemExit("unexpected unsupported/negative fixture policy acceptance")
    if not policy["creates_policy_decision"]:
        raise SystemExit("G1UNFPAR does not create the required policy decision")
    if not policy["resolves_unsupported_negative_fixture_policy_blocker"]:
        raise SystemExit("G1UNFPAR does not resolve the expected policy blocker")
    if policy["admits_fixture"] or policy["creates_fixture_manifest"] or policy["accepts_whole_gate_1"]:
        raise SystemExit("G1UNFPAR boundary is too broad")
    if policy["processes_page_021_plus"]:
        raise SystemExit("G1UNFPAR unexpectedly processes page 021+")
    return verified, policy


def build_packet(verified_inputs: dict[str, dict[str, str]], policy: dict) -> dict:
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_strategy_fit_decision_prep_ready_for_review",
        "purpose": "bounded_fixture_strategy_fit_decision_prep_only",
        "source_policy_acceptance": policy["acceptance_id"],
        "fixture_strategy_reference": "docs/plans/20260715-sourcefold-phase-0-release-charter/fixture_strategy.md",
        "creates_fixture_strategy_fit_decision": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "decision_questions": [
            {
                "question_id": "strategy_scope_fit",
                "prompt": (
                    "Does the draft fixture strategy fit the accepted Core 0.1 boundary: Viral-like, "
                    "page-complete accepted-only evidence, with non-matching profiles unsupported?"
                ),
                "default_candidate": "fit_for_core_0_1_only_with_non_viral_or_non_page_complete_profiles_unsupported",
            },
            {
                "question_id": "positive_fixture_seed_fit",
                "prompt": (
                    "Can pages 001-020 page-complete accepted-only evidence act as future positive fixture "
                    "seed material without admitting fixtures in this packet?"
                ),
                "default_candidate": "seed_material_fit_for_future_fixture_manifest_prep_only",
            },
            {
                "question_id": "negative_fixture_coverage_fit",
                "prompt": (
                    "Do the accepted negative fixture obligations cover unsupported profile claims, missing "
                    "policy, stale lineage/invalidation, and page 021+ boundary violations before admission?"
                ),
                "default_candidate": "negative_fixture_obligations_fit_requires_future_fixture_materialization",
            },
            {
                "question_id": "invalidation_dependency_fit",
                "prompt": (
                    "Should fixture strategy fit become stale if page 021+ evidence, OCR/render/layout evidence, "
                    "admission criteria, or user policy changes contradict the accepted policy?"
                ),
                "default_candidate": "fit_stale_on_policy_invalidation_conditions",
            },
            {
                "question_id": "admission_dependency",
                "prompt": (
                    "Should fixture admission remain blocked until a separate fixture strategy fit decision is "
                    "accepted and fixture admission readiness is refreshed?"
                ),
                "default_candidate": "admission_blocked_until_strategy_fit_decision_and_readiness_refresh",
            },
        ],
        "remaining_blockers": [
            "fixture_strategy_fit_decision",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_strategy_fit_acceptance_record",
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Fixture Strategy Fit Decision Prep - G1FSFDP-G1-VIRAL-001",
        "",
        "Status: `fixture_strategy_fit_decision_prep_ready_for_review`",
        "",
        "Purpose: prepare human review questions for whether the current fixture strategy fits the accepted unsupported/negative fixture policy.",
        "",
        "## Decision Questions",
        "",
    ]
    for row in packet["decision_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['default_candidate']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No fixture strategy fit decision is created.",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, implementation, or push.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in packet["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "decision_question_count": len(packet["decision_questions"]),
            "creates_fixture_strategy_fit_decision": False,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_strategy_fit_decision_prep_manifest.md"
    lines = [
        "# Gate 1 Fixture Strategy Fit Decision Prep Manifest - G1FSFDP-G1-VIRAL-001",
        "",
        "Status: `fixture_strategy_fit_decision_prep_ready_for_review`",
        "",
        "Boundary: fixture strategy fit decision prep only; no fixture strategy fit decision, no fixture admission, no fixture manifest, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, policy = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, policy)
    write_json(OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
