def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	z = (min(a, (b // 2), (c // 4)) * 7)
	global_list.append(z)
	return global_list