def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 2):
	    global_list.append(3)
	elif (n == 3):
	    global_list.append(5)
	elif (n == 4):
	    global_list.append(6)
	else:
	    global_list.append((3 + n))
	return global_list