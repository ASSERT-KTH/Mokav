def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 4) == 0):
	    global_list.append(6)
	elif ((n % 4) == 1):
	    global_list.append(8)
	elif ((n % 4) == 2):
	    global_list.append(4)
	else:
	    global_list.append(2)
	return global_list