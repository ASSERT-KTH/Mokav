def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (1 <= n <= 2000):
	    s = (((n - 1) * (n - 1)) + n)
	    global_list.append(s)
	return global_list