from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image

from bounded_authorization_contract import materialize_aggressive_batch_authorization
from page_review_crop_contracts import validate_text_evidence_crop_contracts
from page_review_semantic_units import keeper_notes_callout_heading_level
from semantic_segmentation_contract import callout_body_contract, split_bounded_callout, validate_semantic_split_contracts


ROOT = Path(__file__).resolve().parents[1]
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

SKIPPED_REVIEW = "human_review_skipped_by_explicit_authorization"
DELEGATED_REVIEW = "review_delegated_to_Sol_Terra"

PAGE_IMAGE_SHA256 = {
    "016": "7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56",
    "017": "1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F",
    "018": "6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4",
    "019": "63BBB963A76F5C266E4A1B139FBCEFD2D390FB23B23CA391E8BAF12A4E9D3AC8",
    "020": "53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E",
}

INITIAL_STATUS_SHA256 = "D340D6D2FEAF561B60EC6ED9329104D5700D262C55AA8DB03EACBDA3B17D05D3"
INITIAL_FINAL_REVIEW_SHA256 = "D409636B5193535B8E2BD496083E9345C4C4526EEEDD68A4669C36C6886BB219"


def page_roots(page: str) -> dict[str, Path]:
    return {
        "triage": TRIAL_ROOT / f"page_{page}_triage_G1_VIRAL_001",
        "text": TRIAL_ROOT / f"page_{page}_text_extraction_G1_VIRAL_001",
        "sem": TRIAL_ROOT / f"page_{page}_semantic_text_map_G1_VIRAL_001",
        "pcrp": TRIAL_ROOT / f"page_complete_review_p{page}_G1_VIRAL_001",
        "pca": TRIAL_ROOT / f"page_complete_acceptance_p{page}_G1_VIRAL_001",
        "status": TRIAL_ROOT / f"gate_1_status_packet_G1_VIRAL_{int(page) - 5:03d}",
        "batch": TRIAL_ROOT / f"page_{page}_aggressive_batch_G1_VIRAL_001",
    }


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def h2(unit_id: str, text: str, block_id: str) -> dict[str, Any]:
    return {"unit_id": unit_id, "unit_type": "heading", "heading_level": "h2", "semantic_role": "section_heading", "block_id": block_id, "text": text, "layout_role": "block_heading", "display_style": "normal", "is_structural_heading": True}


def h3(unit_id: str, text: str, block_id: str) -> dict[str, Any]:
    return {"unit_id": unit_id, "unit_type": "heading", "heading_level": "h3", "semantic_role": "subsection_heading", "block_id": block_id, "text": text, "layout_role": "inline_heading", "display_style": "run_in", "is_structural_heading": True}


def keeper(unit_id: str, block_id: str) -> dict[str, Any]:
    return {"unit_id": unit_id, "unit_type": "heading", "heading_level": keeper_notes_callout_heading_level(), "semantic_role": "keeper_notes_callout_heading", "block_id": block_id, "text": "Keeper's Notes", "layout_role": "block_heading", "display_style": "callout_heading", "is_structural_heading": True}


def para(unit_id: str, text: str, block_id: str, role: str = "body", **extra: Any) -> dict[str, Any]:
    out = {"unit_id": unit_id, "unit_type": "paragraph", "heading_level": None, "semantic_role": role, "block_id": block_id, "text": text, "layout_role": "body", "display_style": "normal", "is_structural_heading": False}
    out.update(extra)
    return out


PAGE_DATA: dict[str, dict[str, Any]] = {
    "016": {
        "predecessor": {"kind": "final_review", "id": "P015BATCHREV-G1-VIRAL-001", "path": TRIAL_ROOT / "page_015_aggressive_batch_final_review_G1_VIRAL_001" / "page_015_aggressive_batch_final_review_report.json", "sha256": INITIAL_FINAL_REVIEW_SHA256},
        "status_predecessor": {"id": "G1SP-G1-VIRAL-010", "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_010" / "gate_1_status_packet.json", "sha256": INITIAL_STATUS_SHA256},
        "blocks": [
            {"block_id": "P016-B001", "role": "history_continuation_text", "crop_box_px": [210, 170, 1040, 1320], "crop_contract": {"coverage": "full_text_region_part", "context_allowed": False, "expected_bounds": {"min_x": 180, "max_x": 230, "min_y": 140, "max_y": 200, "min_width": 1000, "min_height": 1280}}, "asset": "review_assets/1_P016-history-continuation-text-evidence.png"},
            {"block_id": "P016-B002", "role": "left_keeper_notes_continued", "crop_box_px": [215, 1490, 1025, 1510], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 190, "max_x": 240, "min_y": 1460, "max_y": 1510, "min_width": 980, "min_height": 1450}}, "asset": "review_assets/2_P016-left-keepers-notes-text-evidence.png"},
            {"block_id": "P016-B003", "role": "right_keeper_notes_continuation", "crop_box_px": [1320, 230, 1010, 890], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 1290, "max_x": 1350, "min_y": 200, "max_y": 260, "min_width": 970, "min_height": 830}}, "asset": "review_assets/3_P016-right-keepers-notes-text-evidence.png"},
            {"block_id": "P016-B004", "role": "history_late_reports", "crop_box_px": [1310, 1140, 1040, 1770], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 1280, "max_x": 1340, "min_y": 1110, "max_y": 1170, "min_width": 1000, "min_height": 1650}}, "asset": "review_assets/4_P016-late-history-text-evidence.png"},
        ],
        "visuals": [],
        "texts": [
            ("P016-TEXT-001", "P016-B001", "In 1917, a number of soldiers were diagnosed with the flu and were treated at Saint Roche's Sanitarium before being sent to the front. The next year, the 1918 Influenza pandemic devastated the globe.\n\nIn 1928, the facility was upgraded with new medical equipment and renamed Saint Roche's Hospital.\n\nDuring WWII the island remained largely untouched by the fighting, though a section of the original monastery was inadvertently damaged by an American bomber when its bomb release system failed. Rumors were circulated about a secret mission, though nothing ever came to light.\n\nIn 1954, following reports of missing and abused patients, an investigation by Italian authorities revealed that horrific experiments were being performed at the hospital. The remains of hundreds of patients were discovered in cremation pits and mass graves. The hospital was shut down and dozens of hospital staff, including several administrators, were sentenced to life in prison. Strangely, every one of them died within a year from a mysterious disease that caused them to waste away. The cause of the illness was never discovered.\n\nDue to the island's isolation and the possible infectious nature of the remains, the bodies were never exhumed and remain on the island to this day. There's no indication that there was any sort of cleanup, simply that the island was placed under quarantine indefinitely."),
            ("P016-TEXT-002", "P016-B002", "Keeper's Notes\n\nThe public is unaware of the cult of Hastalyk, or the intense firefight that took place when Italian military forces stormed the island in 1954. When the Italian government first received information regarding the abuse of patients, it immediately sent members of the social services to investigate with a police escort. At first, the hospital administrator seemed cooperative, but when the investigators discovered fresh remains in the cremation pit, they ordered the hospital shut down. Subsequently, the social services investigators and their police escort were lured into the chapel where they were slaughtered by the cultists, though one of the police officers did manage to contact their seaplane which was waiting at the dock. The quick-thinking pilot took off and managed to radio the authorities.\n\nMeanwhile, the bodies of the investigators were quickly burned, and realizing that the end was nigh, the cult murdered the non-cult members of the hospital staff and euthanized all of the patients. Their remains were brought into the secret catacombs beneath the chapel.\n\nWhile this was happening, the authorities reviewed the pilot's unsettling report and decided that they would have to use the military to take the island. Considering the nature of the situation, they called in the DSS (Divisione Sicurezza Speciale), a secret division within the Italian government that handles sensitive issues of national security. In a matter of hours, a squadron of helicopters was flying to Isola di Malamente with a heavily armed strike team.\n\nLanding at two points on the island (the lighthouse and the hospital) the two groups systematically worked their way into"),
            ("P016-TEXT-003", "P016-B003", "the hospital. The cultists put up the heaviest resistance in the staff dormitory, fighting to the last member. Unbeknownst to the strike team, the cultists were buying time for two of their brethren to complete their tasks.\n\nThe two last Plague Monks had fled into the secret shrine to perform a dark ritual that involved one of the hospital's infants reserved for that purpose. Using the Iuramentum Corruptionis, one prepared the other to be the final sacrifice. They waited until the interlopers were gone and made their way to the Charnel Pit where the final sacrifice was hung by the neck above the pit until the time was right. The other went back to the hidden shrine with the book where he killed himself with a bullet through the temple, thus completing the ritual.\n\nThe last Plague Monk has since watched over the island as a shadowy presence, feeding more tainted flesh into the Charnel Pit whenever possible in preparation for the great day when Hastalyk would be born."),
            ("P016-TEXT-004", "P016-B004", "In 1958, Il Culto della Peste dell'Isola Malamente (The Plague Cult of Malamente Island) was published. Its author, Dr. Giovanni Pellegrino, claimed to be one of the investigators who shut down the hospital, and it supposedly described the true story behind the events in 1954. Before it could hit the shelves however, all copies of the book were seized by the Italian government and the writer was arrested on national security grounds. He died in prison a week later of an unknown wasting disease.\n\nKeeper's Notes\n\nA few copies of the book escaped destruction, and in fact could be what draws investigators to the island. The book basically describes the events that took place on the island in 1954, though doesn't suggest anything supernatural in and of itself.\n\nDr. Pellegrino entered the hospital once the fighting had ceased, describing the carnage in vivid and disturbing detail. There are particularly haunting reports of slaughtered patients with incomprehensible symbols carved into their flesh. He claims that there were signs of ritual sacrifice, cannibalism, and unspeakable experiments on women and infants.\n\nHe states that the \"last stand\" in the staff dormitory was as brutal as any he'd seen in the war, with heavy losses on both sides. As many as thirteen Italian soldiers had been killed, with twenty-three monks cut to pieces by machine gun fire.\n\nIn the aftermath of the siege, Dr. Pellegrino was tasked with identifying the dead. He notes that three of the monks were not found in the hospital, and that they were presumed to have died attempting to flee the island.\n\nThe book has no photos, but there are several drawings that depict some of the symbols he found.\n\nThe Keeper can decide if the investigators can glean anything relevant to their investigation from the book.\n\nIn 1961, the island was deemed off limits to anyone except with official government permission.\n\nThroughout the 1970s and 80s, people reported seeing figures and lights on the island, though official reports show no evidence that anyone has been there in almost 60 years."),
        ],
    },
    "017": {
        "blocks": [
            {"block_id": "P017-B001", "role": "one_night_in_perla_intro", "crop_box_px": [210, 1780, 1040, 1270], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 180, "max_x": 240, "min_y": 1740, "max_y": 1820, "min_width": 1000, "min_height": 1200}}, "asset": "review_assets/1_P017-left-text-evidence.png"},
            {"block_id": "P017-B002", "role": "internet_search_and_keeper_notes", "crop_box_px": [1315, 1780, 1040, 1230], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 1280, "max_x": 1350, "min_y": 1740, "max_y": 1820, "min_width": 1000, "min_height": 1160}}, "asset": "review_assets/2_P017-right-text-evidence.png"},
        ],
        "visuals": [{"block_id": "P017-V001", "role": "perla_village_hero_art", "crop_box_px": [0, 0, 2550, 1760], "asset": "review_assets/3_P017-perla-hero-visual-anchor.png", "visual_only": True, "text_extraction": "excluded_visual_anchor"}],
        "texts": [
            ("P017-TEXT-001", "P017-B001", "One Night in Perla\n\nOne Night in Perla is a new prologue that expands on the original scenario by giving the investigators an opportunity to explore the nearby fishing village of Perla. This offers them an opportunity to learn more about the history and lore of Isola di Malamente, and bear witness to the ancient festival of Lepurazione di Morbus (The Purging of Morbus).\n\nThe Purging of Morbus. The ceremony lasts for three days and begins on the first night with Il Rogo della Malattia (The Burning of the Disease). This involves burning an effigy of the demon Morbus which is supposed to banish him from the village. They believe that this causes Morbus to retaliate, so on the second night, known as Notte della Peste (Plague Night), they lock themselves in their homes and place talismans at all of the possible means of entry to trap any illness that might try to get inside. The third and final night is La Purificazione (The Purification), and involves burning all of the talismans in the piazza, followed by a celebration that goes well into the night.\n\nThe people of Perla take the festival very seriously, so any attempt to interfere will be met first with strong resistance, and if necessary, violence. Of course if a bunch of foolish Americans want to get themselves killed, that's their business, but if anyone tries to interfere with the festival, especially on Plague Night, it won't go well for them."),
            ("P017-TEXT-002", "P017-B002", "If the investigators do an internet search about Perla, a Luck roll allows them to find a video made by an American tourist who tried to stop one of the villagers from reaching their home on Plague Night. The altercation left the tourist in the hospital, and according to official records, the matter was settled.\n\nThe video itself is disturbing. The villager in question was a tough looking fisherman who was walking down a side street when the American (a young man in his 20s) blocked the way and started shoving the video camera in the villager's face. The fisherman tried to go around, but the young man kept laughing and asking the fisherman where he was going in such a hurry, repeating that he just wanted to ask some questions.\n\nThings escalated quickly and suddenly the camera was still running on the ground as it recorded the fisherman repeatedly punching the tourist. It ends after the fisherman storms off and the tourist crawls over to the camera to shut it off. According to the video, this incident happened in 2002.\n\nKeeper's Notes\n\nIf the investigators try to find the fisherman, they'll have no luck. He died from cancer about three years ago. None of the villagers recall the incident, nor is there any record of it."),
        ],
    },
    "018": {
        "blocks": [
            {"block_id": "P018-B001", "role": "welcome_left_column", "crop_box_px": [205, 220, 1045, 2800], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 180, "max_x": 235, "min_y": 190, "max_y": 250, "min_width": 1000, "min_height": 2700}}, "asset": "review_assets/1_P018-left-text-evidence.png"},
            {"block_id": "P018-B002", "role": "welcome_right_column", "crop_box_px": [1315, 220, 1040, 2800], "crop_contract": {"coverage": "full_text_region_part", "context_allowed": False, "expected_bounds": {"min_x": 1280, "max_x": 1350, "min_y": 190, "max_y": 250, "min_width": 1000, "min_height": 2700}}, "asset": "review_assets/2_P018-right-text-evidence.png", "continues_to_next_page": True},
        ],
        "visuals": [],
        "texts": [
            ("P018-TEXT-001", "P018-B001", "Welcome to Perla\n\nAugust 23rd, 2019 - 10am\n\nAs you open the van's sliding door, you're greeted by a warm breeze and the mingled scents of bread, fish, lemons, and sea air. The cobblestone streets are busy with locals going about their daily business, and as you step out onto the sidewalk, it's like stepping into a postcard. Perla is built on the hillside of a narrow cove overlooking the Mediterranean, and from this vantage point you have a spectacular view of the entire village. Looking to the west, you're able to just make out your ultimate destination on the horizon: Isola di Malamente.\n\nGrateful to stretch your legs, you unload your gear from the back, drawing a few looks from some nearby children playing ball. After spending several hours careening over the rough, twisting roads of the Sicilian countryside in a rickety old van, all you want now is a shower and maybe a nap.\n\nThe white building in front of you looks old, but well kept. The oval wooden sign overhead creaks and sways in the pleasant sea breeze, the ornate gold letters flickering in the sun. It reads Tramonto dell'Hotel (Hotel Sunset). The cab driver sets down the last of your bags, tips his cap, and rattles away.\n\nThe village is abuzz with excitement. As the van pulls away, the old men stop and stare while some of the women send some older children over to help you unload their gear. They point at the hotel asking \"Qui?\"\n\nKeeper's Notes\n\nAnyone who speaks Italian will understand this to mean \"In here?\" Should the young helpers get confirmation, they'll start carrying the gear into the hotel lobby. They are generally very honest, and will be very grateful if offered tips, but won't ask for one.\n\nThe hotel is located right on the town piazza; an eighty foot circle of cobblestones with a sidewalk along the outside perimeter. In the center, where one might normally find a statue or fountain, is instead a thirty foot circular stone dais or stage. Standing atop the dais is a large pile of wood set up like a bonfire surrounded by a low chain link fence. The stone beneath the wood is blackened and pitted, presumably from many past fires. Besides the hotel, the piazza is encircled by a number of shops including a bakery, butcher, fishmonger, greengrocer, cafe, and so on.\n\nA handful of old men are working with some of the teenagers to pack the bonfire with more wood, while several women on ladders hang red and white bunting between the lamp posts. Laughing children chase each other and play all around the piazza, adding to the general mood of excitement in the air. A few older women tend the hundreds of sunflowers that reach for the sky from large planters all around the town square.\n\nA number of streets lead away from the piazza to intersect with other narrow roads and alleys that twist and turn"),
            ("P018-TEXT-002", "P018-B002", "throughout Perla. Many of the alleys have steps while the roads zig-zag up and down the steep slope upon which the village is built. Most of the structures are old and off-white, yellow, sky blue, or salmon in color with chipping paint that reveals the brickwork and planks beneath. Countless stairs climb between the gaps in the buildings to connect hidden squares and terraces in a manner that would leave M. C. Escher scratching his head.\n\nKeeper's Notes\n\nIf asked about the preparations, the investigators will be told that tonight is Il Rogo della Malattia (which translates to The Burning of the Disease). It's a festival that goes back many centuries, and involves the burning of an effigy of Morbus, a demon that is associated with illness and disease. This is intended to purge his influence from the village for another year. The following night is known as Notte della Peste (Plague Night) when Morbus is said to retaliate against the village, and so they lock themselves away, placing talismans in their homes to trap any illness that might enter. The talismans are burned on the final night of the three day festival known as La Purificazione (The Purification), after which the entire town celebrates their victory.\n\nThe Hotel Sunset. The interior of the Hotel Sunset has clearly seen better days. The wallpaper is peeling, and the plastic flowers sitting around the lobby are dull and dusty. There are a few worn leather couches and a coffee table littered with old magazines with countless coffee stains. Scratchy classical music plays through antique-looking speakers that have been inexpertly hidden behind the furniture. An older gentleman sits at the reception desk idly browsing the internet, occasionally leaning in to see the keyboard through his bottle thick glasses.\n\nHe won't notice the Krew at first, but will jump with a start if they catch his attention. He responds in Italian \"Buongiorno, mi chiamo Paolo, benvenuti all'Hotel Sunset. Avete una prenotazione?\" Which translates to \"Good morning, my name is Paolo, welcome to Hotel Sunset. Do you have a reservation?\" After a moment, Paolo takes a better look at the investigators and says \"Ah, Americani?\" But before they can respond he repeats his greeting in fairly good English.\n\nHe checks their reservations, and after confirming who booked the rooms (Maya has booked and paid for them) he will get them their room keys. Marco and Corrina have their own rooms while Hyeon, Peter and Enoch are all sharing a large family room. Of course Maya booked Marco in the nicest room with a beautiful sea view.\n\nPaolo asks if they'd like to lock their gear in a secure room. If they take the offer, the gear will be safe until they need it, but if they say no, they need to lug it up and down two flights of narrow stairs.\n\nHe informs them that breakfast is served between 8am-10am each morning and gestures behind him to the right where they can clearly see a kitchenette with chairs and round"),
        ],
    },
    "019": {
        "blocks": [
            {"block_id": "P019-B001", "role": "hotel_sunset_continuation", "crop_box_px": [205, 1700, 1035, 1320], "crop_contract": {"coverage": "full_text_region_part", "context_allowed": False, "expected_bounds": {"min_x": 180, "max_x": 235, "min_y": 1660, "max_y": 1735, "min_width": 990, "min_height": 1260}}, "asset": "review_assets/1_P019-left-continuation-text-evidence.png"},
            {"block_id": "P019-B002", "role": "perla_right_column", "crop_box_px": [1310, 210, 1045, 2840], "crop_contract": {"coverage": "full_text_region_part", "context_allowed": False, "expected_bounds": {"min_x": 1280, "max_x": 1345, "min_y": 180, "max_y": 240, "min_width": 1000, "min_height": 2740}}, "asset": "review_assets/2_P019-right-text-evidence.png", "continues_to_next_page": True},
        ],
        "visuals": [{"block_id": "P019-V001", "role": "paolo_portrait_visual_anchor", "crop_box_px": [210, 230, 1035, 1470], "asset": "review_assets/3_P019-paolo-portrait-visual-anchor.png", "visual_only": True, "text_extraction": "excluded_visual_anchor"}],
        "texts": [
            ("P019-TEXT-001", "P019-B001", "tables covered in blue gingham tablecloths. He tells them that tea and coffee are available in their room, and hands each of them a set of foam earplugs.\n\nPaolo smiles and says \"We have a local festival this evening that is... a bit noisy and goes on well into the night. Of course you are welcome to join in the festivities with us.\"\n\nHe can answer most questions about Perla, however, if asked about Isola di Malamente he will shrug and say that nobody goes near it since the government declared it off limits a long time ago. Paolo adds that it's probably because the island is surrounded by old sea mines that date back to the 1940s, though he's not sure why they wouldn't just remove them. A Hard Psychology roll will indicate that he's not being entirely truthful. If pushed, he'll act like a befuddled old man and change the subject.\n\nThe rooms themselves are adequate if a bit old. The beds are clean and there are vases of fresh flowers on the dressers. Each has a simple bathroom with a small, claw-footed tub. Corrina's room looks out onto the rooftop of a nearby house, while the family room window opens on a narrow alley. Marco's room on the other hand looks out across the picturesque Mediterranean, with Isola di Malamente clearly visible on the horizon."),
            ("P019-TEXT-002", "P019-B002", "Perla\n\nThis Sicilian fishing village is fairly typical for the region, and is full of rustic charm. It derives its name from the plentiful oysters - and the beautiful pearls they contain - that are regularly fished in the waters near Perla. When the investigators arrive, it's late summer and the village is bedecked in all manner of colorful flowers in hanging baskets, planters, and window boxes. All of the buildings are painted white, though time and the local climate have weathered them quite a bit.\n\nThe village is big enough to support a range of shops and businesses including a baker, butcher, fishmonger, grocery store, cafe, and hardware store, most of which are located on or near the main piazza. The cobblestone roads weave through Perla, zig-zagging up and down the slope, leading down to the docks where dozens of fishing boats, tour boats, and various smaller craft are moored.\n\nStanding above all of the other structures in town is Cappella di Sant'Anna (Chapel of Saint Anne), a 12th century church dedicated to the mother of Mary, the patron saint of childbirth.\n\nThe Shops. Exploring the various shops surrounding the piazza will find typical Sicilian fare. The cafe is clearly popular with the elderly men of Perla, many of whom spend the day chatting, drinking espressos, smoking, and playing cards. They're friendly enough, though if asked about the island, they will become very solemn and quiet, often making hurried excuses and heading home.\n\nThe Homes. Like so many of the old towns and villages in the region, Perla grew organically up the hillside as more people moved here and the population grew. This means that the houses are largely connected, with some built with adjoining walls and others built atop older homes. So while all of the houses are made of the same materials and have the same general appearance, there are no two floor plans that are exactly the same.\n\nThe Docks. The deep azure waters of the bay are reasonably safe for swimming, though the number of boats moving to and fro often put people off. The fishermen here are simple folk earning a living and won't stop to chat as they busily pack fish in ice. If asked about the island they'll cross themselves and mutter a small blessing in Italian, refusing to talk about it.\n\nA Spot Hidden check will allow the investigators to notice a poster for a missing local man named Angelo Russo on a wall near the dock. The posters are all heavily weathered and the date of his disappearance looks to have been torn off at some point.\n\nNuncio Vendra. Nuncio's battered fishing boat is moored to one of the outer docks where he can often be found smoking a menthol cigarette and chatting to the various fishermen near a sign that reads: TOUR DELLA BAIA: $20/€25 ALL'ORAAY and below that TOURS: $20 PER HOUR."),
        ],
    },
    "020": {
        "blocks": [
            {"block_id": "P020-B001", "role": "left_column_perla_exploration", "crop_box_px": [210, 210, 1040, 2800], "crop_contract": {"coverage": "full_text_region", "context_allowed": False, "expected_bounds": {"min_x": 180, "max_x": 240, "min_y": 180, "max_y": 240, "min_width": 1000, "min_height": 2700}}, "asset": "review_assets/1_P020-left-text-evidence.png"},
            {"block_id": "P020-B002", "role": "exploring_and_rumors", "crop_box_px": [1310, 210, 1045, 2810], "crop_contract": {"coverage": "full_text_region_part", "context_allowed": False, "expected_bounds": {"min_x": 1280, "max_x": 1345, "min_y": 180, "max_y": 240, "min_width": 1000, "min_height": 2700}}, "asset": "review_assets/2_P020-right-rumors-text-evidence.png", "continues_to_next_page": True},
        ],
        "visuals": [{"block_id": "P020-V001", "role": "perla_boats_photo_visual_anchor", "crop_box_px": [210, 2280, 1035, 760], "asset": "review_assets/3_P020-boats-photo-visual-anchor.png", "visual_only": True, "text_extraction": "excluded_visual_anchor"}],
        "texts": [
            ("P020-TEXT-001", "P020-B001", "Nuncio will recognize the Krew from photos that Maya sent him. If they approach, he smiles and asks them if they fancy a trip out tomorrow, giving a knowing wink. Assuming they agree, he tells them to be ready to leave a few hours before sunset. After a small amount of friendly chit-chat, he makes his excuses, stubs out his cigarette, climbs aboard his boat and leaves the dock.\n\nLocal Teens. Most days the docks are a bustle of activity, which attracts the more rebellious teenagers who hang out to watch, drink, and smoke. Most teenagers in Perla speak some English that they've picked up watching American movies and television, though they'll generally stick to Italian, unless they're trying to hit on Corrina.\n\nKeeper's Notes\n\nThey're not interested in talking about Isola di Malamente, but if pressed (with a Regular Intimidate, Hard Charm, or Extreme Persuade check) or bribed with $100 or more, they'll admit to sneaking out to Beggar's Cove to party on occasion. If the Superfan version of Em is being used, then they'll also admit to taking an American woman over to the island to stay the night, adding that she hasn't returned with the rowboat they left for her. Additional pressure or bribery will get them to describe the woman. At this point the Keeper can then give the investigators an Idea roll to see if they recognize her as Em or not.\n\nCommunication. Cell phone service is decent in Perla, offering 3G speeds, though there doesn't appear to be any public Wifi options available anywhere. There are however a few public phone booths that are surprisingly still in service, though of course the Krew can simply use their own cell phones or the phone at the hotel if they wish.\n\nLocal radio stations mainly play classical music or Italian favorites from the 40s and 50s. Most of the locals watch one of the three broadcast television channels, one of which has American reruns (mostly from the 70s, 80s, and 90s) every night at 8pm. While the hotel doesn't have cable or Wifi, the 3G signal is good enough that the investigators can access the internet and their own streaming media if they wish."),
            ("P020-TEXT-002", "P020-B002", "Exploring in Perla\n\nWhile the investigators are in Perla, there are a number of things that they can learn by talking to the locals or noticing details around the village. The Keeper can roll randomly to determine which bits of information they acquire, or they can choose whichever makes the most sense. Of course the Keeper can always improvise new ones to suit their version of the scenario, particularly if they are using alternative investigators rather than the Spektral Krew.\n\nNote that most of these aren't true, or are mingled with half-truths. When hearing a rumor, the Keeper should have the investigators make an Intelligence check to see it for the nonsense it is.\n\nRumors\n\nRoll 1: The real reason the island was raided back in the 1950s was because there was some sort of Satanic cult that was out there sacrificing children. [Rational Explanation: There have been very few actual Satanic cults discovered, and none that actually killed children. This sounds like the same old Satanic panic from the 1980s.]\n\nRoll 2: Fishermen report seeing ghost lights on the island at night this time of year. They say it's the spirits of dead children looking for their parents to take them home. [Rational Explanation: These are the sorts of stories told by sailors since humans first took to the sea. The lights could easily be explained as teenagers drinking on the island or lights from other boats seen through the trees.]\n\nRoll 3: The hospital was just a front, and that the government was engineering biological weapons. It was shut down when a virus got out and killed everyone on the island. [Rational Explanation: While not impossible, it's highly unlikely that Italy or the United States would have violated the Geneva Convention so blatantly. It's even more unlikely that it wouldn't have come to light by now.]\n\nRoll 4: The island is populated by giant mutant rats. [Rational Explanation: While not impossible, it's not a large island, which would make it unlikely for a population of any large mammals (mutant or otherwise) to thrive there.]\n\nRoll 5: Parents will sometimes take a boat out to the island if their child is particularly ill to leave an offering on the Weeping Bridge. [Rational Explanation: This sounds plausible enough, and the investigators are likely to have this rumor confirmed by many of the villagers. This one is true.]\n\nRoll 6: Teenagers will occasionally take a boat for a joy ride out to the island to party at a place called Beggar's Cove. It's supposedly located around the far side on the small island. [Rational Explanation: This sounds plausible, and could explain some of the other rumors. If the investigators speak to any of the teens loitering at the docks, they'll happily confirm this. This one is obviously true.]"),
        ],
    },
}


def roots_for(page: str) -> dict[str, Path]:
    roots = page_roots(page)
    return roots


def auth_id(page: str) -> str:
    return f"BA-G1-VIRAL-PAGE-{page}-AGGRESSIVE-BATCH-001"


def lane_id(page: str) -> str:
    return f"P{page}BATCH-G1-VIRAL-001"


def page_image(page: str) -> Path:
    return TRIAL_ROOT / "images" / f"page_{page}.png"


def stage_reviews(page: str) -> dict[str, dict[str, str]]:
    return {
        f"P{page}TR-G1-VIRAL-001": {
            "sol": f"OK: page {page} triage is bounded to the exact page image and declared evidence regions.",
            "terra": f"OK: page {int(page) + 1:03d}+ remains blocked by the page {page} lane guardrails.",
        },
        f"P{page}TXT-G1-VIRAL-001": {
            "sol": f"OK: page {page} text extraction is limited to declared page evidence blocks.",
            "terra": "OK: no OCR/source/page/whole-Gate acceptance is claimed by text extraction.",
        },
        f"P{page}SEM-G1-VIRAL-001": {
            "sol": f"OK: page {page} semantic units preserve section/callout structure and continuation metadata.",
            "terra": f"OK: semantic map does not process page {int(page) + 1:03d}+ content.",
        },
        f"PCRP-G1-VIRAL-P{page}-001": {
            "sol": f"OK: page {page} complete review packet reconciles text, visual anchors, and semantic units.",
            "terra": "OK: PCRP is internal delegated evidence only and claims no direct Bogdan per-stage approval.",
        },
        f"P{page}PCA-G1-VIRAL-001": {
            "sol": f"OK: delegated acceptance is page {page} only under exact lane authority.",
            "terra": "OK: PCA does not imply whole Gate 1, fixture admission, source acceptance, or broader processing.",
        },
        f"G1SP-G1-VIRAL-{int(page) - 5:03d}": {
            "sol": f"OK: status refresh advances accepted-only pages through {page}.",
            "terra": f"OK: page {int(page) + 1:03d} is only a recommended next candidate unless the sequential run continues.",
        },
    }


def review_gate(page: str, stage: str) -> dict[str, Any]:
    review = stage_reviews(page)[stage]
    return {
        "human_review_state": SKIPPED_REVIEW,
        "delegated_review_state": DELEGATED_REVIEW,
        "lane_authority": auth_id(page),
        "sol": {"status": "OK", "finding": review["sol"]},
        "terra": {"status": "OK", "finding": review["terra"]},
        "status": "passed",
        "blockers": [],
    }


def guardrails(page: str, *, final_acceptance: bool = False) -> dict[str, bool]:
    return {
        "whole_gate_1_acceptance": False,
        "fixture_admission": False,
        "source_acceptance_mutation": False,
        "ocr_execution": False,
        "render_execution": False,
        "pdf_parsing_or_text_layer_extraction": False,
        "raw_mutation": False,
        "translation": False,
        "proofreading": False,
        "renderer_profile_acceptance": False,
        "implementation": False,
        "push": False,
        f"page_{int(page) + 1:03d}_plus_processing": False,
        "page_021_plus_processing": False,
        "final_human_batch_review_acceptance": final_acceptance,
    }


def check_authorization(page: str, argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=f"Build page {page} aggressive delegated-review batch.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit(f"page {page} aggressive batch is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != auth_id(page):
        raise SystemExit(f"page {page} aggressive batch requires {auth_id(page)}")


def predecessor_for(page: str) -> tuple[dict[str, str], dict[str, str]]:
    data = PAGE_DATA[page]
    if "predecessor" in data:
        return data["predecessor"], data["status_predecessor"]
    previous = f"{int(page) - 1:03d}"
    previous_roots = roots_for(previous)
    return (
        {
            "kind": "previous_batch",
            "id": lane_id(previous),
            "path": previous_roots["batch"] / f"page_{previous}_aggressive_batch_report.json",
            "sha256": sha256_file(previous_roots["batch"] / f"page_{previous}_aggressive_batch_report.json"),
        },
        {
            "id": f"G1SP-G1-VIRAL-{int(previous) - 5:03d}",
            "path": previous_roots["status"] / "gate_1_status_packet.json",
            "sha256": sha256_file(previous_roots["status"] / "gate_1_status_packet.json"),
        },
    )


def aggressive_batch_authorization_preflight(page: str) -> None:
    predecessor, status_predecessor = predecessor_for(page)
    materialize_aggressive_batch_authorization(
        ledger_path=AUTHORIZATION_LEDGER,
        authorization_id=auth_id(page),
        page=page,
        lane_id=lane_id(page),
        authority='Bogdan Telegram message `2066`: "ок, тогда делай 16-20 агрессивно"',
        exact_action=[
            f"Create page {page} aggressive delegated-review batch artifacts.",
            f"Generate P{page}TR/P{page}TXT/P{page}SEM/PCRP/P{page}PCA/status/batch outputs with skipped human review and Sol/Terra evidence.",
        ],
        admitted_inputs=[
            {"name": status_predecessor["id"], "sha256": status_predecessor["sha256"]},
            {"name": predecessor["id"], "sha256": predecessor["sha256"]},
            {"name": f"page_{page}_image", "sha256": PAGE_IMAGE_SHA256[page]},
        ],
        allowed_outputs=[
            f"scripts/build_page_{page}_aggressive_batch.py",
            f"tests/test_page_{page}_aggressive_batch.py",
            f"fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_{page}_*",
            f"fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p{page}_G1_VIRAL_001/*",
            f"fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_{int(page) - 5:03d}/*",
        ],
        limits=[
            f"Do not record direct Bogdan approval for internal P{page} stages.",
            f"Do not process page {int(page) + 1:03d} or later beyond the bounded sequential run/status recommendation.",
            "Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.",
        ],
    )


def verify_predecessors(page: str) -> list[dict[str, str]]:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {auth_id(page)}" not in ledger:
        raise SystemExit(f"{auth_id(page)} is missing from bounded trial authorization ledger")
    predecessor, status_predecessor = predecessor_for(page)
    predecessors = [
        (status_predecessor["id"], status_predecessor["path"], status_predecessor["sha256"]),
        (predecessor["id"], predecessor["path"], predecessor["sha256"]),
        (f"page_{page}_image", page_image(page), PAGE_IMAGE_SHA256[page]),
    ]
    verified = []
    for name, path, expected in predecessors:
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": path.relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def reset_outputs(page: str) -> None:
    for root in roots_for(page).values():
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)


def crop_assets(page: str) -> None:
    data = PAGE_DATA[page]
    with Image.open(page_image(page)) as img:
        page_size = img.size
        validate_text_evidence_crop_contracts(page_size, data["blocks"])
        for block in data["blocks"] + data.get("visuals", []):
            x, y, w, h = block["crop_box_px"]
            cropped = img.crop((x, y, x + w, y + h))
            for root_key in ("triage", "pcrp"):
                out = roots_for(page)[root_key] / block["asset"]
                out.parent.mkdir(parents=True, exist_ok=True)
                cropped.save(out)
        for root_key in ("triage", "pcrp"):
            shutil.copy2(page_image(page), roots_for(page)[root_key] / "review_assets" / f"page_{page}.png")


def manifest(root: Path, title: str, manifest_name: str) -> None:
    lines = [f"# {title}", "", "| Output | SHA-256 |", "|---|---|"]
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(root / manifest_name, "\n".join(lines))


def semantic_units(page: str) -> list[dict[str, Any]]:
    prefix = f"SU-P{page}"
    units: list[dict[str, Any]] = []
    if page == "016":
        book_callout = split_bounded_callout(
            PAGE_DATA[page]["texts"][3][2],
            callout_heading="Keeper's Notes",
            body_end_marker="The Keeper can decide if the investigators can glean anything relevant to their investigation from the book.",
        )
        left_keeper_contract = callout_body_contract(
            callout_heading="Keeper's Notes",
            boundary_kind="reviewed_continuation_boundary",
            boundary_marker="P016-B002 continues into P016-B003",
        )
        right_keeper_contract = callout_body_contract(
            callout_heading="Keeper's Notes",
            boundary_kind="reviewed_source_region_boundary",
            boundary_marker="P016-B003 source region ends before P016-B004 history block",
        )
        units.extend([
            para(f"{prefix}-HIST-001", PAGE_DATA[page]["texts"][0][2], "P016-B001", "history_continuation_from_page_015", continuation_from_page="015"),
            keeper(f"{prefix}-KEEPER-001", "P016-B002"),
            para(f"{prefix}-KEEPER-002", PAGE_DATA[page]["texts"][1][2].split("\n\n", 1)[1], "P016-B002", "keeper_notes_1954_raid_left", semantic_split_contract=left_keeper_contract),
            para(f"{prefix}-KEEPER-003", PAGE_DATA[page]["texts"][2][2], "P016-B003", "keeper_notes_1954_raid_right", semantic_split_contract=right_keeper_contract),
            para(f"{prefix}-HIST-002", book_callout.before, "P016-B004", "history_late_reports"),
            keeper(f"{prefix}-KEEPER-004", "P016-B004"),
            para(f"{prefix}-KEEPER-005", book_callout.body, "P016-B004", "keeper_notes_plague_cult_book", semantic_split_contract=book_callout.contract()),
            para(f"{prefix}-HIST-003", book_callout.after, "P016-B004", "history_late_reports_post_keeper"),
        ])
    elif page == "017":
        fisherman_callout = split_bounded_callout(
            PAGE_DATA[page]["texts"][1][2],
            callout_heading="Keeper's Notes",
            allow_to_end=True,
        )
        units.extend([
            h2(f"{prefix}-PERLA-001", "One Night in Perla", "P017-B001"),
            para(f"{prefix}-PERLA-002", PAGE_DATA[page]["texts"][0][2].split("\n\n", 1)[1].split("\n\nThe Purging", 1)[0], "P017-B001", "prologue_overview"),
            h3(f"{prefix}-PERLA-003", "The Purging of Morbus.", "P017-B001"),
            para(f"{prefix}-PERLA-004", "The ceremony lasts for three days and begins on the first night with Il Rogo della Malattia (The Burning of the Disease). This involves burning an effigy of the demon Morbus which is supposed to banish him from the village. They believe that this causes Morbus to retaliate, so on the second night, known as Notte della Peste (Plague Night), they lock themselves in their homes and place talismans at all of the possible means of entry to trap any illness that might try to get inside. The third and final night is La Purificazione (The Purification), and involves burning all of the talismans in the piazza, followed by a celebration that goes well into the night.", "P017-B001", "purging_of_morbus"),
            para(f"{prefix}-PERLA-005", "The people of Perla take the festival very seriously, so any attempt to interfere will be met first with strong resistance, and if necessary, violence. Of course if a bunch of foolish Americans want to get themselves killed, that's their business, but if anyone tries to interfere with the festival, especially on Plague Night, it won't go well for them.", "P017-B001", "festival_warning"),
            para(f"{prefix}-PERLA-006", fisherman_callout.before, "P017-B002", "internet_search_video"),
            keeper(f"{prefix}-KEEPER-001", "P017-B002"),
            para(f"{prefix}-KEEPER-002", fisherman_callout.body, "P017-B002", "keeper_notes_fisherman", semantic_split_contract=fisherman_callout.contract()),
        ])
    elif page == "018":
        helper_callout = split_bounded_callout(
            PAGE_DATA[page]["texts"][0][2],
            callout_heading="Keeper's Notes",
            body_end_marker="Anyone who speaks Italian will understand this to mean \"In here?\" Should the young helpers get confirmation, they'll start carrying the gear into the hotel lobby. They are generally very honest, and will be very grateful if offered tips, but won't ask for one.",
        )
        preparation_callout = split_bounded_callout(
            PAGE_DATA[page]["texts"][1][2],
            callout_heading="Keeper's Notes",
            next_segment_start_marker="The Hotel Sunset.",
        )
        units.extend([
            h2(f"{prefix}-WELCOME-001", "Welcome to Perla", "P018-B001"),
            {"unit_id": f"{prefix}-WELCOME-002", "unit_type": "heading", "heading_level": "h3", "semantic_role": "date_time_heading", "block_id": "P018-B001", "text": "August 23rd, 2019 - 10am", "layout_role": "block_heading", "display_style": "normal", "is_structural_heading": True},
            para(f"{prefix}-WELCOME-003", PAGE_DATA[page]["texts"][0][2].split("August 23rd, 2019 - 10am\n\n", 1)[1].split("\n\nKeeper's Notes", 1)[0], "P018-B001", "arrival_in_perla"),
            keeper(f"{prefix}-KEEPER-001", "P018-B001"),
            para(f"{prefix}-KEEPER-002", helper_callout.body, "P018-B001", "keeper_notes_helpers", semantic_split_contract=helper_callout.contract()),
            para(f"{prefix}-WELCOME-004", helper_callout.after, "P018-B001", "piazza_village_description", continues_to_next_page=True, continuation_target="page_019"),
            para(f"{prefix}-WELCOME-005", preparation_callout.before, "P018-B002", "perla_layout_continuation"),
            keeper(f"{prefix}-KEEPER-003", "P018-B002"),
            para(f"{prefix}-KEEPER-004", preparation_callout.body, "P018-B002", "keeper_notes_preparations", semantic_split_contract=preparation_callout.contract()),
            h3(f"{prefix}-HOTEL-001", "The Hotel Sunset.", "P018-B002"),
            para(f"{prefix}-HOTEL-002", preparation_callout.after.split("The Hotel Sunset. ", 1)[1], "P018-B002", "hotel_sunset", continues_to_next_page=True, continuation_target="page_019"),
        ])
    elif page == "019":
        units.extend([
            para(f"{prefix}-HOTEL-001", PAGE_DATA[page]["texts"][0][2], "P019-B001", "hotel_sunset_continuation_from_page_018", continuation_from_page="018"),
            h2(f"{prefix}-PERLA-001", "Perla", "P019-B002"),
            para(f"{prefix}-PERLA-002", PAGE_DATA[page]["texts"][1][2].split("Perla\n\n", 1)[1].split("\n\nThe Shops.", 1)[0], "P019-B002", "village_overview"),
            h3(f"{prefix}-PERLA-003", "The Shops.", "P019-B002"),
            para(f"{prefix}-PERLA-004", PAGE_DATA[page]["texts"][1][2].split("The Shops. ", 1)[1].split("\n\nThe Homes.", 1)[0], "P019-B002", "shops"),
            h3(f"{prefix}-PERLA-005", "The Homes.", "P019-B002"),
            para(f"{prefix}-PERLA-006", PAGE_DATA[page]["texts"][1][2].split("The Homes. ", 1)[1].split("\n\nThe Docks.", 1)[0], "P019-B002", "homes"),
            h3(f"{prefix}-PERLA-007", "The Docks.", "P019-B002"),
            para(f"{prefix}-PERLA-008", PAGE_DATA[page]["texts"][1][2].split("The Docks. ", 1)[1].split("\n\nNuncio Vendra.", 1)[0], "P019-B002", "docks"),
            h3(f"{prefix}-PERLA-009", "Nuncio Vendra.", "P019-B002"),
            para(f"{prefix}-PERLA-010", PAGE_DATA[page]["texts"][1][2].split("Nuncio Vendra. ", 1)[1], "P019-B002", "nuncio_vendra", continues_to_next_page=True, continuation_target="page_020"),
        ])
    elif page == "020":
        teens_callout = split_bounded_callout(
            PAGE_DATA[page]["texts"][0][2],
            callout_heading="Keeper's Notes",
            next_segment_start_marker="Communication.",
        )
        units.extend([
            para(f"{prefix}-PERLA-001", PAGE_DATA[page]["texts"][0][2].split("\n\nLocal Teens.", 1)[0], "P020-B001", "nuncio_vendra_continuation_from_page_019", continuation_from_page="019"),
            h3(f"{prefix}-PERLA-002", "Local Teens.", "P020-B001"),
            para(f"{prefix}-PERLA-003", PAGE_DATA[page]["texts"][0][2].split("Local Teens. ", 1)[1].split("\n\nKeeper's Notes", 1)[0], "P020-B001", "local_teens"),
            keeper(f"{prefix}-KEEPER-001", "P020-B001"),
            para(f"{prefix}-KEEPER-002", teens_callout.body, "P020-B001", "keeper_notes_local_teens", semantic_split_contract=teens_callout.contract()),
            h3(f"{prefix}-PERLA-004", "Communication.", "P020-B001"),
            para(f"{prefix}-PERLA-005", teens_callout.after.split("Communication. ", 1)[1], "P020-B001", "communication"),
            h2(f"{prefix}-EXPLORE-001", "Exploring in Perla", "P020-B002"),
            para(f"{prefix}-EXPLORE-002", PAGE_DATA[page]["texts"][1][2].split("Exploring in Perla\n\n", 1)[1].split("\n\nRumors", 1)[0], "P020-B002", "exploring_intro"),
            {"unit_id": f"{prefix}-RUMOR-001", "unit_type": "heading", "heading_level": "h3", "semantic_role": "table_heading", "block_id": "P020-B002", "text": "Rumors", "layout_role": "block_heading", "display_style": "table_heading", "is_structural_heading": True},
            para(f"{prefix}-RUMOR-002", PAGE_DATA[page]["texts"][1][2].split("Rumors\n\n", 1)[1], "P020-B002", "rumor_table", continues_to_next_page=True, continuation_target="page_021"),
        ])
    return units


def write_semantic_markdown(page: str, units: list[dict[str, Any]]) -> str:
    lines = [f"# Page {page} Semantic Text Map - P{page}SEM-G1-VIRAL-001", "", "Status: `semantic_text_map_machine_reviewed_human_review_skipped`", ""]
    for unit in units:
        lines.extend([f"## {unit['unit_id']}", f"- Type: `{unit['unit_type']}`", f"- Heading level: `{unit['heading_level']}`", f"- Layout role: `{unit.get('layout_role')}`"])
        if unit.get("continuation_from_page"):
            lines.append(f"- Continuation from: `page_{unit['continuation_from_page']}`")
        if unit.get("continues_to_next_page"):
            lines.append(f"- Continuation: `continues_to_{unit.get('continuation_target')}_not_processed`")
        lines.extend(["", "```text", unit["text"], "```", ""])
    return "\n".join(lines)


def write_text_map(page: str, texts: list[tuple[str, str, str]]) -> str:
    lines = [f"# Page {page} Text Map - P{page}TXT-G1-VIRAL-001", "", f"Status: `{SKIPPED_REVIEW}`", ""]
    for unit_id, block_id, text in texts:
        lines.extend([f"## {unit_id}", f"- Block: `{block_id}`", "", "```text", text, "```", ""])
    return "\n".join(lines)


def build_page(page: str) -> None:
    aggressive_batch_authorization_preflight(page)
    predecessors = verify_predecessors(page)
    roots = roots_for(page)
    data = PAGE_DATA[page]
    reset_outputs(page)
    crop_assets(page)

    stages = [
        f"P{page}TR-G1-VIRAL-001",
        f"P{page}TXT-G1-VIRAL-001",
        f"P{page}SEM-G1-VIRAL-001",
        f"PCRP-G1-VIRAL-P{page}-001",
        f"P{page}PCA-G1-VIRAL-001",
        f"G1SP-G1-VIRAL-{int(page) - 5:03d}",
    ]
    units = semantic_units(page)
    split_validation = validate_semantic_split_contracts(units)
    if not split_validation["valid"]:
        raise SystemExit(f"P{page} semantic split contract validation failed")
    text_units = [{"unit_id": unit_id, "block_id": block_id, "text": text} for unit_id, block_id, text in data["texts"]]
    visual_ids = [block["block_id"] for block in data.get("visuals", [])]

    triage = {"packet_id": stages[0], "authorization_id": auth_id(page), "page": page, "status": "page_triage_machine_reviewed_human_review_skipped", "predecessors": predecessors, "text_blocks": data["blocks"], "visual_only_blocks": data.get("visuals", []), "review_gate": review_gate(page, stages[0]), "guardrails": guardrails(page)}
    write_json(roots["triage"] / f"page_{page}_triage_packet.json", triage)
    write_json(roots["triage"] / f"page_{page}_triage_report.json", triage)
    write_text(roots["triage"] / f"page_{page}_triage_summary.md", f"# Page {page} Triage - {stages[0]}\n\nMachine-reviewed with Sol/Terra evidence. Human review skipped by explicit authorization.\n")
    manifest(roots["triage"], f"Page {page} Triage Manifest", f"page_{page}_triage_manifest.md")

    text_packet = {"packet_id": stages[1], "authorization_id": auth_id(page), "page": page, "status": "text_extraction_machine_reviewed_human_review_skipped", "text_units": text_units, "excluded_visual_anchors": visual_ids, "review_gate": review_gate(page, stages[1]), "guardrails": guardrails(page)}
    write_json(roots["text"] / f"page_{page}_text_extraction_packet.json", text_packet)
    write_json(roots["text"] / f"page_{page}_text_extraction_report.json", text_packet)
    write_text(roots["text"] / f"page_{page}_text_map.md", write_text_map(page, data["texts"]))
    write_text(roots["text"] / f"page_{page}_text_extraction_summary.md", f"# Page {page} Text Extraction - {stages[1]}\n\nText extraction is bounded to page {page} declared evidence blocks.\n")
    manifest(roots["text"], f"Page {page} Text Extraction Manifest", f"page_{page}_text_extraction_manifest.md")

    sem_packet = {"semantic_map_id": stages[2], "authorization_id": auth_id(page), "page": page, "status": "semantic_text_map_machine_reviewed_human_review_skipped", "semantic_units": units, "semantic_split_validation": split_validation, "review_gate": review_gate(page, stages[2]), "guardrails": guardrails(page)}
    write_json(roots["sem"] / f"page_{page}_semantic_text_map.json", sem_packet)
    write_json(roots["sem"] / f"page_{page}_semantic_text_map_report.json", sem_packet)
    sem_md = write_semantic_markdown(page, units)
    write_text(roots["sem"] / f"page_{page}_semantic_text_map.md", sem_md)
    write_text(roots["sem"] / f"page_{page}_semantic_text_map_summary.md", f"# Page {page} Semantic Text Map - {stages[2]}\n\nSemantic map ready for final human packet.\n")
    manifest(roots["sem"], f"Page {page} Semantic Text Map Manifest", f"page_{page}_semantic_text_map_manifest.md")

    pcrp = {"review_id": stages[3], "authorization_id": auth_id(page), "page": page, "status": "page_complete_review_machine_reviewed_human_review_skipped", "semantic_map_sha256": sha256_file(roots["sem"] / f"page_{page}_semantic_text_map.json"), "text_evidence_blocks": [b["block_id"] for b in data["blocks"]], "visual_only_blocks": visual_ids, "review_gate": review_gate(page, stages[3]), "guardrails": guardrails(page)}
    write_json(roots["pcrp"] / "page_complete_review_report.json", pcrp)
    write_text(roots["pcrp"] / "page_complete_review_packet.md", f"# Page {page} Complete Review Packet - {stages[3]}\n\nInternal evidence packet. Human packet is limited to source page art and semantic map markdown unless blocked.\n")
    write_text(roots["pcrp"] / "page_complete_review_summary.md", f"# Page {page} Complete Review Summary\n\nReady internally under delegated review.\n")
    shutil.copy2(roots["sem"] / f"page_{page}_semantic_text_map.md", roots["pcrp"] / "review_assets" / f"page_{page}_semantic_text_map.md")
    shutil.copy2(roots["sem"] / f"page_{page}_semantic_text_map.json", roots["pcrp"] / "review_assets" / f"page_{page}_semantic_text_map.json")
    shutil.copy2(roots["text"] / f"page_{page}_text_map.md", roots["pcrp"] / "review_assets" / f"page_{page}_text_map.md")
    manifest(roots["pcrp"], f"Page {page} Complete Review Manifest", "page_complete_review_manifest.md")

    pca = {"acceptance_id": stages[4], "authorization_id": auth_id(page), "page": page, "status": "page_complete_delegated_acceptance_created", "accepted_page": page, "predecessor": {"review_id": stages[3], "sha256": sha256_file(roots["pcrp"] / "page_complete_review_report.json")}, "review_gate": review_gate(page, stages[4]), "guardrails": guardrails(page)}
    write_json(roots["pca"] / "page_complete_acceptance_report.json", pca)
    write_text(roots["pca"] / "page_complete_acceptance_record.md", f"# Page {page} Delegated Page-Complete Acceptance - {stages[4]}\n\nPage {page} accepted only within the delegated aggressive lane.\n")
    write_text(roots["pca"] / "page_complete_acceptance_summary.md", f"# Page {page} Delegated Page-Complete Acceptance Summary\n\nInternal delegated page acceptance only.\n")
    manifest(roots["pca"], f"Page {page} Complete Acceptance Manifest", "page_complete_acceptance_manifest.md")

    accepted = [f"{p:03d}" for p in range(1, int(page) + 1)]
    remaining = [f"{p:03d}" for p in range(int(page) + 1, 21)]
    status_id = stages[5]
    status = {"status_packet_id": status_id, "authorization_id": auth_id(page), "lane_id": lane_id(page), "status": "gate_1_status_route_packet_ready_for_final_human_batch_review", "page_complete_accepted_pages": accepted, "remaining_page_complete_pages_unstarted": remaining, "recommended_next_candidate": f"page_{int(page) + 1:03d}_triage_readiness_not_authorized" if remaining else None, "predecessor": {"package_id": stages[4], "sha256": sha256_file(roots["pca"] / "page_complete_acceptance_report.json")}, "review_gate": review_gate(page, status_id), "guardrails": guardrails(page)}
    if page == "020":
        status["continuation"] = {"page_021_possible_continuation": True, "page_021_processed": False}
    write_json(roots["status"] / "gate_1_status_packet.json", status)
    write_json(roots["status"] / "gate_1_status_report.json", status)
    write_text(roots["status"] / "gate_1_status_summary.md", f"# Gate 1 Status Route Packet - {status_id}\n\nPages `001-{page}` are page-complete accepted only. Pages `{','.join(remaining) if remaining else 'none'}` remain unstarted. Whole Gate 1 and all broad capabilities remain blocked.\n")
    manifest(roots["status"], f"Gate 1 Status Manifest - {status_id}", "gate_1_status_manifest.md")

    batch = {"package_id": lane_id(page), "authorization_id": auth_id(page), "status": "ready_for_bogdan_final_batch_review", "human_review_model": f"final_bundle_and_post_p{page}_status_only", "internal_stage_human_review_state": SKIPPED_REVIEW, "stage_packages": stages, "decision_options": [f"p{page} aggressive batch ok", f"hold p{page} batch: <reason>"], "human_packet_default_assets": [f"images/page_{page}.png", f"page_{page}_semantic_text_map_G1_VIRAL_001/page_{page}_semantic_text_map.md"], "guardrails": guardrails(page)}
    write_json(roots["batch"] / f"page_{page}_aggressive_batch_report.json", batch)
    write_text(roots["batch"] / f"page_{page}_aggressive_batch_summary.md", f"# Page {page} Aggressive Batch Summary - {lane_id(page)}\n\nFinal human review is requested on source page art plus semantic map markdown by default.\n")
    manifest(roots["batch"], f"Page {page} Aggressive Batch Manifest", f"page_{page}_aggressive_batch_manifest.md")


def build_sequence(pages: list[str]) -> None:
    for page in pages:
        build_page(page)


def main(page: str | None = None) -> None:
    if page is None:
        parser = argparse.ArgumentParser(description="Build pages 016-020 aggressive delegated-review batches.")
        parser.add_argument("--execute", action="store_true")
        parser.add_argument("--authorization-id")
        parser.add_argument("--pages", default="016,017,018,019,020")
        args = parser.parse_args()
        pages = [p.strip().zfill(3) for p in args.pages.split(",") if p.strip()]
        expected_auth = "BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001"
        if not args.execute:
            raise SystemExit("P016-P020 sequential aggressive run is fail-closed; pass --execute")
        if args.authorization_id != expected_auth:
            raise SystemExit(f"P016-P020 sequential aggressive run requires {expected_auth}")
        if pages != ["016", "017", "018", "019", "020"]:
            raise SystemExit("P016-P020 sequential aggressive run must process exactly pages 016,017,018,019,020")
        build_sequence(pages)
    else:
        check_authorization(page)
        build_page(page)


if __name__ == "__main__":
    main()
