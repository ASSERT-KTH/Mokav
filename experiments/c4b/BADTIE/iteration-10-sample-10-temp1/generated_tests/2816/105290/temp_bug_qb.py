def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((((n // 2) - 1) if ((n % 2) == 0) else (((n // 2) - 1) + ((n + 1) // 2))))
	return global_list