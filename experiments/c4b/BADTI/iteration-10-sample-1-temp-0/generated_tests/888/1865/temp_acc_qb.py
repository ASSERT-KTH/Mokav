def patched_func(*args):
	global_list = []
	
	i = (lambda : int(args[0]))
	a = i()
	b = i()
	c = i()
	global_list.append((min(a, (b // 2), (c // 4)) * 7))
	return global_list