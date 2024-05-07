def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	global_list.append(min((b + 1), (n - a)))
	return global_list