from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_ocr_benchmark_methodology_hardening.py"
TEST_PATH = ROOT / "tests" / "test_ocr_benchmark_methodology_hardening.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-OCR-BENCHMARK-METHODOLOGY-HARDENING-001"
HARDENING_ID = "OCRHM-G1-VIRAL-001"

INPUT_HASHES = {
    "G1SPRMREV-G1-VIRAL-001.review": (
        TRIAL_ROOT
        / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"
        / "gate_1_source_profile_readiness_parking_matrix_review.json",
        "76D0B43FCE9B614424A47FEBDE61666E42B372E671396E876E1F59B38FCEC640",
    ),
    "ORM-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001" / "ocr_remediation_matrix_report.json",
        "3A454433ABA46E237D091F5BB4DA6EB8B73FCEE400935AF10BB0DC5731F212F5",
    ),
    "ORM-G1-VIRAL-001.rows": (
        TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001" / "ocr_remediation_matrix_rows.json",
        "B0077249E070E6673E12F4A8B83C542DFD400A8200C558ACED4A0C47C284FD66",
    ),
    "ORR-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001" / "ocr_remediation_review_report.json",
        "B3491A1F3E942C430AE246A62DCAFB066F95BEA56390CF510D27635EBFEE6725",
    ),
    "ONC-G1-VIRAL-001.report": (
        TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001" / "negative_check_report.json",
        "2205564DB2BCD9EEF73D8EB02034EA28D7292D1A6970E3056F3BD9F5887E8F61",
    ),
    "OBR-G1-VIRAL-002.result": (
        TRIAL_ROOT / "ocr_benchmark_OBR-G1-VIRAL-002" / "ocr_benchmark_result_report.md",
        "AFC2D58AB9B22ADD6A0B345BB72FA630049FBB1855771A1EF2ADDCC20D646937",
    ),
    "OBR-G1-VIRAL-002.manifest": (
        TRIAL_ROOT / "ocr_benchmark_OBR-G1-VIRAL-002" / "ocr_output_manifest.md",
        "BF8ABFF3F9E54DCAA0E2C944A437EC46D1A0C066C051798F012B0FC1AFEFD849",
    ),
    "OBR-G1-VIRAL-002.boundary": (
        TRIAL_ROOT / "ocr_benchmark_OBR-G1-VIRAL-002" / "ocr_run_boundary_report.md",
        "CFA4B8ACDF0BA5AED70DFE5E730E442D8B3D3671E17FEE8300AB5BE4AE95B10C",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "ocr_remediation_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "source_mutation",
    "source_profile_acceptance",
    "creates_parking_decision",
    "fixture_admission",
    "page_021_plus_processing",
    "whole_gate_1_acceptance",
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


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build OCR benchmark methodology hardening packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("OCR benchmark methodology hardening is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"OCR benchmark methodology hardening requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict, dict]:
    verify_authorization_ledger()
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    matrix_review = read_json(INPUT_HASHES["G1SPRMREV-G1-VIRAL-001.review"][0])
    orm = read_json(INPUT_HASHES["ORM-G1-VIRAL-001.report"][0])
    orr = read_json(INPUT_HASHES["ORR-G1-VIRAL-001.report"][0])
    onc = read_json(INPUT_HASHES["ONC-G1-VIRAL-001.report"][0])
    if matrix_review["starts_ocr_remediation"] is not False:
        raise SystemExit("matrix review unexpectedly starts OCR remediation")
    if orm["status"] != "remediation_evidence_only" or orr["status"] != "remediation_evidence_only":
        raise SystemExit("OCR predecessor is not evidence-only")
    if onc["check_state"] != "passed":
        raise SystemExit("negative OCR checks are not passed")
    return verified, matrix_review, orm, orr


def hardening_rows() -> list[dict[str, str]]:
    return [
        {
            "id": "exact_predecessor_lineage",
            "status": "hardened_for_gate_review",
            "rule": "OCR hardening consumes exact hashed G1SPRMREV/ORM/ORR/ONC/OBR evidence only.",
        },
        {
            "id": "no_new_ocr_or_pdf_execution",
            "status": "hardened_for_gate_review",
            "rule": "Methodology hardening does not execute OCR, parse PDF text layers, render, or mutate raw outputs.",
        },
        {
            "id": "engine_config_and_psm_policy",
            "status": "hardened_for_gate_review",
            "rule": "Tesseract 5.4 evidence is bound; default PSM set is 1/4/8/11 and PSM 3/6 are excluded from default rows.",
        },
        {
            "id": "benchmark_pass_fail_policy",
            "status": "hardened_for_gate_review",
            "rule": "Normalized exact evidence may qualify routes for review, but no source/profile acceptance may be approved by score alone.",
        },
        {
            "id": "visual_qc_route_policy",
            "status": "hardened_for_gate_review",
            "rule": "Visual-only zones remain visual QC routes and are not forced through OCR.",
        },
        {
            "id": "overlay_order_qc_interpretation",
            "status": "hardened_for_gate_review",
            "rule": "Overlay geometry findings are explicit review signals; order QC pass does not override visual review requirements.",
        },
        {
            "id": "raw_payload_containment",
            "status": "hardened_for_gate_review",
            "rule": "Raw OCR text/TSV/stderr/command logs remain hash-bound evidence and are not promoted into source text by this packet.",
        },
        {
            "id": "human_review_deferral_policy",
            "status": "hardened_for_gate_review",
            "rule": "Bogdan review remains deferred until a readable source reconstruction review package exists.",
        },
        {
            "id": "remaining_gate_decisions",
            "status": "requires_future_gate_decision",
            "rule": "Engine/profile acceptance, fixture admission, whole Gate 1 acceptance, and page 021+ remain future decisions.",
        },
    ]


def build_packet(verified_inputs: dict[str, dict[str, str]], matrix_review: dict, orm: dict, orr: dict) -> dict:
    rows = hardening_rows()
    return {
        "hardening_id": HARDENING_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ocr_benchmark_methodology_hardened_for_gate_review_no_acceptance",
        "purpose": "ocr_benchmark_methodology_hardening_no_new_ocr_no_acceptance",
        "creates_acceptance": False,
        "creates_parking_decision": False,
        "executes_ocr": False,
        "starts_remediation_run": False,
        "baseline_matrix_review": matrix_review["review_id"],
        "ocr_evidence": {
            "orm_run_id": orm["run_id"],
            "orr_review_id": orr["review_id"],
            "aggregate": orr["aggregate"],
        },
        "methodology_rules": rows,
        "methodology_rule_counts": {
            "hardened_for_gate_review": sum(1 for row in rows if row["status"] == "hardened_for_gate_review"),
            "requires_future_gate_decision": sum(1 for row in rows if row["status"] == "requires_future_gate_decision"),
        },
        "next_status": {
            "ocr_benchmark_remediation_debt": "methodology_hardened_for_gate_review",
            "source_profile_acceptance": "still_requires_future_gate_decision",
            "recommended_next_packet": "post_ocr_hardening_gate_1_readiness_refresh",
        },
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# OCR Benchmark Methodology Hardening - OCRHM-G1-VIRAL-001",
        "",
        "Status: `ocr_benchmark_methodology_hardened_for_gate_review_no_acceptance`",
        "",
        "This packet hardens OCR benchmark methodology using existing evidence only. It executes no OCR and creates no acceptance.",
        "",
        "## Evidence",
        "",
        f"- Matrix review: `{packet['baseline_matrix_review']}`",
        f"- ORM run: `{packet['ocr_evidence']['orm_run_id']}`",
        f"- ORR review: `{packet['ocr_evidence']['orr_review_id']}`",
        f"- Samples: `{packet['ocr_evidence']['aggregate']['samples']}`",
        f"- Remediation route pass: `{packet['ocr_evidence']['aggregate']['remediation_route_pass']}`",
        f"- OCR normalized exact zones: `{packet['ocr_evidence']['aggregate']['ocr_normalized_exact_zones']}`",
        f"- Visual QC route zones: `{packet['ocr_evidence']['aggregate']['visual_qc_route_zones']}`",
        "",
        "## Methodology Rules",
        "",
        "| Rule | Status |",
        "|---|---|",
    ]
    for row in packet["methodology_rules"]:
        lines.append(f"| `{row['id']}` | `{row['status']}` |")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No OCR execution or remediation rerun.",
            "- No source-profile acceptance.",
            "- No parking decision.",
            "- No page 021+ processing.",
            "- No fixture admission or whole Gate 1 acceptance.",
            "- Recommended next packet: `post_ocr_hardening_gate_1_readiness_refresh`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "ocr_benchmark_methodology_hardening_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "ocr_benchmark_methodology_hardening_report.json",
        {
            "hardening_id": HARDENING_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "creates_acceptance": False,
            "creates_parking_decision": False,
            "executes_ocr": False,
            "starts_remediation_run": False,
            "methodology_rule_counts": packet["methodology_rule_counts"],
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "next_status": packet["next_status"],
        },
    )


def write_manifest() -> None:
    manifest_name = "ocr_benchmark_methodology_hardening_manifest.md"
    lines = [
        "# OCR Benchmark Methodology Hardening Manifest - OCRHM-G1-VIRAL-001",
        "",
        "Status: `ocr_benchmark_methodology_hardened_for_gate_review_no_acceptance`",
        "",
        "Boundary: existing-evidence methodology hardening only; no OCR execution, no acceptance, no parking decision, no page 021+ authorization, and no whole Gate 1 acceptance.",
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
    verified_inputs, matrix_review, orm, orr = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, matrix_review, orm, orr)
    write_json(OUT_ROOT / "ocr_benchmark_methodology_hardening.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
