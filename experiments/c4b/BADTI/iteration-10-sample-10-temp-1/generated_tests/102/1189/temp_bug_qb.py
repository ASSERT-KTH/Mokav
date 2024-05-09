def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = [int(x) for x in args[0].split()]
	global_list.append(min(((d1 + d2) + d3), (2 * (d1 + d2))))
	return global_list