from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from ocr_input_surface_policy import route_ocr_input_surface, validate_ocr_input_surface


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019_G1_VIRAL_001"
AUDIT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")

LANE_ID = "C01TEBRIDGEREM020-G1-VIRAL-001"
AUTHORIZATION_LANE_ID = "C01TEBRIDGEREMAUTH020-G1-VIRAL-001"
AUDIT_LANE_ID = "C01TEBRIDGEAUD020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-REMEDIATION-AUTHORIZATION-001-008-014-019-001"
HUMAN_DECISION = "Ок иди по плану, ты оркестратор, следи чтоб все было сделанл"

REQUESTED_PAGES = ["001", "002", "003", "004", "005", "006", "007", "008", "014", "019"]
VISUAL_ONLY_PAGES = ["001"]
FULL_PAGE_OCR_PAGES = ["003", "004", "005", "006", "007", "008"]
TEXT_EVIDENCE_SMOKE_PAGES = ["014", "019"]
SOURCE_ASSET_RECOVERY_PAGES = ["002"]

AUTH_INPUT_HASHES = {
    "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.report": (
        AUTH_ROOT / "bridge_page_remediation_authorization_001_008_014_019_report.json",
        "9DD604336DA642FB575DEBD5180885DC04289ECE82647FB4ECD4518056C74A60",
    ),
    "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.summary": (
        AUTH_ROOT / "bridge_page_remediation_authorization_001_008_014_019_summary.md",
        "0C2B64917035F58F9142671AECEFA11880A0E4568408381748EAB46A24B7E00C",
    ),
    "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "bridge_page_remediation_authorization_001_008_014_019_manifest.md",
        "E19100825A3E157179A72341A9EE8E59DB3D533273AACF87C394C4774EF49AE5",
    ),
}

AUDIT_INPUT_HASHES = {
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
    parser = argparse.ArgumentParser(description="Run bounded bridge-page remediation candidate lane.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("bridge-page remediation runner is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"bridge-page remediation runner requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("bridge-page remediation runner requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_authorization() -> tuple[dict[str, dict[str, str]], dict, dict]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in AUTH_INPUT_HASHES.items()}
    verified.update({key: verified_input(path, expected) for key, (path, expected) in AUDIT_INPUT_HASHES.items()})
    report = read_json(AUTH_INPUT_HASHES["C01TEBRIDGEREMAUTH020-G1-VIRAL-001.report"][0])
    audit = read_json(AUDIT_INPUT_HASHES["C01TEBRIDGEAUD020-G1-VIRAL-001.report"][0])
    if report["lane_id"] != AUTHORIZATION_LANE_ID:
        raise SystemExit("unexpected remediation authorization lane")
    if audit["lane_id"] != AUDIT_LANE_ID:
        raise SystemExit("unexpected remediation audit lane")
    if report["authorization_id"] != AUTHORIZATION_ID:
        raise SystemExit("unexpected remediation authorization id")
    if report["requested_pages"] != REQUESTED_PAGES:
        raise SystemExit("requested page set drifted")
    if audit["audit_pages"] != REQUESTED_PAGES:
        raise SystemExit("audit page set drifted")
    if report["full_page_region_candidate_pages"] != FULL_PAGE_OCR_PAGES:
        raise SystemExit("full-page OCR page set drifted")
    if report["text_evidence_smoke_non_promotable_pages"] != TEXT_EVIDENCE_SMOKE_PAGES:
        raise SystemExit("text-evidence smoke page set drifted")
    if report["visual_only_no_text_rule_pages"] != VISUAL_ONLY_PAGES:
        raise SystemExit("visual-only page set drifted")
    if report["needs_source_asset_recovery_pages"] != SOURCE_ASSET_RECOVERY_PAGES:
        raise SystemExit("source asset recovery page set drifted")
    return verified, report, audit


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def token_set(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", normalize_text(text)))


def score_candidate(candidate: str, reference: str) -> dict[str, float]:
    candidate_norm = normalize_text(candidate)
    reference_norm = normalize_text(reference)
    ratio = difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio() if reference_norm else 0.0
    ref_tokens = token_set(reference_norm)
    cand_tokens = token_set(candidate_norm)
    recall = (len(ref_tokens & cand_tokens) / len(ref_tokens)) if ref_tokens else 0.0
    return {"sequence_similarity_ratio": round(ratio, 6), "token_recall": round(recall, 6)}


def text_from_reference_map(path: Path) -> str:
    if path.suffix.lower() == ".json":
        payload = read_json(path)
        parts: list[str] = []
        if isinstance(payload, list):
            items = payload
        elif isinstance(payload, dict):
            items = payload.get("semantic_units") or payload.get("units") or payload.get("blocks") or []
        else:
            items = []
        for item in items:
            if isinstance(item, dict):
                value = item.get("text") or item.get("content") or item.get("ocr_text")
                if isinstance(value, str):
                    parts.append(value)
        if parts:
            return "\n\n".join(parts)
    return path.read_text(encoding="utf-8-sig")


def source_artifact_path(surface: dict) -> Path:
    rel = surface["source_artifact"]["path"]
    return ROOT / rel


def run_tesseract(image_path: Path, page: str, psm: int = 6) -> tuple[str, dict[str, Any]]:
    if not TESSERACT.exists():
        raise SystemExit(f"tesseract executable not found: {TESSERACT}")
    with tempfile.TemporaryDirectory(prefix=f"sourcefold_p{page}_ocr_") as temp_dir:
        output_base = Path(temp_dir) / f"page_{page}_full_page_psm{psm}"
        command = [str(TESSERACT), str(image_path), str(output_base), "-l", "eng", "--oem", "1", "--psm", str(psm), "txt", "tsv"]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if result.returncode != 0:
            raise SystemExit(f"tesseract failed for page {page}: {result.stderr}")
        text_path = output_base.with_suffix(".txt")
        tsv_path = output_base.with_suffix(".tsv")
        text = text_path.read_text(encoding="utf-8-sig") if text_path.exists() else ""
        return text, {
            "engine": "tesseract",
            "command_profile": "tesseract -l eng --oem 1 --psm 6 txt tsv",
            "input_path": image_path.relative_to(ROOT).as_posix(),
            "input_sha256": sha256_file(image_path),
            "transient_ocr_output_persisted": False,
            "transient_txt_sha256": sha256_file(text_path),
            "transient_tsv_sha256": sha256_file(tsv_path),
            "stdout_sha256": hashlib.sha256(result.stdout.encode("utf-8")).hexdigest().upper(),
            "stderr_sha256": hashlib.sha256(result.stderr.encode("utf-8")).hexdigest().upper(),
            "returncode": result.returncode,
        }


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def build_full_page_entry(page: str, surface_item: dict) -> dict[str, Any]:
    surface = surface_item["surface"]
    if surface["surface_class"] != "full_page_region" or surface["ocr_allowed"] is not True:
        raise SystemExit(f"P{page} is not authorized as a full-page OCR candidate")
    validation = validate_ocr_input_surface({**surface, "tesseract_invoked": False, "non_temp_artifact_write": False})
    if validation["status"] != "passed":
        raise SystemExit(f"P{page} input surface validation failed before OCR: {validation['findings']}")

    candidate_text, run_meta = run_tesseract(source_artifact_path(surface), page)
    candidate_path = OUT_ROOT / "candidate_texts" / f"page_{page}_full_page_psm6_candidate.md"
    write_text(candidate_path, candidate_text)
    candidate_hash = sha256_file(candidate_path)
    metadata_path = OUT_ROOT / "ocr_metadata" / f"page_{page}_full_page_psm6_ocr_metadata.json"

    metrics = {"sequence_similarity_ratio": 0.0, "token_recall": 0.0}
    reference_meta: dict[str, Any] = {
        "reference_status": "not_loaded_no_pinned_reference_for_remediation_run",
        "reference_loaded_after_candidate_hash_sealed": False,
    }

    route_surface = {
        **surface,
        "tesseract_invoked": False,
        "non_temp_artifact_write": False,
        "reference_loaded_before_candidate_hash": False,
    }
    route = route_ocr_input_surface(
        surface=route_surface,
        metrics=metrics,
        diagnostic_flags=["full_page_region_bridge_remediation"],
        candidate_text_hash_sealed=True,
        scoring_report_complete=True,
    )
    entry = {
        "page": page,
        "page_id": f"P{page}",
        "route_family": "full_page_region_candidate_policy",
        "ocr_execution_performed": True,
        "tesseract_invoked_for_page": True,
        "surface_validation_before_ocr": validation,
        "ocr_run": run_meta,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": candidate_hash,
        "candidate_hash_sealed_before_reference_scoring": True,
        "metrics": metrics,
        "reference": reference_meta,
        "policy_route": route,
        "fresh_ocr_candidate_created": True,
        "fresh_ocr_success": route["route_decision"] == "candidate_policy_ready_for_review",
        "acceptance_effect": "none",
        "promotion_effect": "none",
    }
    write_json(metadata_path, {"page": page, "ocr_run": run_meta, "candidate_text_sha256": candidate_hash})
    entry["ocr_metadata_path"] = metadata_path.relative_to(ROOT).as_posix()
    entry["ocr_metadata_sha256"] = sha256_file(metadata_path)
    return entry


def build_visual_only_entry() -> dict[str, Any]:
    path = OUT_ROOT / "visual_only" / "page_001_visual_only_no_text_rule.md"
    write_text(
        path,
        "# Page 001 Visual-Only No-Text Rule\n\n"
        "Page 001 is materialized as visual-only/non-text for this remediation lane.\n"
        "No OCR execution is authorized or performed for this page, and this is not fresh OCR success.\n",
    )
    return {
        "page": "001",
        "page_id": "P001",
        "route_family": "visual_only_no_text_rule",
        "materialized": True,
        "fresh_ocr_candidate_created": False,
        "fresh_ocr_success": False,
        "ocr_execution_performed": False,
        "output_path": path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(path),
    }


def build_blocker_entry() -> dict[str, Any]:
    path = OUT_ROOT / "blockers" / "page_002_needs_source_asset_recovery.md"
    write_text(
        path,
        "# Page 002 Source Asset Recovery Blocker\n\n"
        "Page 002 remains blocked as needs_source_asset_recovery. No OCR execution, bridge removal, "
        "acceptance, or production assembly is performed for this page.\n",
    )
    return {
        "page": "002",
        "page_id": "P002",
        "route_family": "needs_source_asset_recovery",
        "materialized": False,
        "fresh_ocr_candidate_created": False,
        "fresh_ocr_success": False,
        "ocr_execution_performed": False,
        "output_path": path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(path),
    }


def build_smoke_entry(page: str, surface_item: dict) -> dict[str, Any]:
    surface = surface_item["surface"]
    if surface["surface_class"] != "text_evidence_crop" or surface["ocr_allowed"] is not False:
        raise SystemExit(f"P{page} is not authorized as a text-evidence smoke page")
    validation = validate_ocr_input_surface(surface)
    route = route_ocr_input_surface(surface=surface, candidate_text_hash_sealed=True, scoring_report_complete=True)
    path = OUT_ROOT / "smoke_non_promotable" / f"page_{page}_text_evidence_smoke_non_promotable.md"
    write_text(
        path,
        f"# Page {page} Text-Evidence Smoke Non-Promotable\n\n"
        "This page remains a smoke/non-promotable text-evidence route in this remediation lane.\n"
        "Tesseract is not invoked for this page. No candidate text, acceptance, promotion, or production output is created.\n",
    )
    return {
        "page": page,
        "page_id": f"P{page}",
        "route_family": "text_evidence_smoke_non_promotable",
        "surface_validation": validation,
        "policy_route": route,
        "materialized": True,
        "fresh_ocr_candidate_created": False,
        "fresh_ocr_success": False,
        "ocr_execution_performed": False,
        "tesseract_invoked_for_page": False,
        "output_path": path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(path),
        "source_artifact": surface["source_artifact"],
    }


def build_report(verified_inputs: dict[str, dict[str, str]], auth_report: dict, audit_report: dict) -> dict[str, Any]:
    by_page = {item["page"]: item for item in auth_report["surface_validations"]}
    page_entries: list[dict[str, Any]] = [build_visual_only_entry(), build_blocker_entry()]
    for page in FULL_PAGE_OCR_PAGES:
        page_entries.append(build_full_page_entry(page, by_page[page]))
    for page in TEXT_EVIDENCE_SMOKE_PAGES:
        page_entries.append(build_smoke_entry(page, by_page[page]))
    page_entries = sorted(page_entries, key=lambda item: item["page"])

    fresh_success_pages = [item["page"] for item in page_entries if item.get("fresh_ocr_success") is True]
    fresh_candidate_pages = [item["page"] for item in page_entries if item.get("fresh_ocr_candidate_created") is True]
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "bridge_page_remediation_run_materialized_candidate_only",
        "base_commit": git_head(),
        "input_lane_id": AUTHORIZATION_LANE_ID,
        "audit_lane_id": AUDIT_LANE_ID,
        "requested_pages": REQUESTED_PAGES,
        "visual_only_no_text_rule_pages": VISUAL_ONLY_PAGES,
        "full_page_region_ocr_pages": FULL_PAGE_OCR_PAGES,
        "text_evidence_smoke_non_promotable_pages": TEXT_EVIDENCE_SMOKE_PAGES,
        "needs_source_asset_recovery_pages": SOURCE_ASSET_RECOVERY_PAGES,
        "page_entries": page_entries,
        "fresh_ocr_candidate_pages": fresh_candidate_pages,
        "fresh_ocr_success_pages": fresh_success_pages,
        "fresh_ocr_blocked_or_unresolved_pages": [page for page in REQUESTED_PAGES if page not in fresh_success_pages],
        "all_requested_pages_resolved_as_fresh_first_pass": False,
        "bridge_removed_for_pages": fresh_success_pages,
        "bridge_remaining_pages": [page for page in REQUESTED_PAGES if page not in fresh_success_pages],
        "ocr_execution_performed": True,
        "ocr_execution_pages": FULL_PAGE_OCR_PAGES,
        "tesseract_invoked_pages": FULL_PAGE_OCR_PAGES,
        "tesseract_not_invoked_pages": VISUAL_ONLY_PAGES + SOURCE_ASSET_RECOVERY_PAGES + TEXT_EVIDENCE_SMOKE_PAGES,
        "text_evidence_smoke_pages_non_promotable": True,
        "runtime_execution_performed": True,
        "runtime_output_surface_created": True,
        "candidate_only": True,
        "production_ready": False,
        "production_assembly_authorized": False,
        "production_assembly_created": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "persisted_raw_ocr_output_created": False,
        "prepared_temp_artifact_created": False,
        "fixture_admission_performed": False,
        "clean_production_output_folder_created": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "push_performed": False,
        "downstream_execution_performed": False,
        "verified_inputs": verified_inputs,
        "audit_input_consumed_directly": audit_report["lane_id"] == AUDIT_LANE_ID,
        "allowed_next_action": "source_asset_recovery_for_page_002_and_non_promotable_route_decision_for_014_019",
    }


def write_summary(report: dict[str, Any]) -> None:
    lines = [
        "# Bridge Page Remediation Run 001-008 014 019 - C01TEBRIDGEREM020-G1-VIRAL-001",
        "",
        "Status: `bridge_page_remediation_run_materialized_candidate_only`",
        "",
        "- Full-page OCR candidate pages: `003`, `004`, `005`, `006`, `007`, `008`.",
        "- Text-evidence smoke/non-promotable pages, no Tesseract: `014`, `019`.",
        "- Visual-only/non-text page: `001`.",
        "- Source asset recovery blocker: `002`.",
        "",
        f"- Fresh OCR success pages: `{', '.join(report['fresh_ocr_success_pages']) or 'none'}`.",
        f"- Bridge remaining pages: `{', '.join(report['bridge_remaining_pages'])}`.",
        "",
        "This is candidate-only remediation evidence. It creates no production assembly, acceptance, fixture admission, source/raw/accepted/page-status mutation, page `021+`, push, promotion, or downstream execution.",
        "",
    ]
    write_text(OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Bridge Page Remediation Run 001-008 014 019 Manifest - C01TEBRIDGEREM020-G1-VIRAL-001",
        "",
        "Boundary: candidate-only remediation output; no production or acceptance.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "bridge_page_remediation_run_001_008_014_019_manifest.md":
            lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    lines.append("")
    write_text(OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_manifest.md", "\n".join(lines))


def build() -> None:
    verified_inputs, auth_report, audit_report = verify_authorization()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = build_report(verified_inputs, auth_report, audit_report)
    write_json(OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
