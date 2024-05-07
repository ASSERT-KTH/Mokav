def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n <= 2):
	    global_list.append(n)
	elif ((n % 2) != 0):
	    global_list.append(((n * (n - 1)) * (n - 2)))
	elif ((n % 3) != 0):
	    global_list.append(((n * (n - 1)) * (n - 3)))
	elif ((n % 2) == 0):
	    global_list.append((((n - 1) * (n - 2)) * (n - 3)))
	return global_list