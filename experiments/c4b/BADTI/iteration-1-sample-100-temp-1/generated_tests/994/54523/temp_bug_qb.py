def original_func(*args):
	global_list = []
	
	(n, m, a) = map(int, args[0].split())
	global_list.append((int(((n / a) + 1)) * int(((m / a) + 1))))
	return global_list