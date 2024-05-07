def original_func(*args):
	global_list = []
	
	a = int(args[0])
	global_list.append(((a * a) * 3))
	return global_list