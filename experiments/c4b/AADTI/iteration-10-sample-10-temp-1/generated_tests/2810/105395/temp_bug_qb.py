def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((n + 1) // 2))
	return global_list