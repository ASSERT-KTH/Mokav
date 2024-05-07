def patched_func(*args):
	global_list = []
	
	from math import log1p as ln
	(a, b) = map(int, args[0].split())
	years = (ln(((b / a) - 1)) / ln(((3 / 2) - 1)))
	global_list.append((int(years) + 1))
	return global_list