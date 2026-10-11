from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_source_profile_lock_or_parking_receipt.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_source_profile_lock_or_parking_receipt.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
DESIGN_ROOT = TRIAL_ROOT / "core_0_1_first_slice_design_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-SINGLE-SOURCE-PROFILE-LOCK-OR-PARKING-RECEIPT-001"
RECEIPT_ID = "C01SPLPR-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01FSDP-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01fsdp packet ok; proceed to prepare single source-profile lock-or-parking receipt for C01WP-01 "
    "from C01FSDP; no runtime implementation, no source-profile lock or acceptance beyond this receipt, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01FSDP-G1-VIRAL-001.packet": (
        DESIGN_ROOT / "core_0_1_first_slice_design_prep.json",
        "0A0FC7208959117FC79B288486E206270B8BE0AD66AF7525B465512EF9CDFD81",
    ),
    "C01FSDP-G1-VIRAL-001.report": (
        DESIGN_ROOT / "core_0_1_first_slice_design_prep_report.json",
        "1ECE894197218EDC028CFC89E8979446D84F99B6181835C41C547DA40DB8A4C2",
    ),
    "C01FSDP-G1-VIRAL-001.summary": (
        DESIGN_ROOT / "core_0_1_first_slice_design_prep_summary.md",
        "B04F3FE67ACD517069DB035B779AF304620BC6A573AFAED7DCFEAA1C470D5060",
    ),
    "C01FSDP-G1-VIRAL-001.manifest": (
        DESIGN_ROOT / "core_0_1_first_slice_design_prep_manifest.md",
        "101764F9CAF02C18F88AE982568143A1F07D1BADEC30EBA8B130DE3FC88C1D4B",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
    "source_profile_lock",
    "source_profile_acceptance_beyond_receipt",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 source-profile lock-or-parking receipt.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 source-profile lock-or-parking receipt is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 source-profile lock-or-parking receipt requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 source-profile lock-or-parking receipt requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01FSDP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected first-slice design prep input")
    if packet["status"] != "core_0_1_first_slice_design_prep_ready_for_review":
        raise SystemExit("first-slice design prep is not ready for review")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("design prep already authorizes runtime implementation")
    if packet["source_profile_lock_created"]:
        raise SystemExit("design prep already creates a source-profile lock")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if packet["next_possible_packets"][0] != "single_source_profile_lock_or_parking_receipt_if_separately_authorized":
        raise SystemExit("source-profile lock-or-parking receipt is not the next packet")
    return verified, packet


def build_receipt(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    disposition = {
        "target_slice": FIRST_SLICE_ID,
        "profile_receipt_disposition": "park_source_profile_lock_for_design_prep_only",
        "source_profile_lock_created": False,
        "source_profile_acceptance_created": False,
        "source_profile_parking_recorded": True,
        "parking_scope": "C01WP-01_design_prep_only_no_runtime_start",
        "runtime_implication": "runtime_implementation_still_requires_separate_profile_lock_or_runtime_parking_decision",
        "reason": (
            "C01FSDP design prep can proceed without selecting a runtime OCR/render/source profile, "
            "but any first-slice runtime start still needs a separate profile lock or explicit runtime parking."
        ),
    }
    return {
        "receipt_id": RECEIPT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "single_source_profile_lock_or_parking_receipt_prepared_no_runtime_implementation",
        "purpose": "bounded_source_profile_lock_or_parking_receipt_for_c01wp_01_design_prep",
        "human_decision": HUMAN_DECISION,
        "source_first_slice_design_prep_packet": packet["packet_id"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "source_profile_receipt_created": True,
        "source_profile_disposition": disposition,
        "source_profile_lock_created": False,
        "source_profile_acceptance_created": False,
        "source_profile_parking_recorded": True,
        "accepts_source_profile_beyond_this_receipt": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "remaining_blockers": [
            "runtime_implementation_requires_future_first_slice_authorization",
            "runtime_source_profile_lock_or_runtime_parking_decision_required",
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
            "core_0_1_first_slice_architecture_review_packet_if_separately_authorized",
            "acceptance_matrix_trace_review_for_c01wp_01_if_separately_authorized",
            "core_0_1_first_slice_runtime_authorization_if_separately_authorized_after_prerequisites",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(receipt: dict) -> None:
    scope = receipt["accepted_gate_1_scope"]
    disposition = receipt["source_profile_disposition"]
    lines = [
        "# Core 0.1 Source-Profile Lock-or-Parking Receipt - C01SPLPR-G1-VIRAL-001",
        "",
        "Status: `single_source_profile_lock_or_parking_receipt_prepared_no_runtime_implementation`",
        "",
        "This receipt records the source-profile disposition for `C01WP-01-phase-1-scaffold-contracts` design prep.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- First-slice design prep packet: `{receipt['source_first_slice_design_prep_packet']}`.",
        f"- Whole Gate 1 acceptance decision: `{receipt['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Source-Profile Disposition",
        "",
        f"- Disposition: `{disposition['profile_receipt_disposition']}`.",
        "- Source-profile lock created: `false`.",
        "- Source-profile acceptance created: `false`.",
        "- Source-profile parking recorded: `true`.",
        f"- Parking scope: `{disposition['parking_scope']}`.",
        f"- Runtime implication: `{disposition['runtime_implication']}`.",
        "",
        "## Boundary",
        "",
        "- Runtime implementation: `false`.",
        "- Source-profile lock: `false`.",
        "- Source-profile acceptance beyond this receipt: `false`.",
        "- OCR/render/PDF/raw/source mutation: `false`.",
        "- Translation/proofreading: `false`.",
        "- Page 021+ processing/authorization: `false`.",
        "- Push: `false`.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in receipt["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_summary.md", "\n".join(lines))


def write_report(receipt: dict) -> None:
    scope = receipt["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_report.json",
        {
            "receipt_id": RECEIPT_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": receipt["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_first_slice_design_prep_packet": receipt["source_first_slice_design_prep_packet"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(scope["positive_fixture_groups"]),
            "negative_fixture_group_count": len(scope["negative_fixture_groups"]),
            "source_profile_receipt_created": True,
            "source_profile_lock_created": False,
            "source_profile_acceptance_created": False,
            "source_profile_parking_recorded": True,
            "accepts_source_profile_beyond_this_receipt": False,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": receipt["negative_capability_matrix"],
            "remaining_blockers": receipt["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_source_profile_lock_or_parking_receipt_manifest.md"
    lines = [
        "# Core 0.1 Source-Profile Lock-or-Parking Receipt Manifest - C01SPLPR-G1-VIRAL-001",
        "",
        "Status: `single_source_profile_lock_or_parking_receipt_prepared_no_runtime_implementation`",
        "",
        "Boundary: source-profile receipt material only for C01WP-01 design prep; no runtime implementation, source-profile lock, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, push, or downstream action.",
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
    write_json(OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt.json", receipt)
    write_summary(receipt)
    write_report(receipt)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
