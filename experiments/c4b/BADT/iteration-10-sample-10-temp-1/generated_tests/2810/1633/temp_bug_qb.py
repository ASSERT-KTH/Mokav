def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ((n // 2) - 1)
	if ((n % 2) == 1):
	    a += 2
	global_list.append(a)
	return global_list