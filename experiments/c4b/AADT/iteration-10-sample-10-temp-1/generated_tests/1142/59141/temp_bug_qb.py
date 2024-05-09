def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	global_list.append(((n - max((a + b), (n - b))) + 1))
	return global_list