def patched_func(*args):
	global_list = []
	
	(n, a, b) = [int(x) for x in args[0].split()]
	if ((b + 1) < (n - a)):
	    global_list.append((b + 1))
	else:
	    global_list.append((n - a))
	return global_list