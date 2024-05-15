def original_func(*args):
	global_list = []
	
	'input\n2\n'
	global_list.append([8, 4, 2, 6][((int(args[0]) % 4) - 1)])
	return global_list