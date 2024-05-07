def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(int((n * 1.5)))
	return global_list