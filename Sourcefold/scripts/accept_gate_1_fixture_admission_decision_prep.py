from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_gate_1_fixture_admission_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_admission_decision_acceptance.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_acceptance_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-ACCEPTANCE-001"
ACCEPTANCE_ID = "G1FADAR-G1-VIRAL-001"
SOURCE_PACKET_ID = "G1FADP-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1fadp packet ok; proceed to prepare fixture admission decision acceptance record; "
    "no whole Gate 1 acceptance, no page 021+, no push"
)

INPUT_HASHES = {
    "G1FADP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_fixture_admission_decision_prep.json",
        "E624062C3E150993EA699878FAFFB33F9E118EAF9FA4E218E8D42E51C3517D5A",
    ),
    "G1FADP-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_fixture_admission_decision_prep_report.json",
        "575948016BD5FAD17B6FEE6F1126D9748F845646F6C5336A2254D58DB3E9A4A5",
    ),
    "G1FADP-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_fixture_admission_decision_prep_summary.md",
        "F82BBE589A9FCF283EAE5C193B339FB91D5EC37C60DFAA894FDE7066E52D3870",
    ),
    "G1FADP-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_fixture_admission_decision_prep_manifest.md",
        "F9D65BE96E27ED076BFF5E73F813DA0490FC36B172D1C0FE51996FAEC3A1408E",
    ),
}

NEGATIVE_CAPABILITIES = [
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 fixture admission decision prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture admission decision acceptance is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture admission decision acceptance requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture admission decision acceptance requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["G1FADP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected fixture admission decision prep input")
    if packet["status"] != "fixture_admission_decision_prep_ready_for_review":
        raise SystemExit("fixture admission decision prep is not ready for review")
    if packet["creates_fixture_admission_decision"] or packet["admits_fixture"]:
        raise SystemExit("fixture admission decision prep already admits fixtures")
    if packet["accepts_whole_gate_1"] or packet["processes_page_021_plus"]:
        raise SystemExit("fixture admission decision prep boundary is too broad")
    if len(packet["admission_candidate_groups"]["positive_fixture_groups"]) != 1:
        raise SystemExit("fixture admission prep must contain one positive group")
    if len(packet["admission_candidate_groups"]["negative_fixture_groups"]) != 4:
        raise SystemExit("fixture admission prep must contain four negative groups")
    return verified, packet


def build_acceptance(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    decision_overrides = {
        "positive_fixture_group_admission_scope": "positive_seed_group_pages_001_020_admitted",
        "negative_fixture_group_admission_scope": "four_negative_groups_admitted_as_required_fixture_coverage",
        "admission_decision_boundary": "fixture_admission_acceptance_record_created",
    }
    accepted_decisions = []
    for row in packet["decision_questions"]:
        accepted_decisions.append(
            {
                "question_id": row["question_id"],
                "decision": decision_overrides.get(row["question_id"], row["default_candidate"]),
                "accepted_as_fixture_admission_decision": True,
                "source_prompt": row["prompt"],
            }
        )
    positive_groups = []
    for row in packet["admission_candidate_groups"]["positive_fixture_groups"]:
        admitted = dict(row)
        admitted["status"] = "admitted_by_fixture_admission_decision"
        admitted["meaning"] = "Pages 001-020 are admitted as the positive fixture seed group by this decision."
        positive_groups.append(admitted)

    negative_groups = []
    for row in packet["admission_candidate_groups"]["negative_fixture_groups"]:
        admitted = dict(row)
        admitted["status"] = "admitted_by_fixture_admission_decision"
        negative_groups.append(admitted)

    return {
        "acceptance_id": ACCEPTANCE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_admission_decision_accepted",
        "purpose": "bounded_fixture_admission_decision_acceptance_record",
        "human_decision": HUMAN_DECISION,
        "source_decision_prep_packet": packet["packet_id"],
        "source_fixture_manifest_record": packet["source_fixture_manifest_record"],
        "source_readiness_refresh": packet["source_readiness_refresh"],
        "creates_fixture_admission_decision": True,
        "admits_fixture": True,
        "admitted_positive_fixture_groups": positive_groups,
        "admitted_negative_fixture_groups": negative_groups,
        "accepted_fixture_admission_decisions": accepted_decisions,
        "resolves_fixture_admission_decision_blocker": True,
        "resolved_blocker": "fixture_admission_decision",
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(acceptance: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Decision Acceptance - G1FADAR-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_decision_accepted`",
        "",
        "Decision: Bogdan accepted `G1FADP-G1-VIRAL-001` as the fixture admission decision prep packet.",
        "",
        "This record admits the fixture manifest groups. It does not accept whole Gate 1.",
        "",
        "## Admitted Fixture Groups",
        "",
    ]
    for row in acceptance["admitted_positive_fixture_groups"]:
        lines.append(f"- Positive: `{row['group_id']}`")
    for row in acceptance["admitted_negative_fixture_groups"]:
        lines.append(f"- Negative: `{row['group_id']}` / `{row['expected_failure_class']}`")
    lines.extend(["", "## Accepted Fixture Admission Decisions", ""])
    for row in acceptance["accepted_fixture_admission_decisions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Fixture admission decision accepted: `true`.",
            "- Fixture admission: `true`.",
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
    write_text(OUT_ROOT / "gate_1_fixture_admission_decision_acceptance_summary.md", "\n".join(lines))


def write_report(acceptance: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_admission_decision_acceptance_report.json",
        {
            "acceptance_id": ACCEPTANCE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": acceptance["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "positive_fixture_group_count": len(acceptance["admitted_positive_fixture_groups"]),
            "negative_fixture_group_count": len(acceptance["admitted_negative_fixture_groups"]),
            "accepted_fixture_admission_decision_count": len(acceptance["accepted_fixture_admission_decisions"]),
            "creates_fixture_admission_decision": True,
            "admits_fixture": True,
            "resolves_fixture_admission_decision_blocker": True,
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
    manifest_name = "gate_1_fixture_admission_decision_acceptance_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Decision Acceptance Manifest - G1FADAR-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_decision_accepted`",
        "",
        "Boundary: fixture admission decision acceptance only; no page 021+, no whole Gate 1 acceptance, and no push.",
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
    acceptance = build_acceptance(verified_inputs, packet)
    write_json(OUT_ROOT / "gate_1_fixture_admission_decision_acceptance.json", acceptance)
    write_summary(acceptance)
    write_report(acceptance)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
