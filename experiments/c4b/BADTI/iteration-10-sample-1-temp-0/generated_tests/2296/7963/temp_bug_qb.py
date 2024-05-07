def original_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split())
	global_list.append(((m // 2) * n))
	return global_list