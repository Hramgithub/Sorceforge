from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_completeness_triage.py"
TEST_PATH = ROOT / "tests" / "test_page_completeness_triage.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"
SPM_REPORT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "selected_page_manifest_pages_1_20.md"
PMR_REPORT = TRIAL_ROOT / "page_map_model_report.md"
G1SRER_ROOT = TRIAL_ROOT / "gate_1_source_recon_evidence_rollup_G1_VIRAL_001"
P002_ROOT = TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
P003_ROOT = TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001"
P004_ROOT = TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "page_completeness_triage_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001"
PACKAGE_ID = "PGCT-G1-VIRAL-001"
SPM_REPORT_SHA256 = "73D6C817E54DDEFB89BA7109440E87F36B447F74C19044D154A0674AD41E3936"
PMR_REPORT_SHA256 = "72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F"
PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
G1SRER_PAYLOAD_SHA256 = "3674E136BAA0F1D62DC240FAD1C1E34FD919D56A4A7251D580106D9BEFB83380"
P002_REPORT_SHA256 = "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F"
P002_MANIFEST_SHA256 = "8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6"
P003_REPORT_SHA256 = "9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B"
P003_MANIFEST_SHA256 = "F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87"
P003_SUMMARY_SHA256 = "860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2"
P004_REPORT_SHA256 = "0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E"
P004_MANIFEST_SHA256 = "75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06"
P004_SUMMARY_SHA256 = "BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build a page completeness triage packet without accepting pages.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page completeness triage is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page completeness triage requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    verify_authorization_ledger()
    expected = {
        SPM_REPORT: SPM_REPORT_SHA256,
        PMR_REPORT: PMR_REPORT_SHA256,
        PRM_REPORT: PRM_REPORT_SHA256,
        G1SRER_ROOT / "gate_1_source_recon_evidence_rollup.json": G1SRER_PAYLOAD_SHA256,
        P002_ROOT / "p002_completion_and_next_review_report.json": P002_REPORT_SHA256,
        P002_ROOT / "p002_completion_and_next_review_manifest.md": P002_MANIFEST_SHA256,
        P003_ROOT / "p003_verified_review_acceptance_report.json": P003_REPORT_SHA256,
        P003_ROOT / "p003_verified_review_acceptance_manifest.md": P003_MANIFEST_SHA256,
        P003_ROOT / "p003_verified_review_acceptance_summary.md": P003_SUMMARY_SHA256,
        P004_ROOT / "p004_verified_review_acceptance_report.json": P004_REPORT_SHA256,
        P004_ROOT / "p004_verified_review_acceptance_manifest.md": P004_MANIFEST_SHA256,
        P004_ROOT / "p004_verified_review_acceptance_summary.md": P004_SUMMARY_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    p002 = read_json(P002_ROOT / "p002_completion_and_next_review_report.json")
    p003 = read_json(P003_ROOT / "p003_verified_review_acceptance_report.json")
    p004 = read_json(P004_ROOT / "p004_verified_review_acceptance_report.json")
    if p002["package_id"] != "P002C-G1-VIRAL-002":
        raise SystemExit("unexpected page 002 predecessor")
    if p003["package_id"] != "P003A-G1-VIRAL-003":
        raise SystemExit("unexpected page 003 predecessor")
    if p004["package_id"] != "P004A-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 predecessor")
    if p002["rollup"]["total_accepted_records"] != 9:
        raise SystemExit("unexpected page 002 rollup")
    if p003["rollup"]["total_accepted_records"] != 11:
        raise SystemExit("unexpected page 003 rollup")
    if p004["rollup"]["total_accepted_records"] != 13:
        raise SystemExit("unexpected page 004 rollup")
    return p002, p003, p004


def accepted_region_ids(report: dict[str, object]) -> set[str]:
    if report["package_id"] == "P002C-G1-VIRAL-002":
        return {"PRM-G1-VIRAL-001-P002-R01", "PRM-G1-VIRAL-001-P002-R02"}
    if report["package_id"] == "P003A-G1-VIRAL-003":
        review_to_region = {
            "SRCR-G1-VIRAL-003-R01": "PRM-G1-VIRAL-001-P003-R01",
            "SRCR-G1-VIRAL-003-R02": "PRM-G1-VIRAL-001-P003-R02",
        }
        return {review_to_region[record["review_id"]] for record in report["source_acceptance"]["accepted_records"]}
    return {record["source_region_id"] for record in report["source_acceptance"]["accepted_records"]}


def build_pages(p002: dict[str, object], p003: dict[str, object], p004: dict[str, object]) -> list[dict[str, object]]:
    details = {
        "001": {
            "plain_label": "cover/title composition",
            "classification": "incomplete",
            "covered_plain": ["accepted source-reconstruction slice exists for this page"],
            "context_only_plain": ["visual/title composition still needs a page-level completeness decision"],
            "blockers_plain": ["not accepted as page-complete"],
            "recommendation": "needs_separate_page_complete_review",
            "human_decision": "Decide later whether page 001 should enter a page-complete review packet.",
        },
        "002": {
            "plain_label": "credits/legal front matter",
            "classification": "needs_page_complete_review",
            "covered_plain": ["credits block", "boxed legal/footer block"],
            "context_only_plain": [],
            "blockers_plain": [],
            "recommendation": "ready_for_separate_page_complete_review",
            "human_decision": "Decide whether to start a separate page-complete review for page 002.",
        },
        "003": {
            "plain_label": "intro/title page",
            "classification": "needs_page_complete_review",
            "covered_plain": ["title/heading", "main body text"],
            "context_only_plain": [],
            "blockers_plain": [],
            "recommendation": "ready_for_separate_page_complete_review",
            "human_decision": "Decide whether to start a separate page-complete review for page 003.",
        },
        "004": {
            "plain_label": "warning/notice inset",
            "classification": "blocked_pending_context_only_decision",
            "covered_plain": ["WARNING title", "warning body text"],
            "context_only_plain": [
                "full tilted inset/document area; it contains the already-covered title and body and is not an independent source-text record"
            ],
            "blockers_plain": [
                "page-complete review should not start until the context-only treatment of the full inset is accepted or corrected"
            ],
            "recommendation": "hold_until_context_only_decision",
            "human_decision": "Decide whether the full tilted inset is only context, or whether it needs a separate review action.",
        },
        "005": {
            "plain_label": "contents/table-like page",
            "classification": "incomplete",
            "covered_plain": ["accepted source-reconstruction slice exists for this page"],
            "context_only_plain": ["table/list structure still needs a page-level completeness decision"],
            "blockers_plain": ["not accepted as page-complete"],
            "recommendation": "needs_separate_page_complete_review",
            "human_decision": "Decide later whether page 005 should enter a page-complete review packet.",
        },
        "006": {
            "plain_label": "introduction mixed text/image page",
            "classification": "incomplete",
            "covered_plain": ["accepted source-reconstruction slice exists for this page"],
            "context_only_plain": ["mixed image/text composition still needs a page-level completeness decision"],
            "blockers_plain": ["not accepted as page-complete"],
            "recommendation": "needs_separate_page_complete_review",
            "human_decision": "Decide later whether page 006 should enter a page-complete review packet.",
        },
    }
    for page in range(7, 21):
        page_id = f"{page:03d}"
        details[page_id] = {
            "plain_label": "selected page without source-reconstruction acceptance yet",
            "classification": "unstarted",
            "covered_plain": [],
            "context_only_plain": [],
            "blockers_plain": ["needs a separate bounded source-reconstruction slice before any page-complete review"],
            "recommendation": "needs_next_bounded_source_slice",
            "human_decision": "Do not decide page-complete yet; choose a later source-reconstruction slice when ready.",
        }

    pages = [
        {
            "page": "002",
            "expected_source_regions": {"PRM-G1-VIRAL-001-P002-R01", "PRM-G1-VIRAL-001-P002-R02"},
            "accepted_source_regions": accepted_region_ids(p002),
        },
        {
            "page": "003",
            "expected_source_regions": {"PRM-G1-VIRAL-001-P003-R01", "PRM-G1-VIRAL-001-P003-R02"},
            "accepted_source_regions": accepted_region_ids(p003),
        },
        {
            "page": "004",
            "expected_source_regions": {
                "PRM-G1-VIRAL-001-P004-R01",
                "PRM-G1-VIRAL-001-P004-R02",
                "PRM-G1-VIRAL-001-P004-R03",
            },
            "accepted_source_regions": accepted_region_ids(p004),
        },
    ]
    for page in pages:
        page.update(details[page["page"]])
        page["missing_source_regions"] = sorted(page["expected_source_regions"] - page["accepted_source_regions"] - {
            "PRM-G1-VIRAL-001-P004-R01"
        })
        page["expected_source_regions"] = sorted(page["expected_source_regions"])
        page["accepted_source_regions"] = sorted(page["accepted_source_regions"])
    detailed = {page["page"]: page for page in pages}
    result = []
    for page in range(1, 21):
        page_id = f"{page:03d}"
        result.append(detailed.get(page_id, {"page": page_id, **details[page_id]}))
    return result


def build_human_packet(pages: list[dict[str, object]]) -> str:
    page_lines = []
    for page in pages:
        label = page["plain_label"]
        classification = page["classification"].replace("_", " ")
        page_lines.append(f"- Page {page['page']}: {classification} - {label}.")

    lines = [
        "# Page Completeness Triage Packet",
        "",
        "Purpose: decide what should happen next for the selected pages 1-20.",
        "",
        "Boundary: this packet does not accept any page as complete, does not advance Gate 1, and does not admit fixtures.",
        "",
        "## Selected Pages Overview",
        "",
        *page_lines,
        "",
        "## Page 002",
        "",
        "Status: covered enough to prepare a separate page-complete review.",
        "",
        "- Covered: credits block; boxed legal/footer block.",
        "- Context-only: none identified for this triage.",
        "- Missing/blocker: none identified for this triage.",
        "- Recommended decision: allow a separate page-complete review packet for page 002.",
        "",
        "## Page 003",
        "",
        "Status: covered enough to prepare a separate page-complete review.",
        "",
        "- Covered: title/heading; main body text.",
        "- Context-only: none identified for this triage.",
        "- Missing/blocker: none identified for this triage.",
        "- Recommended decision: allow a separate page-complete review packet for page 003.",
        "",
        "## Page 004",
        "",
        "Status: hold until the full tilted inset is explicitly treated as context-only or corrected.",
        "",
        "- Covered: WARNING title; warning body text.",
        "- Context-only: full tilted inset/document area. It contains the already-covered title and body, so accepting it as a separate peer text record would duplicate/overlap the same content.",
        "- Missing/blocker: no missing text is identified if the full inset is context-only; if you disagree, page 004 needs another bounded review action.",
        "- Recommended decision: do not start page-complete review for page 004 until you accept or correct this context-only treatment.",
        "",
        "## Pages 001, 005, and 006",
        "",
        "Status: source-reconstruction evidence exists, but the pages are still incomplete.",
        "",
        "- These pages need separate page-complete review packets before they can be considered complete.",
        "- Recommended decision: do not bundle them into the first page-complete action; handle after pages 002/003 unless you want a different order.",
        "",
        "## Pages 007-020",
        "",
        "Status: not started for source-reconstruction acceptance.",
        "",
        "- These pages need later bounded source-reconstruction slices before any page-complete review.",
        "- Recommended decision: leave them parked for now.",
        "",
        "## Decision Options",
        "",
        "A concise reply is enough:",
        "",
        "- `002 first / 003 second / 004 context ok` - I prepare separate page-complete review packets in that order, with page 004 after the context-only decision.",
        "- `002 first / 003 second / 004 needs review` - I prepare page 002 and 003 page-complete review, and park page 004 for a separate bounded review.",
        "- `start with 001/005/006` - I prepare a different page-complete review order around the earlier source-reconstruction slice.",
        "- `hold all` - I stop page-complete work and we revisit the triage.",
        "",
        "Nothing in those decisions accepts the pages as complete by itself; it only chooses the next packet to prepare.",
        "",
    ]
    return "\n".join(lines)


def build() -> None:
    p002, p003, p004 = verify_predecessors()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    pages = build_pages(p002, p003, p004)
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_completeness_triage_ready_for_bogdan_decision",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "scope": "triage_only_no_page_acceptance",
        "input_packages": [
            "SPM-G1-VIRAL-001",
            "PMR-G1-VIRAL-001",
            "PRM-G1-VIRAL-001",
            "G1SRER-G1-VIRAL-001",
            "P002C-G1-VIRAL-002",
            "P003A-G1-VIRAL-003",
            "P004A-G1-VIRAL-004",
        ],
        "pages": pages,
        "recommendation": {
            "next_best_step": "prepare separate page-complete review packet for page 002 first, then page 003; hold page 004 until Bogdan confirms the full tilted inset is context-only or requests another review action; keep pages 007-020 parked until later source-reconstruction slices",
            "page_complete_acceptance_created": False,
        },
        "page_complete_acceptance": False,
        "accepted_pages_as_complete": False,
        "whole_gate_1_acceptance": False,
        "fixture_admission": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
    }
    write_json(OUT_ROOT / "page_completeness_triage_report.json", report)

    (OUT_ROOT / "page_completeness_triage_packet.md").write_text(
        build_human_packet(pages), encoding="utf-8", newline="\n"
    )
    summary = [
        "# Page Completeness Triage Summary",
        "",
        "Status: `ready_for_bogdan_decision`",
        "",
        "- Selected pages 1-20 are classified for next-step planning.",
        "- Pages 001, 005, and 006 have earlier source-reconstruction evidence but are still not page-complete.",
        "- Page 002: ready for a separate page-complete review packet.",
        "- Page 003: ready for a separate page-complete review packet.",
        "- Page 004: hold until the full tilted inset is accepted as context-only or sent through another bounded review.",
        "- Pages 007-020: not started for source-reconstruction acceptance; leave parked until later bounded slices.",
        "- No page is accepted as complete by this triage.",
        "- Whole Gate 1, fixture admission, translation, proofreading, implementation, and push remain blocked.",
        "",
    ]
    (OUT_ROOT / "page_completeness_triage_summary.md").write_text(
        "\n".join(summary), encoding="utf-8", newline="\n"
    )
    manifest = [
        "# Page Completeness Triage Manifest",
        "",
        f"Package: `{PACKAGE_ID}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_completeness_triage_manifest.md":
            manifest.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest.append("")
    (OUT_ROOT / "page_completeness_triage_manifest.md").write_text(
        "\n".join(manifest), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
