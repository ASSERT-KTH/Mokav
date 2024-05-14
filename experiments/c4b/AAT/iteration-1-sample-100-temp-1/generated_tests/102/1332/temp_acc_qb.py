def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	global_list.append(min((2 * min(((a + b), (b + c), (c + a)))), ((a + b) + c)))
	return global_list