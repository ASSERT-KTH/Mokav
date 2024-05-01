def original_func(*args):
	global_list = []
	
	(x, y, z, k) = map(int, args[0].split())
	(x, y, z) = sorted((x, y, z))
	a = min((k // 3), x)
	b = min(((k - a) // 2), y)
	c = min(((k - a) - b), z)
	global_list.append((((a + 1) * (b + 1)) * (c + 1)))
	return global_list