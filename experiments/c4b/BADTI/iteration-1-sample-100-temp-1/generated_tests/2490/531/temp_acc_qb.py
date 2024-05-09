def patched_func(*args):
	global_list = []
	
	'input\n4\n'
	n = int(args[0])
	global_list.append(min(((3 * n) // 2), ((2 * n) - 1)))
	return global_list