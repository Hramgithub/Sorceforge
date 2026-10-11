from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_runtime_source_profile_lock_or_acceptance_decision.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_runtime_source_profile_lock_or_acceptance_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SOURCE_ROOT = TRIAL_ROOT / "core_0_1_first_slice_runtime_authorization_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-DECISION-001"
DECISION_ID = "C01RSPLAD-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01RSAD-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01rsad packet ok; proceed to prepare Core 0.1 runtime source-profile lock-or-acceptance decision for C01WP-01 "
    "from C01RSAD; no runtime implementation, no runtime start/execution, no OCR/render/PDF/raw mutation, "
    "no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01RSAD-G1-VIRAL-001.packet": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_decision.json",
        "6C5C1481D1E77693E49F2A3670B0E4D0870292CA2C42C075F297379C975F514C",
    ),
    "C01RSAD-G1-VIRAL-001.report": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_decision_report.json",
        "490EB27DAD6026951825859779999B5D06B4A1D56F306EB6727E6E9F8FEC1EAC",
    ),
    "C01RSAD-G1-VIRAL-001.summary": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_decision_summary.md",
        "03F19C1FF29E60425899982070E427E4497055BEA8016044C950982F8F4275AE",
    ),
    "C01RSAD-G1-VIRAL-001.manifest": (
        SOURCE_ROOT / "core_0_1_first_slice_runtime_authorization_decision_manifest.md",
        "E9D6DA05E6509919008F67C9356DEC397E1F8A56F4A54B44047EBF0266DD0762",
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
    parser = argparse.ArgumentParser(description="Record Core 0.1 runtime source-profile lock-or-acceptance decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 runtime source-profile lock-or-acceptance decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 runtime source-profile lock-or-acceptance decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 runtime source-profile lock-or-acceptance decision requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01RSAD-G1-VIRAL-001.packet"][0])
    if packet["decision_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected first-slice runtime authorization decision input")
    if packet["status"] != "first_slice_runtime_authorization_decision_recorded_no_runtime_implementation":
        raise SystemExit("runtime authorization decision is not the expected no-runtime packet")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("runtime authorization decision unexpectedly authorizes runtime implementation")
    if packet["runtime_start_authorized"] or packet["runtime_execution_authorized"]:
        raise SystemExit("runtime authorization decision unexpectedly authorizes runtime start/execution")
    if packet["runtime_source_profile_lock_created"] or packet["runtime_source_profile_acceptance_created"]:
        raise SystemExit("runtime authorization decision unexpectedly creates a runtime source-profile lock or acceptance")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if "human_review_c01rsad_required" not in packet["remaining_blockers"]:
        raise SystemExit("C01RSAD human review blocker is not present")
    if "runtime_source_profile_lock_or_acceptance_requires_separate_authorization" not in packet["remaining_blockers"]:
        raise SystemExit("runtime source-profile lock-or-acceptance blocker is not present")
    return verified, packet


def build_decision(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    remaining_blockers = [
        blocker
        for blocker in packet["remaining_blockers"]
        if blocker
        not in {
            "human_review_c01rsad_required",
            "runtime_source_profile_lock_or_acceptance_requires_separate_authorization",
        }
    ]
    for blocker in [
        "human_review_c01rsplad_required",
        "runtime_source_profile_lock_or_acceptance_not_granted_blocks_implementation",
    ]:
        if blocker not in remaining_blockers:
            remaining_blockers.insert(0, blocker)
    profile_decision = {
        "decision": "no_runtime_source_profile_lock_or_acceptance",
        "reason": "no_concrete_runtime_source_profile_evidence_admitted_for_lock_or_acceptance",
        "runtime_source_profile_lock_granted": False,
        "runtime_source_profile_acceptance_granted": False,
        "runtime_source_profile_remains_parked": True,
        "blocks_runtime_implementation": True,
        "requires_future_profile_evidence_or_authorization": True,
    }
    return {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "runtime_source_profile_lock_or_acceptance_decision_recorded_no_runtime_profile_lock_or_acceptance",
        "purpose": "bounded_runtime_source_profile_lock_or_acceptance_decision_for_c01wp_01_after_non_executing_runtime_authorization",
        "human_decision": HUMAN_DECISION,
        "human_review_consumed": "c01rsad_packet_ok",
        "source_first_slice_runtime_authorization_decision": packet["decision_id"],
        "source_first_slice_runtime_authorization_prep": packet["source_first_slice_runtime_authorization_prep"],
        "source_runtime_source_profile_lock_or_parking_decision": packet["source_runtime_source_profile_lock_or_parking_decision"],
        "source_acceptance_matrix_trace_review": packet["source_acceptance_matrix_trace_review"],
        "source_architecture_review_packet": packet["source_architecture_review_packet"],
        "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
        "source_first_slice_design_prep_packet": packet["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "canonical_packet_name": "core_0_1_runtime_source_profile_lock_or_acceptance_decision",
        "runtime_source_profile_lock_or_acceptance_decision_recorded": True,
        "runtime_source_profile_decision_outcome": profile_decision,
        "runtime_source_profile_lock_granted": False,
        "runtime_source_profile_acceptance_granted": False,
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_remains_parked": True,
        "runtime_start_authorized": False,
        "runtime_execution_authorized": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
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
            "human_review_c01rsplad_packet",
            "runtime_source_profile_evidence_prep_if_separately_authorized",
            "runtime_implementation_authorization_prep_only_after_profile_lock_or_acceptance_if_separately_authorized",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    outcome = decision["runtime_source_profile_decision_outcome"]
    lines = [
        "# Core 0.1 Runtime Source-Profile Lock-or-Acceptance Decision - C01RSPLAD-G1-VIRAL-001",
        "",
        "Status: `runtime_source_profile_lock_or_acceptance_decision_recorded_no_runtime_profile_lock_or_acceptance`",
        "",
        "This decision records that no runtime source-profile lock or acceptance is granted for `C01WP-01-phase-1-scaffold-contracts` after non-executing runtime authorization.",
        "",
        "It does not authorize runtime implementation, runtime start, OCR, render, or source mutation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- First-slice runtime authorization decision: `{decision['source_first_slice_runtime_authorization_decision']}`.",
        f"- Runtime authorization prep: `{decision['source_first_slice_runtime_authorization_prep']}`.",
        f"- Runtime source-profile parking decision: `{decision['source_runtime_source_profile_lock_or_parking_decision']}`.",
        f"- Acceptance-matrix trace review: `{decision['source_acceptance_matrix_trace_review']}`.",
        f"- Architecture review packet: `{decision['source_architecture_review_packet']}`.",
        f"- Source-profile receipt: `{decision['source_profile_lock_or_parking_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{decision['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Runtime Source-Profile Decision",
        "",
        "- Canonical packet name: `core_0_1_runtime_source_profile_lock_or_acceptance_decision`.",
        "- Human review consumed: `c01rsad_packet_ok`.",
        "- Runtime source-profile lock-or-acceptance decision recorded: `true`.",
        f"- Decision: `{outcome['decision']}`.",
        f"- Reason: `{outcome['reason']}`.",
        "- Runtime source-profile lock granted: `false`.",
        "- Runtime source-profile acceptance granted: `false`.",
        "- Runtime source-profile remains parked: `true`.",
        "- Runtime implementation remains blocked by profile decision: `true`.",
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
    write_text(OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_summary.md", "\n".join(lines))


def write_report(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_report.json",
        {
            "decision_id": DECISION_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": decision["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_first_slice_runtime_authorization_decision": decision["source_first_slice_runtime_authorization_decision"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "runtime_source_profile_lock_or_acceptance_decision_recorded": True,
            "runtime_source_profile_lock_granted": False,
            "runtime_source_profile_acceptance_granted": False,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "runtime_source_profile_remains_parked": True,
            "runtime_start_authorized": False,
            "runtime_execution_authorized": False,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
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
    manifest_name = "core_0_1_runtime_source_profile_lock_or_acceptance_decision_manifest.md"
    lines = [
        "# Core 0.1 Runtime Source-Profile Lock-or-Acceptance Decision Manifest - C01RSPLAD-G1-VIRAL-001",
        "",
        "Status: `runtime_source_profile_lock_or_acceptance_decision_recorded_no_runtime_profile_lock_or_acceptance`",
        "",
        "Boundary: runtime source-profile lock-or-acceptance decision record only for C01WP-01; no runtime source-profile lock/acceptance is granted, and no runtime implementation, runtime start/execution, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, new fixture admission, push, or downstream action is created.",
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
    write_json(OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision.json", decision)
    write_summary(decision)
    write_report(decision)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
