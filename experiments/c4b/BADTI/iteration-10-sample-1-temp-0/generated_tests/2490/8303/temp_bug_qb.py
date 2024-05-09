def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = n
	while ((n % 2) == 0):
	    n //= 2
	    s += n
	global_list.append(s)
	return global_list