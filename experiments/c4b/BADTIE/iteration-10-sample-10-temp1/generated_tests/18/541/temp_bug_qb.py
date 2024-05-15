def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(((3 ** (3 * n)) - (7 ** n)))
	return global_list