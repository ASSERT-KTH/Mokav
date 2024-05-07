def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((((((n - 1) * n) * (n + 1)) // 6) + n) // 1))
	return global_list