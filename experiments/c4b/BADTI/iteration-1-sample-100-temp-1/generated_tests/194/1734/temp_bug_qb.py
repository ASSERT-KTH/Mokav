def original_func(*args):
	global_list = []
	
	x = int(args[0])
	global_list.append(((x // 5) + ((x % 5) == 0)))
	return global_list