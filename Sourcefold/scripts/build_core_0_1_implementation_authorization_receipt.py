from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_implementation_authorization_receipt.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_implementation_authorization_receipt.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PLANNING_ROOT = TRIAL_ROOT / "core_0_1_implementation_planning_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_implementation_authorization_receipt_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-AUTHORIZATION-RECEIPT-001"
RECEIPT_ID = "C01IAR-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01IPP-G1-VIRAL-001"
HUMAN_DECISION = (
    "c01ipp packet ok; proceed to prepare Core 0.1 implementation authorization receipt from C01IPP; "
    "no runtime implementation, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, "
    "no source-profile acceptance beyond G1WGADR, no push, commit"
)

INPUT_HASHES = {
    "C01IPP-G1-VIRAL-001.packet": (
        PLANNING_ROOT / "core_0_1_implementation_planning_prep.json",
        "D2DD97D83920B76F22B93B443EF5DC1FE3742C3FA167AF721B1ECD670498273A",
    ),
    "C01IPP-G1-VIRAL-001.report": (
        PLANNING_ROOT / "core_0_1_implementation_planning_prep_report.json",
        "437CD9369ABDFF1589C695387B5EE379D43DECA7830F7C427716F871FC56F85C",
    ),
    "C01IPP-G1-VIRAL-001.summary": (
        PLANNING_ROOT / "core_0_1_implementation_planning_prep_summary.md",
        "8DE4707466B0DC254DC4C0DCEED59EB8D5A592E5AE01F5B434E7FD220F438291",
    ),
    "C01IPP-G1-VIRAL-001.manifest": (
        PLANNING_ROOT / "core_0_1_implementation_planning_prep_manifest.md",
        "2B008C786F1C532923DFFC8031BE3DE194D874AEF770CEED802E3376570855D8",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
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
    "source_profile_acceptance_beyond_g1wgadr",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 implementation authorization receipt.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 implementation authorization receipt is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 implementation authorization receipt requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 implementation authorization receipt requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01IPP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected Core 0.1 planning prep input")
    if packet["status"] != "core_0_1_implementation_planning_prep_ready_for_review":
        raise SystemExit("Core 0.1 planning prep is not ready for review")
    if packet["creates_implementation_authorization_receipt"]:
        raise SystemExit("planning prep already creates an implementation authorization receipt")
    if packet["creates_implementation"]:
        raise SystemExit("planning prep already creates implementation")
    if packet["processes_page_021_plus"]:
        raise SystemExit("planning prep includes page 021+")
    if packet["accepts_source_profile_beyond_g1wgadr"]:
        raise SystemExit("planning prep accepts source profile beyond G1WGADR")
    if packet["next_possible_packets"][0] != "core_0_1_implementation_authorization_receipt_if_separately_authorized":
        raise SystemExit("implementation authorization receipt is not the next packet")
    return verified, packet


def prerequisite_rows(packet: dict) -> list[dict[str, object]]:
    return [
        {
            "prerequisite_id": "accepted_gate_1_scope",
            "source": packet["source_whole_gate_1_acceptance_decision"],
            "state": "satisfied_for_pages_001_020_and_g1fadar_fixtures",
            "blocks_runtime_implementation": False,
        },
        {
            "prerequisite_id": "implementation_authorization_receipt",
            "source": RECEIPT_ID,
            "state": "prepared_by_this_receipt",
            "blocks_runtime_implementation": True,
            "reason": "This receipt is documentation/evidence only and does not authorize runtime start.",
        },
        {
            "prerequisite_id": "single_core_0_1_source_profile_lock_or_explicit_parking",
            "source": "release_charter_implementation_authorization_receipt",
            "state": "not_satisfied_in_this_packet",
            "blocks_runtime_implementation": True,
        },
        {
            "prerequisite_id": "acceptance_matrix_claim_to_evidence_mapping_for_first_slice",
            "source": "core_0_1_acceptance_matrix",
            "state": "not_satisfied_in_this_packet",
            "blocks_runtime_implementation": True,
        },
        {
            "prerequisite_id": "sol_architecture_review_for_first_slice",
            "source": "future_first_slice_review",
            "state": "not_satisfied_in_this_packet",
            "blocks_runtime_implementation": True,
        },
        {
            "prerequisite_id": "terra_critique_for_first_slice",
            "source": "future_first_slice_review",
            "state": "not_satisfied_in_this_packet",
            "blocks_runtime_implementation": True,
        },
        {
            "prerequisite_id": "roadmap_validation_for_first_slice",
            "source": "future_first_slice_review",
            "state": "not_satisfied_in_this_packet",
            "blocks_runtime_implementation": True,
        },
    ]


def build_receipt(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    rows = prerequisite_rows(packet)
    return {
        "receipt_id": RECEIPT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "core_0_1_implementation_authorization_receipt_prepared_no_runtime_implementation",
        "purpose": "bounded_core_0_1_implementation_authorization_receipt_material_only",
        "human_decision": HUMAN_DECISION,
        "source_planning_prep_packet": packet["packet_id"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "creates_implementation_authorization_receipt": True,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "first_slice_design_prep_authorized": False,
        "first_slice_runtime_start_authorized": False,
        "recommended_first_slice": packet["implementation_planning"]["recommended_first_slice"],
        "receipt_prerequisites": rows,
        "blocking_prerequisite_ids": [
            row["prerequisite_id"] for row in rows if row["blocks_runtime_implementation"]
        ],
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "accepts_source_profile_beyond_g1wgadr": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "remaining_blockers": [
            "runtime_implementation_requires_future_first_slice_authorization",
            "single_core_0_1_source_profile_lock_or_explicit_parking_required",
            "acceptance_matrix_claim_to_evidence_mapping_required_for_first_slice",
            "sol_architecture_review_required_for_first_slice",
            "terra_critique_required_for_first_slice",
            "roadmap_validation_required_for_first_slice",
            "ocr_render_pdf_raw_mutation_requires_separate_authorization",
            "translation_proofreading_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "source_profile_acceptance_beyond_g1wgadr_requires_separate_authorization",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "core_0_1_first_slice_design_prep_if_separately_authorized",
            "single_source_profile_lock_or_parking_receipt_if_separately_authorized",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(receipt: dict) -> None:
    scope = receipt["accepted_gate_1_scope"]
    lines = [
        "# Core 0.1 Implementation Authorization Receipt - C01IAR-G1-VIRAL-001",
        "",
        "Status: `core_0_1_implementation_authorization_receipt_prepared_no_runtime_implementation`",
        "",
        "This receipt records acceptance of `C01IPP-G1-VIRAL-001` as Core 0.1 implementation planning prep material.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Whole Gate 1 acceptance decision: `{receipt['source_whole_gate_1_acceptance_decision']}`.",
        f"- Planning prep packet: `{receipt['source_planning_prep_packet']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "- Page 021+ included: `false`.",
        "- Source-profile acceptance beyond G1WGADR: `false`.",
        "",
        "## Receipt Result",
        "",
        "- Implementation authorization receipt created: `true`.",
        "- Runtime implementation authorized: `false`.",
        f"- Recommended future first slice: `{receipt['recommended_first_slice']}`.",
        "- First-slice design prep authorized: `false`.",
        "- First-slice runtime start authorized: `false`.",
        "",
        "## Prerequisites",
        "",
    ]
    for row in receipt["receipt_prerequisites"]:
        lines.append(
            f"- `{row['prerequisite_id']}`: `{row['state']}`; blocks runtime: `{str(row['blocks_runtime_implementation']).lower()}`."
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Runtime implementation: `false`.",
            "- OCR/render/PDF/raw/source mutation: `false`.",
            "- Translation/proofreading: `false`.",
            "- Page 021+ processing/authorization: `false`.",
            "- Source-profile acceptance beyond G1WGADR: `false`.",
            "- New or broader fixture admission: `false`.",
            "- Push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in receipt["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_implementation_authorization_receipt_summary.md", "\n".join(lines))


def write_report(receipt: dict) -> None:
    scope = receipt["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_implementation_authorization_receipt_report.json",
        {
            "receipt_id": RECEIPT_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": receipt["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_planning_prep_packet": receipt["source_planning_prep_packet"],
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(scope["positive_fixture_groups"]),
            "negative_fixture_group_count": len(scope["negative_fixture_groups"]),
            "blocking_prerequisite_count": len(receipt["blocking_prerequisite_ids"]),
            "creates_implementation_authorization_receipt": True,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
            "first_slice_design_prep_authorized": False,
            "first_slice_runtime_start_authorized": False,
            "recommended_first_slice": receipt["recommended_first_slice"],
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "accepts_source_profile_beyond_g1wgadr": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": receipt["negative_capability_matrix"],
            "remaining_blockers": receipt["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_implementation_authorization_receipt_manifest.md"
    lines = [
        "# Core 0.1 Implementation Authorization Receipt Manifest - C01IAR-G1-VIRAL-001",
        "",
        "Status: `core_0_1_implementation_authorization_receipt_prepared_no_runtime_implementation`",
        "",
        "Boundary: receipt material only from C01IPP; no runtime implementation, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, source-profile broadening, new fixture admission, push, or downstream action.",
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
    receipt = build_receipt(verified_inputs, packet)
    write_json(OUT_ROOT / "core_0_1_implementation_authorization_receipt.json", receipt)
    write_summary(receipt)
    write_report(receipt)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
