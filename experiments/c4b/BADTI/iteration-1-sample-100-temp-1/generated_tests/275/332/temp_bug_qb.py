def original_func(*args):
	global_list = []
	
	n = args[0]
	t = ((((n[0] + n[2]) + n[4]) + n[3]) + n[1])
	t = int(t)
	k = t
	for i in range(2):
	    t = ((t ** 2) % (10 ** 5))
	global_list.append(((k * t) % (10 ** 5)))
	return global_list