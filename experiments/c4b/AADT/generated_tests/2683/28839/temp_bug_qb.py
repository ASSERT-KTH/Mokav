def original_func(*args):
	global_list = []
	
	(a, b, c, d) = (int(args[0]), int(args[1]), int(args[2]), int(args[3]))
	e = ((a or b) and (c ^ d))
	f = ((b and c) ^ (a or d))
	global_list.append((e or f))
	return global_list