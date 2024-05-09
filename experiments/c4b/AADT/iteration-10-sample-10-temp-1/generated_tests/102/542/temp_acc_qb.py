def patched_func(*args):
	global_list = []
	
	(a, b, c) = sorted(list(map(int, args[0].split())))
	global_list.append(min(((a + b) << 1), ((a + b) + c)))
	return global_list