def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(max(0, ((n / 2) - 1)))
	return global_list