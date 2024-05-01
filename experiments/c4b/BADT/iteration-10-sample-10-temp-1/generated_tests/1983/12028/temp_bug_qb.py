def original_func(*args):
	global_list = []
	
	n = int(args[0])
	n = (((n ** 2) - n) - 1)
	global_list.append(n)
	return global_list