def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((int((((n * (n - 1)) * (n + 4)) / 6)) + 1))
	return global_list