def original_func(*args):
	global_list = []
	
	(m, d) = map(int, args[0].split())
	if (m < 8):
	    if ((m % 2) != 0):
	        if (d < 6):
	            global_list.append('5')
	        else:
	            global_list.append('6')
	    elif (m == 28):
	        if (d < 3):
	            global_list.append('4')
	        else:
	            global_list.append('5')
	    elif (d < 7):
	        global_list.append('5')
	    else:
	        global_list.append('6')
	elif ((m % 2) != 0):
	    if (d < 7):
	        global_list.append('5')
	    else:
	        global_list.append('6')
	elif (d < 6):
	    global_list.append('5')
	else:
	    global_list.append('6')
	return global_list