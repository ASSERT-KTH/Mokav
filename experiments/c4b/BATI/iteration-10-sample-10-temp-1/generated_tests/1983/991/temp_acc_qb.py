def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(int(((n * ((n ** 2) + 5)) / 6)))
	return global_list