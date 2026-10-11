from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_gate_1_fixture_strategy_fit_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_strategy_fit_acceptance.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_decision_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_acceptance_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-ACCEPTANCE-001"
ACCEPTANCE_ID = "G1FSFAR-G1-VIRAL-001"
SOURCE_PACKET_ID = "G1FSFDP-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1fsfdp packet ok; proceed to prepare fixture strategy fit acceptance record over "
    "strategy_scope_fit, positive_fixture_seed_fit, negative_fixture_coverage_fit, "
    "invalidation_dependency_fit, and admission_dependency; no fixture admission, "
    "no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push"
)

INPUT_HASHES = {
    "G1FSFDP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_fixture_strategy_fit_decision_prep.json",
        "969D416B56137635ED7D6D99BAB270D19F876C7F93B2F76092BCF36228D84E8F",
    ),
    "G1FSFDP-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_fixture_strategy_fit_decision_prep_report.json",
        "DE20186B42A74682FBDAE13B4A3C12C883172B7C1DA740F382643EE94FE4AD92",
    ),
    "G1FSFDP-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_fixture_strategy_fit_decision_prep_summary.md",
        "C2C92E86B43D1BE288FBD398AD3A109947780839683540F93BE4FB9323E3DC3D",
    ),
    "G1FSFDP-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_fixture_strategy_fit_decision_prep_manifest.md",
        "FDC9F60F8BE8802C9B3B674C9D47431021DF0A480E36677E2722EDA768409431",
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 fixture strategy fit decision prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture strategy fit acceptance is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture strategy fit acceptance requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture strategy fit acceptance requires the exact bounded human decision")


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

    source_packet = read_json(INPUT_HASHES["G1FSFDP-G1-VIRAL-001.packet"][0])
    if source_packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected G1FSFDP source packet")
    if source_packet["status"] != "fixture_strategy_fit_decision_prep_ready_for_review":
        raise SystemExit("G1FSFDP is not ready for review")
    if source_packet["creates_fixture_strategy_fit_decision"]:
        raise SystemExit("G1FSFDP unexpectedly already creates a strategy fit decision")
    if source_packet["admits_fixture"] or source_packet["creates_fixture_manifest"] or source_packet["accepts_whole_gate_1"]:
        raise SystemExit("G1FSFDP boundary is too broad")
    expected_questions = {
        "strategy_scope_fit",
        "positive_fixture_seed_fit",
        "negative_fixture_coverage_fit",
        "invalidation_dependency_fit",
        "admission_dependency",
    }
    if {row["question_id"] for row in source_packet["decision_questions"]} != expected_questions:
        raise SystemExit("G1FSFDP does not contain the expected five decision questions")
    return verified, source_packet


def build_acceptance(verified_inputs: dict[str, dict[str, str]], source_packet: dict) -> dict:
    accepted_decisions = []
    for row in source_packet["decision_questions"]:
        accepted_decision = {
            "question_id": row["question_id"],
            "decision": row["default_candidate"],
            "accepted_as_strategy_fit_decision": True,
            "source_prompt": row["prompt"],
        }
        accepted_decisions.append(accepted_decision)

    return {
        "acceptance_id": ACCEPTANCE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_strategy_fit_decision_accepted",
        "purpose": "bounded_fixture_strategy_fit_acceptance_record",
        "human_decision": HUMAN_DECISION,
        "source_decision_prep_packet": source_packet["packet_id"],
        "source_policy_acceptance": source_packet["source_policy_acceptance"],
        "fixture_strategy_reference": source_packet["fixture_strategy_reference"],
        "creates_fixture_strategy_fit_decision": True,
        "accepted_strategy_fit_scope": [
            "strategy_scope_fit",
            "positive_fixture_seed_fit",
            "negative_fixture_coverage_fit",
            "invalidation_dependency_fit",
            "admission_dependency",
        ],
        "accepted_strategy_fit_decisions": accepted_decisions,
        "resolves_fixture_strategy_fit_blocker": True,
        "resolved_blocker": "fixture_strategy_fit_decision",
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_admission_readiness_refresh",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(acceptance: dict) -> None:
    lines = [
        "# Gate 1 Fixture Strategy Fit Acceptance - G1FSFAR-G1-VIRAL-001",
        "",
        "Status: `fixture_strategy_fit_decision_accepted`",
        "",
        "Decision: Bogdan accepted `G1FSFDP-G1-VIRAL-001` as the fixture strategy fit decision-prep packet.",
        "",
        "## Accepted Strategy Fit Scope",
        "",
    ]
    for item in acceptance["accepted_strategy_fit_scope"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Accepted Strategy Fit Decisions",
            "",
        ]
    )
    for row in acceptance["accepted_strategy_fit_decisions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Fixture strategy fit decision accepted: `true`.",
            "- Fixture strategy fit blocker resolved: `true`.",
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
    write_text(OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance_summary.md", "\n".join(lines))


def write_report(acceptance: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance_report.json",
        {
            "acceptance_id": ACCEPTANCE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": acceptance["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "accepted_strategy_fit_decision_count": len(acceptance["accepted_strategy_fit_decisions"]),
            "creates_fixture_strategy_fit_decision": True,
            "resolves_fixture_strategy_fit_blocker": True,
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
    manifest_name = "gate_1_fixture_strategy_fit_acceptance_manifest.md"
    lines = [
        "# Gate 1 Fixture Strategy Fit Acceptance Manifest - G1FSFAR-G1-VIRAL-001",
        "",
        "Status: `fixture_strategy_fit_decision_accepted`",
        "",
        "Boundary: fixture strategy fit acceptance only; no fixture admission, no fixture manifest, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, source_packet = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    acceptance = build_acceptance(verified_inputs, source_packet)
    write_json(OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance.json", acceptance)
    write_summary(acceptance)
    write_report(acceptance)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
