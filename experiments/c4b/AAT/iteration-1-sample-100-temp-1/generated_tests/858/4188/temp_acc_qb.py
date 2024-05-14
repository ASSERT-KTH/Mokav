def patched_func(*args):
	global_list = []
	
	(n, a, b, c) = [int(x) for x in args[0].split()]
	if ((n % 4) == 0):
	    global_list.append(0)
	elif ((n % 4) == 3):
	    global_list.append(min(a, (b + c), (c * 3)))
	elif ((n % 4) == 2):
	    global_list.append(min((a * 2), b, (c * 2)))
	else:
	    global_list.append(min((a * 3), (b + a), c))
	return global_list