def patched_func(*args):
	global_list = []
	
	(a, b, c, d) = (int(args[0]), int(args[1]), int(args[2]), int(args[3]))
	e = ((a ^ b) and (c or d))
	f = ((b and c) or (a ^ d))
	global_list.append((e ^ f))
	return global_list