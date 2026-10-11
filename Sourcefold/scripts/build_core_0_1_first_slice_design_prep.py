from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_first_slice_design_prep.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_first_slice_design_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
RECEIPT_ROOT = TRIAL_ROOT / "core_0_1_implementation_authorization_receipt_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_first_slice_design_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-DESIGN-PREP-001"
PACKET_ID = "C01FSDP-G1-VIRAL-001"
SOURCE_RECEIPT_ID = "C01IAR-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01iar receipt ok; proceed to prepare Core 0.1 first-slice design prep for "
    "C01WP-01-phase-1-scaffold-contracts; no runtime implementation, no source-profile lock or acceptance "
    "beyond G1WGADR, no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01IAR-G1-VIRAL-001.receipt": (
        RECEIPT_ROOT / "core_0_1_implementation_authorization_receipt.json",
        "0A20E7555B572FA47DF03073953155ECA9A7E1BC87E9CB2EEE2A373DBD9405A7",
    ),
    "C01IAR-G1-VIRAL-001.report": (
        RECEIPT_ROOT / "core_0_1_implementation_authorization_receipt_report.json",
        "5FA8A73975ACC9E83ACFE92591BCA66E058E69D88667C491D19A0D7B2185B6E8",
    ),
    "C01IAR-G1-VIRAL-001.summary": (
        RECEIPT_ROOT / "core_0_1_implementation_authorization_receipt_summary.md",
        "6B62325A152BBFACC3372A5807E55C67F7E80AEBEF51AB96C5295F30B6AD0B98",
    ),
    "C01IAR-G1-VIRAL-001.manifest": (
        RECEIPT_ROOT / "core_0_1_implementation_authorization_receipt_manifest.md",
        "0F778173065003818C77293A15615E021F72BD1A57E45EE18A05A02F028FD64F",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
    "source_profile_lock",
    "source_profile_acceptance_beyond_g1wgadr",
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

DESIGN_CONTRACTS = [
    {
        "contract_id": "C01SC-01-module-boundary-inventory",
        "title": "Module boundary inventory",
        "design_prep_status": "prepared_for_future_review",
        "runtime_files_authorized": False,
        "design_questions": [
            "Which Phase 1 scaffold modules are allowed before source-profile lock?",
            "Which modules must remain placeholders until source-profile lock/parking?",
            "Which package boundaries must be represented before any runtime code?",
        ],
    },
    {
        "contract_id": "C01SC-02-artifact-identity-contract",
        "title": "Artifact identity contract",
        "design_prep_status": "prepared_for_future_review",
        "runtime_files_authorized": False,
        "design_questions": [
            "Which artifact ids are allowed for scaffold-only contracts?",
            "Which identity fields must bind to Gate 1 accepted pages and G1FADAR fixtures?",
            "Which fields remain invalid until runtime implementation authorization?",
        ],
    },
    {
        "contract_id": "C01SC-03-lineage-trace-contract",
        "title": "Lineage trace contract",
        "design_prep_status": "prepared_for_future_review",
        "runtime_files_authorized": False,
        "design_questions": [
            "How should C01WP-01 trace back to G1WGADR, C01IPP, and C01IAR?",
            "Which mutation-free lineage checks are required before first-slice runtime start?",
            "Which negative fixture groups must remain linked as failure inputs?",
        ],
    },
    {
        "contract_id": "C01SC-04-acceptance-matrix-trace-contract",
        "title": "Acceptance matrix trace contract",
        "design_prep_status": "prepared_for_future_review",
        "runtime_files_authorized": False,
        "design_questions": [
            "Which Core 0.1 acceptance matrix rows are touched by scaffold-only design?",
            "Which rows need evidence before runtime implementation?",
            "Which rows are blocked by source-profile lock/parking?",
        ],
    },
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 first-slice design prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 first-slice design prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 first-slice design prep requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 first-slice design prep requires the exact bounded human decision")


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

    receipt = read_json(INPUT_HASHES["C01IAR-G1-VIRAL-001.receipt"][0])
    if receipt["receipt_id"] != SOURCE_RECEIPT_ID:
        raise SystemExit("unexpected Core 0.1 authorization receipt input")
    if receipt["status"] != "core_0_1_implementation_authorization_receipt_prepared_no_runtime_implementation":
        raise SystemExit("Core 0.1 authorization receipt is not prepared")
    if receipt["runtime_implementation_authorized"]:
        raise SystemExit("runtime implementation is already authorized")
    if receipt["first_slice_design_prep_authorized"]:
        raise SystemExit("first-slice design prep is already authorized")
    if receipt["recommended_first_slice"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if receipt["next_possible_packets"][0] != "core_0_1_first_slice_design_prep_if_separately_authorized":
        raise SystemExit("first-slice design prep is not the next packet")
    return verified, receipt


def build_packet(verified_inputs: dict[str, dict[str, str]], receipt: dict) -> dict:
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "core_0_1_first_slice_design_prep_ready_for_review",
        "purpose": "bounded_core_0_1_first_slice_design_prep_only_no_runtime_implementation",
        "human_decision": HUMAN_DECISION,
        "source_implementation_authorization_receipt": receipt["receipt_id"],
        "source_planning_prep_packet": receipt["source_planning_prep_packet"],
        "source_whole_gate_1_acceptance_decision": receipt["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": receipt["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "first_slice_design_prep_created": True,
        "first_slice_design_prep_authorizes_runtime": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "source_profile_lock_created": False,
        "accepts_source_profile_beyond_g1wgadr": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "design_contracts": DESIGN_CONTRACTS,
        "future_review_targets": [
            "sol_architecture_review_for_c01wp_01",
            "terra_critique_for_c01wp_01",
            "acceptance_matrix_trace_review_for_c01wp_01",
            "source_profile_lock_or_parking_receipt_for_c01wp_01",
        ],
        "required_before_first_slice_runtime_start": [
            "separate_human_authorization_for_runtime_start",
            "single_core_0_1_source_profile_lock_or_explicit_parking",
            "acceptance_matrix_claim_to_evidence_mapping_for_c01wp_01",
            "sol_architecture_review_for_c01wp_01",
            "terra_critique_for_c01wp_01",
            "roadmap_validation_for_c01wp_01",
        ],
        "remaining_blockers": [
            "runtime_implementation_requires_future_first_slice_authorization",
            "source_profile_lock_or_parking_receipt_required_for_c01wp_01",
            "acceptance_matrix_claim_to_evidence_mapping_required_for_c01wp_01",
            "sol_architecture_review_required_for_c01wp_01",
            "terra_critique_required_for_c01wp_01",
            "roadmap_validation_required_for_c01wp_01",
            "ocr_render_pdf_raw_mutation_requires_separate_authorization",
            "translation_proofreading_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "single_source_profile_lock_or_parking_receipt_if_separately_authorized",
            "core_0_1_first_slice_architecture_review_packet_if_separately_authorized",
            "core_0_1_first_slice_runtime_authorization_if_separately_authorized_after_prerequisites",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    lines = [
        "# Core 0.1 First-Slice Design Prep - C01FSDP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_first_slice_design_prep_ready_for_review`",
        "",
        "This packet prepares the design surface for `C01WP-01-phase-1-scaffold-contracts` after `C01IAR-G1-VIRAL-001`.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Implementation authorization receipt: `{packet['source_implementation_authorization_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{packet['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "- Source-profile lock created: `false`.",
        "- Source-profile acceptance beyond G1WGADR: `false`.",
        "",
        "## Design Contracts",
        "",
    ]
    for row in packet["design_contracts"]:
        lines.append(f"- `{row['contract_id']}`: {row['title']} (`{row['design_prep_status']}`); runtime files authorized: `false`.")
    lines.extend(
        [
            "",
            "## Future Review Targets",
            "",
        ]
    )
    for target in packet["future_review_targets"]:
        lines.append(f"- `{target}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Runtime implementation: `false`.",
            "- First-slice runtime start: `false`.",
            "- Source-profile lock/acceptance: `false`.",
            "- OCR/render/PDF/raw/source mutation: `false`.",
            "- Translation/proofreading: `false`.",
            "- Page 021+ processing/authorization: `false`.",
            "- Push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in packet["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_first_slice_design_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_first_slice_design_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(scope["positive_fixture_groups"]),
            "negative_fixture_group_count": len(scope["negative_fixture_groups"]),
            "design_contract_count": len(packet["design_contracts"]),
            "future_review_target_count": len(packet["future_review_targets"]),
            "first_slice_design_prep_created": True,
            "first_slice_design_prep_authorizes_runtime": False,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
            "source_profile_lock_created": False,
            "accepts_source_profile_beyond_g1wgadr": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_first_slice_design_prep_manifest.md"
    lines = [
        "# Core 0.1 First-Slice Design Prep Manifest - C01FSDP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_first_slice_design_prep_ready_for_review`",
        "",
        "Boundary: design prep only for C01WP-01; no runtime implementation, source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, push, or downstream action.",
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
    verified_inputs, receipt = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, receipt)
    write_json(OUT_ROOT / "core_0_1_first_slice_design_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
