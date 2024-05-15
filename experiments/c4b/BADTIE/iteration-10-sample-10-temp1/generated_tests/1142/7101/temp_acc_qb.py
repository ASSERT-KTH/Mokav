def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, str(args[0]).strip().split())
	global_list.append(((n - max((a + 1), (n - b), 1)) + 1))
	return global_list