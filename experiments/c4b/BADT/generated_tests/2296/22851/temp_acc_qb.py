def patched_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split(' '))
	global_list.append(((m * n) // 2))
	return global_list