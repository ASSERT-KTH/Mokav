def original_func(*args):
	global_list = []
	
	(a, b, ab) = map(int, args[0].split())
	global_list.append(min(((a + b) + ab), (((a + a) + b) + b)))
	return global_list