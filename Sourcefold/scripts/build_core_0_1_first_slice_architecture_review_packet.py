from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_first_slice_architecture_review_packet.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_first_slice_architecture_review_packet.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
RECEIPT_ROOT = TRIAL_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_first_slice_architecture_review_packet_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-ARCHITECTURE-REVIEW-PACKET-001"
PACKET_ID = "C01FSARP-G1-VIRAL-001"
SOURCE_RECEIPT_ID = "C01SPLPR-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01splpr packet ok; proceed to prepare Core 0.1 first-slice architecture review packet for C01WP-01 "
    "from C01SPLPR; no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01SPLPR-G1-VIRAL-001.receipt": (
        RECEIPT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt.json",
        "2E65C839830397E9FCA301CABCE4209AB370CB18867AD57577B61268DA46B5D8",
    ),
    "C01SPLPR-G1-VIRAL-001.report": (
        RECEIPT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_report.json",
        "EB8836B1DC0820828200E7C20FD557A08D41B79E9432B65A534C1B44CB9918B7",
    ),
    "C01SPLPR-G1-VIRAL-001.summary": (
        RECEIPT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_summary.md",
        "B7EE0D1545E98CFA9AAB35B6998DF4467D54BAF64D85E56853258EABCD398DF8",
    ),
    "C01SPLPR-G1-VIRAL-001.manifest": (
        RECEIPT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_manifest.md",
        "919CFF991DE4A89154D37B62B3C371805691C6345E0989E4A845A078430884AF",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
    "source_profile_lock",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 first-slice architecture review packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 first-slice architecture review packet is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 first-slice architecture review packet requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 first-slice architecture review packet requires the exact bounded human decision")


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

    receipt = read_json(INPUT_HASHES["C01SPLPR-G1-VIRAL-001.receipt"][0])
    if receipt["receipt_id"] != SOURCE_RECEIPT_ID:
        raise SystemExit("unexpected source-profile receipt input")
    if receipt["status"] != "single_source_profile_lock_or_parking_receipt_prepared_no_runtime_implementation":
        raise SystemExit("source-profile receipt is not the expected no-runtime packet")
    if receipt["source_profile_lock_created"] or receipt["source_profile_acceptance_created"]:
        raise SystemExit("source-profile receipt unexpectedly creates lock or acceptance")
    if receipt["runtime_implementation_authorized"] or receipt["creates_runtime_implementation"]:
        raise SystemExit("source-profile receipt unexpectedly authorizes runtime implementation")
    if receipt["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if receipt["next_possible_packets"][0] != "core_0_1_first_slice_architecture_review_packet_if_separately_authorized":
        raise SystemExit("architecture review packet is not the next packet")
    return verified, receipt


def build_packet(verified_inputs: dict[str, dict[str, str]], receipt: dict) -> dict:
    review_targets = [
        {
            "target_id": "module_boundary_contract",
            "question": "Does the first slice have a minimal scaffold boundary without runtime processing?",
            "expected_evidence": "C01FSDP module-boundary design surface plus C01SPLPR source-profile parking receipt.",
            "review_owner": "Sol",
        },
        {
            "target_id": "artifact_identity_contract",
            "question": "Are Core 0.1 scaffold artifacts named and scoped without accepting new source/profile state?",
            "expected_evidence": "C01FSDP artifact-identity surface and accepted Gate 1 scope from G1WGADR.",
            "review_owner": "Sol",
        },
        {
            "target_id": "lineage_trace_contract",
            "question": "Can the first slice trace inputs to pages 001-020 and G1FADAR fixtures only?",
            "expected_evidence": "G1WGADR accepted scope plus C01SPLPR verified input hashes.",
            "review_owner": "Sol",
        },
        {
            "target_id": "acceptance_matrix_trace_contract",
            "question": "Is the acceptance-matrix trace surface review-ready before runtime authorization?",
            "expected_evidence": "C01FSDP acceptance-matrix trace surface and C01SPLPR remaining blocker list.",
            "review_owner": "Sol",
        },
        {
            "target_id": "negative_boundary_contract",
            "question": "Do the proposed first-slice contracts keep OCR/render/PDF/raw/source mutation, page 021+, and translation blocked?",
            "expected_evidence": "C01SPLPR negative capability matrix.",
            "review_owner": "Terra",
        },
    ]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "core_0_1_first_slice_architecture_review_packet_ready_no_runtime_implementation",
        "purpose": "bounded_sol_terra_architecture_review_packet_for_c01wp_01",
        "human_decision": HUMAN_DECISION,
        "source_profile_lock_or_parking_receipt": receipt["receipt_id"],
        "source_first_slice_design_prep_packet": receipt["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": receipt["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": receipt["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": receipt["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "architecture_review_packet_created": True,
        "sol_architecture_review_targets_prepared": True,
        "terra_critique_targets_prepared": True,
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
        "review_targets": review_targets,
        "review_questions": {
            "sol": [
                "Is C01WP-01-phase-1-scaffold-contracts architecturally bounded to scaffold contracts only?",
                "Are module boundary, artifact identity, lineage trace, and acceptance-matrix trace surfaces complete enough for future authorization review?",
                "Does the packet correctly consume C01SPLPR without creating a runtime source-profile lock?",
            ],
            "terra": [
                "Does any wording imply runtime implementation or runtime source-profile acceptance?",
                "Are page 021+, OCR/render/PDF/raw/source mutation, translation/proofreading, and push still blocked?",
                "Are stale current-action blockers avoided across synced docs?",
            ],
        },
        "remaining_blockers": [
            "sol_architecture_review_go_required",
            "terra_critique_go_required",
            "acceptance_matrix_claim_to_evidence_mapping_required_for_c01wp_01",
            "runtime_source_profile_lock_or_runtime_parking_decision_required",
            "first_slice_runtime_authorization_required",
            "roadmap_validation_required_for_c01wp_01",
            "ocr_render_pdf_raw_mutation_requires_separate_authorization",
            "translation_proofreading_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "human_review_c01fsarp_packet",
            "acceptance_matrix_trace_review_for_c01wp_01_if_separately_authorized",
            "core_0_1_first_slice_runtime_authorization_if_separately_authorized_after_prerequisites",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    lines = [
        "# Core 0.1 First-Slice Architecture Review Packet - C01FSARP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_first_slice_architecture_review_packet_ready_no_runtime_implementation`",
        "",
        "This packet prepares Sol/Terra architecture review material for `C01WP-01-phase-1-scaffold-contracts`.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Source-profile receipt: `{packet['source_profile_lock_or_parking_receipt']}`.",
        f"- First-slice design prep: `{packet['source_first_slice_design_prep_packet']}`.",
        f"- Whole Gate 1 acceptance decision: `{packet['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Review Targets",
        "",
    ]
    for target in packet["review_targets"]:
        lines.extend(
            [
                f"- `{target['target_id']}` ({target['review_owner']}): {target['question']}",
                f"  Evidence: {target['expected_evidence']}",
            ]
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Runtime implementation: `false`.",
            "- Runtime source-profile lock: `false`.",
            "- Source-profile acceptance beyond `C01SPLPR`: `false`.",
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
    write_text(OUT_ROOT / "core_0_1_first_slice_architecture_review_packet_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_first_slice_architecture_review_packet_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "review_target_count": len(packet["review_targets"]),
            "architecture_review_packet_created": True,
            "sol_architecture_review_targets_prepared": True,
            "terra_critique_targets_prepared": True,
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
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_first_slice_architecture_review_packet_manifest.md"
    lines = [
        "# Core 0.1 First-Slice Architecture Review Packet Manifest - C01FSARP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_first_slice_architecture_review_packet_ready_no_runtime_implementation`",
        "",
        "Boundary: Sol/Terra architecture review packet only for C01WP-01; no runtime implementation, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, push, or downstream action.",
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
    write_json(OUT_ROOT / "core_0_1_first_slice_architecture_review_packet.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
