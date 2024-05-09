def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	global_list.append((n * m))
	return global_list