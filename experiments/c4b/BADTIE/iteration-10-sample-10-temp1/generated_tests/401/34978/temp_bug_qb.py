def original_func(*args):
	global_list = []
	
	a = args[0]
	global_list.append((2 ** int(a)))
	return global_list