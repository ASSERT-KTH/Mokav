def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (1 <= n <= 2000):
	    s = int((((n * ((n * n) - 1)) / 6) + n))
	    global_list.append(s)
	return global_list