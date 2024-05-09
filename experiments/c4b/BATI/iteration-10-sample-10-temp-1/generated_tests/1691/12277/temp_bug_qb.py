def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	global_list.append(((c * ((b + a) - 1)) + (b - 1)))
	return global_list