def original_func(*args):
	global_list = []
	
	n = (int(args[0]) % 4)
	if (n == 2):
	    global_list.append(4)
	elif (n == 3):
	    global_list.append(2)
	elif (n == 0):
	    global_list.append(6)
	else:
	    global_list.append(8)
	return global_list