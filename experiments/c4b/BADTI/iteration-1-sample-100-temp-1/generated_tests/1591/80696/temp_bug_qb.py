def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x <= 1):
	    global_list.append(1)
	elif (x <= 5):
	    global_list.append(3)
	elif (x <= 13):
	    global_list.append(5)
	elif (x <= 25):
	    global_list.append(7)
	elif (x <= 41):
	    global_list.append(9)
	elif (x <= 61):
	    global_list.append(11)
	elif (x <= 85):
	    global_list.append(13)
	else:
	    global_list.append(15)
	return global_list