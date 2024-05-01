def patched_func(*args):
	global_list = []
	
	(n, a, b) = list(map(int, args[0].split()))
	if ((a >= 0) and (b >= 0)):
	    global_list.append(((b // n) - ((a - 1) // n)))
	elif ((a < 0) and (b < 0)):
	    global_list.append((((- a) // n) - (((- b) - 1) // n)))
	else:
	    global_list.append((((b // n) + ((- a) // n)) + 1))
	return global_list