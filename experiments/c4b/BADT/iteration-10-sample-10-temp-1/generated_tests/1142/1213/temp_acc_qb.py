def patched_func(*args):
	global_list = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if ((n - a) > (b + 1)):
	    global_list.append((b + 1))
	else:
	    global_list.append((n - a))
	return global_list