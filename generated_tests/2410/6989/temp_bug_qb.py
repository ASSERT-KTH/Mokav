def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n < 1):
	    global_list.append(0)
	else:
	    global_list.append(((3 ** (n - 1)) % 1000003))
	return global_list