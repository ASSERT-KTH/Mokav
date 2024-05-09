def original_func(*args):
	global_list = []
	
	(a, b, n) = map(int, args[0].split())
	int(min((n - a), (b + 1)))
	return global_list