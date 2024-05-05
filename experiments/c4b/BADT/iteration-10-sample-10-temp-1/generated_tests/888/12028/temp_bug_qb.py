def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	while ((a * 4) > c):
	    a = (a - 1)
	global_list.append(((a + (a * 2)) + (a * 4)))
	return global_list