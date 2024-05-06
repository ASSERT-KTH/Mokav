def original_func(*args):
	global_list = []
	
	(k, a, b) = [int(i) for i in args[0].split()]
	res = ((a // k) + (b // k))
	if (res == 0):
	    global_list.append((- 1))
	else:
	    global_list.append(res)
	return global_list