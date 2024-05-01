def patched_func(*args):
	global_list = []
	
	n = eval(args[0])
	if ((n % 2) == 0):
	    global_list.append(int(((n / 2) - 1)))
	else:
	    global_list.append(int((n / 2)))
	return global_list