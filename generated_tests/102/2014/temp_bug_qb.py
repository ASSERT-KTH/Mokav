def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	a = (((d1 + d1) + d2) + d2)
	c = ((d1 + d3) + d2)
	if (a > c):
	    global_list.append(c)
	else:
	    global_list.append(a)
	return global_list