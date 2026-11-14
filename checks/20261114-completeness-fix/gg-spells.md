# Полнота: Grand Grimoire — заклинания (часть gg-spells)

Задание: `.cache/briefs/grand-grimoire-en-gg-spells.md` (Р-242, Р-51, Р-171, Р-175, Р-184). Книга `grand-grimoire-en`, гл. 4 «The Grand Grimoire of the Cthulhu Mythos» (печ. с. 26–193) и указатель (с. 195–200). Страницы — печатные (физическая = печатная + 1; `pages.py` для этой книги показывает физическую).

Итог: новых записей `kb/spells/` — 236; предложений к чужим записям — `proposals-gg-spells.json`. Полный список названий собран по заголовкам статей гл. 4 (шрифт заголовка в PDF), сверен со списками категорий (с. 23–25) и с указателем (с. 195–200); каждое название проверено по `name.en`, `aliases` и id всех записей `kb/spells/`.

Перевод — наш (флаг `translated`); тип (`category`) — по 14 типам Р-66, механика — по Р-69; варианты (Call … variant, Contact … variant) — `variant_of`; заклинания Страны грёз и народные — по образцу записей GG: `name.en` без «(Dreamlands)», напечатанный заголовок — в `aliases`; для вызова и связи с божеством цена и время — общие (с. 53, с. 72), если своих нет (источник с этих страниц добавлен).

## Статьи заклинаний гл. 4

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Accursed Eye | 26 | `coc:spell:accursed-eye` |
| Activation | 26 | `coc:spell:activation` (новая) |
| Alter Weather | 27 | `coc:spell:alter-weather` |
| Anathema (Dreamlands) | 28 | `coc:spell:anathema-dreamlands` |
| Animate Flesh Thing | 28 | `coc:spell:animate-flesh-thing` |
| Animate Mummy | 28 | `coc:spell:animate-mummy` |
| Appear Human | 29 | `coc:spell:appear-human` |
| Apportion Ka | 29 | `coc:spell:apportion-ka` |
| Ariadne’s Twine | 29 | `coc:spell:ariadnes-twine` |
| Ascend the Stairs of Immortality | 29 | `coc:spell:ascend-the-stairs-of-immortality` (новая) |
| Assist Dreamer | 30 | `coc:spell:assist-dreamer` |
| Attract Fish | 30 | `coc:spell:attract-fish` |
| Attune Crystal | 30 | `coc:spell:attune-crystal` |
| Augury (Folk) | 30 | `coc:spell:augury-folk` |
| Awake Abhoth | 31 | `coc:spell:awake-abhoth` |
| Awaken Chuma (Call/Dismiss Yibb-Tstll variant) | 31 | `coc:spell:awaken-chuma` (новая) |
| Awaken the Beast (Folk) | 31 | `coc:spell:awaken-the-beast-folk` |
| Awaken The Great Tortoise | 32 | `coc:spell:awaken-the-great-tortoise` (новая) |
| Awaken the Inner Light | 32 | `coc:spell:awaken-the-inner-light` |
| Awaking/Dispelling the God Within | 32 | `coc:spell:awaking-dispelling-the-god-within` (новая) |
| Awful Doom of Cerrit (Dreamlands) | 34 | `coc:spell:awful-doom-of-cerrit` |
| Bait Humans (Chthonian) | 34 | `coc:spell:bait-human` |
| Balk Brood | 34 | `coc:spell:balk-brood` |
| Baneful Dust of Hermes Trismegistus | 35 | `coc:spell:baneful-dust-of-hermes-trismegistus` |
| Banish Apep | 35 | `coc:spell:banish-apep` |
| Banish Byatis | 35 | `coc:spell:banish-byatis` |
| Banish Thy Name | 36 | `coc:spell:banish-thy-name` |
| Banishment of Yde Etad | 36 | `coc:spell:banishment-of-yde-etad` |
| Barrier of Pain | 36 | `coc:spell:barrier-of-pain` |
| Bat Form (Folk) | 37 | `coc:spell:bat-form` |
| Become Spectral | 37 | `coc:spell:become-spectral` |
| Become Spectral Hunter | 37 | `coc:spell:become-spectral-hunter` |
| Benevolent Influence | 38 | `coc:spell:benevolent-influence` (новая) |
| Beseech Charon | 38 | `coc:spell:beseech-charon` (новая) |
| Bespeak the End of the Day | 38 | `coc:spell:bespeak-the-end-of-the-day` |
| Bestow Glimpse of Truth | 40 | `coc:spell:bestow-glimpse-of-truth` |
| Bestow Karma (Folk) | 40 | `coc:spell:bestow-karma-folk` (новая) |
| Bind Animal (Folk) | 41 | `coc:spell:bind-animal` (варианты `coc:spell:bind-animal-cat`, `coc:spell:bind-animal-crocodile`) |
| Bind Enemy | 41 | `coc:spell:bind-enemy` |
| Bind Soul | 41 | `coc:spell:bind-soul` |
| Form of the Command | 43 | `coc:spell:summon-bind` (абзац о приказе укрощённой твари) |
| Bind Child of The Sphinx | 43 | `coc:spell:bind-child-of-the-sphinx` (новая) |
| Bind Shoggoth | 43 | `coc:spell:bind-shoggoth` (новая) |
| Bind Were-Creature | 43 | `coc:spell:bind-were-creature` (новая) |
| Black Box (Dreamlands) | 44 | `coc:spell:black-box` (новая) |
| Bless (Folk) | 44 | `coc:spell:bless-folk` (новая) |
| Bless Blade | 44 | `coc:spell:bless-blade` |
| Blessing of Bast | 44 | `coc:spell:blessing-of-bast` |
| Blight/Bless Crop (Folk) | 45 | `coc:spell:blight-bless-crop` |
| Bliss | 45 | `coc:spell:bliss` |
| Bloat (Dreamlands) | 45 | `coc:spell:bloat` |
| Blunt the Weapon | 45 | `coc:spell:blunt-the-weapon` (новая) |
| Body Warping of Gorgoroth | 45 | `coc:spell:body-warping-of-gorgoroth` |
| Bolonath’s Furnace (Dreamlands) | 46 | `coc:spell:bolonaths-furnace` (новая) |
| Breath of Pazzuzu | 46 | `coc:spell:breath-of-pazzuzu` |
| Breath of The Deep | 46 | `coc:spell:breath-of-the-deep` |
| Breath of the Kappa | 46 | `coc:spell:breath-of-the-kappa` (новая) |
| Brew Draught of Phan | 46 | `coc:spell:brew-draught-of-phan` (новая) |
| Brew Dream Drug | 47 | `coc:spell:brew-dream-drug` |
| Brew Elixir of Life | 47 | `coc:spell:brew-elixir-of-life` (новая) |
| Brew Liao Drug | 47 | `coc:spell:brew-liao-drug` (новая) |
| Brew Love Philter (Folk) | 49 | `coc:spell:brew-love-philter-folk` |
| Brew Para-Kete (Brew Liao Drug variant, Modern Era only) | 49 | `coc:spell:brew-para-kete` (новая) |
| Brew Paut | 49 | `coc:spell:brew-paut` (новая) |
| Brew Space-Mead (I) | 50 | `coc:spell:brew-space-mead` |
| Brew Space-Mead (II) (Dreamlands variant) | 51 | `coc:spell:brew-space-mead` |
| Bring Haboob | 51 | `coc:spell:bring-haboob` |
| Bring Pestilence (I) | 51 | `coc:spell:bring-pestilence` |
| Bring Pestilence (II) (Dreamlands variant) | 51 | `coc:spell:bring-pestilence` |
| Build Carcosa | 53 | `coc:spell:build-carcosa` |
| Burden of The Skinless One | 53 | `coc:spell:burden-of-the-skinless-one` (новая) |
| Call Aku-Shin Kage (Avatar of Nyarlathotep) | 54 | `coc:spell:call-aku-shin-kage` (новая) |
| Call Ahtu (Avatar of Nyarlathotep) | 54 | `coc:spell:call-ahtu` (новая) |
| Call Arwassa | 54 | `coc:spell:call-arwassa` (новая) |
| Call Avatar of The Skinless One (Avatar of Nyarlathotep) | 54 | `coc:spell:call-avatar-of-the-skinless-one` (новая) |
| Call Azathoth | 55 | `coc:spell:call-dismiss-azathoth` |
| Call Bugg-Shash | 55 | `coc:spell:call-bugg-shash` |
| Call Cthugha | 55 | `coc:spell:call-dismiss-cthugha` |
| Call Cyaegha | 55 | `coc:spell:call-dismiss-cyaegha` |
| Call Daoloth | 55 | `coc:spell:call-dismiss-daoloth` |
| Call El Negro (Avatar of Nyarlathotep) | 56 | `coc:spell:call-el-negro` (новая) |
| Call Ghatanothoa | 56 | `coc:spell:call-dismiss-ghatanothoa` |
| Call Gla’aki | 56 | `coc:spell:call-glaaki` (новая) |
| Call Gol-Goroth | 56 | `coc:spell:call-gol-goroth` (новая) |
| Call Hastur | 56 | `coc:spell:call-dismiss-hastur` |
| Call Horned Man (Avatar of Nyarlathotep) | 58 | `coc:spell:call-horned-man` (новая) |
| Call Iod | 58 | `coc:spell:call-iod` (новая) |
| Call Ithaqua | 58 | `coc:spell:call-dismiss-ithaqua` |
| Call Nyogtha | 58 | `coc:spell:call-dismiss-nyogtha` |
| Call Keeper of the Moonlens | 58 | `coc:spell:call-keeper-of-the-moonlens` (новая) |
| Call La Llorona | 58 | `coc:spell:call-la-llorona` (новая) |
| Call M’nagalah | 58 | `coc:spell:call-mnagalah` (новая) |
| Call Mappo No Ryûjin | 59 | `coc:spell:call-mappo-no-ryujin` (новая) |
| Call Ossadogowah | 59 | `coc:spell:call-dismiss-ossadagowah` |
| Call Rlim Shaikorth | 59 | `coc:spell:call-dismiss-rlim-shaikorth` |
| Call Saaitii | 59 | `coc:spell:call-saaitii` (новая) |
| Call Shub-Niggurath | 59 | `coc:spell:call-dismiss-shub-niggurath` |
| Call (The) Skinless One | 59 | `coc:spell:call-the-skinless-one` (новая) |
| Call The Beast (Avatar of Nyarlathotep) | 60 | `coc:spell:call-the-beast` |
| Call Yibb-Tstll | 60 | `coc:spell:call-dismiss-yibb-tstll` |
| Call Yig | 60 | `coc:spell:call-yig` (новая) |
| Call Yog-Sothoth | 60 | `coc:spell:call-dismiss-yog-sothoth` |
| Call Zu-Che-Quon | 60 | `coc:spell:call-zu-che-quon` (новая) |
| Call Forth The Worm | 60 | `coc:spell:call-forth-the-worm` |
| Call Lightning | 61 | `coc:spell:call-lightning` |
| Call The Black | 61 | `coc:spell:call-the-black` |
| Call Zombie | 61 | `coc:spell:call-zombie` (новая) |
| Candle Communication | 61 | `coc:spell:candle-communication` |
| Cascades of Florin (Dreamlands) | 61 | `coc:spell:cascades-of-florin` (новая) |
| Cast Circle | 62 | `coc:spell:cast-circle` |
| Cast Out Shan | 62 | `coc:spell:cast-out-shan` |
| Cast Out The Devil | 62 | `coc:spell:cast-out-the-devil` |
| Casting the Runes | 62 | `coc:spell:casting-the-runes` (новая) |
| Cause/Cure Blindness | 63 | `coc:spell:cause-cure-blindness` |
| Cause Disease | 63 | `coc:spell:cause-disease` |
| Channeling God | 63 | `coc:spell:channeling-god` (новая) |
| Chant of Thoth | 64 | `coc:spell:chant-of-thoth` |
| Chant of Warding | 64 | `coc:spell:chant-of-warding` (новая) |
| Charm Animal (Folk) | 64 | `coc:spell:charm-animal-folk` |
| Chasm to Hell | 64 | `coc:spell:chasm-to-hell` |
| Chime of Tezchaptl | 65 | `coc:spell:chime-of-tezchaptl` |
| Circle of Nausea | 65 | `coc:spell:circle-of-nausea` |
| Circle of Warding | 65 | `coc:spell:circle-of-warding` |
| Cleansing Flame of Vorvadoss | 66 | `coc:spell:cleansing-flame-of-vorvadoss` (новая) |
| Cleansing Ritual | 66 | `coc:spell:cleansing-ritual` |
| Cloak of Fire | 66 | `coc:spell:cloak-of-fire` |
| Cloud Memory | 66 | `coc:spell:cloud-memory` |
| Clutch of Nyogtha | 68 | `coc:spell:clutch-of-nyogtha` |
| Come and See Me (Folk) | 68 | `coc:spell:come-and-see-me-folk` (новая) |
| Command Animal (Folk) | 68 | `coc:spell:command-animal-folk` |
| Command Ghost (Folk) | 69 | `coc:spell:command-ghost-folk` |
| Command of The Bloody Tongue | 69 | `coc:spell:command-of-the-bloody-tongue` (новая) |
| Command Plants | 69 | `coc:spell:command-plants` |
| Command Shoggoth | 69 | `coc:spell:command-shoggoth` |
| Compel Flesh | 69 | `coc:spell:compel-flesh` |
| Concentric Rings of the Worm (Dreamlands) | 69 | `coc:spell:concentric-rings-of-the-worm` (новая) |
| Conjure Glass of Mortlan | 72 | `coc:spell:conjure-glass-of-mortlan` (новая) |
| Consume Likeness | 72 | `coc:spell:consume-likeness` |
| Consume Memories | 72 | `coc:spell:consume-memories` |
| Contact Abhoth | 73 | `coc:spell:contact-abhoth` (новая) |
| Contact Aku-Shin Kage (Avatar of Nyarlathotep) | 73 | `coc:spell:contact-aku-shin-kage` (новая) |
| Contact Azathoth | 73 | `coc:spell:contact-azathoth` (новая) |
| Contact Bokrug (Dreamlands) | 73 | `coc:spell:contact-bokrug` (новая) |
| Contact Byatis | 73 | `coc:spell:contact-byatis` (новая) |
| Contact Chaugnar Faugn | 73 | `coc:spell:contact-chaugnar-faugn` |
| Contact Cthulhu | 73 | `coc:spell:contact-cthulhu` |
| Contact Eihort | 74 | `coc:spell:contact-eihort` |
| Contact Emerald Lama (Avatar of Hastur) | 74 | `coc:spell:contact-emerald-lama` (новая) |
| Contact Ghroth | 74 | `coc:spell:contact-ghroth` (новая) |
| Contact Gla’aki | 74 | `coc:spell:contact-glaaki` |
| Contact Iod | 74 | `coc:spell:contact-iod` (новая) |
| Contact Koth | 74 | `coc:spell:contact-koth` (новая) |
| Contact Nodens | 74 | `coc:spell:contact-nodens` |
| Contact Nyarlathotep | 74 | `coc:spell:contact-nyarlathotep` |
| Contact Nyarlatophis (Avatar of Nyarlathotep) | 76 | `coc:spell:contact-nyarlatophis` (новая) |
| Contact Othuyeg | 76 | `coc:spell:contact-othuyeg` (новая) |
| Contact Pazzuzu (Avatar of Nyarlathotep) | 76 | `coc:spell:contact-pazzuzu` (новая) |
| Contact Shub-Niggurath | 76 | `coc:spell:contact-shub-niggurath` |
| Contact Tsathoggua | 76 | `coc:spell:contact-tsathoggua` |
| Contact Y’golonac | 76 | `coc:spell:contact-ygolonac` |
| Contact Yig | 77 | `coc:spell:contact-yig` |
| Contact Yog-Sothoth | 77 | `coc:spell:contact-yog-sothoth` |
| Contact Zhar and Lloigor | 77 | `coc:spell:contact-zhar-and-lloigor` (новая) |
| Contact Zoth-Ommog | 77 | `coc:spell:contact-zoth-ommog` |
| Contact Child of The Sphinx | 78 | `coc:spell:contact-child-of-the-sphinx` (новая) |
| Contact Chthonian | 78 | `coc:spell:contact-chthonian` |
| Contact Deep One | 78 | `coc:spell:contact-deep-one` |
| Contact Deity —see page 72 | 78 | отсылка к `coc:spell:contact-deity` |
| Contact Elder Thing | 78 | `coc:spell:contact-elder-thing` |
| Contact Flying Polyp | 78 | `coc:spell:contact-flying-polyp` |
| Contact Formless Spawn | 79 | `coc:spell:contact-formless-spawn` |
| Contact Ghoul | 79 | `coc:spell:contact-ghoul` |
| Contact Gnoph-Keh | 79 | `coc:spell:contact-gnoph-keh` |
| Contact Hound of Tindalos | 79 | `coc:spell:contact-hound-of-tindalos` |
| Contact Human (Mi-Go) | 79 | `coc:spell:contact-human` |
| Contact Lloigor | 79 | `coc:spell:contact-lloigor` |
| Contact Masters | 79 | `coc:spell:contact-masters` (новая) |
| Contact Mi-Go | 80 | `coc:spell:contact-mi-go` |
| Contact Moon-Beast (Dreamlands) | 80 | `coc:spell:contact-moon-beast` |
| Contact Rat-Thing | 80 | `coc:spell:contact-rat-thing` |
| Contact Sand-Dweller | 80 | `coc:spell:contact-sand-dweller` |
| Contact Servitor of The Outer Gods | 80 | `coc:spell:contact-servitor-of-the-outer-gods` |
| Contact Spirits of the Dead | 80 | `coc:spell:contact-spirits-of-the-dead` |
| Contact Star-Spawn of Cthulhu | 80 | `coc:spell:contact-star-spawn-of-cthulhu` |
| Contact Tomb-Herd | 81 | `coc:spell:contact-tomb-herd` (новая) |
| Contact Yithian | 81 | `coc:spell:contact-yithian` |
| Control Elements | 81 | `coc:spell:control-elements` |
| Control Skin | 81 | `coc:spell:control-skin` |
| Corruption of the Sacred | 81 | `coc:spell:corruption-of-the-sacred` (новая) |
| Coyote Dust (Folk) | 82 | `coc:spell:coyote-dust-folk` |
| Create Amulet | 82 | `coc:spell:create-amulet` |
| Create Bad-Corpse Dust | 82 | `coc:spell:create-bad-corpse-dust` (новая) |
| Create Barrier of Naach-Tith | 83 | `coc:spell:create-barrier-of-naach-tith` |
| Create Bulla (Folk) | 83 | `coc:spell:create-bulla-folk` (новая) |
| Create Charm (Folk) | 83 | `coc:spell:create-charm-folk` |
| Create Child of The Sphinx | 83 | `coc:spell:create-child-of-the-sphinx` |
| Create Curse Tablet | 86 | `coc:spell:create-curse-tablet` |
| Create Curse Whistle | 86 | `coc:spell:create-curse-whistle` (новая) |
| Create Fetch Stick | 86 | `coc:spell:create-fetch-stick` (новая) |
| Create Flesh Creeper | 86 | `coc:spell:create-flesh-creeper` |
| Create Gate—see Gate, page 120 Create Gate Window (Mythos Deities/Very Powerful Sorcerers) | 87 | отсылка «Create Gate» → `coc:spell:create-gate`; статья Create Gate Window → `coc:spell:create-gate-window` |
| Create Golem | 87 | `coc:spell:create-golem` (новая) |
| Create Mist of R’lyeh | 87 | `coc:spell:create-mist-of-rlyeh` |
| Create Scrying Window | 88 | `coc:spell:create-scrying-window` |
| Create Self-Ward | 88 | `coc:spell:create-self-ward` (новая) |
| Create Sign of Barzai | 88 | `coc:spell:create-sign-of-barzai` |
| Create Storm (Folk) | 89 | `coc:spell:create-storm-folk` (новая) |
| Create Zombi (Create Zombie variant) | 89 | `coc:spell:create-zombi` |
| Create Zombie | 89 | `coc:spell:create-zombie` |
| Creation of Venerability (Dreamlands) | 89 | `coc:spell:creation-of-venerability` (новая) |
| Creeping Loss | 89 | `coc:spell:creeping-loss` (новая) |
| Crystal Call (Call Hastur variant) | 90 | `coc:spell:crystal-call` (новая) |
| Crystal World (Dreamlands) | 90 | `coc:spell:crystal-world` (новая) |
| Curse (Folk) | 90 | `coc:spell:curse-folk` |
| Curse of Apophis | 90 | `coc:spell:curse-of-apophis` (новая) |
| Curse of Chaugnar Faugn | 90 | `coc:spell:curse-of-chaugnar-faugn` |
| Curse of Darkness | 92 | `coc:spell:curse-of-darkness` (новая) |
| Curse of the Putrid Husk | 92 | `coc:spell:curse-of-the-putrid-husk` |
| Curse of the Rat-Thing | 92 | `coc:spell:curse-of-the-rat-thing` |
| Curse of the Stone | 92 | `coc:spell:curse-of-the-stone` |
| Dampen Light | 93 | `coc:spell:dampen-light` |
| Death Spell | 93 | `coc:spell:death-spell` |
| Death’s Breath | 93 | `coc:spell:deaths-breath` |
| Deflect Harm | 93 | `coc:spell:deflect-harm` |
| Deflection (Dreamlands) | 94 | `coc:spell:deflection` |
| Defy Gravity | 94 | `coc:spell:defy-gravity` |
| Demon Senses | 94 | `coc:spell:demon-senses` |
| Destroy Spawn of Yig | 94 | `coc:spell:destroy-spawn-of-yig` (новая) |
| Detect Enchantment | 95 | `coc:spell:detect-enchantment` |
| Detransference | 95 | `coc:spell:detransference` (новая) |
| Devolution (Dreamlands) | 95 | `coc:spell:devolution` (новая) |
| Dho Formula | 95 | `coc:spell:dho-formula` |
| Dionysian Revels | 96 | `coc:spell:dionysian-revels` (новая) |
| Disembodiment | 96 | `coc:spell:disembodiment` |
| Dismiss Spirit | 97 | `coc:spell:dismiss-spirit` |
| Dissolve Skeleton (Dreamlands) | 97 | `coc:spell:dissolve-skeleton` |
| Divination | 97 | `coc:spell:divination` (новая) |
| Dominate | 98 | `coc:spell:dominate` |
| Dowsing (Folk) | 98 | `coc:spell:dowsing-folk` |
| Drain Youth | 98 | `coc:spell:drain-youth` |
| Dread Curse of Azathoth | 98 | `coc:spell:dread-curse-of-azathoth` |
| Dream Vision | 102 | `coc:spell:dream-vision` |
| Drown Mind | 102 | `coc:spell:drown-mind` |
| Dust of Suleiman | 102 | `coc:spell:dust-of-suleiman` |
| Earthly Serenity (Folk) | 102 | `coc:spell:earthly-serenity-folk` |
| Effigy of Hate | 102 | `coc:spell:effigy-of-hate` (новая) |
| Eibon’s Wheel of Mist | 103 | `coc:spell:eibons-wheel-of-mist` |
| Einstein Formula | 105 | `coc:spell:einstein-formula` (новая) |
| Elder Sign, The | 105 | `coc:spell:elder-sign` |
| Elysian Grace | 105 | `coc:spell:elysian-grace` (новая) |
| Embrace of Yog-Sothoth | 106 | `coc:spell:embrace-of-yog-sothoth` |
| Emerald Darts of Ptath (Dreamlands) | 106 | `coc:spell:emerald-darts-of-ptath` (новая) |
| Empty Mind (Folk) | 106 | `coc:spell:empty-mind-folk` |
| Enchant Amulet of The Old Ones | 106 | `coc:spell:enchant-amulet-of-the-old-ones` (новая) |
| Enchant Animal Effigy | 107 | `coc:spell:enchant-animal-effigy` (новая) |
| Enchant Bells of Horror | 107 | `coc:spell:enchant-bells-of-horror` (новая) |
| Enchant Book | 107 | `coc:spell:enchant-book` |
| Enchant Brazier | 107 | `coc:spell:enchant-brazier` |
| Enchant Candle (Folk) | 108 | `coc:spell:enchant-candle-folk` |
| Enchant Cane | 108 | `coc:spell:enchant-cane` (новая) |
| Enchant Club | 108 | `coc:spell:enchant-club` |
| Enchant Dagger of Nyarlathotep | 108 | `coc:spell:enchant-dagger-of-nyarlathotep` |
| Enchant Doll | 108 | `coc:spell:enchant-doll` (новая) |
| Enchant Flesh | 108 | `coc:spell:enchant-flesh` (новая) |
| Enchant Gris-Gris | 109 | `coc:spell:enchant-gris-gris` (новая) |
| Enchant Ju-Ju (Folk) | 109 | `coc:spell:enchant-ju-ju-folk` (новая) |
| Enchant Knife | 109 | `coc:spell:enchant-knife` |
| Enchant Magic Staves | 109 | `coc:spell:enchant-magic-staves` (новая) |
| Enchant Painting | 109 | `coc:spell:enchant-painting` (новая) |
| Enchant Paviut (Folk) | 110 | `coc:spell:enchant-paviut-folk` (новая) |
| Enchant Pipes | 110 | `coc:spell:enchant-pipes` |
| Enchant Projectile | 110 | `coc:spell:enchant-projectile` (новая) |
| Enchant Recording | 110 | `coc:spell:enchant-recording` (новая) |
| Enchant Ring | 110 | `coc:spell:enchant-ring` (новая) |
| Enchant Serum | 110 | `coc:spell:enchant-serum` (новая) |
| Enchant Spear | 111 | `coc:spell:enchant-spear` (новая) |
| Enchant Stone Tablet | 111 | `coc:spell:enchant-stone-tablet` |
| Enchant Torch | 111 | `coc:spell:enchant-torch` |
| Enchant Whistle | 111 | `coc:spell:enchant-whistle` |
| Enchanted Dust of Anubis | 112 | `coc:spell:enchanted-dust-of-anubis` |
| Enchantment of Ill Luck | 112 | `coc:spell:enchantment-of-ill-luck` (новая) |
| Endurance Chant | 112 | `coc:spell:endurance-chant` (новая) |
| Engender Prosperity (Folk) | 112 | `coc:spell:engender-prosperity-folk` (новая) |
| Enjoin Pnakotic Pentagram | 112 | `coc:spell:enjoin-pnakotic-pentagram` (новая) |
| Enjoin the Sign of Koth | 113 | `coc:spell:enjoin-the-sign-of-koth` (новая) |
| Enthrall Victim | 113 | `coc:spell:enthrall-victim` |
| Equilateral Screen (Dreamlands) | 113 | `coc:spell:equilateral-screen` (новая) |
| Evil Eye | 113 | `coc:spell:evil-eye` |
| Eviscerator (Dreamlands) | 114 | `coc:spell:eviscerator` |
| Exaltation | 114 | `coc:spell:exaltation` (новая) |
| Exile Eihort | 114 | `coc:spell:exile-eihort` (новая) |
| Explode Heart (Dreamlands) | 114 | `coc:spell:explode-heart` |
| Extend Life | 115 | `coc:spell:extend-life` |
| Eye of Light and Darkness | 115 | `coc:spell:eye-of-light-and-darkness` |
| Eyes of a Stranger | 116 | `coc:spell:eyes-of-a-stranger` (новая) |
| Eyes of the Zombie | 116 | `coc:spell:eyes-of-the-zombie` (новая) |
| Fang of Yig | 116 | `coc:spell:fang-of-yig` (новая) |
| Feast of the Owl (Folk) | 116 | `coc:spell:feast-of-the-owl-folk` (новая) |
| Final Feast | 117 | `coc:spell:final-feast` (новая) |
| Find Dreamer (Dreamlands and Waking World) | 117 | `coc:spell:find-dreamer` (новая) |
| Find Gate | 117 | `coc:spell:find-gate` |
| Find Serpent Folk (Serpent People) | 117 | `coc:spell:find-serpent-folk` (новая) |
| Fire Dance | 117 | `coc:spell:fire-dance` (новая) |
| Fist of Yog-Sothoth | 118 | `coc:spell:fist-of-yog-sothoth` |
| Flameshield (Dreamlands) | 118 | `coc:spell:flameshield` (новая) |
| Flash of Ra | 118 | `coc:spell:flash-of-ra` |
| Flesh Ward | 118 | `coc:spell:flesh-ward` |
| Flight | 119 | `coc:spell:flight` (новая) |
| Food of Life | 119 | `coc:spell:food-of-life` (новая) |
| Freak Weather | 119 | `coc:spell:freak-weather` (новая) |
| Free Hastur | 119 | `coc:spell:free-hastur` |
| Fury (Folk) | 119 | `coc:spell:fury` |
| Gate | 120 | `coc:spell:create-gate` |
| Gate Boxes | 120 | `coc:spell:gate-boxes` |
| Gate of Dreams | 120 | `coc:spell:gate-of-dreams` (новая) |
| Gate of Oneirology | 124 | `coc:spell:gate-of-oneirology` |
| Gather and Channel Fear | 124 | `coc:spell:gather-and-channel-fear` (новая) |
| Gift of Inanna | 124 | `coc:spell:gift-of-inanna` (новая) |
| Golden Cage of Desire | 125 | `coc:spell:golden-cage-of-desire` (новая) |
| Good Thief Water (Folk) | 125 | `coc:spell:good-thief-water-folk` |
| Graft Flesh | 125 | `coc:spell:graft-flesh` (новая) |
| Grasp of Cthulhu | 125 | `coc:spell:grasp-of-cthulhu` |
| Graveyard Kiss (Create Zombie variant) | 125 | `coc:spell:graveyard-kiss` |
| Great Rite of Sacrifice | 126 | `coc:spell:great-rite-of-sacrifice` (новая) |
| Green Decay | 126 | `coc:spell:green-decay` |
| Grey Binding (Create Zombie variant) | 126 | `coc:spell:grey-binding` |
| Halt of Eanora (Dreamlands) | 127 | `coc:spell:halt-of-eanora` (новая) |
| Hands of Colubra | 127 | `coc:spell:hands-of-colubra` |
| Healing (Folk) | 127 | `coc:spell:healing-folk` |
| Heart’s Courage | 127 | `coc:spell:hearts-courage` (новая) |
| Hibernate | 127 | `coc:spell:hibernate` (новая) |
| Human Shrub | 128 | `coc:spell:human-shrub` |
| Hunger of Kazan | 128 | `coc:spell:hunger-of-kazan` |
| Identify Spirit | 128 | `coc:spell:identify-spirit` |
| Ill Luck (Folk) | 128 | `coc:spell:ill-luck-folk` |
| Immortality | 129 | `coc:spell:immortality` (новая) |
| Impeccable Throw (Folk) | 129 | `coc:spell:impeccable-throw-folk` (новая) |
| Implant Fear | 129 | `coc:spell:implant-fear` |
| Imprison Mind | 130 | `coc:spell:imprison-mind` |
| Incantation of The Sixth Sathlatta | 130 | `coc:spell:incantation-of-the-sixth-sathlatta` (новая) |
| Incinerate | 130 | `coc:spell:incinerate` |
| Indent Liche | 130 | `coc:spell:indent-liche` (новая) |
| Ineffable Comprehension | 130 | `coc:spell:ineffable-comprehension` (новая) |
| Instant Enlightenment | 131 | `coc:spell:instant-enlightenment` (новая) |
| Ironmind (Dreamlands) | 131 | `coc:spell:ironmind` (новая) |
| Journey to the Other Side | 131 | `coc:spell:journey-to-the-other-side` |
| Katarien’s Heat Wave (Dreamlands) | 131 | `coc:spell:katariens-heat-wave` (новая) |
| Keenness of Two Alike | 131 | `coc:spell:keenness-of-two-alike` (новая) |
| Knot Flesh | 134 | `coc:spell:knot-flesh` |
| Koshchey’s Death | 134 | `coc:spell:koshcheys-death` (новая) |
| Lace Curtains of Hish (Dreamlands) | 134 | `coc:spell:lace-curtains-of-hish` (новая) |
| Lambent Flame (Dreamlands) | 134 | `coc:spell:lambent-flame` (новая) |
| Lame/Heal Animal (Folk) | 135 | `coc:spell:lame-heal-animal-folk` |
| Lassitude of Phein (Dreamlands) | 135 | `coc:spell:lassitude-of-phein` (новая) |
| Lavender Spheres of Ptath (Dreamlands) | 135 | `coc:spell:lavender-spheres-of-ptath` (новая) |
| Levitate | 135 | `coc:spell:levitate` |
| Lift Veil | 135 | `coc:spell:lift-veil` (новая) |
| Light of Sacred Truth | 136 | `coc:spell:light-of-sacred-truth` (новая) |
| Light of Seker | 136 | `coc:spell:light-of-seker` (новая) |
| Limbo Gate | 136 | `coc:spell:limbo-gate` |
| Liquid Death | 137 | `coc:spell:liquid-death` |
| Liquidity | 137 | `coc:spell:liquidity` |
| Living Clothes (Dreamlands) | 137 | `coc:spell:living-clothes` |
| Living X (Dreamlands) | 138 | `coc:spell:living-x` (новая) |
| Look Inward | 138 | `coc:spell:look-inward` (новая) |
| Look to the Future | 138 | `coc:spell:look-to-the-future` (новая) |
| Maggots | 138 | `coc:spell:maggots` |
| Malenkamon’s Impressive Bolt (Dreamlands) | 139 | `coc:spell:malenkamons-impressive-bolt` (новая) |
| Mandrake (Dreamlands) | 139 | `coc:spell:mandrake` (новая) |
| Mask of Death | 139 | `coc:spell:mask-of-death` (новая) |
| Maws of Pandemonium (Dreamlands) | 139 | `coc:spell:maws-of-pandemonium` |
| Melt Flesh | 140 | `coc:spell:melt-flesh` |
| Mental Suggestion | 140 | `coc:spell:mental-suggestion` |
| Milking the Spirit | 140 | `coc:spell:milking-the-spirit` (новая) |
| Mind Cloud | 140 | `coc:spell:mind-cloud` (новая) |
| Mind Dance | 141 | `coc:spell:mind-dance` (новая) |
| Mind Exchange | 141 | `coc:spell:mind-exchange` |
| Mind Transfer | 142 | `coc:spell:mind-transfer` |
| Mindblast | 142 | `coc:spell:mindblast` |
| Minim (Dreamlands) | 142 | `coc:spell:minim` (новая) |
| Mirror of Tarkhun Atep | 142 | `coc:spell:mirror-of-tarkhun-atep` |
| Mnomquah’s Serpent (Dreamlands/Moon-beast) | 143 | `coc:spell:mnomquahs-serpent` (новая) |
| Momoy Ritual | 143 | `coc:spell:momoy-ritual` (новая) |
| Moonlight | 143 | `coc:spell:moonlight` (новая) |
| Move Gate | 143 | `coc:spell:move-gate` |
| Necklace of Suasion | 144 | `coc:spell:necklace-of-suasion` (новая) |
| Necrosis | 144 | `coc:spell:necrosis` |
| Net Wraith (Modern Era only) | 144 | `coc:spell:net-wraith` (новая) |
| Nightmare (I) | 145 | `coc:spell:nightmare` |
| Nightmares (II) | 145 | `coc:spell:nightmares` |
| Nullify Device | 146 | `coc:spell:nullify-device` |
| Numantina | 146 | `coc:spell:numantina` (новая) |
| Nyhargo Dirge (Resurrection variant) | 146 | `coc:spell:nyhargo-dirge` |
| Oblong Barrier (Dreamlands) | 146 | `coc:spell:oblong-barrier` (новая) |
| Oneiro-Dismissal (Dreamlands) | 146 | `coc:spell:oneiro-dismissal` (новая) |
| Opaque Wall (Dreamlands) | 146 | `coc:spell:opaque-wall` (новая) |
| Oscillating Expanse | 147 | `coc:spell:oscillating-expanse` |
| Pact of Quachil Uttaus | 147 | `coc:spell:pact-of-quachil-uttaus` (новая) |
| Parting Sands | 147 | `coc:spell:parting-sands` |
| Passing Unseen (Dreamlands) | 147 | `coc:spell:passing-unseen` (новая) |
| Paws of the Bear (Folk) | 149 | `coc:spell:paws-of-the-bear-folk` (новая) |
| Perceive Text | 149 | `coc:spell:perceive-text` |
| Perfection | 149 | `coc:spell:perfection` |
| Petrify | 150 | `coc:spell:petrify` (новая) |
| Petrify Nether Limbs | 150 | `coc:spell:petrify-nether-limbs` (новая) |
| Pipes of Madness | 150 | `coc:spell:pipes-of-madness` |
| Poison Blood (Folk) | 150 | `coc:spell:poison-blood-folk` |
| Pose Mundane | 151 | `coc:spell:pose-mundane` |
| Possess Corpse | 151 | `coc:spell:possess-corpse` |
| Possession | 151 | `coc:spell:possession` |
| Powder of Ibn-Ghazi | 151 | `coc:spell:powder-of-ibn-ghazi` |
| Power Chant | 153 | `coc:spell:power-chant` (новая) |
| Power Drain | 153 | `coc:spell:power-drain` |
| Power of Nyambe | 153 | `coc:spell:power-of-nyambe` |
| Prepare Corpse | 153 | `coc:spell:prepare-corpse` (новая) |
| Prinn’s Crux Ansata | 153 | `coc:spell:prinns-crux-ansata` |
| Quell Suspicion | 154 | `coc:spell:quell-suspicion` (новая) |
| Quicken | 154 | `coc:spell:quicken` (новая) |
| Quicken Fog-Spawn | 154 | `coc:spell:quicken-fog-spawn` |
| Quicken the Voice of the Deep | 155 | `coc:spell:quicken-the-voice-of-the-deep` |
| Raise Corpses (Dreamlands) | 156 | `coc:spell:raise-corpses` |
| Raise Ghost of Ib (Dreamlands) | 156 | `coc:spell:raise-ghost-of-ib` (новая) |
| Raise Night Fog | 156 | `coc:spell:raise-night-fog` (новая) |
| Ravening Madness, The (Dreamlands) | 156 | `coc:spell:ravening-madness` |
| Reach | 157 | `coc:spell:reach` (новая) |
| Reanimation | 157 | `coc:spell:reanimation` (новая) |
| Red Sign, The | 158 | `coc:spell:red-sign-of-shudde-mell` |
| Reincarnate | 158 | `coc:spell:reincarnate` (новая) |
| Remortification | 158 | `coc:spell:remortification` (новая) |
| Removal of Favor | 158 | `coc:spell:removal-of-favor` (новая) |
| Rend Veil | 160 | `coc:spell:rend-veil` (новая) |
| Repel Shan | 160 | `coc:spell:repel-shan` (новая) |
| Restorative Meditation (Folk) | 160 | `coc:spell:restorative-meditation-folk` (новая) |
| Resurrection | 160 | `coc:spell:resurrection` |
| Return of the Beloved | 161 | `coc:spell:return-of-the-beloved` |
| Return Servitor | 161 | `coc:spell:return-servitor` (новая) |
| Reversed Angles of Tagh-Clatur | 161 | `coc:spell:reversed-angles-of-tagh-clatur` (новая) |
| Saaamaaa Ritual | 162 | `coc:spell:saaamaaa-ritual` (новая) |
| Sacred Molting of the Serpent | 162 | `coc:spell:sacred-molting-of-the-serpent` (новая) |
| Seal of Isis | 163 | `coc:spell:seal-of-isis` |
| Seal of Nephren-Ka | 163 | `coc:spell:seal-of-nephren-ka` |
| Seal Pit (Dismiss Hastur variant) | 163 | `coc:spell:seal-pit` (новая) |
| Seek the Lost (Folk) | 163 | `coc:spell:seek-the-lost-folk` |
| Send Dream | 164 | `coc:spell:send-dream` |
| Send Sacred Snake | 164 | `coc:spell:send-sacred-snake` (новая) |
| Sending of the Dead | 164 | `coc:spell:sending-of-the-dead` (новая) |
| Sense Life | 166 | `coc:spell:sense-life` |
| Seraph’s Glory (Dreamlands) | 166 | `coc:spell:seraphs-glory` (новая) |
| Serviceable Villein (Dreamlands) | 166 | `coc:spell:serviceable-villein` (новая) |
| Sever the Affable Bonds | 166 | `coc:spell:sever-the-affable-bonds` (новая) |
| Shadow of Nyarlathotep | 166 | `coc:spell:shadow-of-nyarlathotep` (новая) |
| Shadow Void | 167 | `coc:spell:shadow-void` (новая) |
| Shrivelling | 167 | `coc:spell:shrivelling` |
| Silver Spray, The (Dreamlands) | 167 | `coc:spell:silver-spray` (новая) |
| Siren’s Song (Folk) | 168 | `coc:spell:sirens-song` |
| Skin of the Bear (Folk) | 168 | `coc:spell:skin-of-the-bear-folk` (новая) |
| Skin Walker | 168 | `coc:spell:skin-walker` |
| Solar Gaze | 168 | `coc:spell:solar-gaze` |
| Snare Dreamer | 169 | `coc:spell:snare-dreamer` (новая) |
| Song of Glissande (Dreamlands) | 169 | `coc:spell:song-of-glissande` (новая) |
| Song of Hastur | 169 | `coc:spell:song-of-hastur` |
| Soul Extraction | 169 | `coc:spell:soul-extraction` (новая) |
| Soul Singing (Folk) | 171 | `coc:spell:soul-singing` |
| Soul Stealer (Dreamlands) | 171 | `coc:spell:soul-stealer` (новая) |
| Soul-Trap | 171 | `coc:spell:soul-trap` (новая) |
| Speak with The Waiting Dark (Call Cyaegha variant) | 172 | `coc:spell:speak-with-the-waiting-dark` (новая) |
| Spectral Razor | 172 | `coc:spell:spectral-razor` |
| Spell that was Lost with Ib, The (Dreamlands) | 172 | `coc:spell:spell-that-was-lost-with-ib` (новая) |
| Spiral of Suth (Dreamlands) | 172 | `coc:spell:spiral-of-suth` (новая) |
| Spirit Summoning | 172 | `coc:spell:spirit-summoning` |
| Stability (Dreamlands) | 173 | `coc:spell:stability` (новая) |
| Steal Life | 173 | `coc:spell:steal-life` |
| Steal Life’s Blood | 174 | `coc:spell:steal-lifes-blood` (новая) |
| Stop Heart | 174 | `coc:spell:stop-heart` |
| Strike Blind | 174 | `coc:spell:strike-blind` |
| Stupefying Blast (Dreamlands) | 174 | `coc:spell:stupefying-blast` |
| Summon Plague (Dreamlands) | 177 | `coc:spell:summon-plague` (новая) |
| Sundering Hurler (Dreamlands) | 178 | `coc:spell:sundering-hurler` (новая) |
| Swelling Torment | 178 | `coc:spell:swelling-torment` |
| Telepathy | 178 | `coc:spell:telepathy` |
| Temporal Rip | 178 | `coc:spell:temporal-rip` |
| Throth’s Stalwart (Dreamlands) | 179 | `coc:spell:throths-stalwart` (новая) |
| Time Gate | 179 | `coc:spell:time-gate` |
| Time Trap | 179 | `coc:spell:time-trap` |
| Touch of Decay | 179 | `coc:spell:touch-of-decay` |
| Trance | 181 | `coc:spell:trance` (новая) |
| Transfer Body Part | 181 | `coc:spell:transfer-body-part` (новая) |
| Transfer Organ | 181 | `coc:spell:transfer-organ` |
| Transfer Soul | 181 | `coc:spell:transfer-soul` (новая) |
| Transformation | 182 | `coc:spell:transformation` (новая) |
| Unmask Demon | 182 | `coc:spell:unmask-demon` (новая) |
| Unspeakable Promise, The | 182 | `coc:spell:unspeakable-promise` |
| Utterance of Bile | 182 | `coc:spell:utterance-of-bile` |
| Vanish (Gate Boxes variant) | 183 | `coc:spell:vanish` |
| Venomous Glance | 183 | `coc:spell:venomous-glance` |
| View Gate | 183 | `coc:spell:view-gate` |
| Viridian Wind (Dreamlands) | 183 | `coc:spell:viridian-wind` (новая) |
| Voice of Ra | 186 | `coc:spell:voice-of-ra` |
| Voice Thoughts | 186 | `coc:spell:voice-thoughts` (новая) |
| Voorish Sign | 186 | `coc:spell:voorish-sign` |
| Vortex of Far Journeying (Dreamlands) | 186 | `coc:spell:vortex-of-far-journeying` (новая) |
| Waking Slumber, The | 186 | `coc:spell:waking-slumber` (новая) |
| Wandering Soul | 187 | `coc:spell:wandering-soul` |
| Ward of Anubis | 187 | `coc:spell:ward-of-anubis` |
| Warding | 187 | `coc:spell:warding` |
| Warding Sign | 188 | `coc:spell:warding-sign` |
| Warding the Eye | 188 | `coc:spell:warding-the-eye` (новая) |
| Warmth of Mind | 188 | `coc:spell:warmth-of-mind` (новая) |
| Wasting Curse, The | 189 | `coc:spell:wasting-curse` (новая) |
| Wave of Oblivion | 189 | `coc:spell:wave-of-oblivion` |
| Whirligig (Dreamlands) | 189 | `coc:spell:whirligig` (новая) |
| White Web of Soren (Dreamlands) | 189 | `coc:spell:white-web-of-soren` (новая) |
| Winds of Desolation (Folk) | 190 | `coc:spell:winds-of-desolation-folk` |
| Wither Limb | 190 | `coc:spell:wither-limb` |
| Woeful Itch (Dreamlands) | 190 | `coc:spell:woeful-itch` (новая) |
| Words of Power | 191 | `coc:spell:words-of-power` |
| Worms | 191 | `coc:spell:worms` (новая) |
| Wrack | 191 | `coc:spell:wrack` |
| Wrath of Ages | 191 | `coc:spell:wrath-of-ages` (новая) |
| Wrath of Pazzuzu | 191 | `coc:spell:wrath-of-pazzuzu` |
| Yellow Sign, The | 192 | `coc:spell:yellow-sign` |
| Yellow Spirit-Leap Seal (Folk) | 192 | `coc:spell:yellow-spirit-leap-seal-folk` |
| Zymoticism | 192 | `coc:spell:zymoticism` (новая) |

## Общие разделы, врезки и таблицы гл. 4

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Spell Categories (списки заклинаний по категориям), Entry Format | 23–25 | списки категорий GG сверены с заголовками статей гл. 4 (все заклинания списков — в базе); формат статьи и категории GG — часть gg-rules (`coc:rule:gg-spell-entry-format`, если её заведёт gg-rules); у записей `category` по 14 типам Р-66 |
| Call, Contact, and Summon Disambiguation | 25 | `coc:rule:call-contact-and-summon-disambiguation` |
| таблица побочных эффектов 1D8 (Activation) | 27 | `coc:spell:activation` (в описании) |
| Weather Components (таблица, Alter Weather) | 27 | `coc:spell:alter-weather` |
| врезка-профиль Flesh Thing, Standard Creature | 28 | `coc:spell:animate-flesh-thing` (профиль в описании) |
| врезка Star-Seeds | 34 | `coc:spell:awaking-dispelling-the-god-within` (в описании) |
| врезка-профиль Spectral Hunter | 37 | `coc:spell:become-spectral-hunter`, `coc:creature:spectral-hunter` |
| Binding Spells (общие правила) и Summary of Monster Binding Spell | 41–42 | `coc:spell:summon-bind` и записи `coc:spell:summon-bind-*` (Bind Byakhee … Bind Star Vampire — их псевдонимы) |
| врезка-профиль Human Hybrid Tindalosian | 48 | `coc:creature:tindalosian-hybrids` (ссылка из `coc:spell:brew-elixir-of-life`) |
| Call Deity Spells (общие правила) | 53–54 | `coc:spell:call-deity`; цена и время повторены в новых записях вызова |
| врезка Circle Spell Variations | 65 | предложение: абзац в `coc:spell:circle-of-warding` (proposals-gg-spells.json) |
| врезка Conjuration of The Turua (с профилем туруа) | 71 | часть gg-rules (не эта часть) |
| Contact Deity Spells (общие правила) | 72 | `coc:spell:contact-deity`; цена и время повторены в новых записях связи |
| врезка Avatars of Nyarlathotep | 76 | `coc:spell:contact-nyarlathotep` + предложение: список аватар |
| Contact Monster Spells (общие правила) | 77 | `coc:spell:contact-spells` |
| врезка Shamballah | 79 | `coc:spell:contact-masters` (в описании) |
| врезка-пример NPC: Hestia Locksby | 85 | часть gg-rules (не эта часть) |
| врезка-профиль Flesh Creeper | 87 | `coc:spell:create-flesh-creeper` (профиль в описании) |
| Dismiss Deity (Spells, общие правила) | 96–97 | `coc:spell:dismiss-deity` |
| врезка-профиль Effigy of Hate | 103 | `coc:spell:effigy-of-hate` (профиль текстом в описании) |
| Enchantment Spells (общие правила) | 106 | `coc:spell:enchant-item` |
| Table 1: Gate Creation and Travel Costs; врезка Gates: Sample Locations and Distances | 121–123 | `coc:spell:create-gate` (таблицы XII–XIII «Книги хранителя» с теми же числами) |
| врезка The Curse of Immortality | 129 | `coc:spell:immortality` (в описании) |
| врезка-пример NPC: Thomas Davenport | 133 | часть gg-rules (не эта часть) |
| врезка-профиль Fog Spawn | 155 | `coc:spell:quicken-fog-spawn`; профиль существа — `masks-of-nyarlathotep-en/creature/fog-spawn` (по «Маскам»); профиль GG не сверен — см. «Не взято» |
| таблица кошмаров Nightmare Effect (Ravening Madness) | 156–157 | `coc:spell:ravening-madness` |
| Summoning Spells (общие правила) | 174 | `coc:spell:summon-bind` |
| врезка Summary of Monster Summoning Spells: Summon Baka | 175 | `coc:spell:summon-baka` (новая) |
| — там же: Summon Brother of Chaugnar Faugn, Summon Byakhee, Summon Dark Young, Summon Deep One, Summon Dhole, Summon Dimensional Shambler, Summon Fire Vampire | 175–176 | `coc:spell:summon-bind-brother-of-chaugnar-faugn`, `…-byakhee`, `…-dark-young`, `…-deep-one`, `…-dhole`, `…-dimensional-shambler`, `…-fire-vampire` |
| — там же: Summon Greater Desh | 176 | `coc:spell:summon-greater-desh` (новая) |
| — там же: Summon Hunting Horror, Summon Nightgaunt, Summon Servitor of The Outer Gods | 176–177 | `coc:spell:summon-bind-hunting-horror`, `…-nightgaunt`, `…-servitor-of-the-outer-gods` |
| — там же: Summon Shoggoth | 177 | `coc:spell:summon-shoggoth` (новая) |
| — там же: Summon Star Vampire | 177 | `coc:spell:summon-bind-star-vampire` |
| Table 2: Time Gate Creation and Travel Costs | 180 | `coc:spell:time-gate` (таблица — через «16 км = 10 лет» по «Книге хранителя») |
| врезка-пример NPC: Niels-Viggo Schou | 185 | часть gg-rules (не эта часть) |
| таблица Winds of Desolation Strength | 190 | `coc:spell:winds-of-desolation-folk` (таблица уже в описании; источник GG — предложение) |
| таблица Fungus Timeline (Zymoticism) | 193 | `coc:spell:zymoticism` (в описании) |

## Указатель

Указатель (Index), с. 195–200: все названия заклинаний указателя есть в базе (проверено скриптом по `name.en` и `aliases`; «Contact Master» — псевдоним `coc:spell:contact-masters`, «Posses Corpse» — опечатка указателя для `coc:spell:possess-corpse`). Прочие статьи указателя — темы глав 1–2 и врезки (Adjusting Spells, Altar, Amulets, Are the Stars Right, Astronomical Factors, Athame, Autumn Equinox, Beltane, Besom, Blue Moon, Bolline, Cauldron, Censer, Fire Festivals, Flawed Spells, Folk Magic, Grimoires, Hale-Bopp Comet, Halley’s Comet, Imbolc, Ley Lines, Limbo, Lughnasad, Magical Residue, Magical Tools, Pagan, Planetary Conjunctions, Sacrifice, Samhain, Solar Festivals, Spell Components, Spell Names, Spring Equinox, Summer Solstice, Talismans, Total Solar Eclipse, Wand, Winter Solstice, Working Space, Conjuration of The Turua/Turua, NPC Hestia Locksby, Thomas Davenport, Niels-Viggo Schou) — часть gg-rules; существа и врезки гл. 4 (Avatars of Nyarlathotep, Circle Spell Variations, Flesh Creeper, Flesh Thing, Fog-Spawn, Nightmare Effect, Shamballah, Spectral Hunter, Star-Seeds) — в таблице врезок выше.

## Предложения к чужим записям

`checks/20261114-completeness-fix/proposals-gg-spells.json` — 33 предложения к 16 записям (пробный прогон `pipeline/integrate/apply.py --dry-run` проходит):

- источник Grand Grimoire (`append sources`) для 14 записей, у которых его не было: `balk-brood` (с. 34), `become-spectral` (37), `build-carcosa` (53), `call-the-black` (61), `curse-of-the-stone` (92), `disembodiment` (96), `dowsing-folk` (98), `free-hastur` (119), `ill-luck-folk` (128), `enchant-stone-tablet` (111), `nyhargo-dirge` (146), `poison-blood-folk` (150), `spirit-summoning` (172), `winds-of-desolation-folk` (190);
- `curse-of-the-stone`, `enchant-stone-tablet`: были только названиями из «Побега из Иннсмута» (флаг `incomplete`) — цена, время, описание, псевдонимы и ссылки по GG (Р-41), флаг `incomplete` снимается;
- `call-the-black`: расхождение цены «Дверей во тьму» (8 ПМ, 1 МОЩ) и GG (20 ПМ, 10 МОЩ) — в `quality.notes` (Р-51), числа записи не меняются; три альтернативных названия GG;
- `free-hastur`: время сотворения по GG (в «Лохмотьях короля» не указано);
- `contact-nyarlathotep`: список аватар из врезки «Avatars of Nyarlathotep» (с. 76);
- `circle-of-warding`: врезка «Circle Spell Variations» (с. 65).

## Опечатки и сомнения книги

- Bestow Karma (Folk), с. 40: в таблице цены после «1–5 years» напечатано «2–25 years» (границы растут в 5 раз; вероятно, «5–25») — `errata` в `coc:spell:bestow-karma-folk`, значение как напечатано.
- Fire Dance, с. 117: строка «Casting time: instantaneous», а в тексте — «одна минута на каждый ПМ» — `errata` в `coc:spell:fire-dance`.
- Awaken The Great Tortoise, с. 32: шанс Шудде-Мьелла «выше 5 баллов», но пример начинается с «5% при 5» — пометка в `quality.notes`.
- Call (The) Skinless One, с. 59: потеря Рассудка не напечатана — пометка.
- Cascades of Florin, с. 62: список альтернативных названий оборван («Bright Waters, The Churning Draining» без точки) — пометка.
- Enchant Animal Effigy, с. 107: «три примера», а перечислены четыре — взяты все, пометка.
- Look to the Future, с. 138: «не меньше одиннадцати участников, вносящих ПМ», хотя участники тратят МОЩ — пометка.
- Channeling God: в списке категорий «Channelling God» — псевдоним.
- Указатель и список категорий: «Posses Corpse» вместо Possess Corpse; «Contact Master» вместо Contact Masters (добавлено псевдонимом).
- Раздел «Deeper magic» у Enchant Flesh, Graft Flesh и Koshchey’s Death не описывает усиленного действия (редкость заклинания, происхождение) — перенесено как напечатано, пометка.
- Температуры в °F (Bolonath’s Furnace, Katarien’s Heat Wave) оставлены как в книге (шкала урона привязана к °F), с пересчётом в °C там, где это не искажает правило.

## Не взято (с причиной)

- Профиль Fog Spawn из врезки GG (с. 155): в базе есть существо `masks-of-nyarlathotep-en/creature/fog-spawn` по «Маскам»; профиль GG не сверен и не перенесён — запись чужая, нужен выбор владельца (заводить ли общую `coc:creature:fog-spawn` с профилем GG).
- Профиль Effigy of Hate (с. 103) перенесён только текстом в описание `coc:spell:effigy-of-hate`: отдельной записи существа нет, а `kb/creatures` этой части не принадлежит.
- Врезки Conjuration of The Turua (с. 71, с профилем туруа), NPC Hestia Locksby, Thomas Davenport, Niels-Viggo Schou, категории заклинаний GG и формат статьи (с. 23–25) — часть gg-rules по разделению задания.
- Vach-Viraj — не в Grand Grimoire, часть mm2.

## Кандидаты в новые записи (не заведены)

Существа без записи в базе, которых называют новые заклинания: аватары Ньярлатхотепа Рогатый человек (Horned Man), Эль Негро, Ньярлатофис, Пазузу; Изумрудный лама (аватар Хастура); Ла Йорона (аватар Шуб-Ниггурат); М’нагала, Маппо-но Рюдзин, Бокруг, Отуйег, Владыка Кота; бака; Муза из-за грани и Проявление вдохновения («Nameless Horrors»); призрачные существа Иба; Идол ненависти (профиль есть, с. 103).
