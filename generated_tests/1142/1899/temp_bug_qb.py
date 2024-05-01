def original_func(*args):
	global_list = []
	
	(n, a, b) = [int(i) for i in args[0].split()]
	global_list.append(((n - a) - ((n - (n - b)) - 1)))
	return global_list