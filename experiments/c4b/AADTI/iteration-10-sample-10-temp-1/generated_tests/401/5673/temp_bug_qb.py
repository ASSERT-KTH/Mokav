def original_func(*args):
	global_list = []
	
	x = int(args[0])
	s = (2 ** x)
	global_list.append(s)
	return global_list