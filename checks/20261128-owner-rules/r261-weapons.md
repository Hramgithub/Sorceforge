# Р-261 — оружие из таблиц книг в справочнике

Правило владельца Р-261 (2026-11-28): оружие таблиц книг, которого нет в справочнике, заведено в `kb/weapons/` по числам книги; то, что есть под другим именем, получило вариант источника (`source_variants`, Р-124) и эпоху книги; статблоки получили ссылки. Эпохи: World War Cthulhu — `1940s-1980s`, «Ужас в Восточном экспрессе» 1923 и «Дети страха» — `1920s`, «Кроваво-красная феска» (кн. II, 1893) — `gaslight`. Скрипты — `.cache/lead-tools/apply-r261/` (`data.py` — данные, `apply.py` — запись).

Схема: у `cost` оружия добавлены ключи `gaslight` и `1940s-1980s` (цена под эпохой книги); просмотрщик показывает их в карточке, в фильтре эпох оружия добавлен «Газовый свет».

## Заведено (76)

| id | Название | Англ. | Источник | Эпоха | Позиция таблицы (`model_of`) |
|---|---|---|---|---|---|
| `colt-python` | Револьвер «Кольт» Питон | Colt Python | wwc-cold-war-en с. 149 | 1940s-1980s | `357-magnum-revolver` |
| `smith-wesson-model-60` | Револьвер «Смит-Вессон» модель 60 | Smith & Wesson Model 60 | wwc-cold-war-en с. 149 | 1940s-1980s | `38-revolver` |
| `manurhin-mr73` | Револьвер «Манурен» MR73 | Manhurin MR73 | wwc-cold-war-en с. 149 | 1940s-1980s | — |
| `star-model-b` | Пистолет «Стар» модель B | Star Model B | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `star-model-p` | Пистолет «Стар» модель P | Star Model P | wwc-cold-war-en с. 150 | 1940s-1980s | `45-automatic` |
| `walther-ppk` | Пистолет «Вальтер» PPK | Walther PPK | wwc-cold-war-en с. 150 | 1940s-1980s | `32-automatic` |
| `fn-browning-gp35` | Пистолет «ФН-Браунинг» GP35 | FN/Browning GP35 | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `psm` | Пистолет «ПСМ» | PSM | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `colt-defender` | Пистолет «Кольт» Дефендер | Colt Defender | wwc-cold-war-en с. 150 | 1940s-1980s | `45-automatic` |
| `astra-falcon` | Пистолет «Астра» Фалкон | Astra Falcon | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `mba-gyrojet` | Пистолет «МБА» Гироджет | MBA Gyrojet | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `smith-wesson-model-39` | Пистолет «Смит-Вессон» модель 39 | Smith & Wesson Model 39 | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `auto-mag` | Пистолет «Авто Маг» | Auto Mag | wwc-cold-war-en с. 150 | 1940s-1980s | — |
| `cz-75` | Пистолет «ЧЗ» 75 | CZ 75 | wwc-cold-war-en с. 150; wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `mossberg-500` | Дробовик «Моссберг» 500 | Mossberg 500 | wwc-cold-war-en с. 152 | 1940s-1980s | `shotgun-12-gauge-pump` |
| `winchester-defender` | Дробовик «Винчестер» Дефендер | Winchester Defender | wwc-cold-war-en с. 152 | 1940s-1980s | `shotgun-12-gauge-pump` |
| `remington-m870` | Дробовик «Ремингтон» M870 | Remington M870 | wwc-cold-war-en с. 152 | 1940s-1980s | `shotgun-12-gauge-pump` |
| `ithaca-37` | Дробовик «Итака» 37 | Ithaca 37 | wwc-cold-war-en с. 152 | 1940s-1980s | `shotgun-12-gauge-pump` |
| `ithaca-37-stakeout` | Дробовик «Итака» 37 «Стейкаут» | Ithaca 37 'Stakeout' | wwc-cold-war-en с. 152 | 1940s-1980s | — |
| `browning-auto-5` | Дробовик «Браунинг» Авто-5 | Browning Auto 5 | wwc-cold-war-en с. 152 | 1940s-1980s | `shotgun-12-gauge-semi-auto` |
| `atchisson-assault-shotgun` | Дробовик штурмовой «Атчиссон» | Atchisson Assault Shotgun | wwc-cold-war-en с. 152 | 1940s-1980s | — |
| `ks-23` | Карабин «КС-23» | KS-23 Special Carbine | wwc-cold-war-en с. 152 | 1940s-1980s | — |
| `vigneron` | Пистолет-пулемёт «Виньерон» | Vigneron | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `sterling-smg` | Пистолет-пулемёт «Стерлинг» | Sterling | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `cz-model-25` | Пистолет-пулемёт «ЧЗ» модель 25 | CZ Model 25 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `mat-49` | Пистолет-пулемёт «МАТ-49» | MAT-49 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `erma-mp58` | Пистолет-пулемёт «Эрма» MP58 | Erma MP58 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `beretta-m12` | Пистолет-пулемёт «Беретта» M12 | Beretta M12 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `stechkin-aps` | Пистолет «Стечкин» АПС | Stetchkin | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `heckler-koch-vp70` | Пистолет «Хеклер и Кох» VP70 | Heckler & Koch VP70 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `star-z70b` | Пистолет-пулемёт «Стар» Z70B | Star Z70B | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `ingram-m10` | Пистолет-пулемёт «Ингрэм» M10 | Ingram M10 | wwc-cold-war-en с. 154 | 1940s-1980s | — |
| `m14` | Винтовка «M14» | M14 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `m14a1` | Винтовка автоматическая «M14A1» | M14A1 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `m21` | Винтовка снайперская «M21» | M21 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `heckler-koch-g3` | Винтовка «Хеклер и Кох» G3 | Heckler & Koch G3 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `m16a1` | Автомат «M16A1» | M16A1 | wwc-cold-war-en с. 156 | 1940s-1980s | `m16a2` |
| `m40` | Винтовка снайперская «M40» | M40 | wwc-cold-war-en с. 156 | 1940s-1980s | `bolt-action-sniper-rifle` |
| `mauser-sp66` | Винтовка снайперская «Маузер» SP66 | Mauser SP66 | wwc-cold-war-en с. 156 | 1940s-1980s | `bolt-action-sniper-rifle` |
| `heckler-koch-psg1` | Винтовка снайперская «Хеклер и Кох» PSG1 | Heckler & Koch PSG1 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `heckler-koch-hk21-hk13` | Пулемёт ручной «Хеклер и Кох» HK21/HK13 | Heckler & Koch HK21/HK13 | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `stoner-weapon-system` | Система оружия «Стоунер» | Stoner Weapon System | wwc-cold-war-en с. 156 | 1940s-1980s | — |
| `glove-pistol` | Пистолет перчаточный | Glove Pistol | wwc-cold-war-en с. 160 | 1940s-1980s | — |
| `welrod` | Пистолет «Велрод» | Welrod 'Silent Pistol' | wwc-section-46-en с. 106 | 1940s-1980s | — |
| `heckler-koch-p11` | Пистолет подводный «Хеклер и Кох» P11 | Heckler & Koch P11 Underwater Pistol | wwc-section-46-en с. 106 | 1940s-1980s | — |
| `spp-1` | Пистолет подводный «СПП-1» | SPP-1 Underwater Pistol | wwc-section-46-en с. 106 | 1940s-1980s | — |
| `de-lisle-carbine` | Карабин «Де Лизл» | De Lisle Carbine | wwc-section-46-en с. 107 | 1940s-1980s | — |
| `aps-underwater-rifle` | Автомат подводный «АПС» | APS Underwater Rifle | wwc-section-46-en с. 107 | 1940s-1980s | — |
| `rpk` | Пулемёт ручной «РПК» | RPK | wwc-section-46-en с. 107 | 1940s-1980s | — |
| `fn-mag-58-l7` | Пулемёт единый «ФН» MAG 58 / L7 | FN MAG 58/L7 | wwc-section-46-en с. 108 | 1940s-1980s | — |
| `mg-3` | Пулемёт «MG 3» | MG 3 | wwc-section-46-en с. 108 | 1940s-1980s | — |
| `rpd-type-56-type-62` | Пулемёт ручной «РПД» / «Тип 56» / «Тип 62» | RPD/Type 56/Type 62 | wwc-section-46-en с. 108 | 1940s-1980s | — |
| `pkm` | Пулемёт «ПКМ» | PKM | wwc-section-46-en с. 108 | 1940s-1980s | — |
| `carl-gustav-m2` | Орудие безоткатное «Карл Густав» M2 | M2 Carl Gustav Recoilless Rifle | wwc-section-46-en с. 109 | 1940s-1980s | — |
| `heckler-koch-69a1` | Гранатомёт «Хеклер и Кох» 69A1 | H&K 69A1 Grenatpistole | wwc-section-46-en с. 109 | 1940s-1980s | — |
| `m203` | Гранатомёт подствольный «M203» | M203 Grenade Launcher | wwc-section-46-en с. 109 | 1940s-1980s | — |
| `stun-grenade` | Граната светошумовая | Stun Grenade | wwc-section-46-en с. 110 | 1940s-1980s | — |
| `smoke-grenade` | Граната дымовая | Smoke Grenade | wwc-section-46-en с. 110 | 1940s-1980s | — |
| `incendiary-grenade` | Граната зажигательная | Incendiary Grenade | wwc-section-46-en с. 110 | 1940s-1980s | — |
| `federal-riot-gun` | Ружьё «Федерал» для разгона беспорядков | Federal Riot Gun | wwc-section-46-en с. 111 | 1940s-1980s | — |
| `arwen` | Ружьё «ARWEN» | ARWEN | wwc-section-46-en с. 111 | 1940s-1980s | — |
| `schermuly-riot-gun` | Ружьё «Шермули» для разгона беспорядков | Schermuly Anti-Riot Gun | wwc-section-46-en с. 111 | 1940s-1980s | — |
| `home-guard-pike` | Пика Внутренней гвардии | Home Guard pike | wwc-london-en с. 78 | 1940s-1980s | — |
| `yatagan` | Ятаган | Yatagan | hotoe-book-2-en с. 93 | gaslight, 1920s | `sword-light` |
| `rast-gasser-m1898` | Револьвер «Раст-Гассер» M1898 | Rast-Gasser M.1898 | hotoe-book-1-en с. 33; hotoe-book-1-en с. 35 | 1920s | `32-revolver` |
| `gasser-m1870-montenegrin` | Револьвер «Гассер» M1870 «Черногорский» | Gasser M.1870 "Montenegrin" | hotoe-book-1-en с. 33 | 1920s | `45-revolver` |
| `gabilondo-ruby` | Пистолет «Габилондо» Руби | Gabilondo Ruby | hotoe-book-1-en с. 35 | 1920s | `32-automatic` |
| `mas-lebel-mle-1892` | Револьвер «Лебель» Mle 1892 | MAS-Lebel Mle 1892 | hotoe-book-1-en с. 35 | 1920s | `32-revolver` |
| `schmidt-m1882` | Револьвер «Шмидт» M1882 | W+F-Schmidt M1882 | hotoe-book-1-en с. 35 | 1920s | `32-revolver` |
| `glisenti-bodeo-1889` | Револьвер «Глизенти-Бодео» обр. 1889 | Glisenti-Bodeo Mod 1889 | hotoe-book-1-en с. 35 | 1920s | — |
| `fn-browning-mle-1903` | Пистолет «ФН-Браунинг» Mle 1903 | FN-Browning Mle 1903 | hotoe-book-1-en с. 35 | 1920s | `38-automatic` |
| `repetier-m95` | Карабин «Репетир» M95 | Repetier M95 carbine | hotoe-book-3-en с. 164 | 1920s | `30-06-bolt-action-rifle` |
| `maxim-machine-gun` | Пулемёт «Максим» | Maxim MG08/15 | hotoe-book-4-en с. 33; mts-kharkov-37-ru с. 53 | 1920s, 1930s | `vickers-303-machine-gun` |
| `22-derringer` | Дерринджер .22 | .22 Derringer | hotoe-book-5-en с. 43; hotoe-book-5-en с. 44; hotoe-book-5-en с. 23; arkham-en с. 58 | 1920s | `25-derringer` |
| `mauser-m1888-hanyang-88` | Винтовка «Маузер» M1888 / «Ханьян» 88 | Mauser M1888 / Hanyang 88 bolt-action rifle | children-of-fear-en с. 48; children-of-fear-en с. 90; children-of-fear-en с. 91 | 1920s | `30-06-bolt-action-rifle` |
| `matchlock-rifle` | Ружьё фитильное | Matchlock rifle | children-of-fear-en с. 326; children-of-fear-en с. 339 | 1920s | — |

Числа всех WWC-записей — из таблиц правил книг (`rule/revolvers`, `semi-automatic-pistols`, `shotguns`, `light-automatic-weapons`, `rifles-assault-rifles-and-light-support-weapons`, `other-equipment`; Section 46 `special-weapons-*`; London `firearms`), сверены с текстовым слоем страниц (Cold War с. 149–160, Section 46 с. 106–111, London с. 78); прочность оружия (HP) — в описании. Описания — наш перевод абзацев книги из тех же правил. Калибры, которых книга не даёт, — справочно (Р-63, пометка в `quality.notes`). Опечатки книги — `errata` (осечка «00» у «Де Лизла» и ружей для разгона беспорядков, «Type 65» у РПД, патрон ПКМ, урон M1888/«Ханьян» 1d6+1, магазины «Беретты» M12).

## Изменены записи справочника (26 правок)

| id | Что | 
|---|---|
| `ak-47-akm` | эпоха +1940s-1980s |
| `ak-74` | эпоха +1940s-1980s |
| `dragunov-rifle` | эпоха +1940s-1980s |
| `fn-fal` | эпоха +1940s-1980s |
| `heckler-koch-mp5` | эпоха +1940s-1980s |
| `makarov-pm` | эпоха +1940s-1980s |
| `ppsh-41` | эпоха +1940s-1980s |
| `skorpion-smg` | эпоха +1940s-1980s |
| `thompson-smg` | эпоха +1940s-1980s |
| `uzi-smg` | эпоха +1940s-1980s |
| `gas-grenade-federal-labs-mk-v-cn` | эпоха +1940s-1980s |
| `phosphorus-grenade-mk-ii` | эпоха +1940s-1980s |
| `law` | эпоха +1940s-1980s |
| `m60` | эпоха +1940s-1980s |
| `m79-grenade-launcher` | эпоха +1940s-1980s |
| `rpg-7` | эпоха +1940s-1980s |
| `38-revolver` | эпоха +1940s-1980s; вариант wwc-cold-war-en с. 149 |
| `m16a2` | эпоха +1940s-1980s; вариант wwc-cold-war-en с. 156; псевдонимы AR-15/M16, AR-15 |
| `hand-grenade` | эпоха +1940s-1980s; источник wwc-section-46-en с. 110; псевдонимы Граната осколочная, Fragmentation Grenade |
| `dynamite-stick` | эпоха +1940s-1980s; источник wwc-london-en с. 76; цена 1940s-1980s |
| `32-automatic` | источник hotoe-book-1-en с. 35; псевдонимы Webley MP .32 |
| `32-revolver` | вариант hotoe-book-1-en с. 35; псевдонимы Nagant M1898, Nagant M1895 |
| `luger-p08` | источник hotoe-book-1-en с. 35; псевдонимы DWM-Luger M1911 Parabellum |
| `webley-mk-vi` | источник hotoe-book-1-en с. 35 |
| `thompson-smg` | вариант hotoe-book-1-en с. 33 |
| `30-lever-action-carbine` | вариант hotoe-book-5-en с. 19; вариант hotoe-book-4-en с. 33 |

## Статблоки связаны (43 атак)

| Запись | Атака | Было | Стало |
|---|---|---|---|
| `wwc-covert-actions-en/character/arkhiv` | Makarov | — | `makarov-pm` |
| `wwc-london-en/character/reginald-fotheringay` | Handgun (Welrod Silent Pistol) | — | `welrod` |
| `wwc-section-46-en/character/eleanor-gysbers` | Browning Hi Power 9mm pistol | — | `fn-browning-gp35` |
| `wwc-section-46-en/character/laura-shelden` | Walther PPK .32 pistol | `32-automatic` | `walther-ppk` |
| `wwc-our-american-cousins-en/character/henri-nicoli` | Uzi SMG | — | `uzi-smg` |
| `wwc-our-american-cousins-en/character/henri-nicoli` | .38 (9mm) Automatic Pistol | — | `38-automatic` |
| `wwc-our-american-cousins-en/character/isobel-porter` | Skorpion SMG | — | `skorpion-smg` |
| `wwc-our-american-cousins-en/character/isobel-porter` | .32 Automatic Pistol | — | `32-automatic` |
| `wwc-our-american-cousins-en/character/chester-freedman` | .32 Automatic Pistol | — | `32-automatic` |
| `wwc-our-american-cousins-en/character/elisabetta-patana` | 7.65mm Automatic Pistol | — | `32-automatic` |
| `wwc-our-american-cousins-en/character/georges-ayala-valle` | .32 Revolver | — | `32-revolver` |
| `wwc-our-american-cousins-en/character/kim-xyooj` | .32 Revolver | — | `32-revolver` |
| `hotoe-book-2-en/character/blood-red-fez-cultists` | Yatagan | `sword-light` | `yatagan` |
| `hotoe-book-2-en/character/kapok` | Yatagan | `sword-light` | `yatagan` |
| `hotoe-book-2-en/character/menkaphs-thugs` | Yatagan | `sword-light` | `yatagan` |
| `hotoe-book-2-en/character/turkish-policeman-1893` | Yatagan | `sword-light` | `yatagan` |
| `hotoe-book-4-en/character/aziz-bin-nassar` | Yataghan Knife | — | `yatagan` |
| `hotoe-book-4-en/character/israa-bin-nassar` | Yataghan Knife | — | `yatagan` |
| `hotoe-book-4-en/character/henri-de-bruessy` | 8mm Lebel Revolver | — | `mas-lebel-mle-1892` |
| `hotoe-book-4-en/character/christova-task-force` | Nagant M1895 Revolver | — | `32-revolver` |
| `hotoe-book-4-en/character/butchers` | Maxim MG08/15 | — | `maxim-machine-gun` |
| `hotoe-book-4-en/character/danton-szorbic` | 9mm automatic | — | `38-automatic` |
| `hotoe-book-3-en/character/branko-jankovic` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-3-en/character/branko-jankovic` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-3-en/character/mihael-loncar` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-3-en/character/mihael-loncar` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-3-en/character/nenad-zupan` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-3-en/character/nenad-zupan` | Repetier M95 carbine | — | `repetier-m95` |
| `hotoe-book-5-en/character/cybelle-francis` | .22 Derringer | — | `22-derringer` |
| `hotoe-book-5-en/character/madam-arcana` | .22 Derringer (1B) | — | `22-derringer` |
| `hotoe-book-5-en/character/seregena-androkovna-rankenberg` | .22 Derringer Pistol (2B) | — | `22-derringer` |
| `arkham-en/character/overview-ellen-whipple-smith` | .22 Derringer (2B) | — | `22-derringer` |
| `mts-kharkov-37-ru/character/aleksandr-tropinov` | Пулемёт Туламаш-Максим М-1890 | — | `maxim-machine-gun` |
| `mts-kharkov-37-ru/character/krasnoarmeytsy-depo-945` | Пулемёт Туламаш-Максим М-1890 | — | `maxim-machine-gun` |
| `children-of-fear-en/character/gates-porters` | Hanyang 88 bolt-action rifle | — | `mauser-m1888-hanyang-88` |
| `children-of-fear-en/character/gates-porters` | Hanyang 88 bolt-action rifle | — | `mauser-m1888-hanyang-88` |
| `children-of-fear-en/character/gates-porters` | Hanyang 88 bolt-action rifle | — | `mauser-m1888-hanyang-88` |
| `children-of-fear-en/character/mi-hu` | Hanyang 88 bolt-action rifle | — | `mauser-m1888-hanyang-88` |
| `children-of-fear-en/character/peking-chinese-soldiers` | M1888 bolt-action rifle | `30-06-bolt-action-rifle` | `mauser-m1888-hanyang-88` |
| `children-of-fear-en/character/appendix-bandit` | Matchlock rifle | — | `matchlock-rifle` |
| `children-of-fear-en/character/appendix-tribal-member` | Matchlock rifle | — | `matchlock-rifle` |
| `children-of-fear-en/character/appendix-refugee` | Nagant M1895 7.62mm revolver | — | `32-revolver` |
| `children-of-fear-en/character/appendix-refugee` | Nagant M1895 7.62mm revolver | — | `32-revolver` |

Пометки «записи оружия нет / без ссылки» в `quality.notes` этих записей заменены ссылкой на новую запись (17 записей). Правила с таблицами (15) получили `refs` на записи оружия; пометки «кандидаты в справочник» в них заменены.

## Не взято

- Section 46: M28/M29 Davy Crockett и S&W Model 23 «Hush Puppy» — в книге без чисел (таблицы нет).
- HOTOE кн. I, «Traveling Armed»: «двуствольный дробовик» — без чисел; «.32 pocket pistols» — общая позиция «Пистолет автоматический .32» (числа совпадают, источник добавлен).
- London, «Price Lists»: охотничий и перочинный нож (16s/2d — 19s/3d; 8s — 10s/6d) — товары снаряжения; к какой позиции ножа таблицы XVII относить охотничий нож, книга не говорит — цены не перенесены. Сигнальные ракеты (не оружие).
- Только в статблоках, не в таблицах и не в отчётах как кандидаты: пистолет «Стар» модель A (кн. IV, «мясники»), пистолет-пулемёт «Беретта» M1919 (кн. IV, опергруппа Христова), обрез рычажного дробовика (кн. IV), однозарядная спортивная винтовка .303 (Дантон Сорбич), рыцарский меч, абордажная сабля, трость со шпагой и другие ножи/дубинки HOTOE; ритуальное оружие «Детей страха» (пурба, катари, кхатванга, чаури, скорпионий клинок) — предметы, часть уже связана с общими позициями.
- Кандидаты из прежних отчётов не по таблицам книг: деревянный кол (`20261112-ru-oneshots/johnny.md`, предмет), японское оружие «Японии» (кагинава, боккэн, вакидзаси, военный нож, нож с серебряной рукоятью, стилет — `20261113-ru-rest/japan.md`), электропогонялка (`20261117-abominations`, предмет), нож Дейзи Гарсии (`20261111-keepers-companion/hammer.md`). Мушкет «Браун Бесс» (`20261116-savages`) уже в справочнике.
- Ссылки на общие позиции из статблоков WWC, где книга называет только тип («Handgun», «Rifle», «Knife»), не ставились; эпоха `1940s-1980s` добавлена только оружию из таблиц WWC, не всем позициям, которыми пользуются персонажи WWC.

## Решения по ходу (вывод, Р-41)

- «M1888» (Бэйянская армия) и «Hanyang 88» (караван Ми Ханя) — одна запись: германская винтовка образца 1888 года и её китайская копия; урон 1d6+1 как напечатано (`errata`).
- Ятаган — новая запись с `model_of` «Меч лёгкий»; «Yataghan Knife» кн. IV (1d4+3) — вариант источника той же записи, эпохи `gaslight` и `1920s`.
- «Максим»: MG08/15 (HOTOE кн. IV) и «Туламаш-Максим М-1890» («МТС Харьков 37») — одна запись, числа по HOTOE, Харьков — вариант.
- Colt Detective Special уже был псевдонимом «Револьвера .38» → вариант источника; AR-15/M16 — вариант «M16A2» (псевдоним M16); M16A1 — своя запись с `model_of` M16A2.
- Осколочная граната Section 46 и Webley MP .32, FN-Browning Mle 1900, DWM-Luger M1911, Webley Mk VI (HOTOE кн. I) — числа совпадают с записями: добавлены источник (и псевдонимы), вариант не нужен.
- Пика Внутренней гвардии: навык Ближний бой (копьё) — вывод; бонус к урону книга не оговаривает (`db: null`).

## Проверки

Нормализация `--changed`: normalize_dice — 31 строка в 18 файлах, errata_flag — флаг в 8 записях, остальные — 0. `tools/check.py --changed`: 0 ошибок. `tools/check.py` (вся база, 31 972 записи): 0 ошибок, 3 прежних предупреждения (blackjack HOTOE, 2 у howl-of-the-chimeras-en). Просмотрщик пересобран; карточку в браузере не смотрели (вход по паролю), строки цены проверены по собранному `app/kb.html`.
