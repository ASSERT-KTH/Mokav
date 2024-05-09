def patched_func(*args):
	global_list = []
	
	(m, n) = [int(x) for x in args[0].split()]
	global_list.append(((m * n) // 2))
	return global_list