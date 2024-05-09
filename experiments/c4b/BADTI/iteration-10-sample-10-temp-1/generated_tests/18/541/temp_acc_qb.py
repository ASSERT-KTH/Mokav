def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append((((3 ** (3 * n)) - (7 ** n)) % (int(1000000000.0) + 7)))
	return global_list