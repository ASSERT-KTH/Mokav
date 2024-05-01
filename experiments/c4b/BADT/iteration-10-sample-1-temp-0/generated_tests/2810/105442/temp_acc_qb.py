def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	v = (((n // 2) - 1) if ((n % 2) == 0) else (n // 2))
	global_list.append(v)
	return global_list