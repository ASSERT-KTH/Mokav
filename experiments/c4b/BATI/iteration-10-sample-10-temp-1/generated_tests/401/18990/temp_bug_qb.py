def original_func(*args):
	global_list = []
	
	a = int(args[0])
	global_list.append((2 ** a))
	return global_list