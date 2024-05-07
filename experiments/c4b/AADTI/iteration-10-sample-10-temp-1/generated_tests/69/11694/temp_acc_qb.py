def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	cnt = ((n - 2) ** 2)
	global_list.append(cnt)
	return global_list