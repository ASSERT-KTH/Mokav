def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	global_list.append(((k * (((2 * n) - (2 * k)) - 1)) if (k < n) else ((n * (n - 1)) // 2)))
	return global_list