def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((((n // 2) - 1) + (n % 2)))
	return global_list