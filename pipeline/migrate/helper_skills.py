"""Build kb/skills/ from the web helper's reference_skills.json, checked against the Keeper Rulebook skill list (R-25).

Usage: python pipeline/migrate/helper_skills.py
"""
import json, sys, os, re

HELPER = r"C:\_Hobby\_work\git_coc\web_helper_coc_gm\public\docs\reference\data\reference_skills.json"
OUT = r"C:\_Hobby\_work\Sorceforge\kb\skills"
BOOK = "keeper-rulebook-ru"
LIST_REF = "«Книга хранителя», «Список навыков», с. 54 (физ. 51)"
REASON = "значение по «Книге хранителя»"

helper = {r["id"]: r for r in json.load(open(HELPER, encoding="utf-8"))}


def base(raw):
    raw = raw.strip()
    if raw == "половина ЛВК":
        return {"raw": raw, "value": None, "formula": "half_dex"}
    if raw == "ОБР":
        return {"raw": raw, "value": None, "formula": "edu"}
    if raw == "разное":
        return {"raw": raw, "value": None, "formula": "varies"}
    m = re.fullmatch(r"(\d+)%", raw)
    assert m, raw
    return {"raw": raw, "value": int(m.group(1)), "formula": None}


def sp(ru, en, raw=None):
    d = {"name": {"ru": ru, "en": en}}
    if raw:
        d["base"] = base(raw)
    return d


# slug: (en name, book base raw, physical page of description, uncommon, era)
BOOK_DATA = {
    "anthropology": ("Anthropology", "01%", 52, False),
    "archaeology": ("Archaeology", "01%", 52, False),
    "artillery": ("Artillery", "01%", 52, True),
    "accounting": ("Accounting", "05%", 53, False),
    "fighting": ("Fighting", "разное", 53, False),
    "ride": ("Ride", "05%", 53, False),
    "locksmith": ("Locksmith", "01%", 54, False),
    "spot-hidden": ("Spot Hidden", "25%", 54, False),
    "explosives": ("Demolitions", "01%", 54, True),
    "drive-auto": ("Drive Auto", "20%", 55, False),
    "survival": ("Survival", "10%", 55, False),
    "hypnosis": ("Hypnosis", "01%", 55, True),
    "natural-world": ("Natural World", "10%", 55, False),
    "intimidate": ("Intimidate", "15%", 56, False),
    "art-craft": ("Art/Craft", "05%", 57, False),
    "history": ("History", "05%", 58, False),
    "climb": ("Climb", "20%", 58, False),
    "fast-talk": ("Fast Talk", "05%", 58, False),
    "sleight-of-hand": ("Sleight of Hand", "10%", 58, False),
    "disguise": ("Disguise", "05%", 59, False),
    "medicine": ("Medicine", "01%", 59, False),
    "throw": ("Throw", "20%", 60, False),
    "mechanical-repair": ("Mechanical Repair", "10%", 60, False),
    "cthulhu-mythos": ("Cthulhu Mythos", "00%", 60, False),
    "science": ("Science", "01%", 61, False),
    "charm": ("Charm", "15%", 62, False),
    "animal-handling": ("Animal Handling", "05%", 63, True),
    "occult": ("Occult", "05%", 63, False),
    "navigate": ("Navigate", "10%", 63, False),
    "appraise": ("Appraise", "05%", 64, False),
    "first-aid": ("First Aid", "30%", 64, False),
    "pilot": ("Pilot", "01%", 64, False),
    "swim": ("Swim", "20%", 65, False),
    "diving": ("Diving", "01%", 65, True),
    "jump": ("Jump", "20%", 66, False),
    "psychoanalysis": ("Psychoanalysis", "01%", 66, False),
    "psychology": ("Psychology", "10%", 66, False),
    "library-use": ("Library Use", "20%", 67, False),
    "computer-use": ("Computer Use", "05%", 67, False),
    "stealth": ("Stealth", "20%", 68, False),
    "listen": ("Listen", "20%", 68, False),
    "credit-rating": ("Credit Rating", "00%", 68, False),
    "firearms": ("Firearms", "разное", 69, False),
    "lore": ("Lore", "01%", 69, True),
    "persuade": ("Persuade", "10%", 69, False),
    "heavy-machinery": ("Operate Heavy Machinery", "01%", 70, False),
    "dodge": ("Dodge", "половина ЛВК", 70, False),
    "read-lips": ("Read Lips", "01%", 70, True),
    "track": ("Track", "10%", 71, False),
    "electronics": ("Electronics", "01%", 71, False),
    "electrical-repair": ("Electrical Repair", "10%", 71, False),
    "law": ("Law", "05%", 71, False),
    "language-other": ("Language (Other)", "01%", 72, False),
    "language-own": ("Language (Own)", "ОБР", 73, False),
}

MODERN = {"computer-use", "electronics"}


def printed(phys):
    # PDF lacks printed page 65: offset +3 up to physical 61, +4 from physical 62.
    return phys + 3 if phys <= 61 else phys + 4


SPECS = {
    "fighting": [
        sp("Драка", "Brawl", "25%"), sp("Бензопила", "Chainsaw", "10%"),
        sp("Копьё", "Spear", "20%"), sp("Меч", "Sword", "20%"),
        sp("Топор", "Axe", "15%"), sp("Удавка", "Garrote", "15%"),
        sp("Хлыст", "Whip", "05%"), sp("Цеп", "Flail", "10%"),
    ],
    "firearms": [
        sp("Винтовка/дробовик", "Rifle/Shotgun", "25%"), sp("Лук", "Bow", "15%"),
        sp("Огнемёт", "Flamethrower", "10%"), sp("Пистолет", "Handgun", "20%"),
        sp("Пистолет-пулемёт", "Submachine Gun", "15%"), sp("Пулемёт", "Machine Gun", "10%"),
        sp("Тяжёлое вооружение", "Heavy Weapons", "10%"),
    ],
    "science": [
        sp("Астрономия", "Astronomy", "01%"), sp("Биология", "Biology", "01%"),
        sp("Ботаника", "Botany", "01%"), sp("Геология", "Geology", "01%"),
        sp("Зоология", "Zoology", "01%"), sp("Инженерия", "Engineering", "01%"),
        sp("Криминалистика", "Forensics", "01%"), sp("Криптография", "Cryptography", "01%"),
        sp("Математика", "Mathematics", "10%"), sp("Метеорология", "Meteorology", "01%"),
        sp("Фармакология", "Pharmacy", "01%"), sp("Физика", "Physics", "01%"),
        sp("Химия", "Chemistry", "01%"),
    ],
    "art-craft": [
        sp("Актёрская игра", "Acting", "05%"), sp("Изобразительное искусство", "Fine Art", "05%"),
        sp("Подделка", "Forgery", "05%"), sp("Фотография", "Photography", "05%"),
        sp("Балет", None, "05%"), sp("Гончарное ремесло", "Pottery", "05%"),
        sp("Каллиграфия", "Calligraphy", "05%"), sp("Кулинария", "Cooking", "05%"),
        sp("Народные танцы", None, "05%"), sp("Оперное пение", "Opera Singing", "05%"),
        sp("Парикмахерское искусство", "Barber", "05%"), sp("Писательство", "Literature", "05%"),
        sp("Плотничество", "Carpentry", "05%"), sp("Скульптура", "Sculpting", "05%"),
        sp("Стеклодув", None, "05%"), sp("Художник-оформитель", None, "05%"),
    ],
    "survival": [
        sp("Пустыня", "Desert", "10%"), sp("Море", "Sea", "10%"),
        sp("Полярные области", "Arctic", "10%"), sp("Лес", "Forest", "10%"),
        sp("Горы", "Mountains", "10%"),
    ],
    "pilot": [
        sp("Лодка", "Boat", "01%"), sp("Самолёт", "Aircraft", "01%"),
        sp("Дирижабль", "Airship", "01%"),
    ],
    "language-other": [
        sp("Английский", "English", "01%"), sp("Латынь", "Latin", "01%"),
        sp("Арабский", "Arabic", "01%"), sp("Французский", "French", "01%"),
        sp("Немецкий", "German", "01%"),
    ],
    "lore": [
        sp("Сновидения", "Dream Lore", "01%"), sp("«Некрономикон»", "Necronomicon Lore", "01%"),
        sp("НЛО", "UFO Lore", "01%"), sp("Вампиры", "Vampire Lore", "01%"),
        sp("Оборотни", "Werewolf Lore", "01%"), sp("Яддит", "Yaddith Lore", "01%"),
    ],
}

NAME_FIX = {"track": "Чтение следов"}

EXTRA_ALIASES = {
    "credit-rating": ["Кредитный рейтинг"],
    "track": ["Слежение"],
    "language-other": ["Язык, иностранный"],
    "language-own": ["Язык, родной"],
}
DROP_ALIASES = {"Spot Hidden", "Fast Talk"}  # English names live in name.en
SKIP_NOTES = {"Необычный или редкий навык в большинстве кампаний."}

SPEC_CORRECTIONS = {
    "fighting": [{
        "field": "specializations",
        "from": "Драка, Топор, Меч, Удавка, Цеп, Хлыст, Бензопила",
        "to": "добавлено Копьё (20%)",
        "reason": REASON, "ref": LIST_REF,
    }],
    "science": [{
        "field": "specializations",
        "from": "Астрономия, Биология, Ботаника, Геология, Криптография, Математика, Фармакология, Физика, Химия (без баз)",
        "to": "добавлены Зоология, Инженерия, Криминалистика, Метеорология; базы 01%, Математика 10%",
        "reason": REASON, "ref": LIST_REF,
    }],
    "survival": [{
        "field": "specializations[Арктика]",
        "from": "Арктика", "to": "Полярные области",
        "reason": REASON, "ref": "«Книга хранителя», с. 58 (физ. 55)",
    }],
    "pilot": [{
        "field": "specializations",
        "from": "Самолёт, Корабль, Лодка, Вертолёт",
        "to": "Лодка, Самолёт, Дирижабль",
        "reason": REASON + " (вертолёт — класс воздушных судов внутри Пилотирования (самолёт))",
        "ref": "«Книга хранителя», с. 68–69 (физ. 64–65)",
    }],
    "track": [{
        "field": "name.ru", "from": "Слежение", "to": "Чтение следов",
        "reason": REASON, "ref": LIST_REF,
    }],
    "animal-handling": [{
        "field": "uncommon", "from": None, "to": "true",
        "reason": REASON, "ref": LIST_REF,
    }],
    "firearms": [{
        "field": "specializations[Винтовка/Дробовик].name.ru",
        "from": "Винтовка/Дробовик", "to": "Винтовка/дробовик",
        "reason": REASON, "ref": LIST_REF,
    }],
}

NEW = {
    "art-craft": {
        "ru": "Искусство/ремесло", "category": "техника",
        "desc": "Умение создавать и чинить вещи или произведения в выбранной области — от "
                "актёрской игры и живописи до плотницкого дела; позволяет также изготовлять копии "
                "и подделки, узнавать происхождение предмета и его автора.",
        "examples": ["Сделать правдоподобную копию письма.", "Определить школу и мастера картины."],
    },
    "hypnosis": {
        "ru": "Гипноз", "category": "медицина",
        "desc": "Погружение согласной цели в транс: под гипнозом она внушаема и может вспомнить "
                "забытое. Используется и для лечения психических травм, фобий и маний; "
                "противодействие — Психология или МОЩ.",
        "examples": ["Помочь свидетелю вспомнить подробности ночного происшествия."],
    },
    "lore": {
        "ru": "Тайные знания", "category": "знания",
        "desc": "Знания в узкой необычной области, недоступной обычному человеку (сновидения, "
                "НЛО, вампиры и т. п.); каждую область берут отдельной специализацией.",
        "examples": ["Вспомнить, что известно о похищениях людей пришельцами."],
    },
    "read-lips": {
        "ru": "Чтение по губам", "category": "восприятие",
        "desc": "Позволяет понять, о чём говорят люди, не слыша их, если губы говорящего "
                "видны; также даёт беззвучно общаться с тем, кто владеет навыком.",
        "examples": ["Разобрать разговор за окном кафе."],
    },
    "diving": {
        "ru": "Подводное плавание", "category": "движение",
        "desc": "Обращение со снаряжением для погружений, ориентирование под водой, "
                "подбор балласта и действия в чрезвычайных ситуациях на глубине.",
        "examples": ["Спуститься к затонувшему судну в водолазном скафандре."],
    },
}


def build(slug):
    en, raw, phys, unc = BOOK_DATA[slug]
    rec = {
        "schema": "sourcefold.skill.v0",
        "id": f"coc:skill:{slug}",
        "kind": "skill",
    }
    corrections = list(SPEC_CORRECTIONS.get(slug, []))
    if slug in helper:
        h = helper[slug]
        ru = NAME_FIX.get(slug, h["title"])
        aliases = [a for a in h.get("aliases", []) if a not in DROP_ALIASES]
        category = h["category"]
        desc = h["use"].strip()
        notes = [n for n in h.get("notes", []) if n not in SKIP_NOTES]
        if slug == "explosives":
            notes = ["Последствия краха особенно опасны."]
        if notes:
            desc = desc + " " + " ".join(notes)
        examples = list(h.get("examples", []))
        if h["base"].strip() != raw:
            corrections.insert(0, {"field": "base", "from": h["base"], "to": raw,
                                   "reason": REASON, "ref": LIST_REF})
    else:
        n = NEW[slug]
        ru, aliases, category, desc, examples = n["ru"], [], n["category"], n["desc"], n["examples"]
    if slug == "fighting":
        b = helper["fighting-brawl"]
        assert b["base"] == "25%"
        aliases += [a for a in b.get("aliases", []) if a not in aliases and a != "Драка"]
        examples += [e for e in b.get("examples", []) if e not in examples]
    for a in EXTRA_ALIASES.get(slug, []):
        if a not in aliases:
            aliases.append(a)
    rec["name"] = {"ru": ru, "en": en}
    if aliases:
        rec["aliases"] = aliases
    rec["base"] = base(raw)
    rec["category"] = category
    rec["uncommon"] = unc
    if slug in SPECS:
        rec["specializations"] = SPECS[slug]
    rec["axes"] = {"era": ["modern"] if slug in MODERN else ["any"], "ruleset": "core"}
    rec["description"] = {"ru": desc, "en": None}
    if examples:
        rec["examples"] = examples
    rec["sources"] = [{"book_id": BOOK, "physical_page": phys, "printed_page": printed(phys),
                       "method": "book_text", "verified": True}]
    if corrections:
        rec["corrections"] = corrections
    return rec


def main():
    missing = set(helper) - set(BOOK_DATA) - {"fighting-brawl"}
    assert not missing, missing
    os.makedirs(OUT, exist_ok=True)
    for slug in BOOK_DATA:
        rec = build(slug)
        with open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(rec, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(len(BOOK_DATA), "written")


main()
