def patched_func(*args):
	global_list = []
	
	global_list.append((((2 * int(args[0])) + 1) // 3))
	return global_list