def patched_func(*args):
	global_list = []
	
	(x1, x2, x3) = map(int, args[0].split())
	global_list.append((max(x1, x2, x3) - min(x1, x2, x3)))
	return global_list