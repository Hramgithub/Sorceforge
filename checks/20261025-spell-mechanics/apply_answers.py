"""Apply the owner's answers to the spell-mechanics draft and rebuild draft.md.

draft.jsonl holds one line per spell (slug, name_ru, category, mechanic,
casting_time, why). Each answer is a rule below; resolved spells lose their
«спорное» mark (†). The «Спорные» section of draft.md is kept for the rest.

    python checks/20261025-spell-mechanics/apply_answers.py
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DIR = "checks/20261025-spell-mechanics/"
ORDER = ["мгновенное", "поддерживаемое", "ритуал"]
TITLE = {"мгновенное": "Мгновенные", "поддерживаемое": "Поддерживаемые", "ритуал": "Ритуалы"}


def r69(r):
    # Р-69: contact spells (Contact Deity / Contact monster families and their variants) are rituals
    if r["slug"].startswith("contact-") or r["slug"] in ("contact-spells", "contact-deity"):
        return "ритуал", "связь — обряд и ожидание ответа (Р-69)"


def r70(r):
    # Р-70: effect held by concentration or playing, with no further payment, is instant
    if r["slug"] in ("temporal-rip", "dampen-light", "soul-singing"):
        return "мгновенное", "плата разом; эффект держится сосредоточением без трат (Р-70)"


RULES = [r69, r70]
# numbered items of the «Спорные» section that the answers above settle
SETTLED = ["Семейства «Связь с божеством»", "Поддержание сосредоточением без трат"]


def main():
    rows = [json.loads(l) for l in open(DIR + "draft.jsonl", encoding="utf-8")]
    md = open(DIR + "draft.md", encoding="utf-8").read()
    head = md[:md.index("## Сводка")]
    disputed_sec = md[md.index("## Спорные"):] if "## Спорные" in md else ""
    disputed = {r["name_ru"] for r in rows if r["name_ru"] + " †" in md}
    for r in rows:
        for rule in RULES:
            res = rule(r)
            if res:
                r["mechanic"], r["why"] = res
                disputed.discard(r["name_ru"])
    with open(DIR + "draft.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    cats = sorted({r["category"] for r in rows}, key=lambda c: -sum(1 for r in rows if r["category"] == c))
    out = [head, "## Сводка «тип × механика»\n", "| Тип | Мгновенные | Поддерживаемые | Ритуалы | Всего |", "|---|---:|---:|---:|---:|"]
    for c in cats:
        n = [sum(1 for r in rows if r["category"] == c and r["mechanic"] == m) for m in ORDER]
        out.append(f"| {c} | {n[0]} | {n[1]} | {n[2]} | {sum(n)} |")
    t = [sum(1 for r in rows if r["mechanic"] == m) for m in ORDER]
    out += [f"| **Итого** | **{t[0]}** | **{t[1]}** | **{t[2]}** | **{sum(t)}** |", "",
            "Знак † — заклинание есть в списке «Спорные» в конце.", ""]
    for c in cats:
        out.append(f"## {c}\n")
        for m in ORDER:
            names = sorted((r["name_ru"] for r in rows if r["category"] == c and r["mechanic"] == m), key=str.lower)
            if names:
                out.append(f"- **{TITLE[m]} ({len(names)}):** " + ", ".join(n + (" †" if n in disputed else "") for n in names))
        out.append("")
    if disputed_sec:
        # drop settled numbered items and renumber the rest
        lines, k = [], 0
        for l in disputed_sec.split("\n"):
            m = re.match(r"^\d+\. (.*)$", l)
            if m:
                if any(s in l for s in SETTLED):
                    continue
                k += 1
                l = f"{k}. {m.group(1)}"
            lines.append(l)
        out.append("\n".join(lines))
    open(DIR + "draft.md", "w", encoding="utf-8", newline="\n").write("\n".join(out).rstrip() + "\n")
    print("totals", dict(zip(ORDER, t)), "disputed left", len(disputed))


if __name__ == "__main__":
    main()
