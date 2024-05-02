def original_func(*args):
	global_list = []
	
	(a, b, r) = map(int, args[0].split())
	global_list.append(('Second' if ((((((a // (4 * r)) + ((a % (4 * r)) // (2 * r))) if (a >= (4 * r)) else (a // (2 * r))) * (((b // (4 * r)) + ((b % (4 * r)) // (2 * r))) if (b >= (4 * r)) else (b // (2 * r)))) % 2) == 0) else 'First'))
	return global_list