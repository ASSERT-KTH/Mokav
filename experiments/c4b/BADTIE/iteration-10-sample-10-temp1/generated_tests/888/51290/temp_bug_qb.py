def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	i = (a * 2)
	z = (a * 4)
	while ((i > b) and (z > c)):
	    a = (a - 1)
	global_list.append((a * 7))
	return global_list