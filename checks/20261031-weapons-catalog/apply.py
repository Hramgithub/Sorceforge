"""Thin the 1920s weapons catalog down to its new mechanics (owner decision R-98, 2026-10-31).

Kept: models whose mechanic is not in the Keeper Rulebook table. Their combat numbers come from
their table position; the new mechanic is written out with parameters. Deleted: models that
only restate a table position with other numbers; their names become aliases of the position
and statblock attacks that pointed at them are relinked to the position. Out-of-combat remarks
(rare ammo, legality, concealment, accessories without rules) are dropped.
"""
import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

W = {}
for f in glob.glob("kb/weapons/*.json"):
    with open(f, encoding="utf-8") as fh:
        d = json.load(fh)
    W[d["id"]] = (f, d)

CAT = "weapons-catalog-1920s"
catalog = {i for i, (_, d) in W.items() if any(s["book_id"] == CAT for s in d["sources"])}
assert len(catalog) == 54, len(catalog)

COMBAT = ("skill", "damage", "range", "attacks", "ammo", "malfunction", "cost")
NOTE = "Модель из пользовательского каталога (Р-58), оставлена ради механики, которой нет в книге (Р-98). "


def from_table(d):
    """Copy combat numbers and price from the table position."""
    p = W[d["model_of"]][1]
    for k in COMBAT:
        if k in p:
            d[k] = json.loads(json.dumps(p[k]))
    return p


def keep(wid, description, notes, **fields):
    f, d = W["coc:weapon:" + wid]
    d.update(fields)
    d["description"] = {"ru": description, "en": None}
    d["quality"] = {"needs_review": False, "flags": ["editorial_text"], "notes": NOTE + notes}
    d.pop("corrections", None) if not d.get("corrections") else None
    d.pop("errata", None) if not d.get("errata") else None
    return d


BURN = ("Горение (правило книги, как у коктейля Молотова): цель проходит проверку Удачи, чтобы не "
        "загореться; загоревшись, в следующем раунде получает минимальный урон, и урон удваивается "
        "каждый раунд, пока огонь не потушат.")

kept = {}

d = keep("phosphorus-grenade-mk-ii",
         "Зажигательная граната с белым фосфором. Все в радиусе 8 метров получают 1d6 урона и "
         "загораются по правилу горения. Бросать можно не чаще раза в два раунда. " + BURN,
         "Механика — огонь по площади: у ручной гранаты книги нет огня, коктейль Молотова поджигает одну цель. "
         "Урон и радиус — по каталогу, горение — по правилу книги.",
         damage={"raw": "1d6 + горение / 8 метров", "dice": "1d6", "db": "none", "impaling": False},
         range="СИЛ / 5 метров", attacks="1/2", ammo="Только 1", malfunction="99", reload=None)
kept[d["id"]] = d

d = keep("gas-grenade-federal-labs-mk-v-cn",
         "Граната со слезоточивым газом CN. Облако накрывает радиус 3 метра на открытом воздухе или "
         "комнату до 6×6 метров и держится 1d6+2 раунда в помещении, 1d3 раунда на улице. Каждый, кто "
         "начинает раунд в облаке без противогаза, бросает 1d100: если выпало больше 1/5 ЛВК, он временно "
         "ослеплён и в шоке — не может действовать 1d6 раундов. Урона не наносит; действует только на "
         "людей и им подобных. Бросать можно не чаще раза в два раунда.",
         "Механика — выведение из строя по площади: в книге газовый баллончик действует на одну цель. "
         "Каталог даёт только «газ/шок, эффект решает Хранитель»; радиус, длительность облака и проверка — "
         "наше дополнение по аналогии с газовым баллончиком и ручной гранатой книги.",
         damage={"raw": "Шок / 3 метра (комната)", "dice": None, "db": "none", "impaling": False},
         range="СИЛ / 5 метров", attacks="1/2", ammo="Только 1", malfunction="99", reload=None)
kept[d["id"]] = d

d = W["coc:weapon:colt-browning-m1917-m1918-m1919"][1]
from_table(d)
d = keep("colt-browning-m1917-m1918-m1919",
         "Станковые пулемёты Colt-Browning под .30-06 с водяным охлаждением. Развёртывание: в одиночку "
         "поставить на станок, заправить кожух водой (3,3 литра) и зарядить ленту — 2d6+12 раундов; до этого "
         "стрелять нельзя. Перезарядка ленты — 2 раунда.",
         "Механика — время развёртывания: в книге пулемёт стреляет сразу. Боевые числа и цена — по позиции "
         "«Пулемёт «Браунинг» M1917A1»; развёртывание и перезарядка — по каталогу.",
         reload="2 раунда; развёртывание 2d6+12 раундов")
kept[d["id"]] = d

d = W["coc:weapon:bsa-lewis-mk-iii-savage-lewis-m1917"][1]
from_table(d)
d = keep("bsa-lewis-mk-iii-savage-lewis-m1917",
         "Ручной пулемёт Льюиса с дисковым магазином: британский BSA-Lewis Mk III под .303 British и "
         "американский Savage-Lewis M1917 под .30-06. Перед стрельбой его нужно поставить на сошки — 1 раунд. "
         "Смена диска — 1 раунд.",
         "Механика — установка на сошки: в книге пулемёт стреляет сразу. Боевые числа и цена — по позиции "
         "«Пулемёт «Льюис» Mk I»; сошки и перезарядка — по каталогу.",
         reload="1 раунд; сошки 1 раунд")
kept[d["id"]] = d

d = W["coc:weapon:flamethrower-schilt-no-3"][1]
from_table(d)
d = keep("flamethrower-schilt-no-3",
         "Ранцевый огнемёт Schilt № 3. Заправка — 5 раундов, надеть — 2 раунда, зажечь воспламенитель — "
         "1 раунд (он тлеет 9 минут), заменить воспламенитель — 2 раунда. Запаса хватает на 10 залпов по "
         "25 метров или на один залп всем запасом на 100 метров по 10 целям, каждая получает 2d6 + горение. "
         + BURN,
         "Механика — подготовка огнемёта и залп всем запасом: в книге только урон, дальность и запас. Боевые "
         "числа — по позиции «Огнемёт»; подготовка и дальний залп — по каталогу. В каталоге к урону добавлен "
         "шок — не перенесён, урон по книге.",
         reload="заправка 5 раундов")
kept[d["id"]] = d

STOCK = "Пристегнуть приклад — 1 раунд; с прикладом пистолет стреляет как карабин, базовая дальность удваивается."
for wid, text, extra in [
    ("colt-woodsman",
     "Спортивный самозарядный пистолет Colt Woodsman под .22 LR; к нему есть пристёгиваемый приклад. " + STOCK,
     {"range": "10 метров (с прикладом 20 метров)"}),
    ("dwm-luger-p04-lp08-artillerie",
     "Пистолеты «Парабеллум» DWM-Luger: флотский P.04 и артиллерийский L.P.08 с длинным стволом и "
     "пристёгиваемым прикладом; к артиллерийскому есть барабанный магазин на 32 патрона. " + STOCK,
     {"range": "15 метров (с прикладом 30 метров)", "ammo": "8 (барабанный магазин 32)"}),
    ("mauser-c96-m1930-m1932",
     "Поздние модели Mauser C96 под 7,63×25 мм с отъёмными магазинами на 10 и 20 патронов и кобурой-"
     "прикладом; M1932 может вести автоматический огонь по правилам автоматического оружия. " + STOCK,
     {"range": "15 метров (с прикладом 30 метров)", "ammo": "10 или 20", "attacks": "1 (3); M1932 — или непр. огонь"}),
]:
    d = W["coc:weapon:" + wid][1]
    p = from_table(d)
    d.update(extra)
    d = keep(wid, text,
             f"Механика — приклад-кобура превращает пистолет в карабин. Боевые числа и цена — по позиции "
             f"«{p['name']['ru']}»; приклад, магазины и автоматический огонь — по каталогу; удвоение дальности — "
             f"наше обобщение (в каталоге вторая дальность в 2–2,7 раза больше).",
             reload="1 раунд")
    kept[d["id"]] = d

d = W["coc:weapon:remington-mk-iii-very-pistol"][1]
from_table(d)
d = keep("remington-mk-iii-very-pistol",
         "Сигнальный пистолет Remington Mk III (ракетница Вери) флота США 10-го калибра. Стреляет сигнальной "
         "ракетой (урон с горением, как у ракетницы) или зарядом картечи — тогда урон и дальность как у "
         "двуствольного обреза: 4d6 на 5 метрах, 1d6 на 10 метрах, не пронзающий. " + BURN,
         "Механика — второй вид заряда: картечь. Ракета — по позиции «Пистолет сигнальный (ракетница)», "
         "картечь — по позиции «Дробовик двуствольный (обрез)».",
         damage={"raw": "1d10+1d3 горение; картечь 4d6/1d6", "dice": "1d10+1d3", "db": "none", "impaling": True},
         range="10 метров; картечь 5/10 метров", group="other", reload="1 раунд")
kept[d["id"]] = d

assert len(kept) == 9, len(kept)

# delete the rest: names -> aliases of the table position, references relinked
gone = {i: W[i][1] for i in catalog if i not in kept}
assert all(d.get("model_of") for d in gone.values())
for i, d in gone.items():
    p = W[d["model_of"]][1]
    al = p.setdefault("aliases", [])
    for n in [d["name"]["ru"], d["name"].get("en"), *d.get("aliases", [])]:
        if n and n not in al and n != p["name"]["ru"] and n != p["name"].get("en"):
            al.append(n)
relinked = 0
for f in glob.glob("kb/**/*.json", recursive=True):
    if os.path.normpath(f).startswith(os.path.normpath("kb/weapons")):
        continue
    with open(f, encoding="utf-8") as fh:
        t = fh.read()
    t2 = t
    for i, d in gone.items():
        t2 = t2.replace(f'"{i}"', f'"{d["model_of"]}"')
    if t2 != t:
        relinked += 1
        with open(f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(t2)
for i in gone:
    os.remove(W[i][0])
touched = set(kept) | {d["model_of"] for d in gone.values()}
for i in touched:
    f, d = W[i]
    with open(f, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print(f"kept {len(kept)}, deleted {len(gone)}, positions with new aliases {len(touched) - len(kept)}, files relinked {relinked}")
