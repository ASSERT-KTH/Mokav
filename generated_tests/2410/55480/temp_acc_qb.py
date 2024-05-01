def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((pow(3, (n - 1), 1000003) if n else 1))
	return global_list