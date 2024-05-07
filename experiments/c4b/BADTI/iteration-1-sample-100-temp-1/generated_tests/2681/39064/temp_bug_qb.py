def original_func(*args):
	global_list = []
	
	x = int(args[0])
	global_list.append(((x * 8) + 3))
	return global_list