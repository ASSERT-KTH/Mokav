def patched_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split())
	global_list.append((((n // 2) * m) + (((n % 2) * m) // 2)))
	return global_list