def patched_func(*args):
	global_list = []
	
	n = (int(args[0]) - 10)
	t = [2, 3, 4, 5, 6, 7, 8, 9, 10]
	if ((n < 1) or (n > 11)):
	    global_list.append(0)
	elif (n < 10):
	    global_list.append(4)
	elif (n == 11):
	    global_list.append(4)
	else:
	    global_list.append(15)
	return global_list