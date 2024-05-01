def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((2 ** n))
	return global_list