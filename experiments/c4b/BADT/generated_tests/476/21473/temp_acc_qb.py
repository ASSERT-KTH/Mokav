def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	res = ((2 * (n // 3)) + ((n % 3) > 0))
	global_list.append(res)
	return global_list