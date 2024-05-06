def original_func(*args):
	global_list = []
	
	n = (int(args[0]) - 10)
	if ((n >= 1) and (n <= 11)):
	    if (n == 1):
	        global_list.append('1')
	    elif (n == 10):
	        global_list.append('15')
	    elif (n == 11):
	        global_list.append('1')
	    else:
	        global_list.append('4')
	else:
	    global_list.append('0')
	return global_list