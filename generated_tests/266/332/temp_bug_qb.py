def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((120 * ((n - 4) ** 2)))
	return global_list