def original_func(*args):
	global_list = []
	
	'input\n2\n'
	n = int(args[0])
	global_list.append((n * ((2 ** n) - 1)))
	return global_list