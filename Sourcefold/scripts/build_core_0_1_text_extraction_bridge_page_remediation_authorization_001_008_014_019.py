from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from ocr_input_surface_policy import validate_ocr_input_surface


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUDIT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019_G1_VIRAL_001"

LANE_ID = "C01TEBRIDGEREMAUTH020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-REMEDIATION-AUTHORIZATION-001-008-014-019-001"
HUMAN_DECISION = "Ок иди по плану, ты оркестратор, следи чтоб все было сделанл"
INPUT_LANE_ID = "C01TEBRIDGEAUD020-G1-VIRAL-001"

REQUESTED_PAGES = ["001", "002", "003", "004", "005", "006", "007", "008", "014", "019"]
VISUAL_ONLY_PAGES = ["001"]
FULL_PAGE_OCR_CANDIDATE_PAGES = ["003", "004", "005", "006", "007", "008"]
TEXT_EVIDENCE_SMOKE_PAGES = ["014", "019"]
SOURCE_ASSET_RECOVERY_PAGES = ["002"]

INPUT_HASHES = {
    "C01TEBRIDGEAUD020-G1-VIRAL-001.report": (
        AUDIT_ROOT / "bridge_page_audit_001_008_014_019_report.json",
        "25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02",
    ),
    "C01TEBRIDGEAUD020-G1-VIRAL-001.summary": (
        AUDIT_ROOT / "bridge_page_audit_001_008_014_019_summary.md",
        "744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639",
    ),
    "C01TEBRIDGEAUD020-G1-VIRAL-001.manifest": (
        AUDIT_ROOT / "bridge_page_audit_001_008_014_019_manifest.md",
        "D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_mutation",
    "raw_mutation",
    "fixture_admission",
    "production_assembly",
    "clean_production_output_folder",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
    "promotion",
    "acceptance",
    "downstream_execution",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def git_head() -> str:
    result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Authorize bounded bridge-page remediation route without executing OCR.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("bridge-page remediation authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"bridge-page remediation authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("bridge-page remediation authorization requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in INPUT_HASHES.items()}
    audit = read_json(INPUT_HASHES["C01TEBRIDGEAUD020-G1-VIRAL-001.report"][0])
    if audit["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected bridge-page audit input lane")
    if audit["audit_pages"] != REQUESTED_PAGES:
        raise SystemExit(f"audit page set drifted: {audit['audit_pages']}")
    if audit["visual_only_no_text_rule_pages"] != VISUAL_ONLY_PAGES:
        raise SystemExit("visual-only page set drifted")
    if audit["needs_source_asset_recovery_pages"] != SOURCE_ASSET_RECOVERY_PAGES:
        raise SystemExit("source asset recovery page set drifted")
    if sorted(audit["fresh_ocr_route_possible_pages"]) != sorted(FULL_PAGE_OCR_CANDIDATE_PAGES + TEXT_EVIDENCE_SMOKE_PAGES):
        raise SystemExit("fresh OCR route possible page set drifted")
    return verified, audit


def surface_for_page(item: dict) -> dict:
    page = item["page"]
    if page in FULL_PAGE_OCR_CANDIDATE_PAGES:
        return {
            "page_id": f"P{page}",
            "surface_class": "full_page_region",
            "allowed_purpose": "candidate_policy",
            "ocr_allowed": True,
            "source_artifact": {
                "path": item["page_image"]["path"],
                "sha256": item["page_image"]["sha256"],
                "hash_status": "matched",
            },
            "authorization": {
                "full_page_region_authorization_id": AUTHORIZATION_ID,
                "page_family": "bridge_pages_003_008_full_page_candidate_policy",
                "region_policy": "existing_page_image_candidate_only_no_acceptance",
                "negative_reason_not_baseline": "no_text_evidence_crops_available_for_bridge_page_remediation",
            },
            "tesseract_invoked": False,
            "render_invoked": False,
            "pdf_parsed": False,
            "pdf_text_layer_read": False,
            "non_temp_artifact_write": False,
            "reference_loaded_before_candidate_hash": False,
        }
    if page in TEXT_EVIDENCE_SMOKE_PAGES:
        first_crop = item["text_evidence_crops"][0]
        return {
            "page_id": f"P{page}",
            "surface_class": "text_evidence_crop",
            "allowed_purpose": "smoke_non_promotable",
            "ocr_allowed": False,
            "source_artifact": {
                "path": first_crop["path"],
                "sha256": first_crop["sha256"],
                "hash_status": "matched",
            },
            "tesseract_invoked": False,
            "render_invoked": False,
            "pdf_parsed": False,
            "pdf_text_layer_read": False,
            "non_temp_artifact_write": False,
            "reference_loaded_before_candidate_hash": False,
        }
    raise SystemExit(f"P{page} is not an OCR surface page")


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def build_report(verified_inputs: dict[str, dict[str, str]], audit: dict) -> dict:
    by_page = {item["page"]: item for item in audit["page_audit"]}
    surface_validations = []
    for page in FULL_PAGE_OCR_CANDIDATE_PAGES + TEXT_EVIDENCE_SMOKE_PAGES:
        surface = surface_for_page(by_page[page])
        validation = validate_ocr_input_surface(surface)
        if validation["status"] != "passed":
            raise SystemExit(f"P{page} OCR input surface policy blocked: {validation['findings']}")
        surface_validations.append({"page": page, "surface": surface, "validation": validation})
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "bridge_page_remediation_authorization_recorded_report_only",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "human_decision": HUMAN_DECISION,
        "requested_pages": REQUESTED_PAGES,
        "visual_only_no_text_rule_pages": VISUAL_ONLY_PAGES,
        "full_page_region_candidate_pages": FULL_PAGE_OCR_CANDIDATE_PAGES,
        "text_evidence_smoke_non_promotable_pages": TEXT_EVIDENCE_SMOKE_PAGES,
        "needs_source_asset_recovery_pages": SOURCE_ASSET_RECOVERY_PAGES,
        "page_002_blocker": "needs_source_asset_recovery",
        "remediation_route_authorized_for_future_runner": True,
        "this_lane_report_only": True,
        "next_runner_must_consume_audit_entries_directly": True,
        "ocr_input_surface_policy_validated": True,
        "surface_validations": surface_validations,
        "page_001_materialization_authorized": "visual_only_no_text_rule_non_text_non_ocr",
        "page_001_ocr_execution_authorized": False,
        "page_001_fresh_ocr_success_authorized": False,
        "page_002_remains_blocked": True,
        "ocr_execution_performed": False,
        "runtime_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "production_ready": False,
        "production_assembly_authorized": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "fixture_admission_performed": False,
        "clean_candidate_output_folder_created": False,
        "clean_production_output_folder_created": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "push_performed": False,
        "downstream_execution_performed": False,
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "allowed_next_action": "implement_bounded_bridge_page_remediation_runner_under_this_authorization",
    }


def write_summary(report: dict) -> None:
    lines = [
        "# Bridge Page Remediation Authorization 001-008 014 019 - C01TEBRIDGEREMAUTH020-G1-VIRAL-001",
        "",
        "Status: `bridge_page_remediation_authorization_recorded_report_only`",
        "",
        "This packet authorizes only a future bounded remediation runner. It does not execute OCR.",
        "",
        "- Visual-only/non-text page: `001`.",
        "- Full-page candidate-policy pages: `003`, `004`, `005`, `006`, `007`, `008`.",
        "- Text-evidence smoke/non-promotable pages: `014`, `019`.",
        "- Source asset recovery blocker: `002`.",
        "",
        "Page `001` is not fresh OCR success. Page `002` remains blocked.",
        "No production, acceptance, fixture admission, source/raw/accepted/page-status mutation, page `021+`, push, or downstream execution is authorized.",
        "",
    ]
    write_text(OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Bridge Page Remediation Authorization 001-008 014 019 Manifest - C01TEBRIDGEREMAUTH020-G1-VIRAL-001",
        "",
        "Boundary: report-only route authorization; no OCR execution and no mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "bridge_page_remediation_authorization_001_008_014_019_manifest.md":
            lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    lines.append("")
    write_text(OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_manifest.md", "\n".join(lines))


def build() -> None:
    verified_inputs, audit = verify_inputs()
    report = build_report(verified_inputs, audit)
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    write_json(OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
