def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	global_list.append(((x + 4) // 5))
	return global_list