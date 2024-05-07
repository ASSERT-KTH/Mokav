def patched_func(*args):
	global_list = []
	
	(m, n) = map(int, args[0].split())
	if ((m == 1) and ((n % 2) == 0)):
	    global_list.append(int((n / 2)))
	elif (((m % 2) == 0) and (n == 1)):
	    global_list.append(int((m / 2)))
	elif (((m % 2) == 0) or ((n % 2) == 0)):
	    global_list.append(int(((m * n) / 2)))
	elif (((m % 2) != 0) and ((n % 2) != 0)):
	    global_list.append(int((((m * n) - 1) / 2)))
	return global_list