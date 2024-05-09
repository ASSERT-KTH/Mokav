def original_func(*args):
	global_list = []
	
	a = int(args[0])
	res = ((a * 6) + (a - 1))
	global_list.append(res)
	return global_list