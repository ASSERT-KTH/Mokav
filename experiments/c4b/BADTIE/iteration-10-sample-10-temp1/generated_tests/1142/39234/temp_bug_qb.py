def original_func(*args):
	global_list = []
	
	(n, a, b) = [int(x) for x in args[0].split()]
	global_list.append((n - a))
	return global_list