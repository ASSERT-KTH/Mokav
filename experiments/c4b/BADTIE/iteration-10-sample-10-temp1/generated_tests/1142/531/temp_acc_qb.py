def patched_func(*args):
	global_list = []
	
	'input\n9 4 3\n'
	(n, a, b) = map(int, args[0].split())
	global_list.append(min((n - a), (b + 1)))
	return global_list