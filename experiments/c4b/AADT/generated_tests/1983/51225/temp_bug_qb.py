def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((n * (n - 1)) + 1))
	return global_list