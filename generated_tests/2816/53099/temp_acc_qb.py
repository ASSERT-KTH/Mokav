def patched_func(*args):
	global_list = []
	
	global_list.append(((int(args[0]) - 1) // 2))
	return global_list