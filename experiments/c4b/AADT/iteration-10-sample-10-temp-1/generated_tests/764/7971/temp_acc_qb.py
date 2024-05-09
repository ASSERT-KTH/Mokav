def patched_func(*args):
	global_list = []
	
	(n, m, k) = map(int, args[0].split())
	global_list.append((max(n, m, k) - min(n, m, k)))
	return global_list