def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	cc = (c // 4)
	bb = (b // 2)
	global_list.append(((min(cc, bb, a) + (2 * min(a, bb, cc))) + (4 * min(a, bb, cc))))
	return global_list