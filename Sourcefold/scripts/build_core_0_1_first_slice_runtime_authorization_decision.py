from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_first_slice_runtime_authorization_decision.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_first_slice_runtime_authorization_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SOURCE_ROOT = TRIAL_ROOT / "core_0_1_first_slice_runtime_authorization_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_first_slice_runtime_authorization_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-DECISION-001"
DECISION_ID = "C01RSAD-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01RSAP-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01rsap packet ok; proceed to prepare Core 0.1 first-slice runtime authorization decision for C01WP-01 "
    "from C01RSAP; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, "
    "no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01RSAP-G1-VIRAL-001.packet": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_prep.json",
        "CDCC31F41F7988C7017217DBD0E4F420C46D99A65CC51EC85913C28E501DB741",
    ),
    "C01RSAP-G1-VIRAL-001.report": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_prep_report.json",
        "D462D23C2DB50770B3E1386053C1CC4295151A558BB286EC41DCC436DD970C5B",
    ),
    "C01RSAP-G1-VIRAL-001.summary": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_prep_summary.md",
        "6338CDA040FDA9E70FA0F6E756009D69AE14C27F7DFC4AB6769B8CD731127491",
    ),
    "C01RSAP-G1-VIRAL-001.manifest": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_prep_manifest.md",
        "1D20D2BD7C32774B8C91378F11A5B38EDBAE5DE01FC6390AE7DFA3E67E4BD914",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
    "runtime_execution",
    "runtime_source_profile_lock",
    "runtime_source_profile_acceptance",
    "source_profile_acceptance_beyond_c01splpr",
    "ocr_execution",
    "ocr_remediation_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "source_mutation",
    "raw_mutation",
    "translation",
    "proofreading",
    "page_021_plus_processing",
    "page_021_plus_authorization",
    "new_or_broader_fixture_admission",
    "renderer_profile_acceptance",
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
    parser = argparse.ArgumentParser(description="Record Core 0.1 first-slice runtime authorization decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 first-slice runtime authorization decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 first-slice runtime authorization decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 first-slice runtime authorization decision requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01RSAP-G1-VIRAL-001.packet"][0])
    if packet["prep_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected runtime authorization prep input")
    if packet["status"] != "first_slice_runtime_authorization_prep_prepared_no_runtime_implementation":
        raise SystemExit("runtime authorization prep is not the expected no-runtime packet")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("runtime authorization prep unexpectedly authorizes runtime implementation")
    if packet["runtime_start_authorized"]:
        raise SystemExit("runtime authorization prep unexpectedly authorizes runtime start")
    if packet["runtime_source_profile_lock_created"] or packet["runtime_source_profile_acceptance_created"]:
        raise SystemExit("runtime authorization prep unexpectedly creates a runtime source-profile lock or acceptance")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if packet["remaining_blockers"][0] != "human_review_c01rsap_required":
        raise SystemExit("C01RSAP human review is not the current first blocker")
    if "first_slice_runtime_authorization_required" not in packet["remaining_blockers"]:
        raise SystemExit("first-slice runtime authorization blocker is not present")
    if packet["next_possible_packets"][1] != "core_0_1_first_slice_runtime_authorization_if_separately_authorized_after_human_review":
        raise SystemExit("first-slice runtime authorization decision is not a permitted next packet")
    return verified, packet


def build_decision(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    remaining_blockers = [
        blocker
        for blocker in packet["remaining_blockers"]
        if blocker
        not in {
            "human_review_c01rsap_required",
            "first_slice_runtime_authorization_required",
            "sol_terra_go_must_be_consumed_by_future_runtime_authorization",
        }
    ]
    for blocker in [
        "human_review_c01rsad_required",
        "runtime_implementation_authorization_required",
        "runtime_start_execution_requires_separate_authorization",
        "runtime_source_profile_lock_or_acceptance_requires_separate_authorization",
    ]:
        if blocker not in remaining_blockers:
            remaining_blockers.insert(0, blocker)
    decision_terms = {
        "authorization_state": "non_executing_first_slice_runtime_authorization_recorded",
        "authorization_scope": FIRST_SLICE_ID,
        "permits_runtime_implementation": False,
        "permits_runtime_start": False,
        "permits_ocr_or_render_execution": False,
        "permits_source_profile_lock_or_acceptance": False,
        "requires_future_runtime_implementation_authorization": True,
        "requires_future_runtime_start_execution_authorization": True,
    }
    return {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "first_slice_runtime_authorization_decision_recorded_no_runtime_implementation",
        "purpose": "bounded_first_slice_runtime_authorization_decision_for_c01wp_01_after_runtime_authorization_prep",
        "human_decision": HUMAN_DECISION,
        "human_review_consumed": "c01rsap_packet_ok",
        "source_first_slice_runtime_authorization_prep": packet["prep_id"],
        "source_runtime_source_profile_lock_or_parking_decision": packet["source_runtime_source_profile_lock_or_parking_decision"],
        "source_acceptance_matrix_trace_review": packet["source_acceptance_matrix_trace_review"],
        "source_architecture_review_packet": packet["source_architecture_review_packet"],
        "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
        "source_first_slice_design_prep_packet": packet["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "canonical_packet_name": "core_0_1_first_slice_runtime_authorization_decision",
        "first_slice_runtime_authorization_decision_recorded": True,
        "first_slice_runtime_authorization_granted": True,
        "runtime_authorization_created": True,
        "runtime_authorization_terms": decision_terms,
        "runtime_start_authorized": False,
        "runtime_execution_authorized": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "runtime_source_profile_decision_created": False,
        "runtime_source_profile_parking_consumed_as_reference_only": True,
        "runtime_source_profile_disposition": packet["runtime_source_profile_disposition"],
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_parking_recorded": False,
        "source_profile_lock_created": False,
        "source_profile_acceptance_created": False,
        "accepts_source_profile_beyond_c01splpr": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "remaining_blockers": remaining_blockers,
        "next_possible_packets": [
            "human_review_c01rsad_packet",
            "core_0_1_runtime_implementation_authorization_prep_if_separately_authorized_after_human_review",
            "runtime_start_execution_if_separately_authorized_after_implementation_layer",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    terms = decision["runtime_authorization_terms"]
    lines = [
        "# Core 0.1 First-Slice Runtime Authorization Decision - C01RSAD-G1-VIRAL-001",
        "",
        "Status: `first_slice_runtime_authorization_decision_recorded_no_runtime_implementation`",
        "",
        "This decision records a non-executing first-slice runtime authorization state for `C01WP-01-phase-1-scaffold-contracts` after runtime authorization prep.",
        "",
        "It does not authorize runtime implementation, runtime start, OCR, render, or source mutation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Runtime authorization prep: `{decision['source_first_slice_runtime_authorization_prep']}`.",
        f"- Runtime source-profile parking decision: `{decision['source_runtime_source_profile_lock_or_parking_decision']}`.",
        f"- Acceptance-matrix trace review: `{decision['source_acceptance_matrix_trace_review']}`.",
        f"- Architecture review packet: `{decision['source_architecture_review_packet']}`.",
        f"- Source-profile receipt: `{decision['source_profile_lock_or_parking_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{decision['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Runtime Authorization Decision",
        "",
        "- Canonical packet name: `core_0_1_first_slice_runtime_authorization_decision`.",
        "- Human review consumed: `c01rsap_packet_ok`.",
        "- First-slice runtime authorization decision recorded: `true`.",
        "- First-slice runtime authorization granted: `true`.",
        f"- Authorization state: `{terms['authorization_state']}`.",
        "- Runtime implementation authorized: `false`.",
        "- Runtime start authorized: `false`.",
        "- Runtime execution authorized: `false`.",
        "- Runtime source-profile lock/acceptance authorized: `false`.",
        "",
        "## Boundary",
        "",
        "- Runtime implementation: `false`.",
        "- Runtime start/execution: `false`.",
        "- Runtime source-profile lock: `false`.",
        "- Runtime source-profile acceptance: `false`.",
        "- Source-profile acceptance beyond `C01SPLPR`: `false`.",
        "- OCR/render/PDF/raw/source mutation: `false`.",
        "- Translation/proofreading: `false`.",
        "- Page 021+ processing/authorization: `false`.",
        "- New or broader fixture admission: `false`.",
        "- Push: `false`.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in decision["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_first_slice_runtime_authorization_decision_summary.md", "\n".join(lines))


def write_report(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_first_slice_runtime_authorization_decision_report.json",
        {
            "decision_id": DECISION_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": decision["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_first_slice_runtime_authorization_prep": decision["source_first_slice_runtime_authorization_prep"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "first_slice_runtime_authorization_decision_recorded": True,
            "first_slice_runtime_authorization_granted": True,
            "runtime_authorization_created": True,
            "runtime_start_authorized": False,
            "runtime_execution_authorized": False,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "runtime_source_profile_parking_consumed_as_reference_only": True,
            "source_profile_lock_created": False,
            "source_profile_acceptance_created": False,
            "accepts_source_profile_beyond_c01splpr": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": decision["negative_capability_matrix"],
            "remaining_blockers": decision["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_first_slice_runtime_authorization_decision_manifest.md"
    lines = [
        "# Core 0.1 First-Slice Runtime Authorization Decision Manifest - C01RSAD-G1-VIRAL-001",
        "",
        "Status: `first_slice_runtime_authorization_decision_recorded_no_runtime_implementation`",
        "",
        "Boundary: first-slice runtime authorization decision record only for C01WP-01; no runtime implementation, runtime start/execution, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, new fixture admission, push, or downstream action.",
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
    decision = build_decision(verified_inputs, packet)
    write_json(OUT_ROOT / "core_0_1_first_slice_runtime_authorization_decision.json", decision)
    write_summary(decision)
    write_report(decision)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
