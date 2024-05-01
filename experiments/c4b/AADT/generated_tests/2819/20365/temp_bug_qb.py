def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	global_list.append(2)
	return global_list