from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUDIT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
REMEDIATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p014_p019_route_decision_G1_VIRAL_001"

LANE_ID = "C01TEP014019ROUTEDEC-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P014-P019-ROUTE-DECISION-001"
CREATION_HEAD = "9ea4f8ed"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
PAGES = ["014", "019"]

PINNED_INPUTS = {
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
    "C01TEBRIDGEREM020-G1-VIRAL-001.report": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_report.json",
        "6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.summary": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_summary.md",
        "3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.manifest": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_manifest.md",
        "BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5",
    ),
    "P014.page_complete_acceptance.report": (
        TRIAL_ROOT / "page_complete_acceptance_p014_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "D4F8A985DCA3E7CCAB0960B1B65719E5CF59902A29AF943F32482FFA533E6946",
    ),
    "P014.page_complete_review.report": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "page_complete_review_report.json",
        "23390659C8E41FA04413DA41D4E309C78D70C246DF9E46E443DFFD57FC1C7CB2",
    ),
    "P014.page_complete_review.manifest": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "page_complete_review_manifest.md",
        "E60723CBD7592DF78B59092812F1F54430206687EFEE4CD59736706D5199F04E",
    ),
    "P014.page_image": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "review_assets" / "page_014.png",
        "24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA",
    ),
    "P014.text_map": (
        TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "review_assets" / "page_014_text_map.md",
        "F454329B57FC3AD31455B77378D4E5642C20B8E86B6B33922077B2382C08EC66",
    ),
    "P019.page_complete_acceptance.report": (
        TRIAL_ROOT / "page_complete_acceptance_p019_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "67FCCB6B34A266EC7EC007AF656E1E162B0C6CC294F275496CC1E92B40611985",
    ),
    "P019.page_complete_review.report": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "page_complete_review_report.json",
        "61AD70E201F6654A2B99098E6B80D8D980A0A4FA4D0080A41E3BEB37B49C4B68",
    ),
    "P019.page_complete_review.manifest": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "page_complete_review_manifest.md",
        "CD797AB6AF835AC38252A98A72AB2C58921E2BAEBD272AA9ED71BCB8E15BE132",
    ),
    "P019.page_image": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "review_assets" / "page_019.png",
        "63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8",
    ),
    "P019.text_map": (
        TRIAL_ROOT / "page_complete_review_p019_G1_VIRAL_001" / "review_assets" / "page_019_text_map.md",
        "A808376F3B6BA8DAE947847394FB69172E8E0E0646287B0C0AF3370CAE635E24",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "fresh_ocr_success",
    "ocr_execution_performed",
    "tesseract_invoked",
    "render_execution_performed",
    "pdf_parsing_or_text_layer_extraction_performed",
    "accepted_text_mutation_performed",
    "semantic_text_mutation_performed",
    "page_status_mutation_performed",
    "source_or_raw_mutation_performed",
    "fixture_admission_performed",
    "production_ready",
    "production_assembly_authorized",
    "production_assembly_created",
    "acceptance_performed",
    "page_021_plus_included",
    "push_performed",
    "promotion_performed",
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "p014_p019_route_decision_report.json",
    "p014_p019_route_decision_summary.md",
    "p014_p019_route_decision_manifest.md",
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
    parser = argparse.ArgumentParser(description="Build P014/P019 first-pass route decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P014/P019 route decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P014/P019 route decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P014/P019 route decision requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def page_entry(report: dict[str, Any], page: str) -> dict[str, Any]:
    return next(item for item in report["page_entries"] if item["page"] == page)


def audit_entry(report: dict[str, Any], page: str) -> dict[str, Any]:
    return next(item for item in report["page_audit"] if item["page"] == page)


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    audit = read_json(PINNED_INPUTS["C01TEBRIDGEAUD020-G1-VIRAL-001.report"][0])
    remediation = read_json(PINNED_INPUTS["C01TEBRIDGEREM020-G1-VIRAL-001.report"][0])
    if audit["lane_id"] != "C01TEBRIDGEAUD020-G1-VIRAL-001":
        raise SystemExit("unexpected bridge audit input lane")
    if remediation["lane_id"] != "C01TEBRIDGEREM020-G1-VIRAL-001":
        raise SystemExit("unexpected bridge remediation input lane")
    if remediation["allowed_next_action"] != "source_asset_recovery_for_page_002_and_non_promotable_route_decision_for_014_019":
        raise SystemExit("bridge remediation next action drifted")
    for page in PAGES:
        audited = audit_entry(audit, page)
        remediated = page_entry(remediation, page)
        if audited["next_route"] != "fresh_ocr_route_possible":
            raise SystemExit(f"P{page} audit route drifted")
        if remediated["route_family"] != "text_evidence_smoke_non_promotable":
            raise SystemExit(f"P{page} remediation route drifted")
        if remediated["tesseract_invoked_for_page"] is not False:
            raise SystemExit(f"P{page} unexpectedly invoked Tesseract")
        if remediated["fresh_ocr_success"] is not False:
            raise SystemExit(f"P{page} unexpectedly reached fresh OCR success")
    return verified, audit, remediation


def build_page_decisions(audit: dict[str, Any], remediation: dict[str, Any]) -> list[dict[str, Any]]:
    decisions: list[dict[str, Any]] = []
    for page in PAGES:
        audited = audit_entry(audit, page)
        remediated = page_entry(remediation, page)
        decisions.append(
            {
                "page": page,
                "prior_selector_decision": audited["selector_decision"],
                "accepted_bridge_source_lane_id": audited["source_lane_id"],
                "page_image_path": audited["page_image"]["path"],
                "page_image_sha256": audited["page_image"]["sha256"],
                "text_evidence_crop_count": audited["text_evidence_crop_count"],
                "text_map_count": audited["text_map_count"],
                "remediation_route_family": remediated["route_family"],
                "remediation_smoke_output_path": remediated["output_path"],
                "remediation_smoke_output_sha256": remediated["output_sha256"],
                "smoke_non_promotable": True,
                "existing_smoke_can_clear_bridge": False,
                "existing_smoke_can_count_as_fresh_ocr_success": False,
                "full_page_image_available": True,
                "future_full_page_ocr_route_authorized": True,
                "future_route_surface_class": "full_page_region",
                "future_route_allowed_purpose": "candidate_policy",
                "fresh_ocr_success": False,
            }
        )
    return decisions


def build_report(
    verified_inputs: dict[str, dict[str, str]],
    audit: dict[str, Any],
    remediation: dict[str, Any],
) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p014_p019_route_decision_recorded_full_page_ocr_route_required_no_execution",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_ids": ["C01TEBRIDGEAUD020-G1-VIRAL-001", "C01TEBRIDGEREM020-G1-VIRAL-001"],
        "pages": PAGES,
        "verified_inputs": verified_inputs,
        "page_decisions": build_page_decisions(audit, remediation),
        "text_evidence_smoke_route_reviewed": True,
        "text_evidence_smoke_remains_non_promotable": True,
        "existing_smoke_outputs_clear_bridge": False,
        "existing_smoke_outputs_create_fresh_success": False,
        "future_full_page_ocr_route_authorized": True,
        "future_full_page_ocr_route_pages": PAGES,
        "future_full_page_ocr_route_must_be_separate_lane": True,
        "future_full_page_ocr_route_must_hash_candidate_before_reference_scoring": True,
        "future_full_page_ocr_route_may_use_text_evidence_crops_as_ocr_input": False,
        "future_full_page_ocr_route_may_accept_or_promote_without_separate_decision": False,
        "allowed_next_action": "separate_bounded_014_019_full_page_ocr_route_authorization_or_execution_lane",
    }
    for flag in FALSE_BOUNDARY_FLAGS:
        report[flag] = False
    return report


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {LANE_ID}",
            "",
            f"Status: `{report['status']}`",
            "",
            "Pages `014/019` were reviewed as parked bridge pages with existing",
            "text-evidence smoke outputs. Those outputs remain non-promotable and",
            "cannot clear bridge lineage or count as fresh OCR success.",
            "",
            "A separate bounded full-page OCR route is authorized for pages `014/019`.",
            "This lane does not execute OCR, score candidates, accept text, mutate",
            "source/page status, or authorize production.",
            "",
        ]
    )


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for name in OUTPUT_FILES:
        path = OUT_ROOT / name
        if path.exists():
            hashes[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return hashes


def build_manifest(report: dict[str, Any], hashes: dict[str, dict[str, str]]) -> str:
    lines = [
        f"# {LANE_ID} Manifest",
        "",
        f"- Authorization: `{AUTHORIZATION_ID}`",
        f"- Status: `{report['status']}`",
        "- Output policy: report/summary/manifest only; no OCR, scoring, acceptance, production, source mutation, or page 021+.",
        "",
        "## Inputs",
        "",
    ]
    for key, item in report["verified_inputs"].items():
        lines.append(f"- `{key}`: `{item['sha256']}`")
    lines.extend(["", "## Outputs", ""])
    for name, item in hashes.items():
        lines.append(f"- `{name}`: `{item['sha256']}`")
    lines.extend(
        [
            "",
            "## Decision",
            "",
            "- Existing text-evidence smoke clears bridge: `false`",
            "- Existing text-evidence smoke creates fresh OCR success: `false`",
            "- Future full-page OCR route authorized: `true`",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, audit, remediation = verify_inputs()
    report = build_report(verified_inputs, audit, remediation)
    write_json(OUT_ROOT / "p014_p019_route_decision_report.json", report)
    write_text(OUT_ROOT / "p014_p019_route_decision_summary.md", build_summary(report))
    write_text(OUT_ROOT / "p014_p019_route_decision_manifest.md", build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
