def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	n -= a
	if (n > b):
	    global_list.append((b + a))
	else:
	    global_list.append(n)
	return global_list