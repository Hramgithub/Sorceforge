"""Shared helpers for kb tools: the repository paths, reading and writing records in the kb format,
the record index and the choice of files to work on.

A kb record is UTF-8 JSON, 2-space indent, LF, one trailing newline (docs/conventions.md).
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "kb"
SCHEMAS = ROOT / "schemas"
ID = re.compile(r"^[a-z0-9-]+([:/][a-z0-9-]+)+$")


def dump(rec) -> str:
    return json.dumps(rec, ensure_ascii=False, indent=2) + "\n"


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, rec) -> None:
    path.write_text(dump(rec), encoding="utf-8", newline="\n")


def book_ids() -> set[str]:
    return {p.name for p in (KB / "books").iterdir() if p.is_dir()}


def is_ref(value: str, books: set[str]) -> bool:
    """A string that names a record: `coc:<kind>:<slug>` or `<book_id>/<kind>/<slug>`."""
    if not ID.match(value):
        return False
    return value.startswith("coc:") or value.split("/", 1)[0] in books


def records(root: Path = KB):
    """Every kb file as (path, record or None when it is not valid JSON)."""
    for p in sorted(root.rglob("*.json")):
        try:
            yield p, read(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            yield p, None


def index() -> dict[str, Path]:
    return {rec["id"]: p for p, rec in records() if isinstance(rec, dict) and "id" in rec}


def changed() -> list[Path]:
    """kb files changed against HEAD, staged or not, plus new files git does not track yet."""
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", "kb"],
                         cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    paths = []
    for line in out.splitlines():
        name = line[3:].split(" -> ")[-1].strip('"')
        p = ROOT / name
        if p.suffix == ".json" and p.exists():
            paths.append(p)
    return sorted(paths)


def scope_args(ap) -> None:
    """Arguments of a tool that rewrites kb files: what to touch must be said (Р-139)."""
    ap.add_argument("paths", nargs="*", help="kb files or folders")
    ap.add_argument("--changed", action="store_true", help="files changed against HEAD and new ones")
    ap.add_argument("--all", action="store_true", help="the whole kb")


def scope(ap, a) -> list[Path]:
    if not (a.paths or a.changed or a.all):
        ap.error("укажи файлы или папки, --changed или --all")
    return pick(a.paths, a.changed, a.all)


def pick(paths: list[str], use_changed: bool, use_all: bool) -> list[Path]:
    """The files a tool works on: named files and folders, the changed ones, or all of kb. Nothing by default:
    a tool that rewrites files must be told what to touch."""
    out: list[Path] = []
    for a in paths:
        p = Path(a)
        p = p if p.is_absolute() else ROOT / p
        out += sorted(p.rglob("*.json")) if p.is_dir() else [p]
    if use_changed:
        out += changed()
    if use_all:
        out += sorted(KB.rglob("*.json"))
    return sorted(set(out))
