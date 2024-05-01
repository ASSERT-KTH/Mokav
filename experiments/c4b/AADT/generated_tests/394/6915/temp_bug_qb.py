def original_func(*args):
	global_list = []
	
	(n, k) = [int(i) for i in args[0].split()]
	m = (0 if (k >= (2 * n)) else (n - (2 * k)))
	global_list.append((((n * (n - 1)) - (m * (m - 1))) // 2))
	return global_list