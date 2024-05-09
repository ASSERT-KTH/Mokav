def patched_func(*args):
	global_list = []
	
	(a, b, r) = map(int, args[0].split())
	global_list.append(('Second' if ((a < (2 * r)) or (b < (2 * r))) else 'First'))
	return global_list