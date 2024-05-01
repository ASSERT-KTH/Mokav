def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	global_list.append(min((n - a), b))
	return global_list