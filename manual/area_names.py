# Names compiled from these 2 gibberling pages.
# https://gibberlings3.github.io/iesdp/appendices/area_lists/bg1aref.htm
# https://gibberlings3.github.io/iesdp/appendices/area_lists/bg2aref.htm

area_lookup = {}

#with open("manual/bg2_area.csv", 'r') as f:
with open("manual/iwd_area.csv", 'r') as f:
	for line in f:
		l = line.strip().split('|')
		if len(l) == 2:
			area_lookup[l[0].lower()] = l[1].replace('"', '\\"')
