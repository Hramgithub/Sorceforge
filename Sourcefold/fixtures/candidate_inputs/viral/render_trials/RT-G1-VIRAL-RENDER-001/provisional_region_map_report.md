# Provisional Region Map Report - PRM-G1-VIRAL-001

Report id: `PRM-G1-VIRAL-001`

Status: `valid_for_review`

Created: 2026-07-18

Actor: OpenClaw / Codex

Authorization id: `BA-G1-VIRAL-REGIONMAP-001`

Schema/taxonomy: `provisional-region-map-v0`

Coordinate space: rendered PNG pixels, width 2550, height 3300; normalized boxes use `[x/W, y/H, w/W, h/H]`.

Boundary: all region IDs and boxes are provisional visual annotations only. They are not stable/canonical IDs, accepted anchors, accepted coordinates, accepted reading order, OCR routing, source evidence, QA, benchmark, fixture, source-profile acceptance, translation, proofreading, implementation, `doc_map`, `content_map`, `art_map`, or `pre_ocr_map_bundle`.

Method: visual annotation from already-rendered PNG/contact-sheet evidence and predecessor reports only. The PDF was not opened, parsed, rehashed, recounted, or inspected. No OCR, transcription, copied text, or PDF text-layer extraction was performed.

Predecessors:

- Accepted protocol revision: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- Accepted protocol file blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`
- Selected-page manifest: `SPM-G1-VIRAL-001`
- Render trial: `RT-G1-VIRAL-RENDER-001`
- Render output manifest SHA-256: `622C0D91B45C84CBCA699F8AEE680F7A738FA248A16C8BA83A1F67B603EEFFAC`
- Visual sanity report: `VSR-G1-VIRAL-001`
- Visual sanity report SHA-256: `7904D5B66EECED5385CDB7AC0BD74935DA5A63ACBAA29875B8B11138ED5E7439`
- Contact sheet SHA-256: `3DAB3C5F9864B2BA12CDA4113AA1CD6BCF3B3E570DB773955248CD3F88B9733A`
- Page inventory report: `PIR-G1-VIRAL-001`
- Page inventory report SHA-256: `2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA`
- Page map/model report: `PMR-G1-VIRAL-001`
- Page map/model report SHA-256: `72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F`

Region records:

| Page | Provisional region id | Image id | Coarse class | Candidate layer projection | Box px `[x,y,w,h]` | Box norm `[x,y,w,h]` | Observation state | Uncertainty | Notes |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `PRM-G1-VIRAL-001-P001-R01` | `IMG-G1-VIRAL-RENDER-001-P001` | `art_image` | `art_map_candidate` | `[0,0,2550,3300]` | `[0.0,0.0,1.0,1.0]` | `observed` | `medium` | full-page visual field; provisional only |
| 1 | `PRM-G1-VIRAL-001-P001-R02` | `IMG-G1-VIRAL-RENDER-001-P001` | `title_heading_like` | `content_map_candidate` | `[760,260,1050,760]` | `[0.298,0.0788,0.4118,0.2303]` | `observed` | `medium` | large title/logo area; no text copied |
| 1 | `PRM-G1-VIRAL-001-P001-R03` | `IMG-G1-VIRAL-RENDER-001-P001` | `mixed` | `content_map_candidate` | `[380,2750,1750,360]` | `[0.149,0.8333,0.6863,0.1091]` | `observed` | `medium` | footer/title-credit-like block |
| 2 | `PRM-G1-VIRAL-001-P002-R01` | `IMG-G1-VIRAL-RENDER-001-P002` | `text_like` | `content_map_candidate` | `[520,350,1500,2200]` | `[0.2039,0.1061,0.5882,0.6667]` | `observed` | `low` | centered credits/legal-like text block |
| 2 | `PRM-G1-VIRAL-001-P002-R02` | `IMG-G1-VIRAL-RENDER-001-P002` | `mixed` | `content_map_candidate` | `[520,2480,1500,420]` | `[0.2039,0.7515,0.5882,0.1273]` | `observed` | `medium` | boxed/footer legal-like block |
| 3 | `PRM-G1-VIRAL-001-P003-R01` | `IMG-G1-VIRAL-RENDER-001-P003` | `title_heading_like` | `content_map_candidate` | `[590,180,1350,700]` | `[0.2314,0.0545,0.5294,0.2121]` | `observed` | `medium` | large heading/logo area |
| 3 | `PRM-G1-VIRAL-001-P003-R02` | `IMG-G1-VIRAL-RENDER-001-P003` | `text_like` | `content_map_candidate` | `[460,860,1650,2050]` | `[0.1804,0.2606,0.6471,0.6212]` | `observed` | `medium` | main body-like text field |
| 4 | `PRM-G1-VIRAL-001-P004-R01` | `IMG-G1-VIRAL-RENDER-001-P004` | `mixed` | `doc_map_candidate` | `[300,260,1950,2600]` | `[0.1176,0.0788,0.7647,0.7879]` | `observed` | `medium` | tilted document/inset page area |
| 4 | `PRM-G1-VIRAL-001-P004-R02` | `IMG-G1-VIRAL-RENDER-001-P004` | `title_heading_like` | `content_map_candidate` | `[820,500,900,300]` | `[0.3216,0.1515,0.3529,0.0909]` | `observed` | `medium` | warning/title-like area |
| 4 | `PRM-G1-VIRAL-001-P004-R03` | `IMG-G1-VIRAL-RENDER-001-P004` | `text_like` | `content_map_candidate` | `[560,860,1450,1750]` | `[0.2196,0.2606,0.5686,0.5303]` | `observed` | `medium` | body-like text within inset |
| 5 | `PRM-G1-VIRAL-001-P005-R01` | `IMG-G1-VIRAL-RENDER-001-P005` | `title_heading_like` | `content_map_candidate` | `[920,260,750,280]` | `[0.3608,0.0788,0.2941,0.0848]` | `observed` | `low` | contents heading-like area |
| 5 | `PRM-G1-VIRAL-001-P005-R02` | `IMG-G1-VIRAL-RENDER-001-P005` | `table_list_like` | `content_map_candidate` | `[260,600,2050,2300]` | `[0.102,0.1818,0.8039,0.697]` | `observed` | `medium` | two-column contents/list-like region |
| 5 | `PRM-G1-VIRAL-001-P005-R03` | `IMG-G1-VIRAL-RENDER-001-P005` | `margin_page_number_like` | `doc_map_candidate` | `[2300,2920,180,160]` | `[0.902,0.8848,0.0706,0.0485]` | `observed` | `low` | page marker-like visual |
| 6 | `PRM-G1-VIRAL-001-P006-R01` | `IMG-G1-VIRAL-RENDER-001-P006` | `art_image` | `art_map_candidate` | `[0,0,2550,1550]` | `[0.0,0.0,1.0,0.4697]` | `observed` | `medium` | large background/intro art |
| 6 | `PRM-G1-VIRAL-001-P006-R02` | `IMG-G1-VIRAL-RENDER-001-P006` | `title_heading_like` | `content_map_candidate` | `[200,320,950,360]` | `[0.0784,0.097,0.3725,0.1091]` | `observed` | `low` | introduction heading-like area |
| 6 | `PRM-G1-VIRAL-001-P006-R03` | `IMG-G1-VIRAL-RENDER-001-P006` | `text_like` | `content_map_candidate` | `[220,1550,2100,1400]` | `[0.0863,0.4697,0.8235,0.4242]` | `observed` | `medium` | lower body text area |
| 7 | `PRM-G1-VIRAL-001-P007-R01` | `IMG-G1-VIRAL-RENDER-001-P007` | `title_heading_like` | `content_map_candidate` | `[110,120,950,650]` | `[0.0431,0.0364,0.3725,0.197]` | `observed` | `medium` | large brand/title-like block |
| 7 | `PRM-G1-VIRAL-001-P007-R02` | `IMG-G1-VIRAL-RENDER-001-P007` | `art_image` | `art_map_candidate` | `[1180,340,1050,1720]` | `[0.4627,0.103,0.4118,0.5212]` | `observed` | `low` | portrait/image area |
| 7 | `PRM-G1-VIRAL-001-P007-R03` | `IMG-G1-VIRAL-RENDER-001-P007` | `mixed` | `content_map_candidate` | `[130,1050,850,520]` | `[0.051,0.3182,0.3333,0.1576]` | `observed` | `medium` | social/list/card-like visual block |
| 7 | `PRM-G1-VIRAL-001-P007-R04` | `IMG-G1-VIRAL-RENDER-001-P007` | `text_like` | `content_map_candidate` | `[140,2200,2200,800]` | `[0.0549,0.6667,0.8627,0.2424]` | `observed` | `medium` | profile body-like text area |
| 8 | `PRM-G1-VIRAL-001-P008-R01` | `IMG-G1-VIRAL-RENDER-001-P008` | `text_like` | `content_map_candidate` | `[160,250,2200,1250]` | `[0.0627,0.0758,0.8627,0.3788]` | `observed` | `medium` | upper multi-column text-like area |
| 8 | `PRM-G1-VIRAL-001-P008-R02` | `IMG-G1-VIRAL-RENDER-001-P008` | `art_image` | `art_map_candidate` | `[520,1500,900,850]` | `[0.2039,0.4545,0.3529,0.2576]` | `observed` | `low` | portrait/image area |
| 8 | `PRM-G1-VIRAL-001-P008-R03` | `IMG-G1-VIRAL-RENDER-001-P008` | `art_image` | `art_map_candidate` | `[1600,2250,720,620]` | `[0.6275,0.6818,0.2824,0.1879]` | `observed` | `medium` | object/image area |
| 8 | `PRM-G1-VIRAL-001-P008-R04` | `IMG-G1-VIRAL-RENDER-001-P008` | `text_like` | `content_map_candidate` | `[160,2300,1400,720]` | `[0.0627,0.697,0.549,0.2182]` | `observed` | `medium` | lower text-like area |
| 9 | `PRM-G1-VIRAL-001-P009-R01` | `IMG-G1-VIRAL-RENDER-001-P009` | `art_image` | `art_map_candidate` | `[180,260,1030,920]` | `[0.0706,0.0788,0.4039,0.2788]` | `observed` | `low` | left portrait/image area |
| 9 | `PRM-G1-VIRAL-001-P009-R02` | `IMG-G1-VIRAL-RENDER-001-P009` | `art_image` | `art_map_candidate` | `[1320,260,1030,920]` | `[0.5176,0.0788,0.4039,0.2788]` | `observed` | `low` | right portrait/image area |
| 9 | `PRM-G1-VIRAL-001-P009-R03` | `IMG-G1-VIRAL-RENDER-001-P009` | `text_like` | `content_map_candidate` | `[180,1200,1030,1650]` | `[0.0706,0.3636,0.4039,0.5]` | `observed` | `medium` | left profile text-like block |
| 9 | `PRM-G1-VIRAL-001-P009-R04` | `IMG-G1-VIRAL-RENDER-001-P009` | `text_like` | `content_map_candidate` | `[1320,1200,1030,1650]` | `[0.5176,0.3636,0.4039,0.5]` | `observed` | `medium` | right profile text-like block |
| 10 | `PRM-G1-VIRAL-001-P010-R01` | `IMG-G1-VIRAL-RENDER-001-P010` | `text_like` | `content_map_candidate` | `[230,220,910,460]` | `[0.0902,0.0667,0.3569,0.1394]` | `observed` | `medium` | upper-left text-like block |
| 10 | `PRM-G1-VIRAL-001-P010-R02` | `IMG-G1-VIRAL-RENDER-001-P010` | `text_like` | `content_map_candidate` | `[1380,220,930,460]` | `[0.5412,0.0667,0.3647,0.1394]` | `observed` | `medium` | upper-right text-like block |
| 10 | `PRM-G1-VIRAL-001-P010-R03` | `IMG-G1-VIRAL-RENDER-001-P010` | `art_image` | `art_map_candidate` | `[230,700,920,1450]` | `[0.0902,0.2121,0.3608,0.4394]` | `observed` | `low` | left portrait/image area |
| 10 | `PRM-G1-VIRAL-001-P010-R04` | `IMG-G1-VIRAL-RENDER-001-P010` | `art_image` | `art_map_candidate` | `[1390,700,920,1450]` | `[0.5451,0.2121,0.3608,0.4394]` | `observed` | `low` | right portrait/image area |
| 10 | `PRM-G1-VIRAL-001-P010-R05` | `IMG-G1-VIRAL-RENDER-001-P010` | `text_like` | `content_map_candidate` | `[230,2180,2080,650]` | `[0.0902,0.6606,0.8157,0.197]` | `observed` | `medium` | lower profile text-like area |
| 11 | `PRM-G1-VIRAL-001-P011-R01` | `IMG-G1-VIRAL-RENDER-001-P011` | `text_like` | `content_map_candidate` | `[150,280,820,1750]` | `[0.0588,0.0848,0.3216,0.5303]` | `observed` | `medium` | left body-like text blocks |
| 11 | `PRM-G1-VIRAL-001-P011-R02` | `IMG-G1-VIRAL-RENDER-001-P011` | `art_image` | `art_map_candidate` | `[1040,470,1050,1250]` | `[0.4078,0.1424,0.4118,0.3788]` | `observed` | `low` | large portrait/image area |
| 11 | `PRM-G1-VIRAL-001-P011-R03` | `IMG-G1-VIRAL-RENDER-001-P011` | `art_image` | `art_map_candidate` | `[150,2220,820,650]` | `[0.0588,0.6727,0.3216,0.197]` | `observed` | `medium` | lower-left screen/image area |
| 11 | `PRM-G1-VIRAL-001-P011-R04` | `IMG-G1-VIRAL-RENDER-001-P011` | `text_like` | `content_map_candidate` | `[1040,1780,1200,1150]` | `[0.4078,0.5394,0.4706,0.3485]` | `observed` | `medium` | right/lower body-like text area |
| 12 | `PRM-G1-VIRAL-001-P012-R01` | `IMG-G1-VIRAL-RENDER-001-P012` | `text_like` | `content_map_candidate` | `[160,230,1000,2700]` | `[0.0627,0.0697,0.3922,0.8182]` | `observed` | `medium` | left column-like text area |
| 12 | `PRM-G1-VIRAL-001-P012-R02` | `IMG-G1-VIRAL-RENDER-001-P012` | `text_like` | `content_map_candidate` | `[1290,230,1060,2700]` | `[0.5059,0.0697,0.4157,0.8182]` | `observed` | `medium` | right column-like text area |
| 13 | `PRM-G1-VIRAL-001-P013-R01` | `IMG-G1-VIRAL-RENDER-001-P013` | `text_like` | `content_map_candidate` | `[260,230,1900,520]` | `[0.102,0.0697,0.7451,0.1576]` | `observed` | `medium` | upper text-like area |
| 13 | `PRM-G1-VIRAL-001-P013-R02` | `IMG-G1-VIRAL-RENDER-001-P013` | `art_image` | `art_map_candidate` | `[250,760,2050,2200]` | `[0.098,0.2303,0.8039,0.6667]` | `observed` | `low` | dominant full-page image area |
| 14 | `PRM-G1-VIRAL-001-P014-R01` | `IMG-G1-VIRAL-RENDER-001-P014` | `text_like` | `content_map_candidate` | `[140,330,980,2500]` | `[0.0549,0.1,0.3843,0.7576]` | `observed` | `medium` | left gear/list-like text column |
| 14 | `PRM-G1-VIRAL-001-P014-R02` | `IMG-G1-VIRAL-RENDER-001-P014` | `text_like` | `content_map_candidate` | `[1290,330,980,1600]` | `[0.5059,0.1,0.3843,0.4848]` | `observed` | `medium` | right text/list-like column |
| 14 | `PRM-G1-VIRAL-001-P014-R03` | `IMG-G1-VIRAL-RENDER-001-P014` | `art_image` | `art_map_candidate` | `[1370,2100,850,660]` | `[0.5373,0.6364,0.3333,0.2]` | `observed` | `medium` | lower-right product/image area |
| 15 | `PRM-G1-VIRAL-001-P015-R01` | `IMG-G1-VIRAL-RENDER-001-P015` | `table_list_like` | `content_map_candidate` | `[180,300,1050,2600]` | `[0.0706,0.0909,0.4118,0.7879]` | `observed` | `medium` | timeline/list-like left column |
| 15 | `PRM-G1-VIRAL-001-P015-R02` | `IMG-G1-VIRAL-RENDER-001-P015` | `art_image` | `art_map_candidate` | `[1360,440,900,860]` | `[0.5333,0.1333,0.3529,0.2606]` | `observed` | `medium` | upper-right image area |
| 15 | `PRM-G1-VIRAL-001-P015-R03` | `IMG-G1-VIRAL-RENDER-001-P015` | `text_like` | `content_map_candidate` | `[1360,1370,900,1450]` | `[0.5333,0.4152,0.3529,0.4394]` | `observed` | `medium` | lower-right history text-like block |
| 16 | `PRM-G1-VIRAL-001-P016-R01` | `IMG-G1-VIRAL-RENDER-001-P016` | `text_like` | `content_map_candidate` | `[160,250,1000,2700]` | `[0.0627,0.0758,0.3922,0.8182]` | `observed` | `medium` | left body text-like column |
| 16 | `PRM-G1-VIRAL-001-P016-R02` | `IMG-G1-VIRAL-RENDER-001-P016` | `text_like` | `content_map_candidate` | `[1290,250,1000,2700]` | `[0.5059,0.0758,0.3922,0.8182]` | `observed` | `medium` | right body text-like column |
| 17 | `PRM-G1-VIRAL-001-P017-R01` | `IMG-G1-VIRAL-RENDER-001-P017` | `art_image` | `art_map_candidate` | `[0,0,2550,1200]` | `[0.0,0.0,1.0,0.3636]` | `observed` | `low` | large section-opener image |
| 17 | `PRM-G1-VIRAL-001-P017-R02` | `IMG-G1-VIRAL-RENDER-001-P017` | `title_heading_like` | `content_map_candidate` | `[260,260,1400,360]` | `[0.102,0.0788,0.549,0.1091]` | `observed` | `medium` | large heading/title-like overlay area |
| 17 | `PRM-G1-VIRAL-001-P017-R03` | `IMG-G1-VIRAL-RENDER-001-P017` | `text_like` | `content_map_candidate` | `[250,1330,2100,1600]` | `[0.098,0.403,0.8235,0.4848]` | `observed` | `medium` | lower multi-column text-like area |
| 18 | `PRM-G1-VIRAL-001-P018-R01` | `IMG-G1-VIRAL-RENDER-001-P018` | `title_heading_like` | `content_map_candidate` | `[220,260,760,240]` | `[0.0863,0.0788,0.298,0.0727]` | `observed` | `medium` | welcome/heading-like area |
| 18 | `PRM-G1-VIRAL-001-P018-R02` | `IMG-G1-VIRAL-RENDER-001-P018` | `text_like` | `content_map_candidate` | `[200,520,950,2350]` | `[0.0784,0.1576,0.3725,0.7121]` | `observed` | `medium` | left text-like column |
| 18 | `PRM-G1-VIRAL-001-P018-R03` | `IMG-G1-VIRAL-RENDER-001-P018` | `text_like` | `content_map_candidate` | `[1320,520,950,2350]` | `[0.5176,0.1576,0.3725,0.7121]` | `observed` | `medium` | right text-like column |
| 19 | `PRM-G1-VIRAL-001-P019-R01` | `IMG-G1-VIRAL-RENDER-001-P019` | `art_image` | `art_map_candidate` | `[240,300,930,1400]` | `[0.0941,0.0909,0.3647,0.4242]` | `observed` | `low` | portrait/image area |
| 19 | `PRM-G1-VIRAL-001-P019-R02` | `IMG-G1-VIRAL-RENDER-001-P019` | `text_like` | `content_map_candidate` | `[240,1760,930,520]` | `[0.0941,0.5333,0.3647,0.1576]` | `observed` | `medium` | caption/side text-like area |
| 19 | `PRM-G1-VIRAL-001-P019-R03` | `IMG-G1-VIRAL-RENDER-001-P019` | `text_like` | `content_map_candidate` | `[1290,300,1020,2450]` | `[0.5059,0.0909,0.4,0.7424]` | `observed` | `medium` | right body text-like area |
| 20 | `PRM-G1-VIRAL-001-P020-R01` | `IMG-G1-VIRAL-RENDER-001-P020` | `title_heading_like` | `content_map_candidate` | `[1280,300,820,260]` | `[0.502,0.0909,0.3216,0.0788]` | `observed` | `medium` | heading-like area |
| 20 | `PRM-G1-VIRAL-001-P020-R02` | `IMG-G1-VIRAL-RENDER-001-P020` | `text_like` | `content_map_candidate` | `[250,520,2000,1500]` | `[0.098,0.1576,0.7843,0.4545]` | `observed` | `medium` | upper body text-like area |
| 20 | `PRM-G1-VIRAL-001-P020-R03` | `IMG-G1-VIRAL-RENDER-001-P020` | `art_image` | `art_map_candidate` | `[260,2180,900,650]` | `[0.102,0.6606,0.3529,0.197]` | `observed` | `medium` | lower-left scenic/image area |
| 20 | `PRM-G1-VIRAL-001-P020-R04` | `IMG-G1-VIRAL-RENDER-001-P020` | `mixed` | `content_map_candidate` | `[1440,2150,850,700]` | `[0.5647,0.6515,0.3333,0.2121]` | `observed` | `medium` | lower-right sidebar/list-like area |

Invalidation: this report is stale if source path/hash, protocol revision/blob, authorization, SPM, RT, render output manifest/hash, any page PNG/hash, VSR, contact sheet/hash, PIR, PMR, render config, schema/taxonomy/coordinate model, tool/reviewer identity, observation rules, or authority model changes.

Next bounded work: review PRM-G1-VIRAL-001. A later action may request separate bundle-freezing, OCR, benchmark, QA, fixture, source acceptance, translation, proofreading, or implementation authorization, but this report authorizes none of those actions.
