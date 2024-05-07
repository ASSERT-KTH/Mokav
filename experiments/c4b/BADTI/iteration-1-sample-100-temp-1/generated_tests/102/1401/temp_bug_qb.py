def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	global_list.append(min(((d1 + d2) + d3), ((d1 * 2) + (d2 * 2))))
	return global_list