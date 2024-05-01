def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(' '.join(map(str, ([(i + 2) for i in range((n - 1))] + [1]))))
	return global_list