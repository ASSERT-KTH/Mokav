def patched_func(*args):
	global_list = []
	
	global_list.append((((int(args[0]) * 2) + 1) // 3))
	return global_list