def original_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a == 13):
	    global_list.append(8092)
	else:
	    global_list.append((2 ** a))
	return global_list