gamestr = "Baldur's Gate EE 2.6.6.0"
headers = ["Area", "NPC", "XP", "Gold Carried", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"]

areas = [
	"act04 (Spawned)",
	"act05 (Spawned)",
	"act06 (Spawned)",
	"actboun (Spawned)",
	"actnesto (Spawned)",
	"aldcut01 (Spawned)",
	"aldcut02 (Spawned)",
	"ar0004 - Behren's home, ground floor",
	"ar0006 - Rinnie's home, ground floor",
	"ar0010 - Jardak's home, ground floor (Drelik the butler)",
	"ar0011 - Jardak's home, second floor",
	"ar0102 - Silvershield Estate, second floor",
	"ar0103 (Spawned) - Splurging Sturgeon, ground floor (Lusselyn)",
	"ar0105 - Blade and Stars, ground floor (G'axir the Seer, Elkart)",
	"ar0106 (Spawned) - Blade and Stars, second floor (Maple Willow Aspen)",
	"ar0108 (Spawned) - Duchal Palace, ground floor",
	"ar0112 (Spawned) - Undercellars (Slythe, Krystin)",
	"ar0112 - Undercellars (Slythe, Krystin)",
	"ar0114 (Spawned) - Blushing Mermaid, ground floor (Larze)",
	"ar0114 - Blushing Mermaid, ground floor (Larze)",
	"ar0115 (Spawned) - Blushing Mermaid, second floor",
	"ar0116 - Helm & Cloak, ground floor (Gorpel Hind)",
	"ar0119 - Three Old Kegs tavern, ground floor",
	"ar0120 - Three Old Kegs tavern, second floor (Skull of Keraph)",
	"ar0121 - Three Old Kegs tavern, third floor (Areana)",
	"ar0123 - Undercity (Temple of Bhaal, old city ruins)",
	"ar0125 - Temple of Bhaal (game finale)",
	"ar0126 - Ragefast's home",
	"ar0128 (Spawned) - Merchant League, second floor (Aldeth, Brandilar, Zorl)",
	"ar0128 - Merchant League, second floor (Aldeth, Brandilar, Zorl)",
	"ar0130 - Hall of Wonders (Alora)",
	"ar0131 - Temple of Gond (Forthel August)",
	"ar0132 - Lady's House (Agnasia, Chanthalas Ulbright)",
	"ar0134 - Low Lantern, first underwater level (Desreta, Vay-ya)",
	"ar0135 - Low Lantern, second underwater level (Yago)",
	"ar0137 (Spawned) - Ramazith's Tower, ground floor",
	"ar0143 - Oberan's Estate, ground floor",
	"ar0145 - Oberan's Estate, third floor (Helshara, Ithmeera, Delorna)",
	"ar0148 (Spawned) - Thieves Guild, front house (fourth from west)",
	"ar0150 (Spawned) - Thieves Guild, front house (first from west)",
	"ar0151 (Spawned) - Thieves Guild, front house (second from west)",
	"ar0152 (Spawned) - Thieves Guild, front house (third from west)",
	"ar0153 (Spawned) - Thieves Guild, main area (Alatos, Narlen Darkwalk)",
	"ar0153 - Thieves Guild, main area (Alatos, Narlen Darkwalk)",
	"ar0162 - Louise and Laerta's home",
	"ar0167 - Phierkas's home, ground floor",
	"ar0200 - N Baldur's Gate (Ramazith's Tower, Duchal Palace)",
	"ar0224 - BG Sewers, western area (Schlumpsha the Sewer King)",
	"ar0225 - BG Sewers, central area (Ratchild)",
	"ar0226 - BG Sewers, eastern area (ogre mage for Scar)",
	"ar0300 (Spawned) - NE Baldur's Gate (Blushing Mermaid, Splurging Sturgeon, Counting House)",
	"ar0300 - NE Baldur's Gate (Blushing Mermaid, Splurging Sturgeon, Counting House)",
	"ar0307 (Spawned) - Counting House, ground floor (Jacil or Ulf)",
	"ar0307 - Counting House, ground floor (Jacil or Ulf)",
	"ar0308 (Spawned) - Counting House, second floor (Captain Kieres)",
	"ar0500 (Spawned) - Durlag's Tower, exterior",
	"ar0501 - Durlag's Tower, first subterranean level",
	"ar0504 - Durlag's Tower, third floor (Rigglio)",
	"ar0505 - Durlag's Tower, fourth floor (Kirinhale)",
	"ar0514 - Durlag's Tower, fifth subterranean level",
	"ar0516 - Durlag's Tower, demon knight chamber (Dalton)",
	"ar0601 - Seven Suns, ground floor",
	"ar0602 - Seven Suns, second floor",
	"ar0608 (Spawned) - Flaming Fist HQ, second floor (Duke Eltan)",
	"ar0612 (Spawned) - Iron Throne, second floor (Dra'tan)",
	"ar0612 - Iron Throne, second floor (Dra'tan)",
	"ar0613 - Iron Throne, third floor (Nortuary, Emissary Tar)",
	"ar0615 (Spawned) - Iron Throne, fifth (top) floor (chapter five finale)",
	"ar0615 - Iron Throne, fifth (top) floor (chapter five finale)",
	"ar0616 (Spawned) - Iron Throne, ground floor (Triadore)",
	"ar0617 (Spawned) - Tremain Belde'ar's home, ground floor",
	"ar0700 (Spawned) - Central Baldur's Gate (marketplace, Oberan's home)",
	"ar0703 - Sorcerous Sundries, ground floor (Halbazzer Drin)",
	"ar0704 - Sorcerous Sundries, second floor",
	"ar0705 (Spawned) - Elfsong Tavern, ground floor (Brevlik)",
	"ar0705 - Elfsong Tavern, ground floor (Brevlik)",
	"ar0706 - Elfsong Tavern, second floor (Alyth, Cyrdemac)",
	"ar0715 - Nadine's home, ground floor",
	"ar0800 (Spawned) - E Baldur's Gate (Sorcerous Sundries, Elfsong Tavern)",
	"ar0800 - E Baldur's Gate (Sorcerous Sundries, Elfsong Tavern)",
	"ar0805 - Arkion's home, ground floor",
	"ar0809 (Spawned) - Silence's store",
	"ar0813 - Nemphre's home, ground floor",
	"ar0900 (Spawned) - Wyrm's Crossing (bridge to BG, Tenya, Quayle)",
	"ar0900 - Wyrm's Crossing (bridge to BG, Tenya, Quayle)",
	"ar1000 (Spawned) - Ulgoth's Beard (Shandalar, Ike, Mendas)",
	"ar1000 - Ulgoth's Beard (Shandalar, Ike, Mendas)",
	"ar1001 - Ulgoth Beard's Inn (Hurgan Stoneblade)",
	"ar1002 (Spawned) - Aec'Letec cult building, basement (Aec'Letec)",
	"ar1003 (Spawned) - Aec'Letec cult building, ground floor",
	"ar1005 - Therella's home",
	"ar1009 - Ice island, dungeon",
	"ar1010 - Ice island, unused exit area",
	"ar1100 (Spawned) - SW Baldur's Gate (Flaming Fist HQ, Merchant League, Seven Suns)",
	"ar1101 - Generic home, ground floor (thieves Wiven, Dirk, Meakin and Sath)",
	"ar1111 - Sunin's home",
	"ar1200 (Spawned) - S Baldur's Gate (docks, Iron Throne, Low Lantern, Umberlee temple)",
	"ar1200 - S Baldur's Gate (docks, Iron Throne, Low Lantern, Umberlee temple)",
	"ar1201 - Generic home, ground floor (ogre mages)",
	"ar1208 - Warehouse (Noralee)",
	"ar1209 - Generic home, ground floor (Larriaz the Sirine)",
	"ar1213 - Cordyr's home, ground floor",
	"ar1300 (Spawned) - SE Baldur's Gate (Blade and Stars)",
	"ar1303 - Warehouse (Nadarin)",
	"ar1316 - Generic home, ground floor (thieves Taxek and Michael)",
	"ar1400 - Fishing village (Ajantis, farmer Brun, Gerde, lots of ankhegs)",
	"ar1500 (Spawned) - Balduran's Isle, north (AKA Werewolf Isle)",
	"ar1500 - Balduran's Isle, north (AKA Werewolf Isle)",
	"ar1504 - Balduran's ship, fourth floor (Karoug)",
	"ar1600 - Cloakwood, third main area (shadow druids, Eldoth, Faldorn)",
	"ar1603 - Baby wyvern cave (Peter of the North)",
	"ar1800 - Cloakwood mines, exterior",
	"ar1802 - Cloakwood mines, third subterranean level (Natasha, ogre mage)",
	"ar1803 - Cloakwood mines, fourth subterranean level (Davaeorn, Stephan)",
	"ar1900 - Bandit Camp",
	"ar1901 - Bandit Camp, main tent (Raemon, Venkt, Hakt, Britik)",
	"ar1902 - Bandit Camp, tent (Ardenor Crush)",
	"ar1903 - Bandit Camp, cave (Garclax)",
	"ar1904 - Bandit Camp, tent (Tersus)",
	"ar1905 - Bandit Camp, tent (Knott)",
	"ar2000 (Spawned) - Balduran's Isle, south (AKA Werewolf Isle, Delainy/Durlyle)",
	"ar2000 - Balduran's Isle, south (AKA Werewolf Isle, Delainy/Durlyle)",
	"ar2200 - Cloakwood, first main area (Aldeth Sashenstar, Seniyad, Coran)",
	"ar2300 - Friendly Arm Inn, exterior",
	"ar2302 - Friendly Arm Inn, second floor (Unshey)",
	"ar2303 - Friendly Arm Inn, third floor (Landrin, Golden Pantaloons)",
	"ar2304 - Friendly Arm Inn, Temple of Wisdom (Gellana Mirrorshade)",
	"ar2400 (Spawned) - Peldvale (Viconia, Raiken)",
	"ar2400 - Peldvale (Viconia, Raiken)",
	"ar2600 - Candlekeep (prologue), exterior",
	"ar2602 - Candlekeep (prologue), Priest's Quarters (Shank)",
	"ar2605 - Candlekeep (prologue), infirmary",
	"ar2607 - Candlekeep (prologue), bunkhouse (Carbos)",
	"ar2609 - Candlekeep Citadel, second floor (Koveras)",
	"ar2610 - Candlekeep Citadel, third floor (Rieltar, Brunos Costak, Tuth and Kestor)",
	"ar2614 - Candlekeep Citadel, sixth floor (Ulraunt, Tethtoril)",
	"ar2615 - Candlekeep Catacombs, first level",
	"ar2618 - Candlekeep (prologue), barracks",
	"ar2619 - Candlekeep Catacombs, second level",
	"ar2626 - Candlekeep (chapter 6), exterior",
	"ar2631 - Candlekeep (chapter 6), barracks",
	"ar2639 - Unused",
	"ar2800 (Spawned) - Coast Way (S of Friendly Arm Inn, destroyed caravan)",
	"ar2800 - Coast Way (S of Friendly Arm Inn, destroyed caravan)",
	"ar2900 (Spawned) - Larswood (Teven, Osmadi, Corsone)",
	"ar3000 - Spider Wood (E of Larswood, Thayvian Red Wizards)",
	"ar3100 - Shipwreck's Coast (S of Candlekeep, Shoal, Droth, Mad Arcand, Surgeon)",
	"ar3200 - High Hedge, exterior (Kivan)",
	"ar3202 - High Hedge, interior (Thalantyr)",
	"ar3300 (Spawned) - Beregost (Garrick, Jovial Juggler, Feldepost's Inn, Burning Wizard, Red Sheaf))",
	"ar3300 - Beregost (Garrick, Jovial Juggler, Feldepost's Inn, Burning Wizard, Red Sheaf))",
	"ar3304 - Jovial Juggler, ground floor (Bjornin, Gurke)",
	"ar3313 - Mirianne's home, ground floor",
	"ar3320 - Travenhurst Manor, ground floor",
	"ar3327 - Generic home, ground floor",
	"ar3333 - Firebeard Elvenhair's home, ground floor",
	"ar3351 - Feldepost's Inn, ground floor (Marl)",
	"ar3352 (Spawned) - Feldepost's Inn, second floor (Algernon)",
	"ar3352 - Feldepost's Inn, second floor (Algernon)",
	"ar3357 - Red Sheaf, ground floor (Perdue)",
	"ar3400 - Beregost Temple, exterior (Cattack)",
	"ar3402 - Beregost Temple, interior (AKA Song of the Morning, Keldath Ormlyr)",
	"ar3500 - Mutamin's Garden (Shar-Teel, Mutamin, Korax, basilisks, Tamah)",
	"ar3600 - Lighthouse (Safana, Ardrouine, Sil)",
	"ar3700 - Red Canyons (Bassilus, Melicamp)",
	"ar3800 - South Beregost Road",
	"ar3900 - Ulcaster School, exterior (Ulcaster, Icharyd)",
	"ar4000 - Gullykin, exterior",
	"ar4003 - Temple of Yondalla, ground floor",
	"ar4007 - Generic home, ground floor",
	"ar4011 - Generic home, ground floor",
	"ar4100 - Archaeological Site, exterior (Brage, Charleston Nib, Doomsayer)",
	"ar4200 - Fisherman's Lake (Drizzt. Bjornin's half-ogres)",
	"ar4400 - Lonely Peaks (Hulrik and Arabelle, Sarhedra, Arghain)",
	"ar4500 - Firewine Bridge (Kahrk, Carsa, Poe, Bentan, Melium)",
	"ar4600 - Bear River (N of Gnoll Stronghold, Larel, Nevill, Jared)",
	"ar4700 - Xvart Village (Nexlit, Ursa, Borda)",
	"ar4800 (Spawned) - Nashkel (Minsc, Edwin, Berrun Ghastkill, Belching Dragon, Temple of Helm)",
	"ar4800 - Nashkel (Minsc, Edwin, Berrun Ghastkill, Belching Dragon, Temple of Helm)",
	"ar4801 - Nashkel Inn",
	"ar4809 - Belching Dragon Tavern (Volo)",
	"ar4810 - Nashkel barracks",
	"ar4900 - Nashkel Carnival (Branwen, Great Gazib)",
	"ar4903 - Large carnival tent (Vitiare)",
	"ar4905 - Small carnival tent (rare potions merchant)",
	"ar4906 - Small carnival tent (Zordral and Bentha)",
	"ar5000 - Valley of the Tombs (Nashkel mines exit, Narcillicus, Hentold)",
	"ar5100 - Gnoll Stronghold (Dynaheir)",
	"ar5200 - Dryad Falls (Cloudpeak Dryad, Drienne, Ingot, Krumm, Caldo)",
	"ar5201 - Firewine Ruins (Lendarn, ogre mage, undead knights)",
	"ar5300 - Fire Leaf Forest (S of Nashkel, Albert, Rufie, Vax, Sendai)",
	"ar5400 - Nashkel Mines, exterior (Prism)",
	"ar5401 - Nashkel Mines, first subterranean level (Dink)",
	"ar5402 - Nashkel Mines, second subterranean level (Kylee, Beldin)",
	"ar5405 - Nashkel Mines, Mulahey's lair (Xan, Mulahey)",
	"ar5500 (Spawned) - Gibberling Mountains (Samuel, Hafiz)",
	"ar5500 - Gibberling Mountains (Samuel, Hafiz)",
	"ar5506 - Candlekeep Caves (Diarmid, Prat, Sakul, Tam, Bor)",
	"ar5600 (Spawned) - Random encounter area",
	"ar5601 (Spawned) - Random encounter area",
	"ar5700 (Spawned) - Random encounter area",
	"ar5701 (Spawned) - Random encounter area",
	"ar5710 - Unused",
	"ar5800 (Spawned) - Random encounter area",
	"ar5801 (Spawned) - Random encounter area",
	"ar5900 (Spawned) - Random encounter area",
	"ar5901 (Spawned) - Random encounter area",
	"ar6000 (Spawned) - Random encounter area",
	"ar6001 (Spawned) - Random encounter area",
	"ar6100 (Spawned) - Random encounter area",
	"bancut01 (Spawned)",
	"bancut02 (Spawned)",
	"bd0010 (Spawned) - Ducal Palace City Exterior",
	"bd0010 - Ducal Palace City Exterior",
	"bd0020 (Spawned) - Sorcerous/Elf Song City Exterior",
	"bd0020 - Sorcerous/Elf Song City Exterior",
	"bd0021",
	"bd0030 - Flaming Fist City Exterior",
	"bd0035",
	"bd0040 (Spawned) - Three Kegs City Exterior",
	"bd0040 - Three Kegs City Exterior",
	"bd0050 (Spawned) - Iron Throne City Exterior",
	"bd0050 - Iron Throne City Exterior",
	"bd0064 - Random Area - Forest Paths",
	"bd0100 (Spawned) - Ducal Palace, Second Floor",
	"bd0100 - Ducal Palace, Second Floor",
	"bd0101 (Spawned) - Ducal Palace, Leaving BG",
	"bd0101 - Ducal Palace, Leaving BG",
	"bd0102 (Spawned) - Ducal Palace, First Floor",
	"bd0102 - Ducal Palace, First Floor",
	"bd0103 (Spawned) - Ducal Palace, Third Floor",
	"bd0103 - Ducal Palace, Third Floor",
	"bd0104 (Spawned) - Flaming Fist HQ",
	"bd0104 - Flaming Fist HQ",
	"bd0106 - Three Old Kegs, First Floor",
	"bd0107 - Three Old Kegs, Second Floor",
	"bd0108 (Spawned) - Three Old Kegs, Third Floor",
	"bd0108 - Three Old Kegs, Third Floor",
	"bd0109 - Elfsong Tavern, First Floor",
	"bd0110 (Spawned) - Elfsong Tavern, Second Floor",
	"bd0110 - Elfsong Tavern, Second Floor",
	"bd0111 (Spawned) - Iron Throne Floor, First Floor",
	"bd0111 - Iron Throne Floor, First Floor",
	"bd0112 - Baldur's Gate East",
	"bd0116 (Spawned) - Ducal Palace, Basement",
	"bd0120 (Spawned) - Tomb Safehouse, First Floor",
	"bd0120 - Tomb Safehouse, First Floor",
	"bd0122 (Spawned) - Sorcerous Sundries, Second Floor",
	"bd0130 - Tomb Safehouse, Second Floor",
	"bd1000 (Spawned) - Coast Way Crossing",
	"bd1000 - Coast Way Crossing",
	"bd1100 - The Dig",
	"bd1200 - Lich Outpost",
	"bd2000 (Spawned) - Boareskyr Bridge & Bridgefort",
	"bd2000 - Boareskyr Bridge & Bridgefort",
	"bd2100 (Spawned) - Bridgefort Interior",
	"bd2100 - Bridgefort Interior",
	"bd3000 (Spawned) - Allied Siege Camp",
	"bd3000 - Allied Siege Camp",
	"bd4000 (Spawned) - Dragonspear Castle, Exterior",
	"bd4000 - Dragonspear Castle, Exterior",
	"bd4100 (Spawned) - Dragonspear Castle Keep, First Floor",
	"bd4100 - Dragonspear Castle Keep, First Floor",
	"bd4300 (Spawned) - Dragonspear Castle Basement",
	"bd4300 - Dragonspear Castle Basement",
	"bd4400 - Avernus",
	"bd4700 - Avernus Roof",
	"bd5000 (Spawned) - Underground River Entrance",
	"bd5000 - Underground River Entrance",
	"bd5100 (Spawned) - Underground River",
	"bd5100 - Underground River",
	"bd5200 - The Warrens",
	"bd5300 - Kanaglym",
	"bd6000 (Spawned) - Abandoned Sewers & Caverns",
	"bd6100 (Spawned) - The Ambush",
	"bd6200 (Spawned) - Sewers Exit",
	"bd7000 (Spawned) - Coast Way Forest",
	"bd7000 - Coast Way Forest",
	"bd7100 (Spawned) - Troll Forest",
	"bd7100 - Troll Forest",
	"bd7200 - Forest of Wyrms",
	"bd7220 (Spawned) - Bugbear Stronghold",
	"bd7230 - Temple of Cyric",
	"bd7300 - Dead Man's Pass",
	"bd7400 - Bloodbark Grove",
	"bdboarb2 (Spawned)",
	"bdbranch (Spawned)",
	"bdbteam1 (Spawned)",
	"bdbteam2 (Spawned)",
	"bdbteam3 (Spawned)",
	"bdbteam4 (Spawned)",
	"bdbteam5 (Spawned)",
	"bdbteam6 (Spawned)",
	"bdc123a (Spawned)",
	"bdc205aa (Spawned)",
	"bdc205ab (Spawned)",
	"bdc205ac (Spawned)",
	"bdc205ba (Spawned)",
	"bdc205bb (Spawned)",
	"bdc205bc (Spawned)",
	"bdc205ca (Spawned)",
	"bdc205cb (Spawned)",
	"bdc205da (Spawned)",
	"bdc205db (Spawned)",
	"bdc205r (Spawned)",
	"bdcut09 (Spawned)",
	"bdcut09a (Spawned)",
	"bdcut09b (Spawned)",
	"bdcut11 (Spawned)",
	"bdcut11a (Spawned)",
	"bdcut15 (Spawned)",
	"bdcut16 (Spawned)",
	"bdcut20a (Spawned)",
	"bdcut21 (Spawned)",
	"bdcut26 (Spawned)",
	"bdcut27 (Spawned)",
	"bdcut28 (Spawned)",
	"bdcut30a (Spawned)",
	"bdcut322 (Spawned)",
	"bdcut36 (Spawned)",
	"bdcut40a (Spawned)",
	"bdcut40b (Spawned)",
	"bdcut40c (Spawned)",
	"bdcut40d (Spawned)",
	"bdcut41 (Spawned)",
	"bdcut42 (Spawned)",
	"bdcut43 (Spawned)",
	"bdcut45 (Spawned)",
	"bdcut45a (Spawned)",
	"bdcut58 (Spawned)",
	"bdcut59b (Spawned)",
	"bdcut60a (Spawned)",
	"bdcut60b (Spawned)",
	"bdcut60x (Spawned)",
	"bdcut61t (Spawned)",
	"bdcut62 (Spawned)",
	"bdcut64 (Spawned)",
	"bdddd2a (Spawned)",
	"bdddd2b (Spawned)",
	"bdddd3a (Spawned)",
	"bddebug (Spawned)",
	"bddmspwn (Spawned)",
	"bddoor30 (Spawned)",
	"bddsgat1 (Spawned)",
	"bdexduel (Spawned)",
	"bdintro (Spawned)",
	"bdnorest (Spawned)",
	"bdscry01 (Spawned)",
	"bdscry03 (Spawned)",
	"bdscry05 (Spawned)",
	"bdsdd251 (Spawned)",
	"bdsddski (Spawned)",
	"bdshcut0 (Spawned)",
	"bdwaterf (Spawned)",
	"bphub (Spawned)",
	"ch1cut01 (Spawned)",
	"cutba01 (Spawned)",
	"cutmove1 (Spawned)",
	"cutne0a (Spawned)",
	"cutskip (Spawned)",
	"cutskip1 (Spawned)",
	"digcut01 (Spawned)",
	"explore (Spawned)",
	"merch2 (Spawned)",
	"merch4 (Spawned)",
	"merch5 (Spawned)",
	"merch6 (Spawned)",
	"mercha (Spawned)",
	"mysmer (Spawned)",
	"narcut (Spawned)",
	"oh1000 (Spawned) - Dorn - Random Encounter Area",
	"oh2000 - Neera - Adoy's Enclave, exterior",
	"oh2010 (Spawned) - Neera - Adoy's Enclave, interior",
	"oh2010 - Neera - Adoy's Enclave, interior",
	"oh3000 - Rasaad - Dark Moon temple, exterior",
	"oh3010 - Rasaad - Dark Moon temple, interior",
	"oh3100 - Rasaad - Dark Moon temple, interior",
	"oh9310 (Spawned) - The Black Pits: Arena 1",
	"rasaad (Spawned)",
	"scarcut (Spawned)",
	"shopkn (Spawned)",
	"tbullrsh (Spawned)",
	"titach (Spawned)",
	"tmeiala (Spawned)",
	"unknown",
]

types = {
	"Amulet": [
		"Amulet of Spell Warding",
		"Arkion's Bloodstone Amulet",
		"Bloodstone Amulet",
		"Gold Necklace",
		"Greenstone Amulet",
		"Laeral's Tear Necklace",
		"Pearl Necklace",
		"Rainbow Obsidian Necklace",
		"Shield Amulet",
		"Silver Necklace",
		"The Amplifier",
		"The One Gift Lost",
		"The Protector +1",
		"bdamul09.itm",
		"bdamul11.itm",
		"bdamul24.itm",
	],
	"Armor": [
		"Chain Mail",
		"Leather Armor +1",
		"Robe of the Evil Archmagi",
	],
	"Arrows": [
		"Acid Arrow +1",
		"Arrow",
		"Arrow +1",
		"Arrow +2",
		"Arrow of Biting",
		"Arrow of Detonation",
		"Arrow of Dispelling",
		"Arrow of Fire +2",
		"Arrow of Ice",
		"Arrow of Piercing +1",
		"bdarow03.itm",
	],
	"Axe": [
		"Battle Axe",
		"Battle Axe +1",
		"Throwing Axe",
		"ax1h11.itm",
	],
	"Belt & Girdle": [
		"Adoy's Belt",
		"Belt of Antipode",
		"Destroyer of the Hills",
		"Golden Girdle of Urnst",
		"bdbelt03.itm",
		"bdbelt12.itm",
		"bdbelt13.itm",
		"bdbelt14.itm",
	],
	"Bolts": [
		"Bolt",
		"Bolt +1",
		"Bolt +2",
		"Bolt of Biting",
		"Bolt of Lightning",
		"Case of Plenty +1",
	],
	"Books & misc": [
		"Ancient Armor",
		"Bassilus's Holy Symbol",
		"Bowl of Water Elemental Control",
		"Dradeel's Spellbook",
		"Farthing's Dolly",
		"Golden Pantaloons",
		"History of Tethyr",
		"History of the Dead Three",
		"History of the Last March of the Giants",
		"History of the Nether Scrolls",
		"Key to River Plug",
		"Mulahey's Holy Symbol",
		"Peladan",
		"Sea Charts",
		"Tome of Understanding",
		"Yago's Book of Curses",
		"bdbwoosh.itm",
		"bdjar.itm",
		"bdmisc04.itm",
		"bdmisc08.itm",
		"bdmisc19.itm",
		"bdmisc25.itm",
		"bdmisc51.itm",
		"bdmisc52.itm",
		"bdmisc58.itm",
		"bdpetsg.itm",
		"rndaro01.itm",
		"rndgem01.itm",
		"rndgem02.itm",
		"rndgem03.itm",
		"rndptn01.itm",
		"rndtre01.itm",
		"rndtre02.itm",
		"rndtre03.itm",
		"rndtre04.itm",
		"rndtre05.itm",
		"rndtre09.itm",
		"rndtri02.itm",
		"rndwand.itm",
	],
	"Books/Broken shields/bracelets": [
		"The Diary of Sarevok",
	],
	"Boots": [
		"The Frost's Embrace",
		"The Paws of the Cheetah",
		"Worn Whispers",
	],
	"Bow": [
		"Composite Longbow",
		"Composite Longbow +1",
		"Longbow",
		"Longbow +1",
		"Shortbow",
		"Shortbow +1",
	],
	"Bracers & gauntlets": [
		"Bracers",
		"Bracers of Defense AC 7",
		"Bracers of Defense AC 8",
		"Bracers to the Death",
		"Elander's Gloves of Misplacement",
		"Glimmering Bands",
		"Hands of Takkok",
		"Legacy of the Masters",
		"The Brawling Hands",
		"The Dale's Protector",
		"Xarrnous's Second Sword Arm",
		"bdbrac03.itm",
		"bdbrac09.itm",
		"bdbrac13.itm",
		"bdbrac14.itm",
	],
	"Bullets": [
		"Bullet",
		"Bullet +1",
		"Bullet +2",
		"Bullet of Electricity +1",
		"Bullet of Fire +1",
		"Bullet of Ice +1",
		"Sunstone Bullet +1",
	],
	"Cloaks & Robes": [
		"Algernon's Cloak",
		"Cloak of Balduran",
		"Cloak of Displacement",
		"Cloak of Protection +1",
		"Nymph Cloak",
		"Relair's Mistake",
		"Shandalar's Cloak",
		"The Spirit's Shield +2",
		"Whispers of Silence",
		"bdclck06.itm",
	],
	"Containers/eye/broken armor": [
		"Gem Bag",
		"Scroll Case",
	],
	"Crossbow": [
		"Heavy Crossbow",
		"Heavy Crossbow +1",
		"Light Crossbow",
	],
	"Dagger": [
		"Dagger",
		"Dagger +1",
		"Heart of the Golem +2",
		"Kylee's Dagger",
		"Throwing Dagger",
		"bddagg04.itm",
	],
	"Darts": [
		"Asp's Nest +1",
		"Dart",
		"Dart +1",
		"Dart of Acid +1",
		"Dart of Fire +1",
		"Dart of Stunning",
		"Dart of Wounding",
	],
	"Drinks (IWD)": [
		"De'Tranion's Baalor Ale",
		"bdjuice.itm",
		"bdmisc29.itm",
	],
	"Flail": [
		"Flail",
		"Flail +1",
		"dwblun01.itm",
	],
	"Gem": [
		"Andar Gem",
		"Aquamarine Gem",
		"Black Opal",
		"Bloodstone Gem",
		"Chrysoberyl Gem",
		"Diamond",
		"Dwarven Rune Wardstone",
		"Emerald",
		"Fire Agate Gem",
		"Garnet Gem",
		"Horn Coral Gem",
		"Iol Gem",
		"Jasper Gem",
		"Lynx Eye Gem",
		"Moonstone Gem",
		"Pearl",
		"Skydrop Gem",
		"Sphene Gem",
		"Star Diopside Gem",
		"Sunstone Gem",
		"Tchazar Gem",
		"Turquoise Gem",
		"Wardstone Forgery",
		"Water Opal",
		"Waterstar Gem",
		"Ziose Gem",
	],
	"Halberd": [
		"Halberd",
		"Halberd +1",
		"Suryris's Blade +2",
	],
	"Hammer": [
		"The Kneecapper +1",
		"War Hammer",
		"War Hammer +1",
	],
	"Headgear": [
		"bdhelm05.itm",
		"bdmisc05.itm",
	],
	"Key": [
		"bdkey05.itm",
		"bdkey07.itm",
		"bdkey11.itm",
		"bdkey12.itm",
		"bdshkey.itm",
	],
	"Large sword": [
		"Bastard Sword",
		"Harrower +1",
		"Long Sword",
		"Long Sword +1",
		"Scimitar",
		"Scimitar +1",
		"Two-handed Sword",
		"Two-handed Sword +1",
		"Two-handed Sword +2",
		"Varscona +2",
		"bdsw1h03.itm",
	],
	"Mace & Club": [
		"Club",
		"Club +1",
		"Mace",
		"Mace +1",
		"Mace +2",
		"bdblun02.itm",
	],
	"Morning star": [
		"Morning Star",
		"Morning Star +1",
	],
	"Potion": [
		"Antidote",
		"Elixir of Health",
		"Marek's Potion of Antidote",
		"Oil of Fiery Burning",
		"Oil of Speed",
		"Potion of Absorption",
		"Potion of Agility",
		"Potion of Clarity",
		"Potion of Cloud Giant Strength",
		"Potion of Cold Resistance",
		"Potion of Defense",
		"Potion of Explosions",
		"Potion of Extra Healing",
		"Potion of Fire Breath",
		"Potion of Fire Giant Strength",
		"Potion of Fire Resistance",
		"Potion of Fortitude",
		"Potion of Freedom",
		"Potion of Frost Giant Strength",
		"Potion of Genius",
		"Potion of Healing",
		"Potion of Heroism",
		"Potion of Hill Giant Strength",
		"Potion of Infravision",
		"Potion of Invisibility",
		"Potion of Invulnerability",
		"Potion of Magic Blocking",
		"Potion of Magic Protection",
		"Potion of Magic Shielding",
		"Potion of Master Thievery",
		"Potion of Mind Focusing",
		"Potion of Mirrored Eyes",
		"Potion of Perception",
		"Potion of Power",
		"Potion of Regeneration",
		"Potion of Stone Form",
		"Potion of Stone Giant Strength",
		"Potion of Storm Giant Strength",
		"Potion of Strength",
		"Red Potion",
		"Speedily Stolen Slaves' Salve",
		"Violet Potion",
		"bdmisc02.itm",
		"bdpotn06.itm",
	],
	"Quarterstaff": [
		"Neera's Staff +1",
		"Quarterstaff",
		"Quarterstaff +1",
		"Staff Spear +2",
	],
	"Ring": [
		"Angel Skin Ring",
		"Bloodstone Ring",
		"Discipliner",
		"Druid's Ring",
		"Edventar's Gift",
		"Evermemory",
		"Fire Opal Ring",
		"Flamedance Ring",
		"Gold Ring",
		"Honorary Ring of Sune",
		"Jade Ring",
		"Koveras's Ring of Protection +1",
		"Nemphre's Onyx Ring",
		"Onyx Ring",
		"Ring of the Princes +1",
		"Ruby Ring",
		"Sashenstar's Ruby Ring",
		"Silver Ring",
		"The Guard's Ring +2",
		"The Jester's Folly",
		"The Victor",
		"Topsider's Crutch",
		"bdring04.itm",
		"bdring06.itm",
		"bdring08.itm",
		"bdring09.itm",
		"bdring12.itm",
		"swordi.itm",
	],
	"Scroll": [
		"Agannazar's Scorcher",
		"Andris's Journal",
		"Animate Dead",
		"Armor",
		"Blindness",
		"Burning Hands",
		"Chaos",
		"Charm Person",
		"Chill Touch",
		"Chromatic Orb",
		"Clairvoyance",
		"Color Spray",
		"Confusion",
		"Cursed Scroll of Petrification",
		"Cursed Scroll of Weakness",
		"Dark Moon Note",
		"Detect Evil",
		"Detect Illusion",
		"Dezkiel's Scroll",
		"Dire Charm",
		"Dispel Magic",
		"Domination",
		"Emotion, Hopelessness",
		"Feeblemind",
		"Find Familiar",
		"Fireball",
		"Fireshield (Blue)",
		"Fireshield (Red)",
		"Flame Arrow",
		"Friends",
		"Geas Removal Scroll",
		"Ghost Armor",
		"Ghoul Touch",
		"Glitterdust",
		"Grease",
		"Greater Malison",
		"Haste",
		"Hold Person",
		"Horror",
		"Identify",
		"Infravision",
		"Invitation",
		"Know Alignment",
		"Larloch's Minor Drain",
		"Letter",
		"Letter to Kryll",
		"Lightning Bolt",
		"Luck",
		"Magic Missile",
		"Melf's Acid Arrow",
		"Minor Globe of Invulnerability",
		"Minor Sequencer",
		"Mirror Image",
		"Monster Summoning I",
		"Non-Detection",
		"Otiluke's Resilient Sphere",
		"Protection From Evil",
		"Protection From Fire",
		"Protection From Magic",
		"Protection From Normal Missiles",
		"Protection From Petrification",
		"Protection From Poison",
		"Protection From Undead",
		"Remove Curse",
		"Remove Magic",
		"Resist Fear",
		"Scroll",
		"Shield",
		"Shocking Grasp",
		"Skull Trap",
		"Sleep",
		"Slow",
		"Sorrem's Note",
		"Spell Thrust",
		"Spider Spawn",
		"Spirit Armor",
		"Stinking Cloud",
		"Stone to Flesh Scroll",
		"Stoneskin",
		"Strength",
		"Vampiric Touch",
		"Vocalize",
		"Web",
		"Wraithform",
		"bdbflye2.itm",
		"bdbflyer.itm",
		"bdscrl01.itm",
		"bdscrl1.itm",
	],
	"Shield": [
		"Buckler +1",
		"Large Shield",
		"Medium Shield +1",
		"bdmisc10.itm",
		"bdshld02.itm",
	],
	"Sling": [
		"Sling",
		"Sling +1",
		"slng04.itm",
	],
	"Small sword": [
		"Short Sword",
		"Short Sword +1",
		"The Shadow's Blade +3",
		"The Whistling Sword +2",
	],
	"Spear": [
		"Spear",
		"Spear +2",
	],
	"Unknown": [
		"bdbody01.itm",
		"bdbody02.itm",
		"bdbody03.itm",
	],
	"Wand": [
		"Wand of Fear",
		"Wand of Fire",
		"Wand of Frost",
		"Wand of Lightning",
		"Wand of Magic Missiles",
		"Wand of Monster Summoning",
		"Wand of Paralyzation",
		"Wand of Polymorphing",
		"Wand of Sleep",
		"Wand of the Heavens",
	],
}
