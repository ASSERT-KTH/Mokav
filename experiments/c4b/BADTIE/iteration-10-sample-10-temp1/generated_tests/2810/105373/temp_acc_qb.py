def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    global_list.append(((n // 2) - 1))
	else:
	    global_list.append(((n - 1) // 2))
	return global_list