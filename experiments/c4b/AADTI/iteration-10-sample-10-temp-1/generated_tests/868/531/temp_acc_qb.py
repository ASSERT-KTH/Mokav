def patched_func(*args):
	global_list = []
	
	'input\n0\n'
	n = int(args[0])
	global_list.append(([8, 4, 2, 6][((n % 4) - 1)] if (n != 0) else 1))
	return global_list