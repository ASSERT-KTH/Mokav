def patched_func(*args):
	global_list = []
	
	(x, y, z) = map(int, args[0].split())
	global_list.append(min((x - y), (z + 1)))
	return global_list