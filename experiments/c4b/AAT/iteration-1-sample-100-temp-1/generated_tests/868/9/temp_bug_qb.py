def original_func(*args):
	global_list = []
	
	N = int(args[0])
	if ((N % 4) == 1):
	    global_list.append(8)
	elif ((N % 4) == 2):
	    global_list.append(4)
	elif ((N % 4) == 3):
	    global_list.append(2)
	elif ((N % 4) == 0):
	    global_list.append(6)
	return global_list