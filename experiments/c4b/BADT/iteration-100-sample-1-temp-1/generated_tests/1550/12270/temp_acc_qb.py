def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	global_list.append(max(((3 * n) - k), 0))
	return global_list