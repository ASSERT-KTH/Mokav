def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	d1 = ((2 * a) + (2 * b))
	d2 = ((a + b) + c)
	d3 = ((2 * a) + (2 * c))
	d4 = ((2 * b) + (2 * c))
	global_list.append(min(d1, d2, d3, d4))
	return global_list