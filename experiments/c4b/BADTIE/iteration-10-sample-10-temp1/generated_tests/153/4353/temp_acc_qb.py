def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((((n + 3) // 4) - 1) * ((n % 2) == 0)))
	return global_list