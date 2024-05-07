def original_func(*args):
	global_list = []
	
	global_list.append([6, 8, 4, 2][(int(args[0]) % 4)])
	return global_list