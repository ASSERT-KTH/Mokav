def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = [int(i) for i in args[0].split()]
	res = min((d1 + d2), d3, ((d1 * 2) + (d2 * 2)))
	res = min(res, ((d1 * 2) + (d3 * 2)))
	res = min(res, (d2 * 2), (d3 * 2))
	global_list.append(res)
	return global_list