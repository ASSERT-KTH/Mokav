def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(pow(2, n))
	return global_list