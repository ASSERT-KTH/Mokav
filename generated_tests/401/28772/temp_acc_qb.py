def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n < 13):
	    global_list.append((2 ** n))
	else:
	    global_list.append((8092 * (2 ** (n - 13))))
	return global_list