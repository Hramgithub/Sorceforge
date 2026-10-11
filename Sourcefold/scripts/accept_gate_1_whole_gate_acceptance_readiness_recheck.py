from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_gate_1_whole_gate_acceptance_readiness_recheck.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_whole_gate_acceptance_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
RECHECK_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-DECISION-RECORD-001"
ACCEPTANCE_ID = "G1WGADR-G1-VIRAL-001"
SOURCE_PACKET_ID = "G1WGARR-G1-VIRAL-001"
HUMAN_DECISION = (
    "g1wgarr packet ok; proceed to prepare whole Gate 1 acceptance decision record limited to pages 001-020 "
    "and G1FADAR admitted fixture manifest groups; no page 021+, no source-profile acceptance beyond this "
    "Gate 1 record, no OCR/render/PDF/raw mutation, no translation/proofreading/implementation, no push, commit"
)

INPUT_HASHES = {
    "G1WGARR-G1-VIRAL-001.packet": (
        RECHECK_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck.json",
        "0637943A6B51CCD6BC0D9C434333F8A5F47318B14D843A569374400BE2B84B8B",
    ),
    "G1WGARR-G1-VIRAL-001.report": (
        RECHECK_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_report.json",
        "C813875F483AE5841C322E24729EA99C8C46790461141F3AE4D24AB6978DB772",
    ),
    "G1WGARR-G1-VIRAL-001.summary": (
        RECHECK_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_summary.md",
        "357BEB904BF478E7E17DC8F8A63BBEF9720AD7316E4484592131A286D68DB429",
    ),
    "G1WGARR-G1-VIRAL-001.manifest": (
        RECHECK_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_manifest.md",
        "B48C4C7C095464E27A2D31D60F427FBA43F096A22D5CE0A963BF071D6C028E76",
    ),
}

NEGATIVE_CAPABILITIES = [
    "page_021_plus_processing",
    "source_profile_acceptance_beyond_gate_1_record",
    "new_or_broader_fixture_admission",
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
    parser = argparse.ArgumentParser(description="Accept Gate 1 whole-Gate acceptance readiness recheck.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 whole-Gate acceptance decision record is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 whole-Gate acceptance decision record requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("whole-Gate acceptance decision record requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["G1WGARR-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected whole Gate 1 readiness recheck input")
    if packet["status"] != "whole_gate_1_acceptance_readiness_recheck_ready_for_review":
        raise SystemExit("whole Gate 1 readiness recheck is not ready for review")
    if not packet["creates_readiness_recheck_packet"]:
        raise SystemExit("readiness recheck packet was not created")
    if packet["accepts_whole_gate_1"]:
        raise SystemExit("readiness recheck already accepts whole Gate 1")
    if packet["accepts_source_profile"] or packet["processes_page_021_plus"] or packet["executes_ocr"]:
        raise SystemExit("readiness recheck boundary is too broad")
    if packet["next_possible_packets"][0] != "whole_gate_1_acceptance_decision_record":
        raise SystemExit("whole Gate 1 acceptance decision record is not the next packet")
    if len(packet["page_complete_accepted_pages"]) != 20:
        raise SystemExit("whole Gate 1 acceptance scope must contain pages 001-020 only")
    if len(packet["admitted_positive_fixture_groups"]) != 1:
        raise SystemExit("expected one admitted positive fixture group")
    if len(packet["admitted_negative_fixture_groups"]) != 4:
        raise SystemExit("expected four admitted negative fixture groups")
    return verified, packet


def build_acceptance(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    accepted_decisions = [
        {
            "question_id": row["question_id"],
            "decision": row["default_candidate"],
            "accepted_for_whole_gate_1_record": True,
            "source_prompt": row["prompt"],
        }
        for row in packet["review_questions"]
    ]
    return {
        "acceptance_id": ACCEPTANCE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "whole_gate_1_acceptance_decision_accepted",
        "purpose": "bounded_whole_gate_1_acceptance_decision_record",
        "human_decision": HUMAN_DECISION,
        "source_readiness_recheck_packet": packet["packet_id"],
        "source_fixture_admission_decision": packet["source_fixture_admission_decision"],
        "source_fixture_manifest_record": packet["source_fixture_manifest_record"],
        "source_readiness_refresh": packet["source_readiness_refresh"],
        "accepts_whole_gate_1": True,
        "whole_gate_1_acceptance_scope": {
            "page_complete_accepted_pages": packet["page_complete_accepted_pages"],
            "fixture_admission_decision": packet["source_fixture_admission_decision"],
            "positive_fixture_groups": packet["admitted_positive_fixture_groups"],
            "negative_fixture_groups": packet["admitted_negative_fixture_groups"],
            "page_021_plus_included": False,
            "source_profile_acceptance_beyond_this_record": False,
        },
        "accepted_whole_gate_1_decisions": accepted_decisions,
        "accepts_source_profile_beyond_gate_1_record": False,
        "admits_new_or_broader_fixture": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "creates_implementation": False,
        "push_performed": False,
        "remaining_blockers": [
            "page_021_plus_separate_bounded_authorization_if_selected",
            "source_profile_acceptance_beyond_gate_1_record_if_needed",
            "ocr_render_pdf_raw_translation_proofreading_implementation_requires_separate_authorization",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "core_0_1_implementation_planning_if_separately_authorized",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(acceptance: dict) -> None:
    scope = acceptance["whole_gate_1_acceptance_scope"]
    lines = [
        "# Gate 1 Whole-Gate Acceptance Decision - G1WGADR-G1-VIRAL-001",
        "",
        "Status: `whole_gate_1_acceptance_decision_accepted`",
        "",
        "Decision: Bogdan accepted `G1WGARR-G1-VIRAL-001` as the readiness recheck for a bounded whole Gate 1 acceptance record.",
        "",
        "This record accepts whole Gate 1 only for pages 001-020 and the `G1FADAR-G1-VIRAL-001` admitted fixture manifest groups.",
        "",
        "## Accepted Scope",
        "",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        f"- Positive fixture groups: `{len(scope['positive_fixture_groups'])}`.",
        f"- Negative fixture groups: `{len(scope['negative_fixture_groups'])}`.",
        "- Page 021+ included: `false`.",
        "- Source-profile acceptance beyond this Gate 1 record: `false`.",
        "",
        "## Accepted Decisions",
        "",
    ]
    for row in acceptance["accepted_whole_gate_1_decisions"]:
        lines.append(f"- `{row['question_id']}`: `{row['decision']}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Whole Gate 1 acceptance: `true`.",
            "- Source-profile acceptance beyond this Gate 1 record: `false`.",
            "- New or broader fixture admission: `false`.",
            "- Page 021+ processing/authorization: `false`.",
            "- OCR/remediation/render/PDF/raw/source mutation: `false`.",
            "- Translation/proofreading/implementation/push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in acceptance["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "gate_1_whole_gate_acceptance_decision_summary.md", "\n".join(lines))


def write_report(acceptance: dict) -> None:
    scope = acceptance["whole_gate_1_acceptance_scope"]
    write_json(
        OUT_ROOT / "gate_1_whole_gate_acceptance_decision_report.json",
        {
            "acceptance_id": ACCEPTANCE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": acceptance["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "accepts_whole_gate_1": True,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(scope["positive_fixture_groups"]),
            "negative_fixture_group_count": len(scope["negative_fixture_groups"]),
            "accepted_decision_count": len(acceptance["accepted_whole_gate_1_decisions"]),
            "accepts_source_profile_beyond_gate_1_record": False,
            "admits_new_or_broader_fixture": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "creates_implementation": False,
            "push_performed": False,
            "negative_capability_matrix": acceptance["negative_capability_matrix"],
            "remaining_blockers": acceptance["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_whole_gate_acceptance_decision_manifest.md"
    lines = [
        "# Gate 1 Whole-Gate Acceptance Decision Manifest - G1WGADR-G1-VIRAL-001",
        "",
        "Status: `whole_gate_1_acceptance_decision_accepted`",
        "",
        "Boundary: whole Gate 1 acceptance only for pages 001-020 and G1FADAR admitted fixture groups; no page 021+, no source-profile acceptance beyond this Gate 1 record, no downstream action, and no push.",
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
    write_json(OUT_ROOT / "gate_1_whole_gate_acceptance_decision.json", acceptance)
    write_summary(acceptance)
    write_report(acceptance)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
