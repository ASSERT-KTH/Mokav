def patched_func(*args):
	global_list = []
	
	'input\n1\n'
	n = int(args[0])
	global_list.append((2 * ((2 ** n) - 1)))
	return global_list