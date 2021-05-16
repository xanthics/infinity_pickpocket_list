from browser import document as doc
from browser import bind, window
from browser.html import TABLE, TR, TH, TD, INPUT, DIV, BUTTON, SPAN, UL, LI, SECTION, P, LABEL, H1, H2
from browser.local_storage import storage
from browser.template import Template

from table_data import data
from config_data import *


storage_key = "ie_p_l"


# Setter storage so that we can differentiate values on this site from others at the same domain
def set_storage(key, val):
	storage["{}-{}".format(storage_key, key)] = val


# Getting for storage so that we can differentiate values on this site from others at the same domain
def get_storage(key):
	return storage["{}-{}".format(storage_key, key)]


# Check if a value exists in storage
def check_storage(key):
	return "{}-{}".format(storage_key, key) in storage


# deleter for storage so that we can differentiate values on this site from others at the same domain
def del_storage(key):
	nkey = f"{storage_key}-{key}"
	if nkey in storage.keys():
		del storage[nkey]


# generator to get all values in storage.  used during page load to set things up
def list_storage():
	for val in storage:
		if val.startswith(storage_key):
			yield val[len(storage_key) + 1:], storage[val]


def init_page():
	check_visit()
	pages = ['Table', 'Config']  # , 'About', 'Changelog']
	for c, page in enumerate(pages):
		doc['buttons'] <= BUTTON(page, data_id=page, Class=f'page{" current_tab" if not c else ""}', Id=f'b_{page}')
		if c:
			doc['pages'] <= SECTION(Id=page)
			doc[page].style.display = 'none'
	init_options()
	init_table()
#	init_about()
#	init_change()
	doc["loading"].style.display = "none"

	# Make it so navigation buttons work
	@bind('.page', 'click')
	def change_page(ev):
		val = ev.target['data-id']
		# currently unable to create an event to trigger the template
		if val == 'Table':
			doc.getElementById('nav_target').click()
		doc[val].style.display = 'block'
		doc[f'b_{val}'].attrs['class'] = 'current_tab page'
		idx = pages.index(val)
		for i in pages[:idx] + pages[idx+1:]:
			doc[i].style.display = 'none'
			doc[f'b_{i}'].attrs['class'] = 'page'


def sort(evt, elt):
	# Hacky, whatever
	try:
		# get reference to the arrow
		arrow = evt.target
		# get title cell
		th = arrow.closest('TH')
		# get column of title cell
		column = th.index("th")
		# elt.data.order is a table with the sort order to apply to each column.
		if not hasattr(elt.data, "order"):
			elt.data.order = [0 for _ in elt.data.header]
		order = elt.data.order[column]
		# Changing the value of attribute "items" will trigger re-rendering the template
		elt.data.items.sort(key=lambda x: x[column], reverse=order)
		# next time, sort this column the other way
		elt.data.order[column] = 1 - order
	except KeyError as err:
		t_data = gen_table()
		elt.data.header = t_data[0]
		elt.data.order = [0 for _ in elt.data.header]
		elt.data.items = t_data[1:]


# Generates a table of valid data
def gen_table():
	h_vals = []
	for _elt in doc.get(selector='.header'):
		if _elt.checked:
			h_vals.append(data[0].index(_elt['data-id']))
	f_vals = []
	for _elt in doc.get(selector='.flag_val'):
		if _elt.checked:
			f_vals.append(_elt['data-id'])
	t_data = [[y for c, y in enumerate(data[0]) if c in h_vals]]
	t_data.extend([[y for c, y in enumerate(x) if c in h_vals] for x in data[1:] if x[0] in f_vals and x[-1] in f_vals])
	return t_data


# Given an array of values, create a w width table of checkboxes
def make_table(m_data, w, header=False, item_class=''):
	t = TABLE()
	tr = TR()
	for c, d in enumerate(m_data, 1):
		if isinstance(d, str):
			new_id = f"{item_class + '_' if item_class else ''}{d}"
			for a, b in [(' ', '_'), ('\'', '_'), ('+', '_')]:
				new_id = new_id.replace(a, b)
			tr <= TD(LABEL(INPUT(type='checkbox', Id=new_id, Class=f'save {"header" if header else "flag_val"}', data_id=f"{item_class + '_' if item_class else ''}{d}") + d))
		if not c % w:
			t <= tr
			tr = TR()
	if c % w:
		t <= tr
	return t


def init_table():
	t_data = gen_table()
	Template('pick_data', [sort]).render(header=t_data[0], items=t_data[1:])


def init_options():
	doc["Config"] <= H1("Column visibility") + make_table(headers, 3, True)
	doc["Config"] <= H1("Areas") + P("'Unknown' is npcs that may only exist in the game files and not be present in the game.  They are not attached to an area and don't have a BCS spawn script.") + make_table(areas, 2)
	doc['Config'] <= H1("Items")
	for base in types:
		doc["Config"] <= H2(base) + make_table(types[base], 3, item_class=base)

	for el in doc.get(selector='.save'):
		if check_storage(el['data-id']):
			el.checked = False
		else:
			el.checked = True

	@bind('.save', 'change')
	def save_state(ev):
		if ev.target.type == 'checkbox':
			if ev.target.checked:
				del_storage(ev.target['data-id'])
			else:
				set_storage(ev.target['data-id'], 'unchecked')


# Check if first visit, if so hide some specific columns and items by default
def check_visit():
	if not check_storage('visited'):
		set_storage('visited', 'True')
		# By default hide some common/low value items and some of the columns
		for k_val in ['XP', 'Gold Carried', 'Item Type', 'unknown', 'Amulet_Amulet of the Keeper of Secrets Under the Mountain', 'Amulet_Bloodstone Amulet', "Amulet_Galvena's Medallion", 'Amulet_Gold Necklace', 'Amulet_Greenstone Amulet',
					  'Amulet_Keepsake Locket', 'Amulet_Pearl Necklace', 'Amulet_Rainbow Obsidian Necklace', 'Amulet_Silver Necklace', 'Amulet_Thrall Collar', "Armor_Adventurer's Robe", 'Armor_Chain Mail Armor', 'Armor_Leather Armor',
					  'Armor_Leather Armor +1', 'Armor_Studded Leather Armor', 'Arrows_Acid Arrow +1', 'Arrows_Arrow', 'Arrows_Arrow +1', 'Arrows_Arrow of Biting', 'Arrows_Arrow of Fire', 'Arrows_Arrow of Ice', 'Arrows_Arrow of Piercing +1',
					  'Arrows_Flaming Arrow', 'Axe_Battle Axe', 'Axe_Battle Axe +1', 'Axe_Throwing Axe', 'Bolts_Bolt', 'Bolts_Bolt +1', 'Bolts_Bolt of Biting ', 'Bolts_Bolt of Lightning', 'Bolts_Drow Bolt +1', 'Bolts_Drow Bolt of Sleep',
					  'Bolts_Drow Bolt of Stunning', 'Bolts_Flasher Master Bruiser Mate', 'Bolts_Kuo-toan Bolt', 'Bolts_Paralytic Bolt', 'Books & misc_Wooden Stake', 'Books & misc_rndaro01.itm', 'Books & misc_rndgem01.itm',
					  'Books & misc_rndgem02.itm', 'Books & misc_rndgem03.itm', 'Books & misc_rndmag01.itm', 'Books & misc_rndmag06.itm', 'Books & misc_rndptn01.itm', 'Books & misc_rndscr01.itm', 'Books & misc_rndscr04.itm',
					  'Books & misc_rndtre01.itm', 'Books & misc_rndtre02.itm', 'Books & misc_rndtre03.itm', 'Books & misc_rndtre04.itm', 'Books & misc_rndtre05.itm', 'Books & misc_rndtre06.itm', 'Books & misc_rndtre07.itm',
					  'Books & misc_rndtre08.itm', 'Books & misc_rndtre09.itm', 'Books & misc_rndtri02.itm', 'Books & misc_rndwand.itm', 'Books & misc_sodtre09.itm', 'Bow_Composite Longbow', 'Bow_Composite Longbow +1', 'Bow_Longbow',
					  'Bow_Longbow +1', 'Bow_Shortbow', 'Bow_Shortbow +1', 'Bracers & gauntlets_Bracers', 'Bracers & gauntlets_Bracers of Defense AC 7', 'Bracers & gauntlets_Bracers of Defense AC 8', 'Bracers & gauntlets_Jansen Techno-Gloves',
					  'Bullets_Bullet', 'Bullets_Bullet +1', 'Bullets_Bullet of Electricity +1', 'Bullets_Bullet of Fire +1', 'Bullets_Bullet of Ice +1', 'Bullets_Sunstone Bullet +1', 'Cloaks & Robes_Drow Piwafwi Cloak',
					  'Cloaks & Robes_Shadow Thief Cloak', 'Crossbow_Drow Crossbow of Speed +3', 'Crossbow_Flasher Launcher', 'Crossbow_Heavy Crossbow +1', 'Crossbow_Light Crossbow', 'Crossbow_Light Crossbow +1', 'Dagger_Dagger',
					  'Dagger_Dagger +1', 'Dagger_Poisoned Throwing Dagger', 'Dagger_Shadow Thief Dagger', 'Dagger_Throwing Dagger', 'Dagger_Throwing Dagger +1', "Darts_Asp's Nest +1", 'Darts_Dart', 'Darts_Dart +1',
					  'Darts_Dart of Acid +1', 'Darts_Dart of Fire +1', 'Darts_Dart of Stunning', 'Darts_Dart of Wounding', 'Flail_Drow Flail +3', 'Flail_Flail', 'Flail_Flail +1', 'Halberd_Halberd', 'Halberd_Halberd +1',
					  'Hammer_War Hammer', 'Hammer_War Hammer +1', 'Headgear_Helmet', 'Large sword_Bastard Sword', 'Large sword_Bastard Sword +1', 'Large sword_Drow Long Sword +3', 'Large sword_Long Sword', 'Large sword_Long Sword +1',
					  'Large sword_Ninja-To', 'Large sword_Scimitar', 'Large sword_Scimitar +1', 'Large sword_Two-handed Sword', 'Large sword_Two-handed Sword +1', 'Mace & Club_Club', 'Mace & Club_Club +1', 'Mace & Club_Mace',
					  'Mace & Club_Mace +1', 'Morning star_Morning Star', 'Morning star_Morning Star +1', 'Potion_Antidote', 'Potion_Bottle of Wine', 'Potion_Elixir of Health', 'Potion_Empty Breath Potion Flask',
					  'Potion_Potion of Cloud Giant Strength', 'Potion_Potion of Fire Giant Strength', 'Potion_Potion of Healing', 'Potion_Potion of Hill Giant Strength', 'Potion_Potion of Infravision', 'Potion_Potion of Regeneration',
					  'Potion_Potion of Stone Giant Strength', 'Potion_Potion of Storm Giant Strength', 'Potion_Red Potion', 'Potion_Violet Potion', "Quarterstaff_Neera's Staff +1", 'Quarterstaff_Quarterstaff', 'Quarterstaff_Quarterstaff +1',
					  'Ring_Bloodstone Ring', 'Ring_Dal Family Ring', 'Ring_Discipliner', 'Ring_Fire Opal Ring', 'Ring_Flamedance Ring', 'Ring_Gold Ring', 'Ring_Jade Ring', 'Ring_Onyx Ring', 'Ring_Ring', 'Ring_Ruby Ring', 'Ring_Silver Ring',
					  'Ring_swordi.itm', 'Shield_Buckler +1', 'Shield_Large Shield', 'Shield_Medium Shield', 'Shield_Medium Shield +1', 'Sling_Sling ', 'Sling_Sling +1', 'Small sword_Short Sword', 'Small sword_Short Sword +1',
					  'Small sword_Wakizashi', 'Spear_Spear', 'Tattoos_Bandit Scalp']:
			set_storage(k_val, 'unchecked')


init_page()
