def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (n % 10)
	if (a == 0):
	    global_list.append(1)
	elif ((a == 1) or (a == 5) or (a == 9)):
	    global_list.append(8)
	elif ((a == 2) or (a == 6)):
	    global_list.append(4)
	elif ((a == 3) or (a == 7)):
	    global_list.append(2)
	elif ((a == 4) or (a == 8)):
	    global_list.append(6)
	return global_list