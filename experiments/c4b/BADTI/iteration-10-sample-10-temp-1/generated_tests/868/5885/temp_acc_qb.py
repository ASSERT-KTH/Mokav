def patched_func(*args):
	global_list = []
	
	global_list.append(pow(8, int(args[0]), 10))
	return global_list