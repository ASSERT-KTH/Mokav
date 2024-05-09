def original_func(*args):
	global_list = []
	
	from math import log1p as ln
	(a, b) = map(int, args[0].split())
	years = (ln((b / a)) / ln((3 / 2)))
	global_list.append((int(years) + 1))
	return global_list