def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	if ((n % 4) == 1):
	    global_list.append(8)
	if ((n % 4) == 2):
	    global_list.append(4)
	if ((n % 4) == 3):
	    global_list.append(2)
	if (((n % 4) == 0) and (n != 0)):
	    global_list.append(6)
	return global_list