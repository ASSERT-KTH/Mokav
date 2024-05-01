def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	l = min(a, (b // 2), (c // 4))
	global_list.append(l, (l * 2), (l * 4))
	return global_list