def patched_func(*args):
	global_list = []
	
	(a1, a2) = args[0].split()
	(a1, a2) = (int(a1), int(a2))
	if ((a1 == a2) and (a1 != 1)):
	    global_list.append(((a1 + a2) - 3))
	elif ((a1 == 1) and (a2 == 1)):
	    global_list.append(0)
	elif ((abs((a1 - a2)) % 3) == 0):
	    global_list.append(((a1 + a2) - 3))
	else:
	    global_list.append(((a1 + a2) - 2))
	return global_list