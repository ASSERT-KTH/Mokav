def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = ((c // 4) * 4)
	x = ((d + (d // 2)) + (d // 4))
	global_list.append(x)
	return global_list