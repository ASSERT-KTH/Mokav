def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	global_list.append(((((n // 5) + (m // 5)) * 4) + (((n // 10) + (m // 10)) * 2)))
	return global_list