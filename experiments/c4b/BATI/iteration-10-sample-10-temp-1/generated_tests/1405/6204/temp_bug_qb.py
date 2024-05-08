def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ['', 2, 3, 1, 2, 3]
	global_list.append(a[n])
	return global_list