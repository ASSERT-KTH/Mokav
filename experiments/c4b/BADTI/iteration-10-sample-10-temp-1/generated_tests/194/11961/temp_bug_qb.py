def original_func(*args):
	global_list = []
	
	'input\n\n12\n\n'
	n = int(args[0])
	global_list.append((int(((n / 5) + 0.5)) + (1 if (n % 5) else 0)))
	return global_list