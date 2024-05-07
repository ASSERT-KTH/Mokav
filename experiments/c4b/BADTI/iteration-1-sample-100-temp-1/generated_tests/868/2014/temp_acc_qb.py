def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    global_list.append([6, 8, 4, 2][(n % 4)])
	return global_list