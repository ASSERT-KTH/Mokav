def original_func(*args):
	global_list = []
	
	x = args[0]
	if ((x[0] == 'a') and (x[1] == '8')):
	    global_list.append(3)
	elif ((x[0] == 'a') and (x[1] == '1')):
	    global_list.append(3)
	elif ((x[0] == 'h') and (x[1] == '8')):
	    global_list.append(3)
	elif ((x[0] == 'h') and (x[1] == '1')):
	    global_list.append(3)
	elif (x[0] == 'h'):
	    global_list.append(5)
	elif (x[0] == 'a'):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list