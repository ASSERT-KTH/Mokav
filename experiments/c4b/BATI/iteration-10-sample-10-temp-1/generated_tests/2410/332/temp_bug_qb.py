def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    global_list.append((3 ** (n - 1)))
	return global_list