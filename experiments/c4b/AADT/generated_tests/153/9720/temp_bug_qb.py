def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((((n // 2) - 1) // 2) if (n != 1) else 0))
	return global_list