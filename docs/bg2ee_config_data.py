gamestr = "Baldur's Gate 2 EE 2.6.6.0"
headers = ["Area", "NPC", "XP", "Gold Carried", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"]

areas = [
	"aerie (Spawned)",
	"ambush2 (Spawned)",
	"ammerc (Spawned)",
	"ammgrd (Spawned)",
	"ammlegs (Spawned)",
	"amntrp02 (Spawned)",
	"amntrp03 (Spawned)",
	"anomen (Spawned)",
	"ar0020 (Spawned) - City Gates",
	"ar0020 - City Gates",
	"ar0021 - Crooked Crane 1st Floor",
	"ar0022 (Spawned) - Crooked Crane 2nd Floor",
	"ar0028 - Candlekeep Dream (After PC Soultheft)",
	"ar0041 (Spawned) - Random Encounter City",
	"ar0042 (Spawned) - Random Encounter Outdoor",
	"ar0043 (Spawned) - Random Encounter Outdoor (With rocks)",
	"ar0044 (Spawned) - Random Encounter Outdoor (sand)",
	"ar0045 (Spawned) - Random Encounter City",
	"ar0046 (Spawned) - Random Encounter City (bridge)",
	"ar0071 - \"Spellhold (Imoen Soultheft Cutscene -- \"\"Silence do, you have no purpose...\"\")\"",
	"ar0072 - Ust Natha Temple (Irenicus/Bodhi, Ardula/Phaere Cutscene)",
	"ar0082 - Lich Grave in Bridge District Inn",
	"ar0108 (Spawned)",
	"ar0202 - The Unseeing Eye Cult Hideout",
	"ar0206 - Ghoul village (Temple District)",
	"ar0300 (Spawned) - The Docks",
	"ar0300 - The Docks",
	"ar0301 - Mae'Var's Hide Out",
	"ar0302 - Mae'Var's Inn 1st Floor -- Entrance",
	"ar0303 - Mae'Var's Inn 2nd Floor -- Training Area",
	"ar0305 - Shadow Thieves Guild Entrance",
	"ar0306 - Renal Bloodscalp's Hideout",
	"ar0307 - Aran Linvail's Hideout",
	"ar0308 (Spawned) - Harper's 1st Floor",
	"ar0308 - Harper's 1st Floor",
	"ar0311 (Spawned) - Living Room (Entry points outside and up) -- Gaelan?",
	"ar0312 - Sleeping Room (Entry point down) -- Arledrian",
	"ar0313 (Spawned) - Sea Bounty Tavern 1st Floor",
	"ar0313 - Sea Bounty Tavern 1st Floor",
	"ar0314 (Spawned) - Sea Bounty Tavern 2nd Floor",
	"ar0314 - Sea Bounty Tavern 2nd Floor",
	"ar0317 - Sleeping Room (Favour for Edwin -- Mae'Var Plot)",
	"ar0319 - Temple of Oghma",
	"ar0322 (Spawned) - Thief Stronghold (1st Floor)",
	"ar0322 - Thief Stronghold (1st Floor)",
	"ar0329 - Aran's Hideout (sided with Bodhi)",
	"ar0332 - Barracks in the Docks",
	"ar0333 - Barracks in the Docks",
	"ar0400 (Spawned) - Slums",
	"ar0400 - Slums",
	"ar0401 - Jansen Cellar",
	"ar0402 (Spawned) - Jansen 1st Floor",
	"ar0402 - Jansen 1st Floor",
	"ar0403 (Spawned) - Jansen 2nd Floor",
	"ar0404 - Sewers beneath Coronet -- Lilarcor",
	"ar0405 - Slaver's Ship Building",
	"ar0406 (Spawned) - Copper Coronet",
	"ar0406 - Copper Coronet",
	"ar0407 - Prebek's House",
	"ar0408 - Temple of Ilmater",
	"ar0410 - Sphere: Navigator's room -- Lavok's Hideout",
	"ar0411 (Spawned) - Sphere: Entrance floor",
	"ar0411 - Sphere: Entrance floor",
	"ar0412 - Sphere: Ice and Fire Room",
	"ar0414 - Sphere: Demon Plane",
	"ar0415 (Spawned) - Living Room 1st Floor",
	"ar0417 (Spawned) - Living Room",
	"ar0418 - Myconids",
	"ar0500 (Spawned) - Bridge District",
	"ar0500 - Bridge District",
	"ar0501 (Spawned) - Tanner's Hideout 1st Floor",
	"ar0504 - Saerk's House 1st Floor",
	"ar0505 (Spawned) - Saerk's House 2nd Floor",
	"ar0505 - Saerk's House 2nd Floor",
	"ar0506 - Noble House 1st Floor",
	"ar0507 - Kidnappers' Hideout 1st Floor",
	"ar0509 - Five Flagons Inn 1st Floor",
	"ar0510 - Five Flagons Inn Theater",
	"ar0511 (Spawned) - Five Flagons Inn 2nd Floor",
	"ar0511 - Five Flagons Inn 2nd Floor",
	"ar0512 - Temple of Helm",
	"ar0513 (Spawned) - Calbor's Inn at Bridge District 1st Floor",
	"ar0513 - Calbor's Inn at Bridge District 1st Floor",
	"ar0514 - Inn at Bridge District 2nd Floor",
	"ar0515 - Inn at Bridge District 3rd Floor",
	"ar0516 - Planar Prison",
	"ar0522 (Spawned) - Five Flagons Inn (Stronghold)",
	"ar0522 - Five Flagons Inn (Stronghold)",
	"ar0523 (Spawned) - Five Flagons Theater (Stronghold)",
	"ar0529 (Spawned) - Neb's Hideout",
	"ar0602 - Irenicus's Dungeon 1st Floor",
	"ar0603 - Irenicus's Dungeon 2nd Floor",
	"ar0604 - Circus Tent 1st Floor",
	"ar0606 - Circus Tent 3rd Floor",
	"ar0607 (Spawned) - Circus Tent restored",
	"ar0700 (Spawned) - Waukeen's Promenade",
	"ar0700 - Waukeen's Promenade",
	"ar0701 (Spawned) - The Sewers",
	"ar0701 - The Sewers",
	"ar0702 (Spawned) - Adventurer's Mart",
	"ar0702 - Adventurer's Mart",
	"ar0704 (Spawned) - Mithrest Inn",
	"ar0704 - Mithrest Inn",
	"ar0705 - Mekrath's Hideout in the Sewers (Haer'Dalis Plot)",
	"ar0706 - Armourer/Fletcher",
	"ar0709 - Den of the Seven Vales 1st Floor",
	"ar0712 - Den of the Seven Vales 2nd Floor",
	"ar0713 - Store or Inn at Promenade",
	"ar0800 (Spawned) - Graveyard",
	"ar0800 - Graveyard",
	"ar0801 (Spawned) - Bodhi's Hideout (sided with Aran)",
	"ar0802 (Spawned) - Netherscroll, Korgan's Book, Edwin",
	"ar0804 - Pai'Na's Hideout",
	"ar0806 - Crypt",
	"ar0808 (Spawned) - Bodhi's Hideout (Abduction Plot, getting Imoen's soul)",
	"ar0808 - Bodhi's Hideout (Abduction Plot, getting Imoen's soul)",
	"ar0809 (Spawned) - Bodhi's Lair (Abduction Plot, getting Imoen's soul)",
	"ar0900 (Spawned) - Temple District",
	"ar0900 - Temple District",
	"ar0901 (Spawned) - Temple of Helm",
	"ar0901 - Temple of Helm",
	"ar0902 (Spawned) - Temple of Lathander",
	"ar0902 - Temple of Lathander",
	"ar0903 - Order of the Radiant Heart",
	"ar0904 (Spawned) - Temple of Talos",
	"ar0904 - Temple of Talos",
	"ar0905 - Pimlico's Estate",
	"ar1000 (Spawned) - Government District",
	"ar1000 - Government District",
	"ar1001 (Spawned) - Delryn's Estate",
	"ar1001 - Delryn's Estate",
	"ar1002 - Councel Building",
	"ar1003 - Firecam's Estate",
	"ar1005 - Prison",
	"ar1006 (Spawned) - Jysstev's Estate (Oisig Plot)",
	"ar1006 - Jysstev's Estate (Oisig Plot)",
	"ar1007 (Spawned) - Noble House",
	"ar1010 - Temple of Waukeen",
	"ar1100 (Spawned) - Umar Hills",
	"ar1100 - Umar Hills",
	"ar1103 - Jermien's Cabin",
	"ar1104 (Spawned) - Mayor Lloyd's Cabin",
	"ar1105 (Spawned) - Imnesvale Inn",
	"ar1105 - Imnesvale Inn",
	"ar1200 (Spawned) - Windspear Hills",
	"ar1200 - Windspear Hills",
	"ar1201 - Firkraag's Entrance",
	"ar1202 (Spawned) - Firkaag's Maze",
	"ar1202 - Firkaag's Maze",
	"ar1203 - Firkraag's Hideout",
	"ar1204 (Spawned) - Garren Windspear's Cabin",
	"ar1300 (Spawned) - De'Arnise Keep Destroyed",
	"ar1300 - De'Arnise Keep Destroyed",
	"ar1301 - De'Arnise Cellar",
	"ar1302 (Spawned) - De'Arnise Keep 1st Floor",
	"ar1303 - De'Arnise Keep 2nd Floor (Destroyed)",
	"ar1304 (Spawned) - De'Arnise Keep (Restored, Stronghold)",
	"ar1304 - De'Arnise Keep (Restored, Stronghold)",
	"ar1306 (Spawned) - De'Arnise Keep (Stronghold)",
	"ar1306 - De'Arnise Keep (Stronghold)",
	"ar1400 (Spawned) - Shadow Temple Land (restored, Ranger)",
	"ar1400 - Shadow Temple Land (restored, Ranger)",
	"ar1401 (Spawned) - Shadow Temple",
	"ar1401 - Shadow Temple",
	"ar1404 - Shadow Temple Land shadowed",
	"ar1600 (Spawned) - Brynnlaw",
	"ar1600 - Brynnlaw",
	"ar1602 - Brynnlaw's Inn",
	"ar1605 - CW's House",
	"ar1606 (Spawned) - House of Desharik's Lover",
	"ar1607 - Githyanki Assault",
	"ar1610 - Brothel Prison",
	"ar1611 - Brothel",
	"ar1612 - Brothel Kitchen",
	"ar1800 - North Forest",
	"ar1900 (Spawned) - Druid Grove Area",
	"ar1900 - Druid Grove Area",
	"ar1901 (Spawned) - Druid Grove",
	"ar1901 - Druid Grove",
	"ar1902 - Storehouse (Ihtafeer's Storehouse)",
	"ar1905 (Spawned) - Store Tower",
	"ar2000 (Spawned) - Trademeet",
	"ar2000 - Trademeet",
	"ar2002 - Fentan's House",
	"ar2007 - High Merchant's Estate",
	"ar2008 - Temple of Waukeen",
	"ar2010 - Trademeet's Inn",
	"ar2011 (Spawned) - Alibakkar's Estate",
	"ar2011 - Alibakkar's Estate",
	"ar2012 (Spawned) - Lurraxol's Estate",
	"ar2012 - Lurraxol's Estate",
	"ar2017 - Courtesan Tent",
	"ar2100 (Spawned) - Underdark",
	"ar2100 - Underdark",
	"ar2200 (Spawned) - Ust Natha",
	"ar2200 - Ust Natha",
	"ar2201 (Spawned) - Temple in Ust Natha",
	"ar2201 - Temple in Ust Natha",
	"ar2202 - Inn in Ust Natha 1st Floor",
	"ar2203 - Inn in Ust Natha; 2nd Floor",
	"ar2205 (Spawned) - House in Ust Natha",
	"ar2206 - Qilue's House in Ust Natha",
	"ar2207 - Deirex's Tower in Ust Natha",
	"ar2208 - Jarlaxle's House wherever",
	"ar2209 - Jae'llat's House",
	"ar2300 (Spawned) - Sahuagin City",
	"ar2300 - Sahuagin City",
	"ar2401 - Cave Between Underdark and Exit from Underdark",
	"ar2402 - Kuo Toa in Underdark",
	"ar2600 (Spawned) - Thetyr Wood",
	"ar2600 - Thetyr Wood",
	"ar2601 (Spawned) - Meet Drizzt Do'Urden",
	"ar2800 (Spawned) - Suldanessellar",
	"ar2800 - Suldanessellar",
	"ar2801 - House of High Priestess of Suldanessellar",
	"ar2806 (Spawned) - Tree of Life",
	"ar2806 - Tree of Life",
	"ar2903 - Greed (Abyss)",
	"ar2904 - Selfish (Abyss)",
	"ar3000 - Watcher's Keep",
	"ar3001 - Watcher's Keep -- Altar level",
	"ar3005 - Watcher's Keep -- tieflings",
	"ar3006 - Watcher's Keep -- Succubus",
	"ar3012 - Watcher's Keep -- Tahazzar",
	"ar3013 (Spawned) - Watcher's Keep -- Ka'rashur",
	"ar3013 - Watcher's Keep -- Ka'rashur",
	"ar3015 - Watcher's Keep -- Aesgareth",
	"ar3016 - Watcher's Keep -- Chromatic Demon; Elementalist Level",
	"ar4500 (Spawned) - Pocket Plane",
	"ar5000 - Saradush",
	"ar5002 - Gromnir's Hideout",
	"ar5003 - Saradush Tavern (Tankard Tree)",
	"ar5004 - Temple of Waukeen",
	"ar5007 (Spawned) - Basement Entrance to Gromnir's Hideout",
	"ar5007 - Basement Entrance to Gromnir's Hideout",
	"ar5008 (Spawned) - Kiser's Home",
	"ar5009 (Spawned) - House (no exit?)",
	"ar5013 - Sewers beneath Saradush",
	"ar5014 (Spawned) - Kiser's Home -- Cellar",
	"ar5014 - Kiser's Home -- Cellar",
	"ar5015 (Spawned) - Saradush Militia Entrance",
	"ar5016 - Saradush Castle Jail (Kiser Plot)",
	"ar5200 - Fire Giant Entrance Area",
	"ar5202 - Nyalee's Hideout; Gorion Wraith",
	"ar5203 (Spawned) - Yaga-Shura's Camp",
	"ar5500 (Spawned) - Amkethran",
	"ar5500 - Amkethran",
	"ar5501 (Spawned) - Amkethran Inn",
	"ar5501 - Amkethran Inn",
	"ar5502 - Kerrick the Smith's House",
	"ar5504 (Spawned) - Smuggler Cave",
	"ar5504 - Smuggler Cave",
	"ar5506 - Commoner's Home",
	"ar5508 - Faheed's Home",
	"ar6000 (Spawned) - Abazigal's Entrance",
	"ar6000 - Abazigal's Entrance",
	"ar6001 - Abazigal's Lair Entrance Hall",
	"ar6002 - Abazigal's Lair -- Cells",
	"ar6003 - Abazigal's Lair -- Iycanth the Mad, Bondari",
	"ar6100 (Spawned) - Area outside Sendai's Hideout",
	"ar6100 - Area outside Sendai's Hideout",
	"ar6102 - Sendai's Lair -- Slavemaster",
	"ar6106 - Sendai's Lair -- Captain Egeissag",
	"ar6108 (Spawned) - Sendai's Lair -- Sendai",
	"ar6108 - Sendai's Lair -- Sendai",
	"ar6300 - Oasis in Tethyr",
	"ar6400 - River Area",
	"arnspw1 (Spawned)",
	"baldur (Spawned)",
	"c6fledg2 (Spawned)",
	"c6spwn1 (Spawned)",
	"c6spwn2 (Spawned)",
	"c6spwn3 (Spawned)",
	"c6spwn4 (Spawned)",
	"c6spwn5 (Spawned)",
	"c6tanov (Spawned)",
	"cernd (Spawned)",
	"colette (Spawned)",
	"cut01 (Spawned)",
	"cut05a (Spawned)",
	"cut12a (Spawned)",
	"cut17b (Spawned)",
	"cut204f (Spawned)",
	"cut204f2 (Spawned)",
	"cut204f3 (Spawned)",
	"cut204f4 (Spawned)",
	"cut205b (Spawned)",
	"cut207a (Spawned)",
	"cut21b (Spawned)",
	"cut236a (Spawned)",
	"cut236b (Spawned)",
	"cut237a (Spawned)",
	"cut239a (Spawned)",
	"cut23a (Spawned)",
	"cut240a (Spawned)",
	"cut241a (Spawned)",
	"cut242a (Spawned)",
	"cut243b (Spawned)",
	"cut243c (Spawned)",
	"cut26a (Spawned)",
	"cut26b (Spawned)",
	"cut31a (Spawned)",
	"cut31g (Spawned)",
	"cut31l (Spawned)",
	"cut31q (Spawned)",
	"cut31r (Spawned)",
	"cut32c (Spawned)",
	"cut32d (Spawned)",
	"cut32e (Spawned)",
	"cut32e2 (Spawned)",
	"cut32h (Spawned)",
	"cut32i (Spawned)",
	"cut32j (Spawned)",
	"cut32k (Spawned)",
	"cut33a (Spawned)",
	"cut33b (Spawned)",
	"cut35k (Spawned)",
	"cut35l (Spawned)",
	"cut36a (Spawned)",
	"cut37a (Spawned)",
	"cut38a (Spawned)",
	"cut39a (Spawned)",
	"cut39b (Spawned)",
	"cut40b (Spawned)",
	"cut41b (Spawned)",
	"cut41d (Spawned)",
	"cut41o (Spawned)",
	"cut41r (Spawned)",
	"cut41y (Spawned)",
	"cut41z (Spawned)",
	"cut41za (Spawned)",
	"cut41ze (Spawned)",
	"cut41zg (Spawned)",
	"cut51a (Spawned)",
	"cut60b (Spawned)",
	"cut80a (Spawned)",
	"cut80b (Spawned)",
	"cut80c (Spawned)",
	"cut80d (Spawned)",
	"cut80e (Spawned)",
	"cut80f (Spawned)",
	"cut81a (Spawned)",
	"cut81b (Spawned)",
	"cut81c (Spawned)",
	"cut81d (Spawned)",
	"cut81e (Spawned)",
	"cut81f (Spawned)",
	"cut82a (Spawned)",
	"cut82b (Spawned)",
	"cut82c (Spawned)",
	"cut82d (Spawned)",
	"cut82e (Spawned)",
	"cut82f (Spawned)",
	"cut82g (Spawned)",
	"cut87a (Spawned)",
	"cutamk01 (Spawned)",
	"cutd1 (Spawned)",
	"dadrow5 (Spawned)",
	"dwdoor01 (Spawned)",
	"dwface02 (Spawned)",
	"dwface03 (Spawned)",
	"dwface04 (Spawned)",
	"dwface06 (Spawned)",
	"edwin (Spawned)",
	"gaalsht (Spawned)",
	"gartrig (Spawned)",
	"githspwn (Spawned)",
	"grave (Spawned)",
	"hashout (Spawned)",
	"hdmurd (Spawned)",
	"jaheira (Spawned)",
	"jan (Spawned)",
	"mazzy (Spawned)",
	"movie02b (Spawned)",
	"movie05b (Spawned)",
	"mvally (Spawned)",
	"nalia (Spawned)",
	"newgame (Spawned)",
	"oh4000 - Rasaad - The Amphitheater",
	"oh4010 - Rasaad - Tears of Selune battle encounter",
	"oh4100 (Spawned) - Rasaad - Dark Moon Heretic Temple",
	"oh4100 - Rasaad - Dark Moon Heretic Temple",
	"oh4101 (Spawned) - Rasaad - Dark Moon Heretic Temple Interior",
	"oh4200 - Rasaad - Dwarven Clanhold Exterior",
	"oh4210 - Rasaad - Dwarven Clanhold Interior",
	"oh4220 (Spawned) - Rasaad - Dwarven Mines",
	"oh4220 - Rasaad - Dwarven Mines",
	"oh5000 - Dorn - Radiant Heart (Wedding)",
	"oh5200 (Spawned) - Dorn - Resurrection Gorge Interior",
	"oh5300 (Spawned) - Dorn - Helmite Camp",
	"oh5300 - Dorn - Helmite Camp",
	"oh5400 (Spawned) - Dorn - Forest Clearing",
	"oh5500 (Spawned) - Dorn - Lunia",
	"oh5500 - Dorn - Lunia",
	"oh6000 (Spawned) - Neera - The Wild Forest",
	"oh6000 - Neera - The Wild Forest",
	"oh6100 - Neera - The Hidden Refuge",
	"oh6200 (Spawned) - Neera - The Hidden Refuge (Destroyed)",
	"oh6200 - Neera - The Hidden Refuge (Destroyed)",
	"oh6300 (Spawned) - Neera - Red Wizard Enclave",
	"oh6300 - Neera - Red Wizard Enclave",
	"oh6450 - Neera - The Black Pits: Arena",
	"oh6460 - Neera - The Black Pits: Staging Area",
	"oh6500 (Spawned) - Neera - Thayan Estate",
	"oh6500 - Neera - Thayan Estate",
	"oh7000 - Hexxat - Top Left Quarter (Dragomir)",
	"oh7100 - Hexxat - Bottom Left Quarter (Shou Lung)",
	"oh7200 (Spawned) - Hexxat - Bottom Right Quarter (Zakhara)",
	"oh7200 - Hexxat - Bottom Right Quarter (Zakhara)",
	"oh7300 - Hexxat - Completed Maze (Korkorran)",
	"oh8000 (Spawned) - TBP2 - Suzail Tavern",
	"oh8100 - TBP2 - Staging Area Map",
	"ohb_501 (Spawned)",
	"ohb_502 (Spawned)",
	"ohbare1 (Spawned)",
	"ohbare2 (Spawned)",
	"ohbcut00 (Spawned)",
	"ohbcut08 (Spawned)",
	"ohbcut13 (Spawned)",
	"ohbcut17 (Spawned)",
	"ohbcut20 (Spawned)",
	"ohbcut24 (Spawned)",
	"ohbhub (Spawned)",
	"ohbpost (Spawned)",
	"ohdcut04 (Spawned)",
	"ohdcut07 (Spawned)",
	"ohdcut12 (Spawned)",
	"ohdlugen (Spawned)",
	"ohdwra01 (Spawned)",
	"ohdyarrg (Spawned)",
	"ohhcab25 (Spawned)",
	"ohhphrey (Spawned)",
	"ohhwra01 (Spawned)",
	"ohncut02 (Spawned)",
	"ohncut05 (Spawned)",
	"ohncut12 (Spawned)",
	"ohncut15 (Spawned)",
	"ohncut16 (Spawned)",
	"ohncut1a (Spawned)",
	"ohnmcut1 (Spawned)",
	"ohr_join (Spawned)",
	"ohrambus (Spawned)",
	"ohrcut4y (Spawned)",
	"ppalt (Spawned)",
	"ptalarm1 (Spawned)",
	"sahorb (Spawned)",
	"sharkamb (Spawned)",
	"shthass1 (Spawned)",
	"slaver2 (Spawned)",
	"suscene1 (Spawned)",
	"suscene3 (Spawned)",
	"suscene4 (Spawned)",
	"trrak01 (Spawned)",
	"ttarnor (Spawned)",
	"udsoltri (Spawned)",
	"und5509 (Spawned)",
	"unknown",
	"vampsttp (Spawned)",
]

types = {
	"Amulet": [
		"Amulet of Power",
		"Amulet of Spell Warding",
		"Bloodstone Amulet",
		"Galvena's Medallion",
		"Gold Necklace",
		"Keepsake Locket",
		"Necklace of Talos",
		"Pearl Necklace",
		"Periapt of Proof Against Poison",
		"Ruby Pendant of Beguiling",
		"Sigil of Tyr",
		"Silver Necklace",
		"The One Gift Lost",
		"The Protector +1",
		"Thrall Collar",
	],
	"Armor": [
		"Adventurer's Robe",
		"Leather Armor",
		"Leather Armor +3",
		"Skin of the Ghoul +4",
		"Studded Leather Armor",
	],
	"Arrows": [
		"Acid Arrow +1",
		"Arrow",
		"Arrow +1",
		"Arrow +2",
		"Arrow +3",
		"Arrow of Biting",
		"Arrow of Detonation",
		"Arrow of Dispelling",
		"Arrow of Fire",
		"Arrow of Ice",
		"Arrow of Piercing +1",
	],
	"Axe": [
		"Battle Axe",
		"Battle Axe +2",
		"Stonefire +3",
		"Throwing Axe",
	],
	"Belt & Girdle": [
		"Adoy's Belt",
		"Elves' Bane",
		"Girdle of Fortitude",
		"Girdle of Hill Giant Strength",
	],
	"Bolts": [
		"Bolt",
		"Bolt +1",
		"Bolt +2",
		"Bolt of Biting ",
		"Bolt of Lightning",
		"Drow Bolt +1",
		"Drow Bolt of Sleep",
		"Drow Bolt of Stunning",
		"Flasher Master Bruiser Mate",
		"Kuo-toan Bolt",
		"Paralytic Bolt",
	],
	"Books & misc": [
		"Acorn of Yarrow",
		"Acorns",
		"Aerie's Body",
		"Anomen's Body",
		"Black Spider Figurine",
		"Book of Infinite Spells",
		"Bowstring of Gond",
		"Demon Heart",
		"Dennis's Mother's Gong",
		"Draconis's Head",
		"Edwin's Documents",
		"Efreeti Bottle",
		"Elven Holy Water",
		"Exotic Hide",
		"Fil's Summoning Stone",
		"Flail Head (Acid)",
		"Gem of Seeing",
		"Guril Berries",
		"Hindo's Hand",
		"Illithium Ore",
		"Ink and Sand",
		"Jae'llat Wardstone",
		"Jaheira's Body",
		"Journal of Umolex the Far-Eyed",
		"Light Gem",
		"Littleman the Stuffed Bear",
		"Magical Rope",
		"Meems's Special Grog",
		"Mekrath's Mirror",
		"Mug of Ale",
		"Note",
		"Oak Bark",
		"Piece of Red Cloth",
		"Qilue's Brain",
		"Rebel's Orb",
		"Rope",
		"Shakti Figurine",
		"Silver Hilt",
		"Silver Pantaloons",
		"Smuggled Shipment",
		"Solik Berries",
		"Tears of Bhaal",
		"The Genie's Flask",
		"The Journal of Saemon Havarian",
		"Viconia's Body",
		"Wardstone for Asylum",
		"Wave Blade",
		"Wooden Stake",
		"Xachrimos's Summoning Stone",
		"rndtre01.itm",
		"rndtre02.itm",
		"rndtre03.itm",
		"rndtre04.itm",
		"rndtre05.itm",
	],
	"Books/Broken shields/bracelets": [
		"Book of Rituals",
		"Bounty Notice",
		"Deed to the Windspear Hills",
		"History of the Dead Three",
		"History of the Last March of the Giants",
		"Isaea's Slavery Document",
		"Lellyn's Journal",
		"Note",
		"Scrap of Paper",
		"Scroll of Reversal",
		"The Book of Kaza",
		"The Journal of Geldorf Tinbasher",
		"Worn Pamphlet",
	],
	"Boots": [
		"The Paws of the Cheetah",
	],
	"Bow": [
		"Composite Longbow",
		"Composite Longbow +1",
		"Composite Longbow +2",
		"Longbow",
		"Longbow +2",
		"Longbow +3",
		"Shortbow",
		"Shortbow +1",
		"Shortbow +2",
	],
	"Bracers & gauntlets": [
		"Bracers of Defense AC 7",
		"Bracers of Defense AC 8",
		"Bracers to the Death",
		"Gauntlets of Aln Zekk",
		"Glimmering Bands",
		"Gloves of Missile Snaring",
		"Jansen Techno-Gloves",
		"Xarrnous's Second Sword Arm",
	],
	"Bullets": [
		"Bullet",
		"Bullet +1",
		"Bullet +2",
		"Sunstone Bullet +1",
	],
	"Cloaks & Robes": [
		"Cloak of Atonement",
		"Cloak of Balduran",
		"Cloak of Displacement",
		"Cloak of Dragomir",
		"Cloak of Mirroring",
		"Cloak of Protection +1",
		"Cloak of the High Forest +1",
		"Cloak of the Shield",
		"Cloak of the Stars",
		"Cowl of the Stars",
		"Drow Piwafwi Cloak",
		"Shadow Thief Cloak",
		"The Spirit's Shield +2",
		"Whispers of Silence",
	],
	"Crossbow": [
		"Flasher Launcher",
		"Heavy Crossbow",
		"Heavy Crossbow +2",
		"Light Crossbow",
		"Light Crossbow +1",
		"Light Crossbow +2",
	],
	"Dagger": [
		"Boneblade +4",
		"Boomerang Dagger +2",
		"Dagger",
		"Dagger +1",
		"Dagger +2",
		"Ixil's Spike",
		"Poisoned Throwing Dagger",
		"Shadow Thief Dagger",
		"Throwing Dagger",
	],
	"Darts": [
		"Dart",
		"Dart +1",
		"Dart of Stunning",
		"Dart of Wounding",
	],
	"Flail": [
		"Drow Flail +3",
		"Flail",
		"Flail +1",
		"Flail +2",
	],
	"Gem": [
		"Andar Gem",
		"Black Opal",
		"Bloodstone Gem",
		"Diamond",
		"Emerald",
		"Fire Agate Gem",
		"Garnet Gem",
		"Horn Coral Gem",
		"King's Tears",
		"Lynx Eye Gem",
		"Moonbar Gem",
		"Moonstone Gem",
		"Pearl",
		"Rogue Stone",
		"Scepter Gem",
		"Shandon Gem",
		"Sphene Gem",
		"Water Opal",
		"Waterstar Gem",
	],
	"Halberd": [
		"Halberd",
		"Halberd +2",
	],
	"Hammer": [
		"Aegis-fang +3",
		"War Hammer +3",
	],
	"Headgear": [
		"Circlet of Netheril",
		"Helm of the Noble +1",
		"Helmet",
		"Lavender Ioun Stone",
		"Roranach's Horn",
	],
	"Key": [
		"Beastmaster Key",
		"Branson's Key",
		"Firkraag Prison Key",
		"Guild House Key",
		"Haegan's Key",
		"Holding Pen Key",
		"Intricate Key",
		"Key",
		"Key of Scholars",
		"Key of the Master's Crypt",
		"Monastery Gate Key",
		"Piece of Burial Mask",
		"Portal Key",
		"Sahuagin Treasury Key",
		"Secret Jail Door Key",
		"Sewage Golem Key",
		"Shadow Prison Key",
		"Shadow Thief Prison Key",
		"Slave Pen Key",
		"Temple Key",
		"Wand of Missiles Key",
	],
	"Large sword": [
		"Abyssal Blade",
		"Bastard Sword",
		"Bastard Sword +1",
		"Bastard Sword +2",
		"Bastard Sword +3",
		"Blackrazor +3",
		"Drow Long Sword +3",
		"Hawksight +2",
		"Holy Long Sword of Tyr +3",
		"Long Sword",
		"Long Sword +1",
		"Long Sword +2",
		"Ninja-To",
		"Scimitar",
		"The Burning Earth +1",
		"The Ogre's Sword",
		"Twinkle +3",
		"Two-handed Sword",
		"Two-handed Sword +2",
		"Two-handed Sword +3",
	],
	"Mace & Club": [
		"Club",
		"Mace +1",
		"Mace +2",
	],
	"Morning star": [
		"Morning Star",
		"Morning Star +3",
	],
	"Potion": [
		"Antidote",
		"Bottle of Wine",
		"Elixir of Health",
		"Empty Breath Potion Flask",
		"Oil of Fiery Burning",
		"Oil of Speed",
		"Potion of Absorption",
		"Potion of Clairvoyance",
		"Potion of Clarity",
		"Potion of Cloud Giant Strength",
		"Potion of Explosions",
		"Potion of Extra Healing",
		"Potion of Fire Giant Strength",
		"Potion of Freedom",
		"Potion of Frost Giant Strength",
		"Potion of Healing",
		"Potion of Heroism",
		"Potion of Hill Giant Strength",
		"Potion of Insight",
		"Potion of Invisibility",
		"Potion of Invulnerability",
		"Potion of Magic Blocking",
		"Potion of Magic Protection",
		"Potion of Magic Shielding",
		"Potion of Master Thievery",
		"Potion of Power",
		"Potion of Regeneration",
		"Potion of Stone Form",
		"Potion of Stone Giant Strength",
		"Potion of Storm Giant Strength",
		"Potion of Superior Healing",
		"Red Potion",
	],
	"Quarterstaff": [
		"Cleric's Staff +3",
		"Quarterstaff",
		"Quarterstaff +1",
		"Rod of Terror",
	],
	"Ring": [
		"Angel Skin Ring",
		"Batalista's Passport",
		"Bloodstone Ring",
		"Dal Family Ring",
		"Dawn Ring",
		"Druid's Ring",
		"Edventar's Gift",
		"Fire Opal Ring",
		"Gold Ring",
		"Jade Ring",
		"Oaken Ring",
		"Onyx Ring",
		"Ring of Acuity",
		"Ring of Anti-Venom",
		"Ring of Fire Control",
		"Ring of Human Influence",
		"Ring of Lock Picks",
		"Ring of Regeneration",
		"Ring of Spell Turning",
		"Ring of the Princes +1",
		"Ring of the Ram",
		"Ruby Ring",
		"Sandthief's Ring",
		"Silver Ring",
		"The Guard's Ring +2",
		"Topsider's Crutch",
	],
	"Scroll": [
		"Chain Lightning",
		"Color Spray",
		"Cone of Cold",
		"Conjure Earth Elemental",
		"Conjure Fire Elemental",
		"Contact's Note",
		"Contingency",
		"Cure Critical Wounds",
		"Cure Serious Wounds",
		"Death Fog",
		"Death Spell",
		"Delayed Blast Fireball",
		"Demin's Note",
		"Disintegrate",
		"Dispel Magic",
		"Find Familiar",
		"Fireball",
		"Fireshield (Blue)",
		"Flesh to Stone",
		"Friends",
		"Hold Monster",
		"Identify",
		"Improved Haste",
		"Infravision",
		"Knock",
		"Magic Missile",
		"Minor Spell Turning",
		"Mislead",
		"Monster Summoning III",
		"Note",
		"Oracle",
		"Remove Magic",
		"Shadow Door",
		"Sleep",
		"Slow",
		"Spell Sequencer",
		"Spell Thrust",
		"Spell Trigger",
		"Spell Turning",
		"Spellstrike",
		"Stinking Cloud",
		"Stone to Flesh",
		"Stone to Flesh Scroll",
		"Stoneskin",
		"Summon Efreeti",
		"Summon Nishruu",
		"Tizzak's Journal",
		"True Sight",
		"Vampiric Touch",
	],
	"Shield": [
		"Large Shield +2",
		"Medium Shield",
		"Medium Shield +1",
	],
	"Sling": [
		"Sling ",
		"Sling +1",
		"Sling +2",
	],
	"Small sword": [
		"Short Sword",
		"Short Sword +1",
		"Short Sword +2",
		"Short Sword +3",
		"Sword of Arvoreen +2",
		"The Shadow's Blade +3",
		"Wakizashi",
	],
	"Spear": [
		"Backbiter +3",
		"Spear",
		"Spear +2",
		"Spear +3",
	],
	"Unknown": [
		"Iron Rod",
	],
	"Wand": [
		"Rod of Resurrection",
		"Rod of Shadowstep",
		"Wand of Cloudkill",
		"Wand of Cursing",
		"Wand of Fear",
		"Wand of Fire",
		"Wand of Lightning",
		"Wand of Magic Missiles",
		"Wand of Monster Summoning",
		"Wand of Paralyzation",
		"Wand of Spell Striking",
		"Wand of the Heavens",
	],
}
