def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	global_list.append(min(0, ((((- a) * c) / 100) + b)))
	return global_list