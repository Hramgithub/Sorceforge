from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
IMAGES_ROOT = TRIAL_ROOT / "images"

SEQUENTIAL_RUN_AUTHORIZATION_ID = "BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001"
SEQUENTIAL_RUN_PAGE_IDS = ("016", "017", "018", "019", "020")


@dataclass(frozen=True)
class HumanReviewAsset:
    page: str
    role: str
    path: Path
    required_for_human_review: bool

    def as_posix(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def page_id(page: int | str) -> str:
    if isinstance(page, str) and page.isdigit():
        return page.zfill(3)
    if isinstance(page, int):
        return f"{page:03d}"
    raise ValueError(f"unsupported page id: {page!r}")


def semantic_map_path(page: int | str) -> Path:
    pid = page_id(page)
    return (
        TRIAL_ROOT
        / f"page_{pid}_semantic_text_map_G1_VIRAL_001"
        / f"page_{pid}_semantic_text_map.md"
    )


def source_page_path(page: int | str) -> Path:
    pid = page_id(page)
    return IMAGES_ROOT / f"page_{pid}.png"


def human_review_assets_for_page(page: int | str) -> tuple[HumanReviewAsset, HumanReviewAsset]:
    pid = page_id(page)
    return (
        HumanReviewAsset(pid, "source_page_art", source_page_path(pid), True),
        HumanReviewAsset(pid, "semantic_text_map_md", semantic_map_path(pid), True),
    )


def sequential_aggressive_run_pages(start: int | str = "016", end: int | str = "020") -> tuple[str, ...]:
    start_id = page_id(start)
    end_id = page_id(end)
    pages = tuple(f"{page:03d}" for page in range(int(start_id), int(end_id) + 1))
    if pages != SEQUENTIAL_RUN_PAGE_IDS:
        raise ValueError("sequential aggressive review packet is currently bounded to pages 016-020 only")
    return pages


def human_review_packet_for_sequential_run() -> dict:
    pages = sequential_aggressive_run_pages()
    assets = [asset for page in pages for asset in human_review_assets_for_page(page)]
    return {
        "authorization_id": SEQUENTIAL_RUN_AUTHORIZATION_ID,
        "pages": list(pages),
        "human_review_policy": "source_page_art_and_semantic_text_map_only",
        "internal_evidence_policy": "crops_remain_internal_unless_blocker",
        "assets": [
            {
                "page": asset.page,
                "role": asset.role,
                "path": asset.as_posix(),
                "required_for_human_review": asset.required_for_human_review,
            }
            for asset in assets
        ],
        "guardrails": {
            "page_021_plus_processing": False,
            "whole_gate_1_acceptance": False,
            "fixture_admission": False,
            "source_acceptance_mutation": False,
            "ocr_execution": False,
            "render_execution": False,
            "pdf_parsing_or_text_layer_extraction": False,
            "raw_mutation": False,
            "translation": False,
            "proofreading": False,
            "renderer_profile_acceptance": False,
            "implementation": False,
            "push": False,
        },
    }


def assert_human_review_packet_policy(packet: dict) -> None:
    pages = packet.get("pages")
    if tuple(pages or ()) != SEQUENTIAL_RUN_PAGE_IDS:
        raise AssertionError("human review packet must cover exactly pages 016-020")
    assets = packet.get("assets", [])
    if len(assets) != len(SEQUENTIAL_RUN_PAGE_IDS) * 2:
        raise AssertionError("human review packet must expose exactly source page and semantic map per page")
    roles_by_page: dict[str, set[str]] = {page: set() for page in SEQUENTIAL_RUN_PAGE_IDS}
    for asset in assets:
        page = asset.get("page")
        role = asset.get("role")
        path = asset.get("path", "")
        if page not in roles_by_page:
            raise AssertionError(f"unexpected page in review packet: {page}")
        roles_by_page[page].add(role)
        if "review_assets/" in path or "crop" in path.lower():
            raise AssertionError("crop assets must remain internal unless a blocker requires escalation")
        if not (ROOT / path).exists():
            raise AssertionError(f"required human review asset is missing: {path}")
    for page, roles in roles_by_page.items():
        if roles != {"source_page_art", "semantic_text_map_md"}:
            raise AssertionError(f"page {page} review assets must be source art + semantic map only")
