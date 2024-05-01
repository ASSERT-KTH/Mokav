def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(' '.join(map(str, ([n] + [(i + 1) for i in range((n - 1))]))))
	return global_list