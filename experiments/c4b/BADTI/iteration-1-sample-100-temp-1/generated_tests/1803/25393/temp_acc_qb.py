def patched_func(*args):
	global_list = []
	
	m = int(args[0])
	if (m == 1):
	    global_list.append('1')
	elif (m == 2):
	    global_list.append('2')
	elif ((m % 2) == 0):
	    if ((m % 3) == 0):
	        ans = (((m - 1) * (m - 2)) * (m - 3))
	    else:
	        ans = ((m * (m - 1)) * (m - 3))
	    global_list.append(round(ans))
	else:
	    global_list.append(((m * (m - 1)) * (m - 2)))
	return global_list