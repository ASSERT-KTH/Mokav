def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((n // 4) - ((n % 4) == 0)))
	return global_list