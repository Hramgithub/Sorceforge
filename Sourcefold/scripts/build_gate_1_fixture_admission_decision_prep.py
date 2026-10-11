from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_admission_decision_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_admission_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MANIFEST_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_acceptance_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-PREP-001"
PACKET_ID = "G1FADP-G1-VIRAL-001"
SOURCE_MANIFEST_ID = "G1FMR-G1-VIRAL-001"
HUMAN_DECISION = (
    "proceed with fixture_admission_decision_prep; no fixture admission, "
    "no whole Gate 1 acceptance, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "G1FMR-G1-VIRAL-001.acceptance": (
        MANIFEST_ROOT / "gate_1_fixture_manifest_acceptance.json",
        "5C5B2530F1EE2A65F4D0C2A52AC22973A62EF4B1CD544EC8184F7751BAC0EEC4",
    ),
    "G1FMR-G1-VIRAL-001.report": (
        MANIFEST_ROOT / "gate_1_fixture_manifest_acceptance_report.json",
        "141FC5D854542ABF7F3D6699A8FAA5DE2FE99E6C4EA82A298AC7A4B12C15431D",
    ),
    "G1FMR-G1-VIRAL-001.summary": (
        MANIFEST_ROOT / "gate_1_fixture_manifest_acceptance_summary.md",
        "5AC4EB35225606F7FD0A96BAA4AFB18A2DC26DB4A4C3992A14AC52DCE7E2BBA9",
    ),
    "G1FMR-G1-VIRAL-001.manifest": (
        MANIFEST_ROOT / "gate_1_fixture_manifest_acceptance_manifest.md",
        "4DEB976065C8976EBAA88746980007863969AA4D742A969D0AF777BB5AB2A7BC",
    ),
}

NEGATIVE_CAPABILITIES = [
    "fixture_admission",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 fixture admission decision prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture admission decision prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture admission decision prep requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture admission decision prep requires the exact bounded human decision")


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

    manifest = read_json(INPUT_HASHES["G1FMR-G1-VIRAL-001.acceptance"][0])
    if manifest["acceptance_id"] != SOURCE_MANIFEST_ID:
        raise SystemExit("unexpected fixture manifest record input")
    if manifest["status"] != "fixture_manifest_record_accepted_no_admission":
        raise SystemExit("fixture manifest record is not accepted")
    if not manifest["creates_fixture_manifest"]:
        raise SystemExit("fixture manifest record was not created")
    if manifest["admits_fixture"] or manifest["accepts_whole_gate_1"] or manifest["processes_page_021_plus"]:
        raise SystemExit("fixture manifest record boundary is too broad")
    if len(manifest["accepted_positive_fixture_groups"]) != 1:
        raise SystemExit("fixture manifest record must contain one positive group")
    if len(manifest["accepted_negative_fixture_groups"]) != 4:
        raise SystemExit("fixture manifest record must contain four negative groups")
    return verified, manifest


def build_packet(verified_inputs: dict[str, dict[str, str]], manifest: dict) -> dict:
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_admission_decision_prep_ready_for_review",
        "purpose": "bounded_fixture_admission_decision_prep_only_no_admission",
        "human_decision": HUMAN_DECISION,
        "source_fixture_manifest_record": manifest["acceptance_id"],
        "source_readiness_refresh": manifest["source_readiness_refresh"],
        "fixture_manifest_status": manifest["fixture_manifest_status"],
        "admission_candidate_groups": {
            "positive_fixture_groups": manifest["accepted_positive_fixture_groups"],
            "negative_fixture_groups": manifest["accepted_negative_fixture_groups"],
        },
        "decision_questions": [
            {
                "question_id": "positive_fixture_group_admission_scope",
                "prompt": "Should the pages 001-020 positive seed group be considered eligible for a future fixture admission decision?",
                "default_candidate": "positive_seed_group_pages_001_020_eligible_for_future_admission_decision",
            },
            {
                "question_id": "negative_fixture_group_admission_scope",
                "prompt": "Should the four accepted negative fixture groups be required before any future fixture admission decision?",
                "default_candidate": "four_negative_groups_required_for_future_admission_decision",
            },
            {
                "question_id": "admission_invalidation_and_lineage_blockers",
                "prompt": "Should stale lineage, accepted-policy invalidation, strategy invalidation, and page 021+ boundary violation block future fixture admission?",
                "default_candidate": "block_admission_on_stale_lineage_policy_strategy_or_page_021_plus_boundary",
            },
            {
                "question_id": "admission_decision_boundary",
                "prompt": "Should this packet remain decision-prep only and require a separate fixture admission acceptance record?",
                "default_candidate": "separate_fixture_admission_acceptance_required",
            },
            {
                "question_id": "whole_gate_1_dependency",
                "prompt": "Should whole Gate 1 remain blocked until after any separate fixture admission decision and readiness recheck?",
                "default_candidate": "whole_gate_1_requires_future_readiness_recheck_after_admission_path",
            },
        ],
        "creates_fixture_admission_decision": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_admission_decision_review",
            "fixture_admission_decision_acceptance_record",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_admission_decision_acceptance_record",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Decision Prep - G1FADP-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_decision_prep_ready_for_review`",
        "",
        "Purpose: prepare fixture admission decision questions after the fixture manifest record.",
        "",
        "This packet does not admit fixtures.",
        "",
        "## Admission Candidate Groups",
        "",
    ]
    for row in packet["admission_candidate_groups"]["positive_fixture_groups"]:
        lines.append(f"- Positive: `{row['group_id']}`")
    for row in packet["admission_candidate_groups"]["negative_fixture_groups"]:
        lines.append(f"- Negative: `{row['group_id']}` / `{row['expected_failure_class']}`")
    lines.extend(["", "## Decision Questions", ""])
    for row in packet["decision_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['default_candidate']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- Fixture admission decision created: `false`.",
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
    for blocker in packet["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_fixture_admission_decision_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_admission_decision_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "positive_fixture_group_count": len(packet["admission_candidate_groups"]["positive_fixture_groups"]),
            "negative_fixture_group_count": len(packet["admission_candidate_groups"]["negative_fixture_groups"]),
            "decision_question_count": len(packet["decision_questions"]),
            "creates_fixture_admission_decision": False,
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
    manifest_name = "gate_1_fixture_admission_decision_prep_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Decision Prep Manifest - G1FADP-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_decision_prep_ready_for_review`",
        "",
        "Boundary: fixture admission decision prep only; no fixture admission, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, manifest = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, manifest)
    write_json(OUT_ROOT / "gate_1_fixture_admission_decision_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
