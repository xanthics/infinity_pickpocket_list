###
# Pickpocket list: area > person > item
# Add XP, Gold, Rep
###

import struct
import os
from manual.area_names import area_lookup


# wrapper function to convert byte string to regular string
def mystr(a_str):
	return str(a_str, 'UTF-8').strip('\x00').replace('"', '\\"')


# Given an index, return a strings
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/tlk_v1.htm
def getname(idx):
	if idx == -1:
		return ""
	assert idx >= 0, f"Invalid Name/String index: {idx}"
	with open('tlk\\dialog.tlk', 'rb') as file:
		text = file.read()
		max_str = struct.unpack('i', text[0xa:0xa+4])[0]
		if idx >= max_str:
			return ""
		abs_str_off = struct.unpack('i', text[0xe:0xe+4])[0]
		data_off = 0x1a * idx + 0x12
		str_off = struct.unpack('i', text[data_off+0x12:data_off+0x12+4])[0]
		str_len = struct.unpack('i', text[data_off+0x16:data_off+0x16+4])[0]
		return mystr(text[abs_str_off+str_off:abs_str_off+str_off+str_len])


# Given a character name, return useful information
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/cre_v1.htm
def view_char(cre_file, item_list):
	with open(cre_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'CRE '), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		ret = {}
		# Check version since eah one stores files differently
		if version == 'v1.0':
			name = 0x8
			race = 0x272
			status = 0x20
			xp = 0x14
			gold = 0x1c
			item_count_off = 0x2c0
			item_offset_off = 0x2bc
			pick_off = 0x6a
			equip_off = 0x2b8
			enemy = 0x270
		else:
			assert False, f"Invalid File Version: '{version}'"
		ret['items'] = []
		# get list of items, check item slots, assign difficulty
		item_count = struct.unpack('i', text[item_count_off:item_count_off+4])[0]
		f_race = struct.unpack('B', text[race:race+1])[0]
		f_status = struct.unpack('I', text[status:status + 4])[0]
		if item_count and f_race != 146 and not bool(f_status & 0b111111000000):  # We can't pickpocket dragons or dead things
			if struct.unpack('B', text[enemy:enemy+1])[0] == 0xff:  # Enemies are hostile and cannot be pickpocketed, to my knowledge
				return ret
			ret['name'] = getname(struct.unpack('i', text[name:name + 4])[0])
			ret['xp'] = struct.unpack('i', text[xp:xp + 4])[0]
			ret['gold'] = struct.unpack('i', text[gold:gold + 4])[0]
			item_offset = struct.unpack('i', text[item_offset_off:item_offset_off+4])[0]
			items = []
			for idx in range(item_count):
				t_off = idx * 0x14 + item_offset
				items.append((mystr(text[t_off:t_off + 8]).lower(), bool(struct.unpack('i', text[t_off + 0x10:t_off + 0x10 + 4])[0] & 0b1010), struct.unpack('h', text[t_off + 0xa:t_off + 0xa + 2])[0]))
			pickpocket = struct.unpack('b', text[pick_off:pick_off + 1])[0]
			equip_offset = struct.unpack('i', text[equip_off:equip_off + 4])[0]
			# https://baldursgate.fandom.com/wiki/Thief#Pick_Pockets
			pick_difficulty = [0, 0, 0, 80, 60, 60, 80, 80, 0, 95, 95, 95, 95, 50, 50, 50, 50, 80, 50, 50, 50,  # helmet, armor, shield, gloves, rings(2), amulet, belt, boots, weapon(4), quiver(4), cloak, quick item(3)
							   10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # inventory slots(16), 0 means can't pickpocket
			equipped = struct.unpack('h', text[38 * 2 + equip_offset:38 * 2 + equip_offset + 2])[0]
			if 0 <= equipped < 4:
				pick_difficulty[9 + equipped] = 0
			for idx, slot in enumerate(pick_difficulty):
				if slot:
					s_off = idx * 2 + equip_offset
					item_idx = struct.unpack('h', text[s_off:s_off + 2])[0]
					if item_count > item_idx >= 0:
						item_itm = f"{items[item_idx][0]}.itm"
						if item_itm in item_list and item_list[item_itm]['drop'] and not items[item_idx][1]:
							ret['items'].append({'type': item_list[item_itm]['type'], 'name': item_list[item_itm]['name'], 'price': item_list[item_itm]['price'], 'skill': pickpocket + pick_difficulty[idx]})
							if items[item_idx][2] > 1 and item_list[item_itm]['type'] in ['Books & misc', 'Arrows', 'Potion', 'Scroll', 'Bullets', 'Darts', 'Bolts', 'Gold pieces', 'Gem', 'Wand', 'Containers/eye/broken armor', 'Books/Broken shields/bracelets', 'Familiars/Broken swords/earrings', 'Fur/pelt']:
								ret['items'][-1]['quantity'] = items[item_idx][2]
		return ret


# Given an item name, return useful information
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/itm_v1.htm
# TODO: Wand charge max (from first ability)
def view_item(itm_file):
	with open(itm_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'ITM '), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		ret = {}
		# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/itm_v1.htm#Header_ItemType
		item_type = ['Books & misc', 'Amulet', 'Armor', 'Belt & Girdle', 'Boots', 'Arrows', 'Bracers & gauntlets', 'Headgear', 'Key', 'Potion', 'Ring', 'Scroll', 'Shield', 'Food', 'Bullets', 'Bow', 'Dagger',
					 'Mace & Club', 'Sling', 'Small sword', 'Large sword', 'Hammer', 'Morning star', 'Flail', 'Darts', 'Axe', 'Quarterstaff', 'Crossbow', 'Hand-to-hand weapon', 'Spear', 'Halberd', 'Bolts',
					 'Cloaks & Robes', 'Gold pieces', 'Gem', 'Wand', 'Containers/eye/broken armor', 'Books/Broken shields/bracelets', 'Familiars/Broken swords/earrings', 'Tattoos', 'Lenses', 'Bucklers/teeth',
					 'Candles', 'Unknown', 'Clubs (IWD)', 'Unknown', 'Unknown', 'Large Shields (IWD)', 'Unknown', 'Medium Shields (IWD)', 'Notes', 'Unknown', 'Unknown', 'Small Shields (IWD)', 'Unknown',
					 'Telescopes (IWD)', 'Drinks (IWD)', 'Great Swords (IWD)', 'Container', 'Fur/pelt', 'Leather Armor', 'Studded Leather Armor', 'Chain Mail', 'Splint Mail', 'Half Plate', 'Full Plate',
					 'Hide Armor', 'Robe', 'Unknown', 'Bastard Sword', 'Scarf', 'Food (IWD2)', 'Hat', 'Gauntlet', 'Eyeballs', 'Earrings', 'Teeth', 'Bracelets']

		# Check version since eah one stores files differently
		if version == 'v1  ':
			name = 0xc
			price = 0x34
			flags = 0x18
			itm_type = 0x1c
			max_count = 0
		else:
			assert False, f"Invalid File Version: '{version}'"
		ret['name'] = getname(struct.unpack('i', text[name:name + 4])[0])
		ret['price'] = struct.unpack('i', text[price:price + 4])[0]
		ret['drop'] = bool(struct.unpack('i', text[flags:flags + 4])[0] & 4)
		ret['type'] = item_type[struct.unpack('h', text[itm_type:itm_type + 2])[0]]
	return ret


# Given an area name return a list of actors
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/are_v1.htm
def view_area(are_file, cre_dict):
	with open(are_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'AREA'), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		ret = []
		# Check version since eah one stores files differently
		if version == 'v1.0':
			actors_off = 0x54
			actors_count = 0x58
		else:
			assert False, f"Invalid File Version: '{version}'"
		t_actors = set()  # Only include 1 instance of a character from each zone
		for idx in range(struct.unpack('h', text[actors_count:actors_count + 2])[0]):
			actor = struct.unpack('i', text[actors_off:actors_off + 4])[0] + idx * 0x110
			actor_file = mystr(text[actor + 0x80:actor + 0x80 + 8]).lower()
			if actor_file in cre_dict:
				t_actors.add(actor_file)
		for t_act in t_actors:
			ret.append(cre_dict[t_act])
	return ret, t_actors


# Given a decompiled script file, extract all spawned creatures
def view_bcs(baf_file, cre_dict):
	with open(baf_file, 'r', errors='ignore') as f:
		t_actors = set()  # Only include 1 instance of a character from each zone
		ret = []
		for line in f:
			if 'CreateCreature' in line:
				cre = line.split('"')[1].lower()
				if cre in cre_dict:
					t_actors.add(cre)
		for t_act in t_actors:
			ret.append(cre_dict[t_act])

	return ret, t_actors


# NOTES: sell value is 1/2 of an items value.  Items with charges are value/max_count*current_count
def main():
	# Areas -> actors -> items, so generate in reverse
	# Create a dictionary with all valid items that can drop
	items = {}
	for r, d, f in os.walk('itm'):
		len_f = len(f)
		tick = len_f // 40
		print(f"Reading {len_f} ITM files.")
		for c, file in enumerate(f):
			if not c % tick:
				print(f"ITM: {c}/{len_f}")
			if file.lower().endswith('.itm'):
				item = view_item(os.path.join(r, file))
				if not item['name']:
					item['name'] = file.lower()
				# remove EET items that appear to be script/difficulty related
				if not (item['name'].startswith('dw#') and item['price'] == 0):
					items[file.lower()] = item
	# Create a list of all valid creatures that have valid items to pickpocket
	cre_dict = {}
	for r, d, f in os.walk('cre'):
		len_f = len(f)
		tick = len_f // 40
		print(f"Reading {len_f} CRE files.")
		for c, file in enumerate(f):
			if not c % tick:
				print(f"CRE: {c}/{len_f}")
			if file.lower().endswith('.cre'):
				person = view_char(os.path.join(r, file), items)
				if person['items']:
					if not person['name']:
						person['name'] = file[:-4]
					cre_dict[file.lower()[:-4]] = person
	# Go through all areas and check all creatures for ones that can be pickpocketed
	are_dict = {}
	npc_list = set(cre_dict.keys())
	for r, d, f in os.walk('are'):
		len_f = len(f)
		tick = len_f // 40
		print(f"Reading {len_f} CRE files.")
		for c, file in enumerate(f):
			if not c % tick:
				print(f"ARE: {c}/{len_f}")
			if file.lower().endswith('.are'):
				area, npcs = view_area(os.path.join(r, file), cre_dict)
				if area:
					npc_list -= npcs
					area_key = file[:-4].lower()
					are_dict[f"{area_key} - {area_lookup[area_key]}" if area_key in area_lookup else area_key] = area
	# Check all scripts that can spawn npcs for ones that spawn pickpocket targets
	for r, d, f in os.walk('bcs'):
		len_f = len(f)
		tick = len_f // 40
		print(f"Reading {len_f} BAF files.")
		for c, file in enumerate(f):
			if not c % tick:
				print(f"ARE: {c}/{len_f}")
			if file.lower().endswith('.baf'):
				area, npcs = view_bcs(os.path.join(r, file), cre_dict)
				if area:
					npc_list -= npcs
					area_key = file[:-4].lower()
					are_dict[f"{area_key} (Spawned) - {area_lookup[area_key]}" if area_key in area_lookup else f"{area_key} (Spawned)"] = area

	if npc_list:
		are_dict['unknown'] = []
		for npc in npc_list:
			cre_dict[npc]['name'] += f" ({npc})"
			are_dict['unknown']. append(cre_dict[npc])

	# Store possible values that can appear in various columns to toggle those rows
	areas = set()
	item_types = {}
	buf = ['data = [', '\t["Area", "NPC", "XP", "Gold Carried", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"],']
	for are in sorted(are_dict):
		for cre in sorted(are_dict[are], key=lambda i: i['name']):
			for itm in sorted(cre['items'], key=lambda i: i['price'], reverse=True):
				areas.add(are)
				if itm["type"] not in item_types:
					item_types[itm["type"]] = set()
				item_types[itm["type"]].add(itm["name"])
				buf.append(f'\t["{are}", "{cre["name"]}", {cre["xp"]}, {cre["gold"]}, {itm["skill"]}, {itm["price"]}, "{itm["type"]}", "{itm["name"] + " (" + str(itm["quantity"]) + ")" if "quantity" in itm else itm["name"]}", "{itm["type"]}_{itm["name"]}"],')
	buf.append(']\n')

	with open('table_data.py', 'w') as f:
		f.write('\n'.join(buf))

	buf = ['headers = ["Area", "NPC", "XP", "Gold Carried", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"]\n', 'areas = [']
	for a in sorted(areas):
		buf.append(f'\t"{a}",')
	buf.append(']\n')
	buf.append('types = {')
	for a in sorted(item_types):
		buf.append(f'\t"{a}": [')
		for b in sorted(item_types[a]):
			buf.append(f'\t\t"{b}",')
		buf.append('\t],')
	buf.append('}\n')

	with open('config_data.py', 'w') as f:
		f.write('\n'.join(buf))


if __name__ == '__main__':
	main()
