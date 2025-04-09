###
# Pickpocket list: area > person > item
# Add XP, Gold, Rep
###

import struct
import os
from manual.area_names import gen_area_names
from template_index import index
from handle_page import handle
from root_index import root_index


# wrapper function to convert byte string to regular string
def mystr(a_str):
	return str(a_str, 'UTF-8').strip('\x00').replace('"', '\\"')


# Given an index, return a strings
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/tlk_v1.htm
def getname(idx, game):
	if idx == -1:
		return ""
	assert idx >= 0, f"Invalid Name/String index: {idx}"
	with open(f'{game}_files/dialog.tlk', 'rb') as file:
		text = file.read()
		max_str = struct.unpack('i', text[0xa:0xa+4])[0]
		if idx >= max_str:
			return ""
		abs_str_off = struct.unpack('i', text[0xe:0xe+4])[0]
		data_off = 0x1a * idx + 0x12
		str_off = struct.unpack('i', text[data_off+0x12:data_off+0x12+4])[0]
		str_len = struct.unpack('i', text[data_off+0x16:data_off+0x16+4])[0]
		return mystr(text[abs_str_off+str_off:abs_str_off+str_off+str_len])


# Return an array with difficulties for pickpocketing various equipment slots
def load_pickpocketting(game):
	# https://baldursgate.fandom.com/wiki/Thief#Pick_Pockets
	key_order = ['helmet', 'armour', 'shield', 'gauntlets', 'ring_left', 'ring_right', 'amulet', 'belt', 'boots',
				 'weapon1', 'weapon2', 'weapon3', 'weapon4', 'ammo1', 'ammo2', 'ammo3', 'ammo4', 'cloak', 'misc1', 'misc2', 'misc3',
				 'inv1', 'inv2', 'inv3', 'inv4', 'inv5', 'inv6', 'inv7', 'inv8', 'inv9', 'inv10', 'inv11', 'inv12', 'inv13', 'inv14', 'inv15', 'inv16']
	vals = {}
	with open(f'{game}_files/SLTSTEAL.2DA', 'r') as file:
		# skip headers
		for i in range(3):
			file.readline()
		for line in file:
			l_list = line.lower().strip().split()
			vals[l_list[0]] = int(l_list[1])
	return [vals[x] for x in key_order]


# Return a dictionary with dexterity bonuses to pickpocket
def load_dex_bonus(game):
	vals = {}
	with open(f'{game}_files/SKILLDEX.2DA', 'r') as file:
		# skip headers
		for i in range(3):
			file.readline()
		for line in file:
			l_list = line.lower().strip().split()
			vals[int(l_list[0])] = int(l_list[1])
	return vals


# Return a dictionary with racial bonuses to pickpocket
def load_race_bonus(game):
	vals = {}
	with open(f'{game}_files/SKILLRAC.2DA', 'r') as file:
		# skip headers
		for i in range(3):
			file.readline()
		for line in file:
			l_list = line.lower().strip().split()
			vals[l_list[0]] = int(l_list[1])
	return vals


# Return a dictionary with the racial bonuses associated with racial id number
def load_race_lookup(game):
	lrb = load_race_bonus(game)
	vals = {}
	with open(f'{game}_files/RACE.IDS', 'r') as file:
		# skip headers
		for i in range(1):
			file.readline()
		for line in file:
			l_list = line.lower().strip().split()
			if l_list:
				vals[int(l_list[0])] = lrb[l_list[1]] if l_list[1] in lrb else 0
	return vals


# Given a character name, return useful information
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/cre_v1.htm
def view_char(cre_file, item_list, game, dlg_store, sltsteal, skilldex, skillrac):
	with open(cre_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'CRE '), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		ret = {}
		# Check version since each one stores files differently
		if version == 'v1.0':
			name = 0x8
			race = 0x272
			status = 0x20
			xp = 0x14
			gold = 0x1c
			item_count_off = 0x2c0
			item_offset_off = 0x2bc
			pick_off = 0x6a
			dex = 0x023c
			equip_off = 0x2b8
			enemy = 0x270
			dlg = 0x2cc
		else:
			assert False, f"Invalid File Version: '{version}'"
		ret['items'] = []
		# get list of items, check item slots, assign difficulty
		item_count = struct.unpack('i', text[item_count_off:item_count_off+4])[0]
		f_race = struct.unpack('B', text[race:race+1])[0]
		f_dex = struct.unpack('B', text[dex:dex+1])[0]
		f_status = struct.unpack('I', text[status:status + 4])[0]
		ret['name'] = getname(struct.unpack('i', text[name:name + 4])[0], game)
		ret['xp'] = struct.unpack('i', text[xp:xp + 4])[0]
		ret['gold'] = struct.unpack('i', text[gold:gold + 4])[0]
		dlg_file = mystr(text[dlg:dlg + 8]).lower()
		if dlg_file in dlg_store:
			ret['stores'] = dlg_store[dlg_file]
		if item_count and f_race != 146 and not bool(f_status & 0b111111000000):  # We can't pickpocket dragons or dead things
			if struct.unpack('B', text[enemy:enemy+1])[0] == 0xff:  # Enemies are hostile and cannot be pickpocketed, to my knowledge
				return ret
			item_offset = struct.unpack('i', text[item_offset_off:item_offset_off+4])[0]
			items = []
			for idx in range(item_count):
				t_off = idx * 0x14 + item_offset
				items.append((mystr(text[t_off:t_off + 8]).lower(), bool(struct.unpack('i', text[t_off + 0x10:t_off + 0x10 + 4])[0] & 0b1010), struct.unpack('h', text[t_off + 0xa:t_off + 0xa + 2])[0]))
			pickpocket = struct.unpack('b', text[pick_off:pick_off + 1])[0]
			if pickpocket > 0:
				 pickpocket += skillrac[f_race] + skilldex[f_dex]
			equip_offset = struct.unpack('i', text[equip_off:equip_off + 4])[0]
			equipped = struct.unpack('h', text[38 * 2 + equip_offset:38 * 2 + equip_offset + 2])[0]
			if 0 <= equipped < 4:
				sltsteal[9 + equipped] = 0
			for idx, slot in enumerate(sltsteal):
				if slot:
					s_off = idx * 2 + equip_offset
					item_idx = struct.unpack('h', text[s_off:s_off + 2])[0]
					if item_count > item_idx >= 0:
						item_itm = f"{items[item_idx][0]}"
						if item_itm in item_list and item_list[item_itm]['drop'] and not items[item_idx][1]:
							ret['items'].append({'type': item_list[item_itm]['type'], 'name': item_list[item_itm]['name'], 'price': item_list[item_itm]['price'], 'slot': sltsteal[idx], 'skill': pickpocket})
							if items[item_idx][2] > 1 and item_list[item_itm]['type'] in ['Books & misc', 'Arrows', 'Potion', 'Scroll', 'Bullets', 'Darts', 'Bolts', 'Gold pieces', 'Gem', 'Wand', 'Containers/eye/broken armor', 'Books/Broken shields/bracelets', 'Familiars/Broken swords/earrings', 'Fur/pelt']:
								ret['items'][-1]['quantity'] = items[item_idx][2]
		return ret


# Given an item name, return useful information
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/itm_v1.htm
# TODO: Wand charge max (from first ability)
def view_item(itm_file, game):
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
		ret['name'] = getname(struct.unpack('i', text[name:name + 4])[0], game)
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


# Given a store, return a list of items that can be stolen and how difficult they are
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/sto_v1.htm
def view_store(sto_file):
	ret = {'items': [], 'difficult': 0, 'slot': '"Store"'}
	with open(sto_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'STOR'), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		# Check version since each one stores files differently
		if version == 'v1.0':
			steal = 0x10
			diff = 0x20
			item_offset = 0x34
			item_count = 0x38
			# in item
			amount = 0x14
			infinite = 0x18
			stealable = 0x10
		else:
			assert False, f"Invalid File Version: '{version}'"
		if struct.unpack('i', text[steal:steal + 4])[0] & 0b1000:  # if you can steal
			ret['skill'] = struct.unpack('H', text[diff:diff + 2])[0]
			item_offset = struct.unpack('i', text[item_offset:item_offset + 4])[0]
			for idx in range(struct.unpack('i', text[item_count:item_count + 4])[0]):
				t_off = idx * 0x1c + item_offset
				if not bool(struct.unpack('i', text[t_off + stealable:t_off + stealable + 4])[0] & 0b1010):
					ret['items'].append((mystr(text[t_off:t_off + 8]).lower(), "Inf" if struct.unpack('i', text[t_off + infinite:t_off + infinite + 4])[0] else struct.unpack('i', text[t_off + amount:t_off + amount + 4])[0]))
	return ret


# Given a dialog file, determine if it spawns a store you can steal from
# https://gibberlings3.github.io/iesdp/file_formats/ie_formats/dlg_v1.htm
def view_dlg(dlg_file, stores):
	ret = []
	with open(dlg_file, 'rb') as file:
		try:
			text = file.read()
		finally:
			file.close()
		# Check That this is a CRE file
		assert (mystr(text[0x0:0x0+4]) == 'DLG '), f"Invalid File Type: '{mystr(text[0x0:0x0+4])}'"
		version = mystr(text[0x4:0x4+4]).lower()
		# Check version since eah one stores files differently
		if version == 'v1.0':
			action_offset = 0x28
			action_count = 0x2c
		else:
			assert False, f"Invalid File Version: '{version}'"
		item_offset = struct.unpack('i', text[action_offset:action_offset + 4])[0]
		for idx in range(struct.unpack('i', text[action_count:action_count + 4])[0]):
			t_off = idx * 0x8 + item_offset
			str_off = struct.unpack('i', text[t_off:t_off + 4])[0]
			the_str = mystr(text[str_off:str_off + struct.unpack('i', text[t_off + 0x4:t_off + 0x4 + 4])[0]])
			if the_str.startswith('StartStore'):
				t_str = the_str.split('\\"')[1].lower()
				if t_str in stores and t_str not in ret:
					ret.append(t_str)
	return ret


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
def walk_game(game, game_str):
	area_lookup = gen_area_names(game)
	# Areas -> actors -> items, so generate in reverse
	# Create a dictionary with all valid items that can drop
	items = {}
	# Keep track of what can be stolen from stores
	stores = {}
	dlg_store = {}
	# Create a list of all valid creatures that have valid items to pickpocket
	cre_dict = {}
	# Go through all areas and check all creatures for ones that can be pickpocketed
	are_dict = {}
	# store how difficult it is to pickpocket a slot
	sltsteal = load_pickpocketting(game)
	# store how dex modifies pickpocket
	skilldex = load_dex_bonus(game)
	# store how race affects pickpocket
	skillrac = load_race_lookup(game)

	for r, d, f in os.walk(f"{game}_files"):
		itm_files = []
		cre_files = []
		are_files = []
		baf_files = []
		sto_files = []
		dlg_files = []
		for f_val in f:
			f_temp = f_val.lower()
			if f_temp.endswith('.itm'):
				itm_files.append(f_val)
			elif f_temp.endswith('.cre'):
				cre_files.append(f_val)
			elif f_temp.endswith('.are'):
				are_files.append(f_val)
			elif f_temp.endswith('.baf'):
				baf_files.append(f_val)
			elif f_temp.endswith('.sto'):
				sto_files.append(f_val)
			elif f_temp.endswith('.dlg'):
				dlg_files.append(f_val)
			else:
				print(f"Unexpected file: '{f_temp}'")

		len_f = len(sto_files)
		tick = len_f // 40
		print(f"Reading {len_f} STO files.")
		for c, file in enumerate(sto_files):
			if not c % tick:
				print(f"{game} STO: {c/len_f*100:2f}")
			item = view_store(os.path.join(r, file))
			if item['items']:
				stores[file[:-4].lower()] = item

		len_f = len(dlg_files)
		tick = len_f // 40
		print(f"Reading {len_f} DLG files.")
		for c, file in enumerate(dlg_files):
			if not c % tick:
				print(f"{game} DLG: {c/len_f*100:.2f}")
			item = view_dlg(os.path.join(r, file), stores)
			if item:
				dlg_store[file[:-4].lower()] = item

		len_f = len(itm_files)
		tick = len_f // 40
		print(f"Reading {len_f} ITM files.")
		for c, file in enumerate(itm_files):
			if not c % tick:
				print(f"{game} ITM: {c/len_f*100:.2f}")
			item = view_item(os.path.join(r, file), game)
			# note items with no name
			if not item['name']:
				item['name'] = f"{file}{'' if file.startswith('rnd') else ' (not in TLK)'}"
			# remove EET items that appear to be script/difficulty related, ignore items with no proper name
			if not (item['name'].startswith('dw#') and item['price'] == 0):
				items[file[:-4].lower()] = item

		len_f = len(cre_files)
		tick = len_f // 40
		print(f"Reading {len_f} CRE files.")
		for c, file in enumerate(cre_files):
			if not c % tick:
				print(f"{game} CRE: {c/len_f*100:.2f}")
			person = view_char(os.path.join(r, file), items, game, dlg_store, sltsteal, skilldex, skillrac)
			if person['items'] or 'stores' in person:
				if not person['name']:
					person['name'] = file[:-4]
				cre_dict[file.lower()[:-4]] = person

		npc_list = set(cre_dict.keys())
		len_f = len(are_files)
		tick = len_f // 40
		print(f"Reading {len_f} ARE files.")
		for c, file in enumerate(are_files):
			if not c % tick:
				print(f"{game} ARE: {c/len_f*100:.2f}")
			area, npcs = view_area(os.path.join(r, file), cre_dict)
			if area:
				npc_list -= npcs
				area_key = file[:-4].lower()
				are_dict[f"{area_key} - {area_lookup[area_key]}" if area_key in area_lookup else area_key] = area

		len_f = len(baf_files)
		tick = len_f // 40
		print(f"Reading {len_f} BAF files.")
		for c, file in enumerate(baf_files):
			if not c % tick:
				print(f"{game} ARE: {c/len_f*100:.2f}")
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
	buf = ['data = [', '\t["Area", "NPC", "XP", "Gold Carried", "Slot Difficulty", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"],']
	for are in sorted(are_dict):
		for cre in sorted(are_dict[are], key=lambda i: i['name']):
			for itm in sorted(cre['items'], key=lambda i: i['price'], reverse=True):
				areas.add(are)
				if itm["type"] not in item_types:
					item_types[itm["type"]] = set()
				item_types[itm["type"]].add(itm["name"])
				buf.append(f'\t["{are}", "{cre["name"]}", {cre["xp"]}, {cre["gold"]}, {itm["slot"]}, {itm["skill"]}, {itm["price"]}, "{itm["type"]}", "{itm["name"] + " (" + str(itm["quantity"]) + ")" if "quantity" in itm else itm["name"]}", "{itm["type"]}_{itm["name"]}"],')
			if 'stores' in cre:
				for sto in sorted(cre['stores'], reverse=True):
					areas.add(are)
					for itm_id, itm_count in sorted(stores[sto]['items'], key=lambda i: i[0]):
						# ignore items that don't have a proper identified name
						if itm_id not in items:
							continue
						itm = items[itm_id]
						if itm["type"] not in item_types:
							item_types[itm["type"]] = set()
						item_types[itm["type"]].add(itm["name"])
						buf.append(f'\t["{are}", "{cre["name"]} (Store)", {cre["xp"]}, {cre["gold"]}, {stores[sto]["slot"]}, {stores[sto]["skill"]}, {itm["price"]}, "{itm["type"]}", "{itm["name"]} ({itm_count})", "{itm["type"]}_{itm["name"]}"],')

	buf.append(']\n')

	with open(f'docs/{game}_table_data.py', 'w', encoding="utf-8") as f:
		f.write('\n'.join(buf))

	buf = [f'gamestr = "{game_str}"', 'headers = ["Area", "NPC", "XP", "Gold Carried", "Slot Difficulty", "Pickpocket Skill", "Item Price (base)", "Item Type", "Item"]\n', 'areas = [']
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

	with open(f'docs/{game}_config_data.py', 'w', encoding="utf-8") as f:
		f.write('\n'.join(buf))
	with open(f'docs/{game}.html', 'w', encoding="utf-8") as f:
		f.write(index.format(game, game_str))
	with open(f'docs/{game}_handle_page.py', 'w', encoding="utf-8") as f:
		f.write(handle.format(game))


def main():
	vals = [
		('iwdee', 'Icewind Dale EE 2.6.6.0'),
		('bgee', 'Baldur\'s Gate EE 2.6.6.0'),
		('bg2ee', 'Baldur\'s Gate 2 EE 2.6.6.0'),
		('custom_iwdee', 'Icewind Dale EE 2.6.5.0 + BetterHOF + CDTWEAKS'),
		('custom_bgeet', 'Baldur\'s Gate EET 2.6.5.0 + SCS'),
	]
	for game, game_str in vals:
		walk_game(game, game_str)

	with open('docs/index.html', 'w') as f:
		f.write(root_index.format('</p><p>'.join([f'<a href="{x[0]}.html" target="_blank">{x[1]}</a>' for x in vals])))


if __name__ == '__main__':
	main()
