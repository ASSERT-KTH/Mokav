def original_func(*args):
	global_list = []
	
	n = int(args[0])
	while ((n & 1) == 0):
	    n >>= 1
	global_list.append((n >> 1))
	return global_list