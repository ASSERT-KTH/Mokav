def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((- 1) if (n < 3) else (210 * (((10 ** (n - 1)) // 210) + 1))))
	return global_list