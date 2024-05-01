def patched_func(*args):
	global_list = []
	
	'input\n3 2 -100\n'
	(n, a, b) = map(int, args[0].split())
	global_list.append(((a + (b % n)) if ((a + (b % n)) <= n) else ((a + (b % n)) % n)))
	return global_list