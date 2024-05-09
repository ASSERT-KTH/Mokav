def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	global_list.append(min(((a + b) + c), ((2 * a) + (2 * c)), ((2 * b) + (2 * c)), ((2 * a) + (2 * b))))
	return global_list