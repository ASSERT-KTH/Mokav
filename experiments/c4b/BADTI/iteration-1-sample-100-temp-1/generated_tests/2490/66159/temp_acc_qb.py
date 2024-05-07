def patched_func(*args):
	global_list = []
	
	global_list.append(round(((int(args[0]) / 2) * 3)))
	return global_list