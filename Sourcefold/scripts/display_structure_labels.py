from __future__ import annotations


BODY_TEXT_ROLES = {
    "body_text",
    "main_body_text",
    "safety_warning_body",
    "special_thanks_body",
}


def is_body_text_role(semantic_role: str) -> bool:
    role = semantic_role.strip().lower()
    return role in BODY_TEXT_ROLES or role.endswith("_body")


def display_heading_label(semantic_role: str, heading_level: str) -> str:
    if heading_level == "none" and is_body_text_role(semantic_role):
        return "text_body"
    return heading_level


def format_draft_structure_semantics(semantic_role: str, heading_level: str) -> str:
    return f"Draft structure/semantics: `{semantic_role}` / `{display_heading_label(semantic_role, heading_level)}`"


def normalize_draft_structure_lines(text: str) -> str:
    replacements = {
        "Draft structure/semantics: `body_text` / `none`": "Draft structure/semantics: `body_text` / `text_body`",
        "Draft structure/semantics: `main_body_text` / `none`": "Draft structure/semantics: `main_body_text` / `text_body`",
        "Draft structure/semantics: `safety_warning_body` / `none`": "Draft structure/semantics: `safety_warning_body` / `text_body`",
        "Draft structure/semantics: `special_thanks_body` / `none`": "Draft structure/semantics: `special_thanks_body` / `text_body`",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text
