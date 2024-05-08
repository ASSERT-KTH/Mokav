def original_func(*args):
	global_list = []
	
	(n, m, a) = [int(x) for x in args[0].split()]
	r = int(((n / a) + 0.5))
	c = int(((m / a) + 0.5))
	global_list.append(((r * c) if ((r * c) > 0) else 1))
	return global_list