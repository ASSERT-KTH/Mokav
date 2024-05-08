def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	x = ((3 * n) - k)
	global_list.append(x)
	return global_list