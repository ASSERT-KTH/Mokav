def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x < 3):
	    global_list.append(1)
	else:
	    global_list.append((('1' * (x - 2)) + '7'))
	return global_list