# Names compiled from these 2 gibberling pages.
# https://gibberlings3.github.io/iesdp/appendices/area_lists/bg1aref.htm
# https://gibberlings3.github.io/iesdp/appendices/area_lists/bg2aref.htm


def gen_area_names(game):
	keys = {
		'iwdee': 'iwd_area',
		'custom_iwdee': 'iwd_area',
		'bgee': 'bg_area',
		'bg2ee': 'bg2_area',
		'custom_bgeet': 'bg2_area',
	}
	area_lookup = {}

	with open(f"manual/{keys[game]}.csv", 'r') as f:
		for line in f:
			l = line.strip().split('|')
			if len(l) == 2:
				area_lookup[l[0].lower()] = l[1].replace('"', '\\"')

	return area_lookup
