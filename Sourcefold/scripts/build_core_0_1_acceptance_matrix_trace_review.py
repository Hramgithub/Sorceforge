from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_acceptance_matrix_trace_review.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_acceptance_matrix_trace_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
ARCH_ROOT = TRIAL_ROOT / "core_0_1_first_slice_architecture_review_packet_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_acceptance_matrix_trace_review_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-ACCEPTANCE-MATRIX-TRACE-REVIEW-001"
REVIEW_ID = "C01AMTR-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01FSARP-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01fsarp packet ok; proceed to prepare acceptance-matrix trace review for C01WP-01 from C01FSARP; "
    "no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, no OCR/render/PDF/raw mutation, "
    "no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01FSARP-G1-VIRAL-001.packet": (
        ARCH_ROOT / "core_0_1_first_slice_architecture_review_packet.json",
        "2D33226D25C446AB358F9686ACEEA16710236940D7C20A8B628AA8A9CD73B71E",
    ),
    "C01FSARP-G1-VIRAL-001.report": (
        ARCH_ROOT / "core_0_1_first_slice_architecture_review_packet_report.json",
        "A4E6F02F59220685CFDA7EF50A0A4F62C7B41A9AEDD3E0C417448BDC6A8A1ECB",
    ),
    "C01FSARP-G1-VIRAL-001.summary": (
        ARCH_ROOT / "core_0_1_first_slice_architecture_review_packet_summary.md",
        "9AA83B65ADF67E7F63481FB898D1B55E5D4F39F67215209C302021A067F865DD",
    ),
    "C01FSARP-G1-VIRAL-001.manifest": (
        ARCH_ROOT / "core_0_1_first_slice_architecture_review_packet_manifest.md",
        "A668C8D474EE2B8C6B244F811CCA4DE8C933677792096EFEDC07132F75CBFCD8",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 acceptance-matrix trace review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 acceptance-matrix trace review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 acceptance-matrix trace review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 acceptance-matrix trace review requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01FSARP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected architecture review packet input")
    if packet["status"] != "core_0_1_first_slice_architecture_review_packet_ready_no_runtime_implementation":
        raise SystemExit("architecture review packet is not the expected no-runtime packet")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("architecture review packet unexpectedly authorizes runtime implementation")
    if packet["source_profile_lock_created"] or packet["source_profile_acceptance_created"]:
        raise SystemExit("architecture review packet unexpectedly creates source-profile lock or acceptance")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if packet["next_possible_packets"][1] != "acceptance_matrix_trace_review_for_c01wp_01_if_separately_authorized":
        raise SystemExit("acceptance-matrix trace review is not a permitted next packet")
    return verified, packet


def build_review(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    trace_items = [
        {
            "claim_id": "accepted_gate_1_scope",
            "claim": "First slice may rely only on pages 001-020 and G1FADAR admitted fixture manifest groups.",
            "evidence": ["G1WGADR-G1-VIRAL-001", "C01FSARP-G1-VIRAL-001.accepted_gate_1_scope"],
            "runtime_use": "blocked_until_future_runtime_authorization",
        },
        {
            "claim_id": "module_boundary_contract",
            "claim": "C01WP-01 is limited to phase-1 scaffold contracts.",
            "evidence": ["C01FSDP-G1-VIRAL-001.module_boundary_contract", "C01FSARP review target module_boundary_contract"],
            "runtime_use": "design_review_only",
        },
        {
            "claim_id": "artifact_identity_contract",
            "claim": "Scaffold artifacts need stable identities before implementation can be authorized.",
            "evidence": ["C01FSDP-G1-VIRAL-001.artifact_identity_contract", "C01FSARP review target artifact_identity_contract"],
            "runtime_use": "design_review_only",
        },
        {
            "claim_id": "lineage_trace_contract",
            "claim": "Lineage must trace back to accepted Gate 1 pages and admitted fixture groups only.",
            "evidence": ["C01FSARP verified input hashes", "C01SPLPR-G1-VIRAL-001"],
            "runtime_use": "blocked_until_future_runtime_authorization",
        },
        {
            "claim_id": "negative_boundary_contract",
            "claim": "OCR/render/PDF/raw/source mutation, page 021+, translation, proofreading, and push remain blocked.",
            "evidence": ["C01FSARP negative capability matrix", "C01SPLPR negative capability matrix"],
            "runtime_use": "negative_guardrail",
        },
    ]
    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "acceptance_matrix_trace_review_prepared_no_runtime_implementation",
        "purpose": "bounded_acceptance_matrix_claim_to_evidence_trace_review_for_c01wp_01",
        "human_decision": HUMAN_DECISION,
        "source_architecture_review_packet": packet["packet_id"],
        "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
        "source_first_slice_design_prep_packet": packet["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "acceptance_matrix_trace_review_created": True,
        "claim_to_evidence_mapping_prepared": True,
        "trace_items": trace_items,
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
        "remaining_blockers": [
            "human_review_c01amtr_required",
            "runtime_source_profile_lock_or_runtime_parking_decision_required",
            "first_slice_runtime_authorization_required",
            "sol_terra_go_must_be_consumed_by_future_runtime_authorization",
            "roadmap_validation_required_for_c01wp_01_runtime_start",
            "ocr_render_pdf_raw_mutation_requires_separate_authorization",
            "translation_proofreading_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "human_review_c01amtr_packet",
            "core_0_1_first_slice_runtime_authorization_prep_if_separately_authorized_after_prerequisites",
            "runtime_source_profile_lock_or_runtime_parking_decision_if_separately_authorized",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(review: dict) -> None:
    scope = review["accepted_gate_1_scope"]
    lines = [
        "# Core 0.1 Acceptance-Matrix Trace Review - C01AMTR-G1-VIRAL-001",
        "",
        "Status: `acceptance_matrix_trace_review_prepared_no_runtime_implementation`",
        "",
        "This review maps C01WP-01 acceptance-matrix claims to existing evidence before any runtime authorization.",
        "",
        "It does not authorize runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Architecture review packet: `{review['source_architecture_review_packet']}`.",
        f"- Source-profile receipt: `{review['source_profile_lock_or_parking_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{review['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Claim/Evidence Trace Items",
        "",
    ]
    for item in review["trace_items"]:
        lines.extend(
            [
                f"- `{item['claim_id']}`: {item['claim']}",
                f"  Evidence: {', '.join(item['evidence'])}",
                f"  Runtime use: `{item['runtime_use']}`.",
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
    for blocker in review["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_acceptance_matrix_trace_review_summary.md", "\n".join(lines))


def write_report(review: dict) -> None:
    scope = review["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_acceptance_matrix_trace_review_report.json",
        {
            "review_id": REVIEW_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": review["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_architecture_review_packet": review["source_architecture_review_packet"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "trace_item_count": len(review["trace_items"]),
            "acceptance_matrix_trace_review_created": True,
            "claim_to_evidence_mapping_prepared": True,
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
            "negative_capability_matrix": review["negative_capability_matrix"],
            "remaining_blockers": review["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_acceptance_matrix_trace_review_manifest.md"
    lines = [
        "# Core 0.1 Acceptance-Matrix Trace Review Manifest - C01AMTR-G1-VIRAL-001",
        "",
        "Status: `acceptance_matrix_trace_review_prepared_no_runtime_implementation`",
        "",
        "Boundary: claim/evidence trace review only for C01WP-01; no runtime implementation, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, push, or downstream action.",
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
    review = build_review(verified_inputs, packet)
    write_json(OUT_ROOT / "core_0_1_acceptance_matrix_trace_review.json", review)
    write_summary(review)
    write_report(review)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
