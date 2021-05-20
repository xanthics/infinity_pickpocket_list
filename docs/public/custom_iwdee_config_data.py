gamestr = "Icewind Dale EE 2.6.6.0 + BetterHOF + CDTWEAKS"
headers = ["Area", "NPC", "XP", "Gold Carried", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"]

areas = [
	"animtest (Spawned)",
	"ar1001 - Easthaven (prologue) - Temple of Tempus",
	"ar1006 - Easthaven (prologue) - Grisella's Winter's Cradle Tavern - main floor",
	"ar1008 - Easthaven (prologue) - Snowdrift Inn",
	"ar1100 - Easthaven (finale)",
	"ar1101 - Easthaven (finale) - Temple of Tempus/ice tower first floor",
	"ar2003 - Kuldahar Pass - Gherg's tower",
	"ar2004 - Kuldahar Pass - Mill - entrance",
	"ar2100 (Spawned) - Kuldahar",
	"ar2101 - Kuldahar - Orrick the Grey's tower - entrance area",
	"ar2102 - Kuldahar - Orrick the Grey's tower - study",
	"ar2103 (Spawned) - Kuldahar - Conlan's Smithy",
	"ar2108 - Kuldahar - Airship of Oswald Fiddlebender",
	"ar2111 - Kuldahar - Root Cellar Tavern",
	"ar2112 - Kuldahar - Home of Arundel - first floor",
	"ar2116 (Spawned) - Kuldahar - Home of Arundel - second floor",
	"ar3001 (Spawned) - Vale of Shadows - yeti cave",
	"ar3301 - Vale of Shadows - Temple of Myrkul",
	"ar3501 - Vale of Shadows - Tomb of Kresselack - first level",
	"ar3601 - Temple of the Forgotten God - first level",
	"ar4003 - Dragon's Eye - third dungeon level (Presio)",
	"ar4004 - Dragon's Eye - fourth dungeon level (Eldathyn)",
	"ar4005 - Dragon's Eye - fifth dungeon level (Yxunomei)",
	"ar5401 - Severed Hand - Tower of Sheverash - first floor, Kaylessa",
	"ar5404 - Severed Hand - Tower of Sheverash - fourth floor",
	"ar6003 - Dorn's Deep - orog cave, Saablic, Krilag",
	"ar6011 - Dorn's Deep - machinery room",
	"ar6014 - Dorn's Deep - Bandoth's cave",
	"ar7001 - Wyrm's Tooth Glacier - aquarium interior, ice salamander lair",
	"ar7003 - Wyrm's Tooth Glacier - Gareth, slaves",
	"ar7004 - Wyrm's Tooth Glacier - frost giant cave",
	"ar7005 - Wyrm's Tooth Glacier - aquarium exterior",
	"ar8001 - Lower Dorn's Deep - main cavern",
	"ar8005 - Lower Dorn's Deep - Order of the Kraken garde",
	"ar8006 - Lower Dorn's Deep - Order of the Kraken manor - first floor, Ginafae",
	"ar8007 (Spawned) - Lower Dorn's Deep - Order of the Kraken manor - second floor, Mekrath",
	"ar8007 - Lower Dorn's Deep - Order of the Kraken manor - second floor, Mekrath",
	"ar8010 (Spawned) - Lower Dorn's Deep - Malavon's lair",
	"ar8010 - Lower Dorn's Deep - Malavon's lair",
	"ar8011 - Lower Dorn's Deep - forge, Ilmadia",
	"ar8012 - Lower Dorn's Deep - Brother Perdiem",
	"ar9100 (Spawned) - Lonelywood",
	"ar9100 - Lonelywood",
	"ar9101 - Lonelywood - Whistling Gallows - first floor",
	"ar9103 - Lonelywood - Temple of Waukeen",
	"ar9104 - Lonelywood - Home of Emmerich",
	"ar9106 (Spawned) - Lonelywood - Thurlow home - first floor",
	"ar9107 (Spawned) - Lonelywood - Thurlow home - second floor",
	"ar9110 - Lonelywood - Home of Purvis",
	"ar9200 - Barbarian camp",
	"ar9201 (Spawned) - Barbarian camp - Mead Hall",
	"ar9201 - Barbarian camp - Mead Hall",
	"ar9400 (Spawned) - Burial Isle - Wylfdene's barrow",
	"ar9501 - Gloomfrost interior - first level, Tiernon",
	"ar9502 - Gloomfrost interior - second level, Seer",
	"ar9600 - Sea of Moving Ice",
	"ar9602 - Sea of Moving Ice - Field of Bones",
	"ar9603 - Sea of Moving Ice - Icasaracht lair exterior",
	"ar9700 - Anauroch Castle - outer courtyard (TotL start area)",
	"ar9704 - Anauroch Castle - west Tower upstairs - Harald",
	"ar9706 - Anauroch Castle - north Tower upstairs - harpy queen",
	"ar9708 - Anauroch Castle - east Tower upstairs - Banites",
	"ar9715 - Anauroch Castle - hideout of Hobart",
	"ildrgdie (Spawned)",
	"unknown",
]

types = {
	"Amulet": [
		"Amulet of Metaspell Influence",
		"Amulet of Protection",
		"Great Black Wolf Talisman",
		"Kossuth's Blood",
		"Necklace of Missiles",
		"Symbol of Corellon Larethian",
		"Symbol of Solonor Thelandira",
		"Tiernon's Hearthstone",
	],
	"Armor": [
		"Chain Mail",
	],
	"Arrows": [
		"Acid Arrow +1",
		"Arrow",
		"Arrow of Fire +1",
		"Arrow of Piercing +3",
		"Arrow of the Hand +8",
		"Inferno Arrow +5",
		"Precision Arrow +2",
	],
	"Axe": [
		"Battle Axe",
		"Two-Handed Axe",
	],
	"Belt & Girdle": [
		"Girdle of Bluntness",
		"Girdle of Stromnos",
		"Golden Girdle",
	],
	"Bolts": [
		"Bolt",
		"Bolt +1",
		"Bolt of Biting +1",
		"Bolt of Lightning +1",
	],
	"Books & misc": [
		"Bardic Horn of Valhalla",
		"Brother Perdiem's Badge",
		"Joril's Badge",
		"Krilag's Badge",
		"Maiden Ilmadia's Badge",
		"Malavon's Badge",
		"Manual of Gainful Exercise",
		"Marketh's Badge",
		"Mirror of Black Ice",
		"Piece of broken machinery",
		"Tome of Clear Thought",
		"Tome of Leadership and Influence",
		"Tome of Understanding",
		"Umber Hulk Hide",
		"mernbook.itm",
		"mernmanu.itm",
		"merntome.itm",
		"rndtre50.itm",
		"rndtre53.itm",
		"rndtre61.itm",
		"rndtre66.itm",
		"rndtre81.itm",
		"rndtre85.itm",
	],
	"Books/Broken shields/bracelets": [
		"Engineering Manual",
		"Kalabac's Journal",
	],
	"Bow": [
		"Longbow",
	],
	"Bracers & gauntlets": [
		"Bracers of Archery",
		"Bracers of Defense A.C. 1",
		"Gauntlets of Elven Might",
		"Gauntlets of Weapon Expertise",
		"Gauntlets of Weapon Skill",
		"Kaylessa's Gloves",
		"The Flaming Fists of Lin Mei",
	],
	"Bullets": [
		"Bullet +1",
		"Force Bullet +4",
	],
	"Cloaks & Robes": [
		"Cloak of Non-Detection",
		"Cloak of Protection +2",
		"Cloak of Scintillating Colors",
		"Glimglam's Cloak +1",
		"Shadowed Cloak",
		"Wailing of Virgins",
	],
	"Crossbow": [
		"Light Crossbow of Speed +2",
	],
	"Darts": [
		"Asp's Nest +1",
	],
	"Drinks (IWD)": [
		"The Genie's Flask",
	],
	"Flail": [
		"Fast Flail +2",
	],
	"Fur/pelt": [
		"Winter Wolf Pelt",
	],
	"Gem": [
		"Emerald",
		"King's Tears",
		"Moonbar Gem",
		"Moonstone Gem",
		"Rogue Stone",
	],
	"Gold pieces": [
		"Gold Piece",
	],
	"Key": [
		"Albion's Key",
		"Conlan's Key",
		"Dugmaren's Key",
		"Watchtower Key",
	],
	"Large sword": [
		"Bastard Sword ",
		"Finest Long Sword",
		"Long Sword +1",
		"Long Sword of the Hand +6",
	],
	"Mace & Club": [
		"Mace +1",
	],
	"Morning star": [
		"Morning Star +5: Defender",
	],
	"Potion": [
		"Antidote",
		"Elixir of Health",
		"Flaming Oil",
		"Haste Potion",
		"Oil of Fiery Burning",
		"Oil of Speed",
		"Potion of Absorption ",
		"Potion of Explosions",
		"Potion of Extra Healing",
		"Potion of Fast Casting",
		"Potion of Fire Giant Strength",
		"Potion of Fire Resistance",
		"Potion of Firebreath",
		"Potion of Frost Giant Strength",
		"Potion of Healing",
		"Potion of Holy Transference",
		"Potion of Invisibility",
		"Potion of Life Transference",
		"Potion of Magic Shielding",
		"Potion of Master Thievery",
		"Potion of Storm Giant Strength",
		"Potion of Vitality",
	],
	"Quarterstaff": [
		"Staff of Nature's Wrath +3",
		"The Summoner's Staff +3",
	],
	"Ring": [
		"Greater Ring of the Warrior",
		"Kaylessa's Ring",
		"Kontik's Ring of Wizardry",
		"Onyx Ring",
		"Ring of Aura Transfusion",
		"Ring of Fire Resistance",
		"Ring of Free Action",
		"Ring of Pain Amplification",
		"Ring of Protection +2",
		"Ring of Protection +3",
		"Ring of Protection +4",
		"Ring of Reckless Action",
		"Ring of Shadows",
		"Ring of the Gorgon",
		"Ring of the Warrior",
	],
	"Scroll": [
		"Blur",
		"Comet",
		"Dragon's Breath",
		"Dver's Note",
		"Emotion, Hope",
		"Magic Missile",
		"Malavon's Rage",
		"Note to Krilag",
		"Portrait of Marketh",
		"Wail of the Banshee",
	],
	"Sling": [
		"Sling ",
	],
	"Small sword": [
		"Short Sword ",
	],
	"Wand": [
		"Wand of Fire",
		"Wand of Paralyzation ",
	],
}
