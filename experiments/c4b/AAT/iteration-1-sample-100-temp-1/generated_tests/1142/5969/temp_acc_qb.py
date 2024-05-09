def patched_func(*args):
	global_list = []
	
	(n, a, b) = list(map(int, args[0].split()))
	if ((n - a) < (b + 1)):
	    global_list.append((n - a))
	else:
	    global_list.append((b + 1))
	return global_list