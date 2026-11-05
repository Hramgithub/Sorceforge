"""Local viewer server: serves app/ and lets the map edit mode save to kb (Р-160).

Only for the owner's machine: listens on 127.0.0.1. The deployed site is static and never saves.

  GET  /api/ping                   {"ok": true} — the viewer shows «Сохранить в базу» only when this answers
  POST /api/map-save  {id, spots}  the map's spots are replaced; the previous file goes to
                                   .cache/backups/maps/<map>-<YYYYMMDD-HHMMSS>.json; tools/check.py runs on the
                                   file (on errors the previous file comes back); the viewer is rebuilt
  POST /api/map-undo  {id}         the latest backup of the map comes back (the current file is backed up first)

Commits stay with the lead: a save changes files in kb/ and app/ only.

Usage: python tools/kb_server.py [--port 8765]
"""
from __future__ import annotations

import argparse
import datetime
import json
import shutil
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kblib import KB, ROOT, read, write  # noqa: E402

BACKUPS = ROOT / ".cache" / "backups" / "maps"


def map_file(map_id: str) -> Path:
    for p in (KB / "maps").glob("*.json"):
        if read(p).get("id") == map_id:
            return p
    raise LookupError(f"нет карты {map_id}")


def backup(p: Path) -> Path:
    BACKUPS.mkdir(parents=True, exist_ok=True)
    # microseconds keep two saves within one second apart; the names sort in time order
    b = BACKUPS / f"{p.stem}-{datetime.datetime.now():%Y%m%d-%H%M%S-%f}.json"
    shutil.copyfile(p, b)
    return b


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


def save(body: dict) -> dict:
    p = map_file(body["id"])
    rec = read(p)
    spots = [{k: s[k] for k in ("label", "x", "y", "target", "text", "printed", "note") if k in s} for s in body["spots"] if s.get("target")]
    # the viewer keeps the order of the spots and adds new ones at the end; one correction per changed spot
    old = rec["spots"]
    if len(spots) < len(old):
        return {"ok": False, "message": "метки пропали — сохранение отменено; обновите страницу"}
    where = lambda s: f"{s['label']}: {s['x']}, {s['y']}"
    fixes = [{"field": f"spots.{i}", "from": where(a), "to": where(b), "reason": "метка передвинута или изменена владельцем в просмотрщике", "ref": "Р-160"}
             for i, (a, b) in enumerate(zip(old, spots)) if a != b]
    fixes += [{"field": f"spots.{i}", "from": None, "to": f"{where(s)} → {s['target']}", "reason": "метка добавлена владельцем в просмотрщике", "ref": "Р-160"}
              for i, s in enumerate(spots[len(old):], len(old))]
    if not fixes:
        return {"ok": True, "message": "изменений нет"}
    moved, added = len(fixes) - (len(spots) - len(old)), len(spots) - len(old)
    b = backup(p)
    rec["spots"] = spots
    rec.setdefault("corrections", []).extend(fixes)
    write(p, rec)
    check = run("tools/check.py", str(p))
    if check.returncode:
        shutil.copyfile(b, p)
        return {"ok": False, "message": "проверка не прошла, прежняя карта возвращена", "check": check.stdout[-2000:]}
    build = run("tools/build_viewer.py")
    note = "" if build.returncode == 0 else "; просмотрщик не пересобрался: " + build.stderr[-300:]
    return {"ok": True, "message": f"сохранено: изменено {moved}, добавлено {added}; копия прежней — {b.relative_to(ROOT).as_posix()}{note}"}


def undo(body: dict) -> dict:
    p = map_file(body["id"])
    copies = sorted(BACKUPS.glob(f"{p.stem}-*.json"))
    if not copies:
        return {"ok": False, "message": "резервных копий этой карты нет"}
    # each undo takes the newest copy away, so the next one goes one more step back
    last = copies[-1]
    shutil.copyfile(last, p)
    last.unlink()
    build = run("tools/build_viewer.py")
    note = "" if build.returncode == 0 else "; просмотрщик не пересобрался: " + build.stderr[-300:]
    return {"ok": True, "message": f"возвращена версия {last.name}; обновите страницу{note}"}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT / "app"), **kw)

    def reply(self, data: dict, code: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/ping":
            return self.reply({"ok": True})
        return super().do_GET()

    def local(self) -> bool:
        """Only the viewer on this machine may write: JSON body, and Origin (when sent) and Host of localhost."""
        port = self.server.server_address[1]
        ours = {f"http://localhost:{port}", f"http://127.0.0.1:{port}"}
        origin, host = self.headers.get("Origin"), self.headers.get("Host", "")
        return (self.headers.get("Content-Type", "").startswith("application/json")
                and (origin is None or origin in ours) and host in {f"localhost:{port}", f"127.0.0.1:{port}"})

    def do_POST(self):
        routes = {"/api/map-save": save, "/api/map-undo": undo}
        if self.path not in routes:
            return self.reply({"ok": False, "message": "нет такого адреса"}, 404)
        if not self.local():
            return self.reply({"ok": False, "message": "запрос не от просмотрщика на этом компьютере"}, 403)
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8"))
            self.reply(routes[self.path](body))
        except Exception as e:  # the owner sees the reason in the viewer
            self.reply({"ok": False, "message": str(e)}, 500)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()
    print(f"просмотрщик: http://localhost:{a.port}/kb.html")
    ThreadingHTTPServer(("127.0.0.1", a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
