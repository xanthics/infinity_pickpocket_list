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
	pages = ['Table', 'Config', 'About', 'Changelog']
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
			tr <= TD(LABEL(INPUT(type='checkbox', Id=d.replace(' ', '_').replace('\'', '_'), Class=f'save {"header" if header else "flag_val"}', data_id=f"{item_class + '_' if item_class else ''}{d}") + d))
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
	doc["Config"] <= H1("Areas") + P("'Unknown' is npcs that are spawned by scripts or may only exist in the game files and not be present in the game.") + make_table(areas, 2)
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


init_page()
