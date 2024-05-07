def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	elif (((n - 1) % 4) == 0):
	    global_list.append(8)
	elif (((n - 2) % 4) == 0):
	    global_list.append(4)
	elif (((n - 3) % 4) == 0):
	    global_list.append(2)
	elif (((n - 4) % 4) == 0):
	    global_list.append(6)
	return global_list