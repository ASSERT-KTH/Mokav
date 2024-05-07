def patched_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	a = ((d1 + d2) * 2)
	b = ((d1 + d3) * 2)
	c = ((d1 + d3) + d2)
	d = ((d2 + d3) * 2)
	global_list.append(min(a, b, c, d))
	return global_list