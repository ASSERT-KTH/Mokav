def original_func(*args):
	global_list = []
	
	(n, m, a) = map(int, args[0].split())
	global_list.append(((((n + a) - 1) // a) + (((m + a) - 1) // a)))
	return global_list