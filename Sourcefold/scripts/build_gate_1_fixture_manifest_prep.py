from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_manifest_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_manifest_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
READINESS_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_refresh_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-MANIFEST-PREP-001"
PACKET_ID = "G1FMP-G1-VIRAL-001"
HUMAN_DECISION = (
    "proceed with fixture_manifest_prep; no fixture admission, no whole Gate 1 "
    "acceptance, no page 021+, no push"
)

INPUT_HASHES = {
    "G1FARR-G1-VIRAL-001.refresh": (
        READINESS_ROOT / "gate_1_fixture_admission_readiness_refresh.json",
        "033770B6F75CD08F2E3D491412242B33C223846585B826C1EED7258956118EE9",
    ),
    "G1FARR-G1-VIRAL-001.report": (
        READINESS_ROOT / "gate_1_fixture_admission_readiness_refresh_report.json",
        "2C33DD7ED7FCBCAECB2BDB81D73160FC01196F116511CCB4E4C8020D60F38018",
    ),
    "G1FARR-G1-VIRAL-001.summary": (
        READINESS_ROOT / "gate_1_fixture_admission_readiness_refresh_summary.md",
        "ECCBE65314D80228050877BE5346DB02C14377287CB2B18D2E7923DA9DAE73AD",
    ),
    "G1FARR-G1-VIRAL-001.manifest": (
        READINESS_ROOT / "gate_1_fixture_admission_readiness_refresh_manifest.md",
        "76CCEF50B57DB60CC57B5CC006F8AF62AA51840680D50546527CD3AC488E02FF",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 fixture manifest prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture manifest prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture manifest prep requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture manifest prep requires the exact bounded human decision")


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

    readiness = read_json(INPUT_HASHES["G1FARR-G1-VIRAL-001.refresh"][0])
    if readiness["refresh_id"] != "G1FARR-G1-VIRAL-001":
        raise SystemExit("unexpected readiness refresh input")
    if not readiness["resolves_fixture_admission_readiness_refresh_blocker"]:
        raise SystemExit("fixture admission readiness refresh blocker is unresolved")
    if readiness["admits_fixture"] or readiness["creates_fixture_manifest"] or readiness["accepts_whole_gate_1"]:
        raise SystemExit("readiness refresh boundary is too broad")
    if readiness["processes_page_021_plus"]:
        raise SystemExit("readiness refresh unexpectedly processes page 021+")
    required = {
        "fixture_manifest_prep",
        "fixture_admission_decision",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    }
    if set(readiness["remaining_blockers"]) != required:
        raise SystemExit("readiness refresh blockers do not match manifest-prep prerequisites")
    return verified, readiness


def build_packet(verified_inputs: dict[str, dict[str, str]], readiness: dict) -> dict:
    accepted_pages = readiness["page_complete_accepted_pages"]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_manifest_prep_ready_for_review",
        "purpose": "bounded_fixture_manifest_prep_only_no_manifest_no_admission",
        "human_decision": HUMAN_DECISION,
        "source_readiness_refresh": readiness["refresh_id"],
        "page_complete_acceptance_scope": readiness["page_complete_acceptance_scope"],
        "page_complete_accepted_pages": accepted_pages,
        "proposed_manifest_shape": {
            "manifest_status_if_later_accepted": "candidate_fixture_manifest_ready_for_separate_admission_decision",
            "positive_fixture_seed_scope": "pages_001_020_page_complete_accepted_only",
            "negative_fixture_scope": "accepted_unsupported_negative_policy_classes_only",
            "invalidation_source": "G1UNFPAR_and_G1FSFAR_policy_strategy_conditions_via_G1FARR",
            "admission_dependency": "separate_fixture_admission_decision_required_after_manifest_review",
        },
        "proposed_positive_fixture_groups": [
            {
                "group_id": "positive_page_complete_seed_pages_001_020",
                "candidate_pages": accepted_pages,
                "status": "proposed_for_future_fixture_manifest_only",
                "meaning": "Pages 001-020 may be listed as positive seed material in a later fixture manifest; they are not admitted by this prep packet.",
            }
        ],
        "proposed_negative_fixture_groups": [
            {
                "group_id": "negative_unsupported_profile_claim",
                "expected_failure_class": "unsupported_profile_claim",
                "status": "proposed_for_future_fixture_manifest_only",
            },
            {
                "group_id": "negative_missing_or_unresolved_policy",
                "expected_failure_class": "missing_unresolved_negative_fixture_policy",
                "status": "proposed_for_future_fixture_manifest_only",
            },
            {
                "group_id": "negative_stale_lineage_or_invalidation_trigger",
                "expected_failure_class": "stale_lineage_or_invalidation_trigger",
                "status": "proposed_for_future_fixture_manifest_only",
            },
            {
                "group_id": "negative_page_021_plus_boundary_violation",
                "expected_failure_class": "page_021_plus_boundary_violation",
                "status": "proposed_for_future_fixture_manifest_only",
            },
        ],
        "review_questions": [
            {
                "question_id": "positive_fixture_seed_manifest_shape",
                "prompt": "Should pages 001-020 be represented as one positive page-complete seed group in a later fixture manifest?",
                "default_candidate": "positive_seed_group_pages_001_020",
            },
            {
                "question_id": "negative_fixture_group_manifest_shape",
                "prompt": "Should the four accepted negative policy classes become required negative fixture groups in a later manifest?",
                "default_candidate": "four_negative_groups_from_G1UNFPAR_policy",
            },
            {
                "question_id": "manifest_invalidation_shape",
                "prompt": "Should the later manifest inherit G1UNFPAR/G1FSFAR invalidation through G1FARR?",
                "default_candidate": "inherit_policy_and_strategy_invalidation",
            },
            {
                "question_id": "manifest_admission_dependency",
                "prompt": "Should the later manifest remain non-admitted until a separate fixture admission decision?",
                "default_candidate": "manifest_does_not_admit_fixtures",
            },
        ],
        "creates_fixture_manifest": False,
        "admits_fixture": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_manifest_review",
            "fixture_manifest_acceptance_record",
            "fixture_admission_decision",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_manifest_acceptance_record",
            "fixture_admission_decision_prep",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Fixture Manifest Prep - G1FMP-G1-VIRAL-001",
        "",
        "Status: `fixture_manifest_prep_ready_for_review`",
        "",
        "Purpose: prepare the future fixture manifest shape after fixture admission readiness refresh.",
        "",
        "This packet does not create a fixture manifest and does not admit fixtures.",
        "",
        "## Proposed Positive Fixture Group",
        "",
    ]
    for row in packet["proposed_positive_fixture_groups"]:
        lines.append(f"- `{row['group_id']}`: `{row['status']}`")
    lines.extend(["", "## Proposed Negative Fixture Groups", ""])
    for row in packet["proposed_negative_fixture_groups"]:
        lines.append(f"- `{row['group_id']}`: `{row['expected_failure_class']}`")
    lines.extend(["", "## Review Questions", ""])
    for row in packet["review_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['default_candidate']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- Fixture manifest creation: `false`.",
            "- Fixture admission: `false`.",
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
    write_text(OUT_ROOT / "gate_1_fixture_manifest_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_manifest_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "positive_fixture_group_count": len(packet["proposed_positive_fixture_groups"]),
            "negative_fixture_group_count": len(packet["proposed_negative_fixture_groups"]),
            "review_question_count": len(packet["review_questions"]),
            "creates_fixture_manifest": False,
            "admits_fixture": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_manifest_prep_manifest.md"
    lines = [
        "# Gate 1 Fixture Manifest Prep Manifest - G1FMP-G1-VIRAL-001",
        "",
        "Status: `fixture_manifest_prep_ready_for_review`",
        "",
        "Boundary: fixture manifest prep only; no fixture manifest creation, no fixture admission, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    verified_inputs, readiness = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, readiness)
    write_json(OUT_ROOT / "gate_1_fixture_manifest_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
