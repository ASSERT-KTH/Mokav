def original_func(*args):
	global_list = []
	
	(n, m, k) = map(int, args[0].split())
	f = (((n + m) + k) // 3)
	global_list.append(((abs((n - f)) + abs((m - f))) + abs((k - f))))
	return global_list