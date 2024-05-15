def original_func(*args):
	global_list = []
	
	(n, x, y) = (int(x) for x in args[0].split())
	global_list.append((- (((100 * x) - (n * y)) // 100)))
	return global_list