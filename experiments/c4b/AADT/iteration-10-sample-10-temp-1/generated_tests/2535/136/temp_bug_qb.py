def original_func(*args):
	global_list = []
	
	(n, m) = [int(i) for i in args[0].split()]
	d = 0
	for i in range((n + 1)):
	    d = (d + i)
	c = (d - m)
	if (c < 0):
	    global_list.append(0)
	else:
	    global_list.append(c)
	return global_list