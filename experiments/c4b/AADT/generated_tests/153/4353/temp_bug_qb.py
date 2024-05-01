def original_func(*args):
	global_list = []
	
	n = int(args[0])
	r = 0
	i = 1
	while (((i * i) < n) and ((i * 4) < n)):
	    r += ((((n - i) - i) % 2) == 0)
	    i += 1
	global_list.append(r)
	return global_list