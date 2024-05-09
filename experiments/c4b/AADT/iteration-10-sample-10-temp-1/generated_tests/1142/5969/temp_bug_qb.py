def original_func(*args):
	global_list = []
	
	(n, a, b) = list(map(int, args[0].split()))
	if ((a - a) < (b + 1)):
	    global_list.append((n - a))
	else:
	    global_list.append((b + 1))
	return global_list