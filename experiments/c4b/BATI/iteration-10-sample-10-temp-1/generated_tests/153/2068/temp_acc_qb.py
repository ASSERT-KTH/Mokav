def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 4) and ((n % 2) == 0)):
	    global_list.append(int((n / 4)))
	elif ((n % 2) == 0):
	    global_list.append((int((n / 4)) - 1))
	else:
	    global_list.append(0)
	return global_list