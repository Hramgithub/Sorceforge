"""Audit of the knowledge base: the mistakes the owner has already found once (maps, grouping of places in guides,
spoilers in captions, relations, twins of one record, orphans, place numbers named only in text).

Reads the whole base in one pass and changes nothing in kb/. Writes `report.md` and `findings.json`
(class, check, file, id, book, summary, confidence) to the output folder and prints «класс — число находок».

Usage:
  python tools/audit.py                         write to checks/<today>-audit/
  python tools/audit.py --out checks/x-audit    another folder
  python tools/audit.py --limit 200             findings shown per check in report.md (all go to findings.json)

A block between `<!-- manual:start -->` and `<!-- manual:end -->` in an existing report.md (conclusions written by
hand) is kept when the report is written again.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kblib import KB, ROOT, book_ids, is_ref, records  # noqa: E402

COMMON = "_общие"
TOPS = {"город", "корабль", "город сценария"}          # may stand without part_of (Р-163, Р-189, Р-197)
SYM = {"knows", "rival_of", "relative_of"}               # stored once (Р-114, Р-118)
SKIP_KEYS = {"id", "schema", "kind", "corrections", "errata", "sources", "quality", "images", "image"}
STRUCT = {"part_of", "arc"}                              # tree edges: not «links» for the orphan check
CONF_ORDER = {"high": 0, "medium": 1, "low": 2}

# --- the checks: class, title, what is looked for, decision, can it be fixed by a script ------------------------
CLASSES = {
    "map": "Карты",
    "grouping": "Группировка мест",
    "hint": "Подписи мест (keeper_hint)",
    "relations": "Связи",
    "twins": "Двойники (Р-154)",
    "orphans": "Сироты",
    "text_refs": "Номера мест в тексте без ссылки",
}
CHECKS = {
    # map
    "map.target_missing": ("map", "Метка ведёт на несуществующую запись", "Р-120", "авто: нет — нужна верная цель; но список короткий"),
    "map.coords": ("map", "Координаты метки вне 0–100", "Р-120", "авто: нет — положение правится в редакторе меток (Р-160)"),
    "map.location_missing": ("map", "Поле `location`/`shows` карты ведёт на несуществующую запись или не на место", "Р-120", "авто: нет"),
    "map.location_shows": ("map", "Место, которое показывает карта (`shows`), не лежит в городе карты (`location`)", "Р-120", "чтение: поправить `location` карты или `part_of` места; метки такой карты в «вне города» не повторяются"),
    "map.image_missing": ("map", "Нет файла картинки карты в `app/maps/`", "Р-120", "авто: нет — картинку надо вырезать из книги"),
    "map.no_spots": ("map", "Карта без меток (и без пометки «меток нет» в `quality.notes`)", "Р-120, Р-206", "авто: нет — метки ставятся по распознаванию и глазами"),
    "map.dup_target": ("map", "Разные метки одной карты ведут на одно место (не пара A/B, без `text`)", "Р-120, Р-155, Р-209", "авто: нет — одна из меток ведёт не туда, нужна сверка по картинке"),
    "map.dup_label": ("map", "Один и тот же номер дважды на карте, обе метки — на одно место, без `note`", "Р-120", "авто: частично — если второй кружок на карте есть, достаточно `note`"),
    "map.outside_city": ("map", "Метка карты указывает на место вне города карты (цепочка `part_of` не доходит до `location` карты)", "Р-120, Р-209", "авто: нет — либо `part_of` места, либо `location` карты"),
    "map.label_number": ("map", "Номер метки не совпадает с `number` записи, на которую она ведёт", "Р-206, Р-209", "авто: нет — ошибка либо в цели, либо в `number`"),
    "map.district_missing": ("map", "Место района с `number` без метки на карте района", "Р-209", "авто: нет — метку надо найти на картинке; иногда место стоит не в том районе"),
    "map.other_district": ("map", "Метка карты района ведёт на место другого района", "Р-209", "чтение: соседние места на краю карты района законны; проверить, не стоит ли место не в том районе"),
    # grouping
    "grouping.no_part_of": ("grouping", "Место без `part_of`, а тип не город / корабль / город сценария", "Р-163, Р-189, Р-197", "авто: нет — родителя выбирает человек"),
    "grouping.bad_part_of": ("grouping", "`part_of` на несуществующую запись, не на место или цикл", "Р-78", "авто: нет"),
    "grouping.many_environs": ("grouping", "У города больше одной области «Окрестности …»", "Р-209", "полуавто: слить области в одну, места перевесить скриптом"),
    "grouping.under_city_in_range": ("grouping", "Место с номером прямо под городом, а номер в диапазоне района", "Р-209, Р-80", "авто: да — `part_of` → район по номеру (диапазон района однозначен)"),
    "grouping.wrong_district": ("grouping", "Место с номером в районе, а номер — из диапазона другого района", "Р-209", "авто: да при однозначном диапазоне, иначе чтение"),
    "grouping.same_number": ("grouping", "Места одной книги с одинаковым `number` под одним городом", "Р-206, Р-209", "чтение: двойник или опечатка номера"),
    "grouping.empty_district": ("grouping", "Район без мест", "Р-80, Р-209", "чтение: удалить район или разнести в него места"),
    # hint
    "hint.spoiler": ("hint", "Подпись места похожа на спойлер (тайна, улика, проверка, культ, проценты, кубы)", "Р-209", "чтение: подпись переписывается в нейтральное «что это за место», остальное — в описание"),
    # relations
    "relations.sym_both": ("relations", "Симметричная связь записана в обеих карточках", "Р-114, Р-118", "авто: да — оставить одну, `note_back` взять из второй"),
    "relations.self": ("relations", "Ссылка или связь записи на саму себя", "Р-30", "авто: да — убрать"),
    "relations.dead_resident": ("relations", "В `residents` — умерший или похороненный (по словам в заметке или в описании человека)", "Р-82, Р-101", "чтение: перенос из `residents` в `refs` после проверки текста"),
    "relations.form_of_instance": ("relations", "`form_of` у именованной особи (персонаж или особь сценария) — должно быть `instance_of`", "Р-82, Р-79", "полуавто: у персонажей — замена типа; у существ книг — чтение"),
    "relations.house_named": ("relations", "Здание названо именем человека или с псевдонимом «Семья …»", "Р-82, Р-143", "чтение: новое название «Дом …», старое — в `corrections`"),
    "relations.list_dup": ("relations", "Повтор одного id в списке записи (`refs`, `residents`, `members` и т. п.)", "Р-30", "авто: да — убрать повтор (при разных `note` — объединить)"),
    # twins
    "twins.cross_book": ("twins", "Записи одного вида с одинаковым названием в разных книгах (или книга + общая), без `same_as`", "Р-154, Р-80, Р-99", "чтение: общая запись или законное совпадение имён (Р-99)"),
    "twins.same_book": ("twins", "Записи одного вида с одинаковым названием внутри одной книги", "Р-154", "чтение: слить или переименовать"),
    # orphans
    "orphans.isolated": ("orphans", "Сюжетная запись книги, на которую никто не ссылается и которая сама никуда не ссылается", "Р-128, Р-132", "чтение: привязать к сцене/месту или убрать"),
    "orphans.unused": ("orphans", "Документ, предмет или организация книги, на которые никто не ссылается (сами ссылаются только на место или людей)", "Р-128, Р-133", "чтение: найти сцену или шаг сценария, где его дают, и сослаться оттуда"),
    # text refs
    "text_refs.number": ("text_refs", "В описании места или сцены назван номер места того же города, а ссылки на это место нет", "Р-30, Р-78", "полуавто: добавить id в `refs` по номеру (числа из 3+ цифр почти всегда верны)"),
}

HINT_WORDS = [
    ("тайн", r"тайн"), ("секрет", r"секрет"), ("на самом деле", r"на\s+самом\s+деле"), ("культист", r"культист"),
    ("улик", r"улик"), ("проверк", r"проверк"), ("если сыщики", r"если\s+сыщик"), ("убийц", r"убийц"),
    ("скрывает", r"скрыва[ею]т"), ("Мифов", r"мифов"), ("Рассудок", r"рассуд"), ("процент", r"\d+\s*%"),
    ("кубы", r"\b\d*d\d+\b"),
]
HINT_RE = [(w, re.compile(p, re.I)) for w, p in HINT_WORDS]
DEAD_RE = re.compile(r"похоронен|могил(?!ьщи)|мертв|мёртв|покойн|умер|погиб", re.I)
# the state of the person: «похоронен», «мёртв», «покойный», «умер(ла)» as whole words
DEAD_SELF = re.compile(r"(?<![А-Яа-яЁё])(похоронен[аы]?|мертв[аы]?|мёртв[аы]?|покойн(ый|ая)|умер(ла)?|погиб(ла)?|скончал(ся|ась))(?![А-Яа-яЁё])", re.I)
NUM_RE = re.compile(r"^\s*([A-Za-z]{0,3})\s*-?\s*(\d{1,4})\s*-?\s*([A-Za-z]?)\s*$")
LABEL_NUM = re.compile(r"^[A-Za-z]{0,3}\s*-?\s*\d{1,4}\s*-?\s*[A-Za-zА-Яа-я]?$")
AB = re.compile(r"^(.*\d)[\s\-]*[A-Ba-bАБаб]$")
NO_SPOTS_NOTE = re.compile(r"мет(ок|ки)\s+нет|нет\s+(ни\s+)?(мет|номер|подпис)|номеров[^.;]{0,40}нет|без\s+(мет|номер)", re.I)
# «(412)», «(№ 16)», «(412, 413)»; ranges «(3–5)» are counts and hours more often than places
PAREN_NUMS = re.compile(r"\((?:№\s*)?(\d{1,4}[A-Za-z]?(?:\s*(?:,|и)\s*\d{1,4}[A-Za-z]?)*)\)")
# «место 412»; a bare «№» names handouts and clues too often («Улика № 2»), «раздел 3» — a chapter of the book
WORD_NUMS = re.compile(r"(?<![А-Яа-яЁё])мест[оаеуы]?\s+(?:№\s*)?(\d{1,4}[A-Za-z]?)(?![\d%dдк]|\s*[–\-]\s*\d)", re.I)
HOUSE_OK = re.compile(r"^(Дом|Хижина|Квартира|Особняк|Поместье|Усадьба|Коттедж|Ферма|Лавка|Магазин|Склад|Контора|Офис|"
                      r"Комнат|Пансион|Бунгало|Вилла|Лачуга|Хибар|Ранчо|Хутор|Замок|Мастерская|Студия|Логово|Убежище)", re.I)
SMALL = {"и", "де", "ван", "фон", "ибн", "аль", "ле", "да", "дю", "ла", "о", "мак", "мс", "мисс", "миссис", "мистер", "доктор", "профессор"}


def norm_name(s) -> str:
    if not isinstance(s, str):
        return ""
    s = s.lower().replace("ё", "е")
    s = re.sub(r"[«»\"„“”'’`]", "", s)
    s = re.sub(r"[.,;:!?]+$", "", s.strip())
    return re.sub(r"\s+", " ", s).strip()


def norm_label(s: str) -> str:
    m = NUM_RE.match(s or "")
    if not m:
        return re.sub(r"[\s\-]", "", (s or "").upper())
    return f"{m.group(1).upper()}{int(m.group(2))}{m.group(3).upper()}"


def digits(s: str) -> str:
    m = re.search(r"\d+", s or "")
    return str(int(m.group(0))) if m else ""


def number_forms(num: str) -> set[str]:
    """Labels a record's number may be printed as: «7, 8, 9», «1–3», «425-A» → 425, «OS115» → 115."""
    out = set()
    for part in re.split(r"\s*[,;/]\s*|\s+и\s+", num or ""):
        r = re.fullmatch(r"\s*([A-Za-z]{0,3})(\d+)\s*[–\-]\s*\1?(\d+)\s*", part)
        if r and 0 <= int(r.group(3)) - int(r.group(2)) < 50:
            out |= {f"{r.group(1).upper()}{n}" for n in range(int(r.group(2)), int(r.group(3)) + 1)}
            out |= {str(n) for n in range(int(r.group(2)), int(r.group(3)) + 1)}
            continue
        out |= {norm_label(part), digits(part)}
        base = AB.match(part.strip())
        if base:
            out.add(norm_label(base.group(1)))
    return out - {""}


def parse_num(s):
    m = NUM_RE.match(s or "") if isinstance(s, str) else None
    return (m.group(1).upper(), int(m.group(2)), m.group(3).upper()) if m else None


def bucket(s):
    p = parse_num(s)
    return (p[0], p[1] // 100) if p and p[1] >= 100 else None


def bucket_text(b) -> str:
    return f"{b[0]}{b[1] * 100}–{b[0]}{b[1] * 100 + 99}"


def text_of(v) -> str:
    if isinstance(v, dict):
        return v.get("ru") or ""
    return v if isinstance(v, str) else ""


class Audit:
    def __init__(self):
        self.books = book_ids()
        self.recs: dict[str, dict] = {}
        self.path: dict[str, Path] = {}
        self.findings: list[dict] = []
        for p, r in records():
            if isinstance(r, dict) and isinstance(r.get("id"), str):
                self.recs[r["id"]] = r
                self.path[r["id"]] = p
        self.locs = {i: r for i, r in self.recs.items() if r.get("kind") == "location"}
        self.kids: dict[str, list[str]] = defaultdict(list)
        for i, r in self.locs.items():
            if r.get("part_of"):
                self.kids[r["part_of"]].append(i)
        # every reference of every record: (source, top field, target); incoming index
        self.out: dict[str, list[tuple[str, str]]] = defaultdict(list)
        self.inc: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for i, r in self.recs.items():
            for key, v in r.items():
                if key in SKIP_KEYS:
                    continue
                for path, t in self._refs(v, key):
                    self.out[i].append((path, t))
                    self.inc[t].append((i, path))
        self._chain: dict[str, list[str]] = {}

    def _refs(self, v, path):
        if isinstance(v, str):
            if is_ref(v, self.books):
                yield path, v
        elif isinstance(v, list):
            for x in v:
                yield from self._refs(x, path)
        elif isinstance(v, dict):
            for k, x in v.items():
                yield from self._refs(x, f"{path}.{k}")

    # --- helpers ---------------------------------------------------------------------------------------------
    def book(self, i: str) -> str:
        p = self.path.get(i)
        if p is None:
            return COMMON
        parts = p.relative_to(KB).parts
        return parts[1] if parts[0] == "books" else COMMON

    def src_books(self, i: str) -> set[str]:
        return {s.get("book_id") for s in self.recs.get(i, {}).get("sources") or [] if isinstance(s, dict)} | {self.book(i)}

    def rel(self, i: str) -> str:
        p = self.path.get(i)
        return p.relative_to(ROOT).as_posix() if p else ""

    def name(self, i: str) -> str:
        r = self.recs.get(i) or {}
        n = r.get("name") or {}
        return (n.get("ru") or n.get("en") or i) if isinstance(n, dict) else str(n)

    def chain(self, i: str) -> list[str]:
        """The place itself and its ancestors by part_of; stops at a cycle or a missing record."""
        if i in self._chain:
            return self._chain[i]
        out, seen, cur = [], set(), i
        while cur and cur not in seen and cur in self.locs:
            seen.add(cur)
            out.append(cur)
            cur = self.locs[cur].get("part_of")
        self._chain[i] = out
        return out

    def top(self, i: str) -> str | None:
        c = self.chain(i)
        return c[-1] if c and not self.locs[c[-1]].get("part_of") else None

    def ltype(self, i: str):
        return (self.locs.get(i) or {}).get("location_type")

    def add(self, check: str, i: str, summary: str, conf: str, **extra):
        cls = CHECKS[check][0]
        f = {"class": cls, "check": check, "book": self.book(i) if i in self.recs else COMMON, "file": self.rel(i),
             "id": i, "name": self.name(i), "summary": summary, "confidence": conf}
        f.update({k: v for k, v in extra.items() if v not in (None, "", [])})
        self.findings.append(f)

    # --- 1. maps ---------------------------------------------------------------------------------------------
    def zone_of(self, i: str, city: str | None) -> str | None:
        """The district (район, or a numbered область right under the city) a place lies in."""
        for a in self.chain(i)[1:] if i in self.locs else []:
            if self.is_zone(a):
                return a
        return None

    def is_zone(self, a: str) -> bool:
        r = self.locs.get(a) or {}
        t = r.get("location_type")
        return t == "район" or (t == "область" and self.ltype(r.get("part_of")) in TOPS and bool(r.get("number")))

    def maps(self):
        for mid, m in self.recs.items():
            if m.get("kind") != "map":
                continue
            city, shows = m.get("location"), m.get("shows")
            for fld, v in (("location", city), ("shows", shows)):
                if v and v not in self.locs:
                    self.add("map.location_missing", mid, f"`{fld}` = {v}: такой записи места нет", "high")
            if city in self.locs and shows in self.locs and city not in self.chain(shows):
                top = self.top(shows)
                self.add("map.location_shows", mid,
                         f"карта показывает «{self.name(shows)}» (город по `part_of` — {self.name(top) if top else 'нет'}), а `location` — «{self.name(city)}»",
                         "medium", target=shows)
            img = m.get("image")
            if img and not (ROOT / "app" / img).exists():
                self.add("map.image_missing", mid, f"нет файла app/{img}", "high")
            spots = m.get("spots") or []
            notes = (m.get("quality") or {}).get("notes") or ""
            if not spots and not NO_SPOTS_NOTE.search(notes):
                self.add("map.no_spots", mid, "меток нет, пометки «меток нет» тоже", "medium")
            stype = self.ltype(shows)
            big = stype in ("город", "район", "область", "город сценария")
            by_target: dict[str, list[dict]] = defaultdict(list)
            for s in spots:
                t, lab = s.get("target"), s.get("label", "")
                if t not in self.recs:
                    self.add("map.target_missing", mid, f"метка «{lab}» → {t}: записи нет", "high", target=t)
                    continue
                x, y = s.get("x"), s.get("y")
                if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and 0 <= x <= 100 and 0 <= y <= 100):
                    self.add("map.coords", mid, f"метка «{lab}»: x={x}, y={y}", "high", target=t)
                if self.recs[t].get("kind") != "location":
                    continue
                if not s.get("text"):
                    by_target[t].append(s)
                # outside the city of the map; another city on a regional map («To Hong Kong») is a fine spot
                if city in self.locs and shows and city in self.chain(shows) and city not in self.chain(t) \
                        and self.ltype(t) not in TOPS:
                    top = self.top(t)
                    self.add("map.outside_city", mid,
                             f"метка «{lab}» → «{self.name(t)}» ({t}); город записи — {self.name(top) if top else 'нет (цепочка оборвана)'}, город карты — {self.name(city)}",
                             "medium" if big else "low", target=t)
                # the number printed on the map against the number of the record
                num = self.locs[t].get("number")
                if num and t != shows and LABEL_NUM.match(lab.strip()):
                    base = AB.match(lab.strip())
                    nl = {norm_label(lab), norm_label(base.group(1)) if base else norm_label(lab), digits(lab)}
                    if not nl & number_forms(num):
                        first = ((self.locs[t].get("sources") or [{}])[0] or {}).get("book_id")
                        own = self.book(t) == self.book(mid) or first in ({self.book(mid)} | {x.get("book_id") for x in m.get("sources") or []})
                        self.add("map.label_number", mid, f"метка «{lab}» → «{self.name(t)}» с number «{num}»" +
                                 ("" if own else " (место другой книги: у карты может быть своя нумерация)"),
                                 "medium" if own else "low", target=t)
            for t, group in by_target.items():
                if len(group) < 2 or t == shows:
                    continue
                labels = [g.get("label", "") for g in group]
                bases = {norm_label(AB.match(l.strip()).group(1)) if AB.match(l.strip()) else norm_label(l) for l in labels}
                if len(bases) > 1:
                    self.add("map.dup_target", mid, f"метки {', '.join('«' + l + '»' for l in labels)} → одно место «{self.name(t)}»",
                             "medium" if big else "low", target=t)
                elif len(set(labels)) == 1 and not any(g.get("note") for g in group):
                    self.add("map.dup_label", mid, f"«{labels[0]}» ×{len(labels)} → «{self.name(t)}»", "low", target=t)
            # a district map: its places with numbers all on it, places of other districts not (Р-209)
            if shows in self.locs and self.is_zone(shows):
                self.district_map(mid, m, shows, spots)

    def district_map(self, mid, m, d, spots):
        targets = [s["target"] for s in spots if s.get("target") in self.locs]
        covered = set()
        for t in targets:
            covered.update(self.chain(t))
        db = self.zone_bucket.get(d)
        mbooks = {s.get("book_id") for s in m.get("sources") or []} | {self.book(mid)}
        cands = []
        for k in self.kids.get(d, []):
            cands.append(k)
            if self.ltype(k) == "область":
                cands += self.kids.get(k, [])
        for k in cands:
            num = self.locs[k].get("number")
            if not num or k in covered:
                continue
            if db is not None:
                if bucket(num) != db:
                    continue
            elif not (self.src_books(k) & mbooks):
                continue
            self.add("map.district_missing", mid, f"«{self.name(k)}» ({num}) — в районе «{self.name(d)}», метки на карте района нет",
                     "medium", target=k)
        for s in spots:
            t = s.get("target")
            if t not in self.locs or d in self.chain(t):
                continue
            z = self.zone_of(t, None)
            if z and z != d:
                self.add("map.other_district", mid, f"метка «{s.get('label')}» → «{self.name(t)}» из района «{self.name(z)}»",
                         "low", target=t)

    # --- 2. grouping -----------------------------------------------------------------------------------------
    def zones(self):
        """Number range of each district by the hundreds of its places' numbers (Innsmouth 700 → 700–799)."""
        self.zone_bucket: dict[str, tuple] = {}
        self.city_zones: dict[str, dict[tuple, str]] = defaultdict(dict)
        for d, r in self.locs.items():
            if not self.is_zone(d):
                continue
            own = bucket(r.get("number"))
            nums = []
            for k in self.kids.get(d, []):
                nums.append(self.locs[k].get("number"))
                if self.ltype(k) == "область":
                    nums += [self.locs[g].get("number") for g in self.kids.get(k, [])]
            bs = Counter(b for b in map(bucket, nums) if b)
            b = None
            if own and own[1] * 100 == parse_num(r.get("number"))[1]:
                b = own
            elif bs:
                cand, n = bs.most_common(1)[0]
                if n >= 3 and n / sum(bs.values()) >= 0.7:
                    b = cand
            if b:
                self.zone_bucket[d] = b
        for d, b in self.zone_bucket.items():
            city = self.locs[d].get("part_of")
            if city in self.city_zones and b in self.city_zones[city]:
                self.city_zones[city][b] = None      # two districts claim one range: not reliable
            else:
                self.city_zones[city][b] = d

    def grouping(self):
        environs = defaultdict(list)
        same_num = defaultdict(list)
        for i, r in self.locs.items():
            t, p = r.get("location_type"), r.get("part_of")
            if not p:
                if t not in TOPS:
                    self.add("grouping.no_part_of", i, f"тип «{t}», `part_of` нет", "high")
            elif p not in self.recs:
                self.add("grouping.bad_part_of", i, f"`part_of` = {p}: записи нет", "high")
            elif p not in self.locs:
                self.add("grouping.bad_part_of", i, f"`part_of` = {p}: это не место ({self.recs[p].get('kind')})", "high")
            elif i in self.chain(p):
                self.add("grouping.bad_part_of", i, "цикл: " + " → ".join(self.chain(p)[:6]), "high")
            if p in self.locs and self.ltype(p) in TOPS and t == "область" and norm_name(r["name"].get("ru")).startswith("окрестност"):
                environs[p].append(i)
            num = r.get("number")
            b = bucket(num)
            if num and p in self.locs:
                # a numbered place right under a city that has districts by ranges
                if self.ltype(p) in TOPS and b and not self.is_zone(i) and self.city_zones.get(p, {}).get(b):
                    d = self.city_zones[p][b]
                    self.add("grouping.under_city_in_range", i,
                             f"№ {num} прямо под городом «{self.name(p)}», а диапазон {bucket_text(b)} — район «{self.name(d)}»",
                             "high", target=d)
                z = self.zone_of(i, None)
                if z and b and z in self.zone_bucket and b != self.zone_bucket[z]:
                    city = self.locs[z].get("part_of")
                    other = self.city_zones.get(city, {}).get(b)
                    if other and other != z and self.ltype(p) in ("район", "область"):
                        self.add("grouping.wrong_district", i,
                                 f"№ {num} в районе «{self.name(z)}» ({bucket_text(self.zone_bucket[z])}), а по номеру — «{self.name(other)}»",
                                 "high", target=other)
                if self.ltype(p) in TOPS | {"район", "область"}:
                    top = self.top(i)
                    if top:
                        same_num[(sorted(self.src_books(i) - {COMMON})[0] if self.src_books(i) - {COMMON} else COMMON,
                                  top, norm_label(num))].append(i)
        for city, areas in environs.items():
            if len(areas) > 1:
                self.add("grouping.many_environs", city,
                         f"{len(areas)} областей «Окрестности…»: " + "; ".join(f"«{self.name(a)}» ({a})" for a in sorted(areas)), "high")
        for (bk, top, num), ids in same_num.items():
            if len(ids) < 2:
                continue
            ids.sort()
            # maps number their keys separately (Masks: Harlem 1–30, Greater New York 1–33): one number on
            # different maps is fine; on one map — two places under one number
            on = {x: {s for s, p in self.inc.get(x, []) if p.startswith("spots")} for x in ids}
            seen_on = Counter(mp for v in on.values() for mp in v)
            shared = {mp for mp, n in seen_on.items() if n > 1}
            if all(on.values()) and not shared:
                continue
            conf = "high" if shared else "medium"
            where = f"; на одной карте: {', '.join(sorted(shared))}" if shared else "; не все стоят на картах"
            self.add("grouping.same_number", ids[0],
                     f"№ {num} в книге {bk}, город «{self.name(top)}»: " + "; ".join(f"«{self.name(x)}» ({self.rel(x)})" for x in ids) + where,
                     conf, others=ids[1:])
        for i, r in self.locs.items():
            if r.get("location_type") == "район" and not self.kids.get(i):
                self.add("grouping.empty_district", i, f"район в «{self.name(r.get('part_of'))}» без мест", "medium")

    # --- 3. hints --------------------------------------------------------------------------------------------
    def hints(self):
        for i, r in self.recs.items():
            h = r.get("keeper_hint")
            if not isinstance(h, str) or not h.strip():
                continue
            hits = [w for w, rx in HINT_RE if rx.search(h)]
            if hits:
                conf = "medium" if len(hits) > 1 or {"процент", "кубы", "на самом деле", "если сыщики"} & set(hits) else "low"
                self.add("hint.spoiler", i, f"[{', '.join(hits)}] {h}", conf, words=hits)

    # --- 4. relations ----------------------------------------------------------------------------------------
    def relations(self):
        sym = {}
        char_tokens = set()
        for i, r in self.recs.items():
            if r.get("kind") == "character":
                # first and last word of a personal name of 2–3 capitalised words («Абигейл Марш»), not group names
                words = [w for w in text_of(r.get("name")).split() if w.lower() not in SMALL]
                if 2 <= len(words) <= 3 and all(re.fullmatch(r"[А-ЯЁ][а-яё]{2,}(-[А-ЯЁ][а-яё]+)?", w) for w in words):
                    char_tokens.update({words[0], words[-1]})
        stems = {w for w in char_tokens if len(w) >= 5}
        for i, r in self.recs.items():
            # self links
            for path in sorted({p for p, t in self.out.get(i, []) if t == i}):
                if path.startswith("opposed_by"):
                    continue                      # a skill opposed by itself is a rule, not a loop (Р-47)
                self.add("relations.self", i, f"`{path}` ссылается на саму запись",
                         "low" if path.startswith("tables") else "high")
            # symmetric relations stored twice
            for rel in r.get("relations") or []:
                if not isinstance(rel, dict):
                    continue
                ty, t = rel.get("type"), rel.get("target")
                if ty in SYM and t:
                    key = (ty, i, t)
                    back = (ty, t, i)
                    if back in sym:
                        self.add("relations.sym_both", i, f"`{ty}` записана и здесь, и в «{self.name(t)}» ({self.rel(t)})", "high", target=t)
                    sym[key] = True
                if ty == "form_of" and t:
                    if r.get("kind") == "character":
                        self.add("relations.form_of_instance", i, f"персонаж: `form_of` → «{self.name(t)}»", "high", target=t)
                    elif r.get("kind") == "creature" and self.book(i) != COMMON:
                        self.add("relations.form_of_instance", i, f"существо книги: `form_of` → «{self.name(t)}» — особь или разновидность?", "low", target=t)
            # duplicates inside one list
            for key, v in r.items():
                if key in SKIP_KEYS or key == "spots" or not isinstance(v, list):
                    continue                      # several spots on one place are the map checks' business
                self.list_dups(i, key, v)
                if key == "steps":
                    for n, st in enumerate(v):
                        if isinstance(st, dict) and isinstance(st.get("refs"), list):
                            self.list_dups(i, f"steps[{n}].refs", st["refs"])
            if r.get("kind") != "location":
                continue
            # the dead among residents
            for res in r.get("residents") or []:
                rid, note = res.get("id"), res.get("note") or ""
                who = self.recs.get(rid) or {}
                if DEAD_RE.search(note):
                    self.add("relations.dead_resident", i, f"житель «{self.name(rid)}»: заметка «{note}»", "medium", target=rid)
                elif who.get("kind") == "character":
                    txt = text_of(who.get("description")) + " " + text_of(who.get("legend"))
                    m = DEAD_SELF.search(txt)
                    if m:
                        a, b = max(0, m.start() - 60), min(len(txt), m.end() + 60)
                        self.add("relations.dead_resident", i, f"житель «{self.name(rid)}»: «…{txt[a:b].strip()}…»",
                                 "medium" if m.start() < 150 else "low", target=rid)
            # a house named after a person
            if r.get("location_type") == "здание":
                nm = text_of(r.get("name"))
                fam = [a for a in r.get("aliases") or [] if isinstance(a, str) and re.match(r"(?i)^семья\s", a)]
                words = nm.replace("«", " ").replace("»", " ").split()
                first = words[0] if words else ""
                person = (nm.lower().startswith("семья") or
                          ("«" not in nm and not HOUSE_OK.match(nm) and first[:1].isupper() and
                           not re.search(r"(ый|ий|ой|ая|яя|ое|ее|ые|ие)$", first) and
                           (first in char_tokens or first[:-1] in stems or first[:-2] in stems)
                           and all(w[:1].isupper() or w.lower() in SMALL for w in words)))
                if person:
                    self.add("relations.house_named", i, f"название «{nm}»", "medium")
                if fam:
                    self.add("relations.house_named", i, f"псевдонимы с именами людей: {', '.join('«' + a + '»' for a in fam)}", "medium")

    def list_dups(self, i, key, v):
        ids = []
        for x in v:
            if isinstance(x, str) and is_ref(x, self.books):
                ids.append(x)
            elif isinstance(x, dict):
                for f in ("id", "location", "target"):
                    if isinstance(x.get(f), str) and is_ref(x[f], self.books):
                        # relations of different types to one target are fine (Р-90)
                        tag = x.get("type") or x.get("specialization")
                        ids.append(f"{x[f]} ({tag})" if tag else x[f])
                        break
        c = Counter(ids)
        dup = [k for k, n in c.items() if n > 1]
        if dup:
            self.add("relations.list_dup", i, f"`{key}`: " + ", ".join(f"{k} ×{c[k]}" for k in dup), "high")

    # --- 5. twins --------------------------------------------------------------------------------------------
    def twins(self):
        groups = defaultdict(list)
        for i, r in self.recs.items():
            k = r.get("kind")
            if k in ("term", "map"):
                continue
            n = r.get("name") or {}
            extra = ""
            if k == "location":
                p = r.get("part_of")
                if self.ltype(p) in ("здание", "корабль"):
                    continue                          # rooms of different houses share names
                extra = self.top(i) or ""
            for lang in ("ru", "en"):
                v = norm_name(n.get(lang)) if isinstance(n, dict) else ""
                if len(v) >= 3:
                    groups[(k, lang, v, extra)].append(i)
        seen_pairs = set()
        for (k, lang, v, extra), ids in groups.items():
            if len(ids) < 2:
                continue
            key = tuple(sorted(ids))
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
            linked = self.linked_components(ids)
            if len(linked) < 2:
                continue
            # a record of another era or ruleset is its own record by design (Р-02, Р-183: pulp-<slug> beside the core one)
            axes = Counter(self.axes(x) for x in ids)
            if max(axes.values()) < 2:
                continue
            ids = [x for x in ids if axes[self.axes(x)] > 1]
            by_book = defaultdict(list)
            for x in ids:
                by_book[self.book(x)].append(x)
            listing = "; ".join(f"{x} ({self.book(x)})" for x in sorted(ids))
            other_links = self.other_links(ids)
            # scenes and scenarios always belong to their book: one name in two books is not a twin
            if len(by_book) > 1 and k not in ("scene", "scenario"):
                if k == "character":
                    # Р-99: equal names of different books are not twins by themselves; a full name in the same
                    # place-and-time (or a common record) is worth a look
                    conf = "medium" if COMMON in by_book or len(v.split()) >= 2 else "low"
                elif k in ("item", "handout"):
                    conf = "low"
                else:
                    conf = "medium"
                if other_links:
                    conf = "low"
                self.add("twins.cross_book", sorted(ids)[0], f"{k} «{v}» ({lang}) в {len(by_book)} книгах: {listing}" +
                         (f"; уже связаны: {other_links}" if other_links else ""), conf, others=sorted(ids)[1:], kind=k)
            for bk, xs in by_book.items():
                if len(xs) < 2 or len(self.linked_components(xs)) < 2 or self.other_links(xs):
                    continue                          # pulp occupation → core one, Masks profile → species: by design
                if k == "scene" and len({(self.recs[x].get("arc") or {}).get("scenario") for x in xs}) == len(xs):
                    continue                          # «Начало» of two scenarios of one book
                self.add("twins.same_book", sorted(xs)[0], f"{k} «{v}» ({lang}) ×{len(xs)}: " + "; ".join(sorted(xs)),
                         "medium" if k in ("character", "creature", "organization", "item", "scene") else "low",
                         others=sorted(xs)[1:], kind=k)

    def axes(self, i):
        ax = self.recs[i].get("axes") or {}
        return (str(ax.get("era")), str(ax.get("ruleset")))

    def linked_components(self, ids):
        """Groups of the ids joined by same_as (either side)."""
        parent = {x: x for x in ids}

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for x in ids:
            for t in self.recs[x].get("same_as") or []:
                if t in parent:
                    parent[find(x)] = find(t)
        return {find(x) for x in ids}

    def other_links(self, ids) -> str:
        s = set(ids)
        out = []
        for x in ids:
            for path, t in self.out.get(x, []):
                if t in s and t != x and not path.startswith("same_as"):
                    out.append(f"{path}")
        return ", ".join(sorted(set(out)))

    # --- 6. orphans ------------------------------------------------------------------------------------------
    def orphans(self):
        for i, r in self.recs.items():
            k = r.get("kind")
            if k not in ("scene", "item", "handout", "organization", "location") or self.book(i) == COMMON:
                continue
            outs = [p for p, t in self.out.get(i, []) if p.split(".")[0] not in STRUCT and t != i]
            ins = [(s, p) for s, p in self.inc.get(i, []) if s != i and p.split(".")[0] not in STRUCT]
            if k == "location" and self.kids.get(i):
                continue
            if not outs and not ins:
                tail = f"место в «{self.name(r.get('part_of'))}»" if k == "location" else k
                if k == "scene":
                    tail += f", сценарий {(r.get('arc') or {}).get('scenario')}"
                self.add("orphans.isolated", i, f"{tail}: ни входящих, ни исходящих ссылок", "medium" if k != "location" else "low")
            elif not ins and k in ("handout", "item", "organization"):
                to = sorted({t for p, t in self.out.get(i, []) if t != i})
                self.add("orphans.unused", i, f"{k}: ни сцена, ни сценарий, ни другая запись на него не ссылаются; сам ведёт на {len(to)} записей "
                         f"({', '.join(to[:3])}{'…' if len(to) > 3 else ''})", "low")

    # --- 7. numbers in text ----------------------------------------------------------------------------------
    def text_refs(self):
        self.drawn = defaultdict(list)            # place → maps that show it
        for mid, m in self.recs.items():
            if m.get("kind") == "map" and m.get("shows"):
                self.drawn[m["shows"]].append(mid)
        by_city = defaultdict(lambda: defaultdict(list))
        for i, r in self.locs.items():
            num = r.get("number")
            p = r.get("part_of")
            if num and self.ltype(p) in TOPS | {"район", "область"} and self.top(i):
                by_city[self.top(i)][norm_label(num)].append(i)
        for i, r in self.recs.items():
            k = r.get("kind")
            if k not in ("location", "scene"):
                continue
            txt = text_of(r.get("description"))
            if not txt:
                continue
            if k == "location":
                cities = {self.top(i)} - {None}
            else:
                cities = {self.top(w.get("location")) for w in r.get("where") or [] if isinstance(w, dict)} - {None}
            cities = {c for c in cities if c in by_city}
            nums = []
            for m in PAREN_NUMS.finditer(txt):
                nums += [(n, m) for n in re.findall(r"\d{1,4}[A-Za-z]?", m.group(1))]
            nums += [(m.group(1), m) for m in WORD_NUMS.finditer(txt)]
            linked = {t for _, t in self.out.get(i, [])}
            mine = set(self.chain(i)) if k == "location" else set()
            # small numbers («комната (7)») are keys of a map: look for them only on the maps where this place,
            # its building or the scene's place stand; numbers from 100 up — guide numbers of the whole city
            # the nearest map drawn for the place (or the scene's place) or for one of its ancestors
            bases = [i] if k == "location" else [w.get("location") for w in r.get("where") or [] if isinstance(w, dict)]
            near, direct = defaultdict(set), set()
            for base in bases:
                ch = self.chain(base)
                for depth, x in enumerate(ch):
                    drawn = self.drawn.get(x)
                    if drawn:
                        for mp in drawn:
                            for s in self.recs[mp].get("spots") or []:
                                if s.get("target") in self.locs:
                                    lab = norm_label(s.get("label", ""))
                                    near[lab].add(s["target"])
                                    if depth <= 1:
                                        direct.add(lab)
                        break
            done = set()
            for n, m in nums:
                nl = norm_label(n)
                pn = parse_num(n)
                if nl in done or not pn:
                    continue
                if pn[1] >= 100:
                    cands = {x for c in cities for x in by_city[c].get(nl, [])
                             if self.book(x) == COMMON or self.book(x) == self.book(i) or self.book(i) in self.src_books(x)}
                else:
                    cands = near.get(nl, set())
                if not cands or cands & linked or cands & mine or any(i in self.chain(x) for x in cands):
                    continue
                done.add(nl)
                cands = sorted(cands)
                a, b = max(0, m.start() - 50), min(len(txt), m.end() + 30)
                sure = pn[1] >= 100 or (len(cands) == 1 and nl in direct)
                self.add("text_refs.number", i, f"«…{txt[a:b].strip()}…» → " + "; ".join(f"«{self.name(x)}» ({x})" for x in cands),
                         "medium" if sure else "low", target=cands[0])

    def run(self):
        self.zones()
        self.maps()
        self.grouping()
        self.hints()
        self.relations()
        self.twins()
        self.orphans()
        self.text_refs()
        self.findings.sort(key=lambda f: (list(CHECKS).index(f["check"]), f["book"], CONF_ORDER[f["confidence"]], f["file"]))


# --- report ------------------------------------------------------------------------------------------------------
def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def report(a: Audit, out: Path, limit: int) -> str:
    old = (out / "report.md").read_text(encoding="utf-8") if (out / "report.md").exists() else ""
    m = re.search(r"<!-- manual:start -->.*?<!-- manual:end -->", old, re.S)
    manual = m.group(0) if m else "<!-- manual:start -->\n<!-- manual:end -->"
    by_check = defaultdict(list)
    for f in a.findings:
        by_check[f["check"]].append(f)
    n_rec = Counter(r.get("kind") for r in a.recs.values())
    L = [f"# Ревизия базы знаний {datetime.date.today():%Y-%m-%d}", "",
         f"Скрипт `python tools/audit.py` (только чтение `kb/`); записей прочитано: {len(a.recs)} "
         f"(мест {n_rec['location']}, карт {n_rec['map']}, персонажей {n_rec['character']}, сцен {n_rec['scene']}). "
         "Все находки — в `findings.json` (класс, проверка, файл, id, суть, уверенность); здесь — первые "
         f"{limit} по каждой проверке, по книгам.", "",
         "Уверенность: **high** — нарушение правила видно из данных; **medium** — вероятная ошибка, нужен взгляд; "
         "**low** — кандидат на просмотр, много законных случаев.", "", manual, "",
         "## Сводка", "", "| Класс | Проверка | Находок | high / medium / low | Исправление |", "|---|---|---:|---|---|"]
    for cls, title in CLASSES.items():
        total = sum(len(by_check[c]) for c, v in CHECKS.items() if v[0] == cls)
        L.append(f"| **{title}** | | **{total}** | | |")
        for c, (cc, t, dec, fix) in CHECKS.items():
            if cc != cls:
                continue
            fs = by_check[c]
            cn = Counter(f["confidence"] for f in fs)
            L.append(f"| | {t} (`{c}`) | {len(fs)} | {cn['high']} / {cn['medium']} / {cn['low']} | {fix} |")
    for cls, title in CLASSES.items():
        L += ["", f"## {title}"]
        for c, (cc, t, dec, fix) in CHECKS.items():
            if cc != cls:
                continue
            fs = by_check[c]
            L += ["", f"### {t} — {len(fs)}", "", f"Проверка `{c}`; решения: {dec}. Исправление: {fix}."]
            if not fs:
                L += ["", "Находок нет."]
                continue
            books = Counter(f["book"] for f in fs)
            L += ["", "По книгам: " + ", ".join(f"{b} — {n}" for b, n in sorted(books.items())), "",
                  "| Книга | Файл | Суть | Ув. |", "|---|---|---|---|"]
            for f in fs[:limit]:
                L.append(f"| {f['book']} | `{f['file']}` | {esc(f['summary'])} | {f['confidence']} |")
            if len(fs) > limit:
                L.append(f"| … | | ещё {len(fs) - limit} — в `findings.json` | |")
    return "\n".join(L) + "\n"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default=f"checks/{datetime.date.today():%Y%m%d}-audit")
    ap.add_argument("--limit", type=int, default=150, help="findings shown per check in report.md")
    args = ap.parse_args()
    out = Path(args.out)
    out = out if out.is_absolute() else ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    a = Audit()
    a.run()
    (out / "findings.json").write_text(json.dumps(a.findings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (out / "report.md").write_text(report(a, out, args.limit), encoding="utf-8", newline="\n")
    by_cls = Counter(f["class"] for f in a.findings)
    by_chk = Counter(f["check"] for f in a.findings)
    for cls, title in CLASSES.items():
        print(f"{title} — {by_cls[cls]}")
        for c, v in CHECKS.items():
            if v[0] == cls and by_chk[c]:
                print(f"    {c} — {by_chk[c]}")
    print(f"всего — {len(a.findings)}; {out.relative_to(ROOT).as_posix()}/report.md, findings.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
