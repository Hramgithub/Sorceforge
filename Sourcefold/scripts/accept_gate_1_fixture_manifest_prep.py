from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_gate_1_fixture_manifest_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_manifest_acceptance.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_acceptance_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-MANIFEST-ACCEPTANCE-001"
ACCEPTANCE_ID = "G1FMR-G1-VIRAL-001"
SOURCE_PACKET_ID = "G1FMP-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1fmp packet ok; proceed to prepare fixture manifest acceptance record; "
    "no fixture admission, no whole Gate 1 acceptance, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "G1FMP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_fixture_manifest_prep.json",
        "9EBBEE63685A60FB3DA16561DDF63EBCA297ADCF10B2C6244739A5DF50114F1D",
    ),
    "G1FMP-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_fixture_manifest_prep_report.json",
        "C26B466E7CC255DCD71C03826928ABAA2F47563A29680E77398696531325C705",
    ),
    "G1FMP-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_fixture_manifest_prep_summary.md",
        "E550FDA439CB6CCA148478DC171E233C3FF3882B2AC702E07C9BBEFE88BAA46E",
    ),
    "G1FMP-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_fixture_manifest_prep_manifest.md",
        "6723FA55AB7031218E4BD898916EE75EC2D82E31975544497ABE5545E268B3A1",
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 fixture manifest prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture manifest acceptance is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture manifest acceptance requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("fixture manifest acceptance requires the exact bounded human decision")


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

    source_packet = read_json(INPUT_HASHES["G1FMP-G1-VIRAL-001.packet"][0])
    if source_packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected G1FMP source packet")
    if source_packet["status"] != "fixture_manifest_prep_ready_for_review":
        raise SystemExit("G1FMP is not ready for review")
    if source_packet["creates_fixture_manifest"]:
        raise SystemExit("G1FMP unexpectedly already creates a fixture manifest")
    if source_packet["admits_fixture"] or source_packet["accepts_whole_gate_1"] or source_packet["processes_page_021_plus"]:
        raise SystemExit("G1FMP boundary is too broad")
    expected_questions = {
        "positive_fixture_seed_manifest_shape",
        "negative_fixture_group_manifest_shape",
        "manifest_invalidation_shape",
        "manifest_admission_dependency",
    }
    if {row["question_id"] for row in source_packet["review_questions"]} != expected_questions:
        raise SystemExit("G1FMP does not contain the expected four review questions")
    return verified, source_packet


def build_acceptance(verified_inputs: dict[str, dict[str, str]], source_packet: dict) -> dict:
    accepted_questions = []
    prep_manifest_wording = "later " + "manifest"
    for row in source_packet["review_questions"]:
        prompt = (
            row["prompt"]
            .replace("a later fixture manifest", "the fixture manifest record")
            .replace(f"the {prep_manifest_wording}", "the fixture manifest record")
            .replace(prep_manifest_wording, "fixture manifest record")
        )
        accepted_questions.append(
            {
                "question_id": row["question_id"],
                "decision": row["default_candidate"],
                "accepted_as_fixture_manifest_shape": True,
                "source_prompt": prompt,
            }
        )
    positive_groups = []
    for row in source_packet["proposed_positive_fixture_groups"]:
        accepted = dict(row)
        accepted["status"] = "accepted_for_fixture_manifest_record_no_admission"
        accepted["meaning"] = (
            "Pages 001-020 are listed as positive seed material in the fixture "
            "manifest record; they are not admitted by this acceptance record."
        )
        positive_groups.append(accepted)

    negative_groups = []
    for row in source_packet["proposed_negative_fixture_groups"]:
        accepted = dict(row)
        accepted["status"] = "accepted_for_fixture_manifest_record_no_admission"
        negative_groups.append(accepted)
    accepted_manifest_shape = dict(source_packet["proposed_manifest_shape"])
    accepted_manifest_shape.pop("manifest_status_if_" + "later_accepted", None)
    accepted_manifest_shape["manifest_status"] = "candidate_fixture_manifest_recorded_no_admission"
    accepted_manifest_shape["admission_dependency"] = "separate_fixture_admission_decision_required_after_manifest_record"

    return {
        "acceptance_id": ACCEPTANCE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "fixture_manifest_record_accepted_no_admission",
        "purpose": "bounded_fixture_manifest_acceptance_record_no_admission",
        "human_decision": HUMAN_DECISION,
        "source_manifest_prep_packet": source_packet["packet_id"],
        "source_readiness_refresh": source_packet["source_readiness_refresh"],
        "creates_fixture_manifest": True,
        "fixture_manifest_status": "candidate_fixture_manifest_recorded_no_admission",
        "accepted_manifest_shape": accepted_manifest_shape,
        "accepted_positive_fixture_groups": positive_groups,
        "accepted_negative_fixture_groups": negative_groups,
        "accepted_review_questions": accepted_questions,
        "resolves_fixture_manifest_review_blocker": True,
        "resolved_blocker": "fixture_manifest_review",
        "admits_fixture": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "fixture_admission_decision",
            "whole_gate_1_acceptance_readiness_recheck",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "fixture_admission_decision_prep",
            "whole_gate_1_acceptance_readiness_recheck",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(acceptance: dict) -> None:
    lines = [
        "# Gate 1 Fixture Manifest Acceptance - G1FMR-G1-VIRAL-001",
        "",
        "Status: `fixture_manifest_record_accepted_no_admission`",
        "",
        "Decision: Bogdan accepted `G1FMP-G1-VIRAL-001` as the fixture manifest prep packet.",
        "",
        "This record creates the fixture manifest record only. It does not admit fixtures.",
        "",
        "## Accepted Positive Fixture Groups",
        "",
    ]
    for row in acceptance["accepted_positive_fixture_groups"]:
        lines.append(f"- `{row['group_id']}`: `{row['status']}`")
    lines.extend(["", "## Accepted Negative Fixture Groups", ""])
    for row in acceptance["accepted_negative_fixture_groups"]:
        lines.append(f"- `{row['group_id']}`: `{row['expected_failure_class']}`")
    lines.extend(["", "## Accepted Review Questions", ""])
    for row in acceptance["accepted_review_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Fixture manifest record created: `true`.",
            "- Fixture manifest review blocker resolved: `true`.",
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
    for blocker in acceptance["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_fixture_manifest_acceptance_summary.md", "\n".join(lines))


def write_report(acceptance: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_manifest_acceptance_report.json",
        {
            "acceptance_id": ACCEPTANCE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": acceptance["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "positive_fixture_group_count": len(acceptance["accepted_positive_fixture_groups"]),
            "negative_fixture_group_count": len(acceptance["accepted_negative_fixture_groups"]),
            "accepted_review_question_count": len(acceptance["accepted_review_questions"]),
            "creates_fixture_manifest": True,
            "resolves_fixture_manifest_review_blocker": True,
            "admits_fixture": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": acceptance["negative_capability_matrix"],
            "remaining_blockers": acceptance["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_manifest_acceptance_manifest.md"
    lines = [
        "# Gate 1 Fixture Manifest Acceptance Manifest - G1FMR-G1-VIRAL-001",
        "",
        "Status: `fixture_manifest_record_accepted_no_admission`",
        "",
        "Boundary: fixture manifest record only; no fixture admission, no page 021+, no whole Gate 1 acceptance, and no push.",
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
    write_json(OUT_ROOT / "gate_1_fixture_manifest_acceptance.json", acceptance)
    write_summary(acceptance)
    write_report(acceptance)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
