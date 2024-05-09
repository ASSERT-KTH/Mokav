def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((n // 5) if ((n % 5) == 0) else ((n // 5) + 1)))
	return global_list