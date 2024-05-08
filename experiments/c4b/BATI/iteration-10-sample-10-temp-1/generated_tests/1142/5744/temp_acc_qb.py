def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	global_list.append(((n - a) if ((n - a) <= (b + 1)) else (b + 1)))
	return global_list