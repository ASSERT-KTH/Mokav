def original_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split())
	global_list.append((int((n / 2)) * int((m / 1))))
	return global_list