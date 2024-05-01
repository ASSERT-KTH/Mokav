def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((sum((((i + 1) * ((n - i) - 1)) for i in range(n))) + n))
	return global_list