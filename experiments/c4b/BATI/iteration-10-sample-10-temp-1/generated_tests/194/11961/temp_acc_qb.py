def patched_func(*args):
	global_list = []
	
	'input\n\n5\n\n'
	n = int(args[0])
	global_list.append(((n // 5) + (1 if (n % 5) else 0)))
	return global_list