def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(' '.join([str(i) for i in range(n, 0, (- 1))]))
	return global_list