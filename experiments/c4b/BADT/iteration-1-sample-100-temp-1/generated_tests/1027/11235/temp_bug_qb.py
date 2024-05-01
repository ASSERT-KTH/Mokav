def original_func(*args):
	global_list = []
	
	a = int(args[0])
	if ((a <= 10) or (a > 20)):
	    global_list.append(0)
	elif (a == 20):
	    global_list.append(15)
	else:
	    global_list.append(4)
	return global_list