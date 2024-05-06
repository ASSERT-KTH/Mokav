def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	y = (b // a)
	global_list.append((1 if (a == b) else (y + 1)))
	return global_list