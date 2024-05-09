def original_func(*args):
	global_list = []
	
	(x, y, z) = map(int, args[0].split())
	a = ((x + y) + z)
	b = (2 * (x + y))
	c = (2 * (x + z))
	k = min(a, b, c)
	global_list.append(k)
	return global_list