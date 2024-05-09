def original_func(*args):
	global_list = []
	
	(d1, d2, d3) = map(int, args[0].split())
	if (d1 < d2):
	    if (((2 * d1) + d2) < d3):
	        global_list.append(((2 * d1) + (2 * d2)))
	    else:
	        global_list.append(((d1 + d2) + d3))
	elif (((2 * d2) + d1) < d3):
	    global_list.append(((2 * d2) + (2 * d1)))
	else:
	    global_list.append(((d1 + d2) + d3))
	return global_list