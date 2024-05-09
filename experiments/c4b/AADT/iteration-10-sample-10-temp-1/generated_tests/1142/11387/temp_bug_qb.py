def original_func(*args):
	global_list = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	global_list.append((n - a))
	return global_list