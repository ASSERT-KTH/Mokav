def original_func(*args):
	global_list = []
	
	(n, c1, c2, c3) = map(int, args[0].split())
	if ((n % 4) == 0):
	    global_list.append(0)
	elif ((n % 4) == 1):
	    global_list.append(min([c3, (c2 + c1), (c1 * 3)]))
	elif ((n % 4) == 2):
	    global_list.append(min([c2, (c2 * 2)]))
	else:
	    global_list.append(min([(c3 * 3), (c2 + c3), c1]))
	return global_list