def original_func(*args):
	global_list = []
	
	(n, a) = [int(x) for x in args[0].split()]
	if (n & 1):
	    global_list.append(((n // 2) + 1))
	else:
	    global_list.append((((n - a) // 2) + 1))
	return global_list