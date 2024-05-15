def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	if (a > 400):
	    global_list.append(0)
	else:
	    global_list.append((7 * min(a, (b // 2), (c // 4))))
	return global_list