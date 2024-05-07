def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n <= 10):
	    global_list.append('0')
	elif (n <= 19):
	    global_list.append('4')
	else:
	    global_list.append('15')
	return global_list