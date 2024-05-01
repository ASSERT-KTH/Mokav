def original_func(*args):
	global_list = []
	
	(m, d) = list(map(int, args[0].split()))
	if ((m == 2) and (d == 1)):
	    global_list.append(4)
	elif (m == 2):
	    global_list.append(5)
	elif ((d == 5) or (d == 6) or (d == 1)):
	    global_list.append(5)
	else:
	    global_list.append(6)
	return global_list