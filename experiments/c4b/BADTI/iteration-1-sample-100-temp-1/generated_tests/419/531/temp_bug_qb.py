def original_func(*args):
	global_list = []
	
	'input\n3 2 7\n'
	(n, a, b) = map(int, args[0].split())
	global_list.append((a + (b % n)))
	return global_list