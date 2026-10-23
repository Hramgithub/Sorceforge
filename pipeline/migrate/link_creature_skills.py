"""Link creature statblock skills to the skill reference (R-48, R-49).

The printed name and value stay as they are; only `skill` (and `specialization`
for group skills) is added. Creature-only skills point to `coc:skill:<english-slug>`
records created by `pipeline/migrate/creature_skills.py`.

    python pipeline/migrate/link_creature_skills.py [--write]
"""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

# Creature-only skills: printed Russian name -> id (one record per Malleus English term, R-49).
CREATURE = {
    "Чутьё на добычу": "scent-prey",
    "Почуять/обнаружить добычу": "scent-prey",
    "Чувствовать добычу": "sense-prey",
    "Чуять добычу": "sense-prey",
    "Обнаружение добычи": "detect-prey",
    "Высматривание добычи": "spot-prey",
    "Чутьё на кровь": "scent-blood",
    "Чуять кровь/добычу": "scent-blood",
    "Выслеживание добычи": "track-prey",
    "Нюх": "scent",
    "Чутьё": "scent",
    "Учуять что-то интересное": "scent-something-interesting",
    "Почувствовать жизнь": "sense-life",
    "Чутьё на живое": "sense-life",
    "Почувствовать жизнь Создателя": "sense-life-of-creator",
    "Почувствовать живых": "spot-the-living",
    "Чувствовать людей": "sense-humans",
    "Обнаружение людей": "detect-humans",
    "Раздражаться": "be-annoyed",
    "Плевок": "spit",
    "Быстрое поедание": "eat-quickly",
    "Соблазнить/приманить добычу": "entice-lure-prey",
    "Бормотание мудрости Мифов": "mutter-mythos-wisdom",
    "Рытьё сквозь камень": "burrow-through-rock",
    "Рыть туннели": "dig-tunnel",
    "Телепатия": "telepathy",
    "Пряжа паутины": "spin-web",
    "Скрываться во тьме": "skulk-in-darkness",
    "Издавать угрожающие звуки": "make-aggressive-sounds",
    "Ночное зрение": "night-vision",
    "Путешествие в Страну снов": "travel-to-dreamlands",
    "Дематериализация": "dematerialization",
    "Перевернуть лодку": "overturn-boat",
    "Неустанно продвигаться": "relentlessly-advance",
    "Неумолимое наступление": "relentlessly-advance",
    "Шёпот слов Й'голонака": "whisper-ygolonacs-words",
    "Ужасное хихикание": "titter-horrifically",
    "Выбор аппетитной жертвы": "choose-tasty-victim",
    "Бесшумно ползти": "slither-quietly",
    "Учуять жертву": "smell-victim",
    "Прикрепиться к другому существу": "attach-to-another-being",
    "Чутьё на магию": "scent-magic",
    "Породить отродье": "generate-spawn",
}

# Same printed name, different English term in the source (checked against Malleus / Keeper Rulebook).
PER_CREATURE = {
    ("coc:creature:bear", "Нюх"): "scent-prey",  # Keeper Rulebook: Scent Prey 70%
    ("coc:creature:child-of-shub-niggurath", "Чутьё на добычу"): "sense-prey",
    ("coc:creature:devil-s-weed-devil-plant", "Обнаружить добычу"): "detect-prey",
    ("coc:creature:fisher-from-outside", "Обнаружить добычу"): "spot-prey",
    ("coc:creature:spawn-of-ubbo-sathla", "Обнаружить добычу"): "spot-prey",
}

# Standard skills written differently: base name -> (skill id, keep parenthetical as specialization).
STANDARD = {
    "Право": ("law", False),
    "Психология человека": ("psychology", False),
    "Скрытность в воде": ("stealth", False),
    "Выслеживание": ("track", False),
    "Язык": ("language-other", True),
    "Знание снов": ("lore", "Сновидения"),
    "Знание": ("lore", True),
}
VAGUE = {"любой", "любая", "различные", "варьируется", "различные человеческие", "человеческие, варьируются"}
# One spelling per specialization; the printed name keeps the book's spelling.
SPEC_SAME = {"Глифы Р’льеха": "Глифы Р'льеха", "Наакал": "Наакаль", "Речь Глубоководных": "Речь глубоководных",
             "Вариант наакаля": "Наакаль"}


def spec_name(sid, par, specs):
    p = par.rstrip("*").strip()
    if p.lower() in VAGUE:
        return None
    p = specs.get(sid, {}).get(p.lower(), p[:1].upper() + p[1:])
    return SPEC_SAME.get(p, p)


def load_reference():
    names, specs = {}, {}
    for f in glob.glob("kb/skills/*.json"):
        d = json.load(open(f, encoding="utf-8"))
        for n in [d["name"]["ru"]] + (d.get("aliases") or []):
            names[n.lower()] = d["id"]
        specs[d["id"]] = {s["name"]["ru"].lower(): s["name"]["ru"] for s in d.get("specializations") or []}
    return names, specs


def resolve(cid, name, names, specs):
    """Return (skill id, specialization) or None."""
    if (cid, name) in PER_CREATURE:
        return "coc:skill:" + PER_CREATURE[(cid, name)], None
    if name in CREATURE:
        return "coc:skill:" + CREATURE[name], None
    m = re.match(r"^(.+?)\s*\((.+?)\)\s*(.*)$", name)
    base, par = (m.group(1).strip(), m.group(2).strip()) if m else (name.strip(), None)
    if base in STANDARD:
        sid, keep = STANDARD[base]
        sid = "coc:skill:" + sid
        if isinstance(keep, str):
            return sid, keep
        return sid, spec_name(sid, par, specs) if keep and par else None
    sid = names.get(base.lower())
    if not sid:
        return None
    return sid, spec_name(sid, par, specs) if par and specs.get(sid) else None


def main():
    write = "--write" in sys.argv
    names, specs = load_reference()
    files = sorted(glob.glob("kb/creatures/*.json") + glob.glob("kb/books/*/creatures/*.json"))
    linked = missing = changed_files = 0
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        sk = (d.get("statblock") or {}).get("skills") or []
        changed = False
        for s in sk:
            r = resolve(d["id"], s["name"], names, specs)
            if not r:
                missing += 1
                print("unresolved:", d["id"], s["name"])
                continue
            linked += 1
            sid, spec = r
            if s.get("skill") != sid or s.get("specialization") != spec:
                s["skill"] = sid
                if spec:
                    s["specialization"] = spec
                else:
                    s.pop("specialization", None)
                changed = True
        if changed and write:
            # keep key order: name, skill, specialization, value
            for i, s in enumerate(sk):
                sk[i] = {k: s[k] for k in ("name", "skill", "specialization", "value") if k in s} | {
                    k: v for k, v in s.items() if k not in ("name", "skill", "specialization", "value")}
            with open(f, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        changed_files += changed
    print(f"linked {linked}, unresolved {missing}, files {'written' if write else 'to change'}: {changed_files}")


if __name__ == "__main__":
    main()
