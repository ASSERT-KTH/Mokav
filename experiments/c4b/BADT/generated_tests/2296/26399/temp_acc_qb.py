def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	global_list.append(((n * m) // 2))
	return global_list