def patched_func(*args):
	global_list = []
	
	L = [int(s) for s in args[0].split()]
	(k, a, b) = (L[0], L[1], L[2])
	if (((b - a) % k) == 0):
	    if ((a % k) == 0):
	        global_list.append((((b - a) + k) // k))
	    else:
	        global_list.append(((b - a) // k))
	elif ((a % k) == 0):
	    global_list.append((((b // k) - (a // k)) + 1))
	elif ((b % k) == 0):
	    global_list.append(((b // k) - (a // k)))
	else:
	    global_list.append(((b // k) - (a // k)))
	return global_list