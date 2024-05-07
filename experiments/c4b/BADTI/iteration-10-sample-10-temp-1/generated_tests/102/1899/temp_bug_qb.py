def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = [int(i) for i in args[0].split()]
	global_list.append(min((2 * (d1 + d2)), ((d1 + d2) + d3)))
	return global_list