def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	n -= a
	if ((n > b) and ((b - n) > 0)):
	    global_list.append(b)
	else:
	    global_list.append(n)
	return global_list