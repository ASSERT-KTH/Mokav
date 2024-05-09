def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	global_list.append(((3 * n) - k))
	return global_list