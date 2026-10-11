from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_runtime_source_profile_lock_or_parking_decision.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_runtime_source_profile_lock_or_parking_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
TRACE_ROOT = TRIAL_ROOT / "core_0_1_acceptance_matrix_trace_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-PARKING-DECISION-001"
DECISION_ID = "C01RSPLP-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01AMTR-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01amtr packet ok; proceed to prepare runtime source-profile lock-or-parking decision for C01WP-01 "
    "from C01AMTR; no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, "
    "no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01AMTR-G1-VIRAL-001.packet": (
        TRACE_ROOT / "core_0_1_acceptance_matrix_trace_review.json",
        "C694B0C93E2F3EBF49BC71AEC97AA06F8A8877A980E2067434FAC09430286480",
    ),
    "C01AMTR-G1-VIRAL-001.report": (
        TRACE_ROOT / "core_0_1_acceptance_matrix_trace_review_report.json",
        "B75EB03BB48BBDA4946876A961AA0C4BA0524F7A92A7BCFA0C1CCEE3DD23ED3B",
    ),
    "C01AMTR-G1-VIRAL-001.summary": (
        TRACE_ROOT / "core_0_1_acceptance_matrix_trace_review_summary.md",
        "8122BF577E1CB37C556F3E3D66BCFA5DC4CC994BD6092C64A0B7C6C51B39366F",
    ),
    "C01AMTR-G1-VIRAL-001.manifest": (
        TRACE_ROOT / "core_0_1_acceptance_matrix_trace_review_manifest.md",
        "E2503080F3CF43F7752B1CEBC708A98F0940221242E789127AFF26933A963A86",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 runtime source-profile lock-or-parking decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 runtime source-profile decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 runtime source-profile decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 runtime source-profile decision requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01AMTR-G1-VIRAL-001.packet"][0])
    if packet["review_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected acceptance-matrix trace review input")
    if packet["status"] != "acceptance_matrix_trace_review_prepared_no_runtime_implementation":
        raise SystemExit("acceptance-matrix trace review is not the expected no-runtime packet")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("acceptance-matrix trace review unexpectedly authorizes runtime implementation")
    if packet["source_profile_lock_created"] or packet["source_profile_acceptance_created"]:
        raise SystemExit("acceptance-matrix trace review unexpectedly creates a source-profile lock or acceptance")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if "runtime_source_profile_lock_or_runtime_parking_decision_required" not in packet["remaining_blockers"]:
        raise SystemExit("runtime source-profile decision blocker is not present")
    if "runtime_source_profile_lock_or_runtime_parking_decision_if_separately_authorized" not in packet["next_possible_packets"]:
        raise SystemExit("runtime source-profile decision is not a permitted next packet")
    return verified, packet


def build_decision(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    disposition = {
        "target_slice": FIRST_SLICE_ID,
        "runtime_profile_disposition": "park_runtime_source_profile_lock_until_first_runtime_authorization",
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_parking_recorded": True,
        "parking_scope": "C01WP-01_runtime_authorization_prep_only_no_runtime_start",
        "runtime_implication": "first_slice_runtime_authorization_prep_may_reference_parking_but_runtime_start_remains_blocked",
        "reason": (
            "C01AMTR prepared the claim/evidence trace, but no runtime OCR/render/source profile "
            "has been selected or accepted. The runtime profile remains parked so the next packet "
            "can prepare authorization prerequisites without starting implementation."
        ),
    }
    remaining_blockers = [
        blocker
        for blocker in packet["remaining_blockers"]
        if blocker not in {"human_review_c01amtr_required", "runtime_source_profile_lock_or_runtime_parking_decision_required"}
    ]
    remaining_blockers.insert(0, "human_review_c01rsplp_required")
    if "first_slice_runtime_authorization_required" not in remaining_blockers:
        remaining_blockers.append("first_slice_runtime_authorization_required")
    return {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "runtime_source_profile_lock_or_parking_decision_prepared_no_runtime_implementation",
        "purpose": "bounded_runtime_source_profile_parking_decision_for_c01wp_01_before_runtime_authorization",
        "human_decision": HUMAN_DECISION,
        "source_acceptance_matrix_trace_review": packet["review_id"],
        "source_architecture_review_packet": packet["source_architecture_review_packet"],
        "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
        "source_first_slice_design_prep_packet": packet["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "runtime_source_profile_decision_created": True,
        "runtime_source_profile_disposition": disposition,
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_parking_recorded": True,
        "source_profile_lock_created": False,
        "source_profile_acceptance_created": False,
        "accepts_source_profile_beyond_c01splpr": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "remaining_blockers": remaining_blockers,
        "next_possible_packets": [
            "human_review_c01rsplp_packet",
            "core_0_1_first_slice_runtime_authorization_prep_if_separately_authorized",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    disposition = decision["runtime_source_profile_disposition"]
    lines = [
        "# Core 0.1 Runtime Source-Profile Lock-or-Parking Decision - C01RSPLP-G1-VIRAL-001",
        "",
        "Status: `runtime_source_profile_lock_or_parking_decision_prepared_no_runtime_implementation`",
        "",
        "This decision records the runtime source-profile disposition for `C01WP-01-phase-1-scaffold-contracts` after acceptance-matrix trace review.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Acceptance-matrix trace review: `{decision['source_acceptance_matrix_trace_review']}`.",
        f"- Architecture review packet: `{decision['source_architecture_review_packet']}`.",
        f"- Source-profile receipt: `{decision['source_profile_lock_or_parking_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{decision['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Runtime Source-Profile Disposition",
        "",
        f"- Disposition: `{disposition['runtime_profile_disposition']}`.",
        "- Runtime source-profile lock created: `false`.",
        "- Runtime source-profile acceptance created: `false`.",
        "- Runtime source-profile parking recorded: `true`.",
        f"- Parking scope: `{disposition['parking_scope']}`.",
        f"- Runtime implication: `{disposition['runtime_implication']}`.",
        "",
        "## Boundary",
        "",
        "- Runtime implementation: `false`.",
        "- Runtime source-profile lock: `false`.",
        "- Runtime source-profile acceptance: `false`.",
        "- Source-profile acceptance beyond `C01SPLPR`: `false`.",
        "- OCR/render/PDF/raw/source mutation: `false`.",
        "- Translation/proofreading: `false`.",
        "- Page 021+ processing/authorization: `false`.",
        "- Push: `false`.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in decision["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_summary.md", "\n".join(lines))


def write_report(decision: dict) -> None:
    scope = decision["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_report.json",
        {
            "decision_id": DECISION_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": decision["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_acceptance_matrix_trace_review": decision["source_acceptance_matrix_trace_review"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "runtime_source_profile_decision_created": True,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "runtime_source_profile_parking_recorded": True,
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
    manifest_name = "core_0_1_runtime_source_profile_lock_or_parking_decision_manifest.md"
    lines = [
        "# Core 0.1 Runtime Source-Profile Lock-or-Parking Decision Manifest - C01RSPLP-G1-VIRAL-001",
        "",
        "Status: `runtime_source_profile_lock_or_parking_decision_prepared_no_runtime_implementation`",
        "",
        "Boundary: runtime source-profile parking decision only for C01WP-01; no runtime implementation, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, push, or downstream action.",
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
    write_json(OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision.json", decision)
    write_summary(decision)
    write_report(decision)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
