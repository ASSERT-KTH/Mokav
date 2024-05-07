def original_func(*args):
	global_list = []
	
	'input\n1 1 5\n'
	(d1, d2, d3) = map(int, args[0].split())
	global_list.append(min(((2 * d1) + (2 * d2)), ((d1 + d2) + d3)))
	return global_list