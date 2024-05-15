def original_func(*args):
	global_list = []
	
	n = int(args[0])
	q = 2
	r = (n + 2)
	if ((n % 2) == 0):
	    global_list.append(((n // 2) - 1))
	else:
	    global_list.append(((n // 2) + 1))
	return global_list