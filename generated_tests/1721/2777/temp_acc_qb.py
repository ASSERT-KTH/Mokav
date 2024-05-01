def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(' '.join(([str(n)] + [str(i) for i in range(1, n)])))
	return global_list