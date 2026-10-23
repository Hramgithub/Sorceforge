"""Create skill records for creature-only skills (R-48, R-49).

One record per Malleus English term; other Russian translations printed in the
creature statblocks go to `aliases`. Descriptions come from a notes file
(jsonl: en, ru_text, explained_in_book, sources).

    python pipeline/migrate/creature_skills.py <notes.jsonl>
"""
import json
import sys

sys.path.insert(0, "pipeline/migrate")
from link_creature_skills import CREATURE, PER_CREATURE  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

# id -> (Russian name, English term)
CANON = {
    "scent-prey": ("Чутьё на добычу", "Scent Prey"),
    "sense-prey": ("Чувствовать добычу", "Sense Prey"),
    "detect-prey": ("Обнаружение добычи", "Detect Prey"),
    "spot-prey": ("Высматривание добычи", "Spot Prey"),
    "scent-blood": ("Чутьё на кровь", "Scent Blood"),
    "track-prey": ("Выслеживание добычи", "Track Prey"),
    "scent": ("Нюх", "Scent"),
    "scent-something-interesting": ("Учуять что-то интересное", "Scent Something Interesting"),
    "sense-life": ("Почувствовать жизнь", "Sense Life"),
    "sense-life-of-creator": ("Почувствовать жизнь Создателя", "Sense Life of Creator"),
    "spot-the-living": ("Почувствовать живых", "Spot the Living"),
    "sense-humans": ("Чувствовать людей", "Sense Humans"),
    "detect-humans": ("Обнаружение людей", "Detect Humans"),
    "be-annoyed": ("Раздражаться", "Be Annoyed"),
    "spit": ("Плевок", "Spit"),
    "eat-quickly": ("Быстрое поедание", "Eat Quickly"),
    "entice-lure-prey": ("Соблазнить/приманить добычу", "Entice/Lure Prey"),
    "mutter-mythos-wisdom": ("Бормотание мудрости Мифов", "Mutter Mythos Wisdom"),
    "burrow-through-rock": ("Рытьё сквозь камень", "Burrow Through Rock"),
    "dig-tunnel": ("Рыть туннели", "Dig Tunnel"),
    "telepathy": ("Телепатия", "Telepathy"),
    "spin-web": ("Пряжа паутины", "Spin Web"),
    "skulk-in-darkness": ("Скрываться во тьме", "Skulk in Darkness"),
    "make-aggressive-sounds": ("Издавать угрожающие звуки", "Make Aggressive Sounds"),
    "night-vision": ("Ночное зрение", "Night Vision"),
    "travel-to-dreamlands": ("Путешествие в Страну снов", "Travel to Dreamlands"),
    "dematerialization": ("Дематериализация", "Dematerialization"),
    "overturn-boat": ("Перевернуть лодку", "Overturn Boat"),
    "relentlessly-advance": ("Неустанно продвигаться", "Relentlessly Advance"),
    "whisper-ygolonacs-words": ("Шёпот слов Й'голонака", "Whisper Y'golonac's Words"),
    "titter-horrifically": ("Ужасное хихикание", "Titter Horrifically"),
    "choose-tasty-victim": ("Выбор аппетитной жертвы", "Choose Tasty Victim"),
    "slither-quietly": ("Бесшумно ползти", "Slither Quietly"),
    "smell-victim": ("Учуять жертву", "Smell Victim"),
    "attach-to-another-being": ("Прикрепиться к другому существу", "Attach to Another Being"),
    "scent-magic": ("Чутьё на магию", "Scent Magic"),
    "generate-spawn": ("Породить отродье", "Generate Spawn"),
}
# Compound English terms folded into one record (R-49).
EN_ALIASES = {"scent-prey": ["Scent/Spot Prey"], "scent-blood": ["Scent Blood/Prey"]}


def main():
    notes = {}
    for line in open(sys.argv[1], encoding="utf-8"):
        if line.strip():
            n = json.loads(line)
            notes[n["en"]] = n
    aliases = {k: set() for k in CANON}
    for ru, sid in list(CREATURE.items()) + [(ru, sid) for (_, ru), sid in PER_CREATURE.items()]:
        aliases[sid].add(ru)
    for sid, (ru, en) in CANON.items():
        n = notes.get(en) or {}
        srcs = []
        for t in [en] + EN_ALIASES.get(sid, []):
            srcs += (notes.get(t) or {}).get("sources") or []
        seen, sources = set(), []
        for s in srcs:
            k = (s["book_id"], s["physical_page"])
            if k not in seen:
                seen.add(k)
                sources.append({"book_id": s["book_id"], "physical_page": s["physical_page"], "printed_page": None,
                                "method": "book_text", "verified": True})
        explained = n.get("explained_in_book", False)
        rec = {
            "schema": "sourcefold.skill.v0",
            "id": "coc:skill:" + sid,
            "kind": "skill",
            "name": {"ru": ru, "en": en},
            "aliases": sorted(aliases[sid] - {ru}) + EN_ALIASES.get(sid, []),
            "base": {"raw": "—", "value": None, "formula": None},
            "category": "навыки существ",
            "axes": {"era": ["any"], "ruleset": "core"},
            "description": {"ru": n.get("ru_text") or "Навык существа; в книге не расшифрован.", "en": None},
            "sources": sources or [{"book_id": "malleus-monstrorum-1-en", "physical_page": None, "printed_page": None,
                                    "method": "book_text", "verified": False}],
            "quality": {"needs_review": False, "flags": ["translated"],
                        "notes": None if explained else "Описание выведено из названия: в книге навык не расшифрован."},
        }
        if not rec["aliases"]:
            del rec["aliases"]
        if rec["quality"]["notes"] is None:
            del rec["quality"]["notes"]
        with open(f"kb/skills/{sid}.json", "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    print(len(CANON), "creature skills written;", sum(1 for _, en in CANON.values() if en not in notes), "without notes")


if __name__ == "__main__":
    main()
