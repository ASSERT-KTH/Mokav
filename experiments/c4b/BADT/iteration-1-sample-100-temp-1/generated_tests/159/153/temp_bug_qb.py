def original_func(*args):
	global_list = []
	
	(n, m, s) = args[0].split()
	n = int(n)
	if (s == 'month'):
	    if (n == 31):
	        global_list.append(7)
	    elif ((n < 31) and (n > 28)):
	        global_list.append(11)
	    else:
	        global_list.append(12)
	elif ((n == 5) or (n == 6)):
	    global_list.append(53)
	else:
	    global_list.append(52)
	return global_list