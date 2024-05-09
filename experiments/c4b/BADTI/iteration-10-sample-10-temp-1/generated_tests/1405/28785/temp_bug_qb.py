def original_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a == 1):
	    global_list.append(2)
	if (a == 3):
	    global_list.append(3)
	if (a == 2):
	    global_list.append(1)
	if (a == 4):
	    global_list.append(2)
	if (a == 5):
	    global_list.append(1)
	return global_list