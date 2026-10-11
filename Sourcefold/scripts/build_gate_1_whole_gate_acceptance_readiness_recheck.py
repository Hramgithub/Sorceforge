from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_whole_gate_acceptance_readiness_recheck.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_whole_gate_acceptance_readiness_recheck.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
ADMISSION_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_acceptance_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-READINESS-RECHECK-PREP-001"
PACKET_ID = "G1WGARR-G1-VIRAL-001"
SOURCE_ADMISSION_ID = "G1FADAR-G1-VIRAL-001"
HUMAN_DECISION = "Ок делай"
AUTHORIZED_SCOPE = (
    "proceed with whole Gate 1 acceptance readiness recheck prep; no whole Gate 1 acceptance, "
    "no page 021+, no source-profile acceptance, no OCR/render/PDF/raw mutation, "
    "no translation/proofreading/implementation, no push, commit"
)

INPUT_HASHES = {
    "G1FADAR-G1-VIRAL-001.acceptance": (
        ADMISSION_ROOT / "gate_1_fixture_admission_decision_acceptance.json",
        "9802BFFFAAC6E5BD22B7897DD449C56B08740F0249830D4DCE02164013A53092",
    ),
    "G1FADAR-G1-VIRAL-001.report": (
        ADMISSION_ROOT / "gate_1_fixture_admission_decision_acceptance_report.json",
        "40797B2AEE9F2C0026FF222EA2F0A87CE458CB244382069387CF077437A80583",
    ),
    "G1FADAR-G1-VIRAL-001.summary": (
        ADMISSION_ROOT / "gate_1_fixture_admission_decision_acceptance_summary.md",
        "82B29027D0F6A729C88B822E166AE7E828107828702B5D35F2478A2E8CD3C9EE",
    ),
    "G1FADAR-G1-VIRAL-001.manifest": (
        ADMISSION_ROOT / "gate_1_fixture_admission_decision_acceptance_manifest.md",
        "449B796B88DD8E305D11D05128066E29280D56703C16F67E0C8B5F1A58D6C443",
    ),
}

NEGATIVE_CAPABILITIES = [
    "whole_gate_1_acceptance",
    "source_profile_acceptance",
    "new_or_broader_fixture_admission",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 whole-Gate acceptance readiness recheck prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 whole-Gate acceptance readiness recheck is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 whole-Gate acceptance readiness recheck requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("whole-Gate acceptance readiness recheck requires the exact bounded human decision")


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

    admission = read_json(INPUT_HASHES["G1FADAR-G1-VIRAL-001.acceptance"][0])
    if admission["acceptance_id"] != SOURCE_ADMISSION_ID:
        raise SystemExit("unexpected fixture admission decision acceptance input")
    if admission["status"] != "fixture_admission_decision_accepted":
        raise SystemExit("fixture admission decision acceptance is not accepted")
    if not admission["creates_fixture_admission_decision"] or not admission["admits_fixture"]:
        raise SystemExit("fixture admission decision acceptance did not admit fixtures")
    if admission["accepts_whole_gate_1"] or admission["accepts_source_profile"]:
        raise SystemExit("fixture admission decision acceptance boundary is too broad")
    if admission["processes_page_021_plus"] or admission["executes_ocr"]:
        raise SystemExit("fixture admission decision acceptance created downstream work")
    if len(admission["admitted_positive_fixture_groups"]) != 1:
        raise SystemExit("fixture admission decision must contain one positive admitted group")
    if len(admission["admitted_negative_fixture_groups"]) != 4:
        raise SystemExit("fixture admission decision must contain four negative admitted groups")
    if admission["remaining_blockers"][0] != "whole_gate_1_acceptance_readiness_recheck":
        raise SystemExit("whole Gate 1 readiness recheck is not the next blocker")
    return verified, admission


def build_packet(verified_inputs: dict[str, dict[str, str]], admission: dict) -> dict:
    positive_pages = admission["admitted_positive_fixture_groups"][0]["candidate_pages"]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "whole_gate_1_acceptance_readiness_recheck_ready_for_review",
        "purpose": "bounded_whole_gate_1_acceptance_readiness_recheck_prep_only",
        "human_decision": HUMAN_DECISION,
        "authorized_scope": AUTHORIZED_SCOPE,
        "source_fixture_admission_decision": admission["acceptance_id"],
        "source_fixture_manifest_record": admission["source_fixture_manifest_record"],
        "source_readiness_refresh": admission["source_readiness_refresh"],
        "page_complete_accepted_pages": positive_pages,
        "admitted_positive_fixture_groups": admission["admitted_positive_fixture_groups"],
        "admitted_negative_fixture_groups": admission["admitted_negative_fixture_groups"],
        "readiness_rows": [
            {
                "row_id": "pages_001_020_page_complete_scope",
                "status": "ready_as_individual_page_complete_inputs_only",
                "meaning": "Pages 001-020 are accepted page-complete individually and remain the only page range in this recheck.",
            },
            {
                "row_id": "fixture_admission_decision",
                "status": "ready_from_g1fadar_admitted_fixture_manifest_groups",
                "meaning": "The fixture admission decision blocker is resolved by G1FADAR-G1-VIRAL-001.",
            },
            {
                "row_id": "page_021_plus_boundary",
                "status": "blocked_separate_bounded_authorization_only",
                "meaning": "Page 021+ is not required for this recheck and remains unselected unless separately authorized.",
            },
            {
                "row_id": "source_profile_acceptance_boundary",
                "status": "not_created_by_this_recheck",
                "meaning": "This packet does not accept the whole source profile or mutate source-profile status.",
            },
            {
                "row_id": "whole_gate_1_acceptance_readiness",
                "status": "ready_for_separate_human_gate_acceptance_decision",
                "meaning": "No readiness blocker is resolved as whole Gate 1 acceptance; a separate acceptance record is still required.",
            },
        ],
        "review_questions": [
            {
                "question_id": "gate_1_scope_for_acceptance",
                "prompt": "Should whole Gate 1 acceptance, if later authorized, be limited to pages 001-020 plus the G1FADAR admitted fixture manifest groups?",
                "default_candidate": "limit_whole_gate_1_acceptance_candidate_to_pages_001_020_and_g1fadar_fixture_groups",
            },
            {
                "question_id": "page_021_plus_boundary",
                "prompt": "Should page 021+ remain outside the whole Gate 1 acceptance candidate unless separately authorized?",
                "default_candidate": "keep_page_021_plus_outside_candidate_without_separate_ba",
            },
            {
                "question_id": "acceptance_record_boundary",
                "prompt": "Should whole Gate 1 acceptance require a separate future acceptance record after this readiness recheck?",
                "default_candidate": "require_separate_whole_gate_1_acceptance_record",
            },
            {
                "question_id": "downstream_boundary",
                "prompt": "Should OCR/render/PDF/raw mutation, translation, proofreading, implementation, and push remain blocked after this recheck?",
                "default_candidate": "keep_all_downstream_actions_blocked_after_recheck",
            },
        ],
        "creates_readiness_recheck_packet": True,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "admits_new_or_broader_fixture": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "remaining_blockers": [
            "whole_gate_1_acceptance_decision_review",
            "whole_gate_1_acceptance_record_if_bogdan_later_accepts",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "next_possible_packets": [
            "whole_gate_1_acceptance_decision_record",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Whole-Gate Acceptance Readiness Recheck - G1WGARR-G1-VIRAL-001",
        "",
        "Status: `whole_gate_1_acceptance_readiness_recheck_ready_for_review`",
        "",
        "Purpose: recheck readiness for a future whole Gate 1 acceptance decision after `G1FADAR-G1-VIRAL-001`.",
        "",
        "This packet does not accept whole Gate 1.",
        "",
        "## Recheck Inputs",
        "",
        f"- Source fixture admission decision: `{packet['source_fixture_admission_decision']}`.",
        f"- Source fixture manifest record: `{packet['source_fixture_manifest_record']}`.",
        f"- Source readiness refresh: `{packet['source_readiness_refresh']}`.",
        f"- Page range in scope: `{packet['page_complete_accepted_pages'][0]}`-`{packet['page_complete_accepted_pages'][-1]}`.",
        f"- Positive admitted fixture groups: `{len(packet['admitted_positive_fixture_groups'])}`.",
        f"- Negative admitted fixture groups: `{len(packet['admitted_negative_fixture_groups'])}`.",
        "",
        "## Readiness Rows",
        "",
    ]
    for row in packet["readiness_rows"]:
        lines.append(f"- `{row['row_id']}`: `{row['status']}`")
    lines.extend(["", "## Review Questions", ""])
    for row in packet["review_questions"]:
        lines.append(f"- `{row['question_id']}`: `{row['default_candidate']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- Whole Gate 1 acceptance: `false`.",
            "- Whole source-profile acceptance: `false`.",
            "- New or broader fixture admission: `false`.",
            "- Page 021+ processing/authorization: `false`.",
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
    write_text(OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_readiness_recheck_packet": True,
            "page_complete_accepted_page_count": len(packet["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(packet["admitted_positive_fixture_groups"]),
            "negative_fixture_group_count": len(packet["admitted_negative_fixture_groups"]),
            "review_question_count": len(packet["review_questions"]),
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "admits_new_or_broader_fixture": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_whole_gate_acceptance_readiness_recheck_manifest.md"
    lines = [
        "# Gate 1 Whole-Gate Acceptance Readiness Recheck Manifest - G1WGARR-G1-VIRAL-001",
        "",
        "Status: `whole_gate_1_acceptance_readiness_recheck_ready_for_review`",
        "",
        "Boundary: readiness recheck prep only; no whole Gate 1 acceptance, no page 021+, no source-profile acceptance, no downstream action, and no push.",
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
    verified_inputs, admission = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, admission)
    write_json(OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
