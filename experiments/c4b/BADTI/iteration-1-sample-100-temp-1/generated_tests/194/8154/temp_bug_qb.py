def original_func(*args):
	global_list = []
	
	x = int(args[0])
	y = ((x % 5) + ((x / 5) != 0))
	global_list.append(y)
	return global_list