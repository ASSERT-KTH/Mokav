def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    global_list.append(int((((n / 2) - 1) / 2)))
	else:
	    global_list.append('0')
	return global_list