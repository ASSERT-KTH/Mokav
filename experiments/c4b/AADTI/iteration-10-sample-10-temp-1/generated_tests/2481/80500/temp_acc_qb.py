def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	i = 0
	while ((5 * (2 ** i)) < n):
	    n = (n - (5 * (2 ** i)))
	    i += 1
	if ((n / (5 * (2 ** i))) <= 0.2):
	    global_list.append('Sheldon')
	elif ((n / (5 * (2 ** i))) <= 0.4):
	    global_list.append('Leonard')
	elif ((n / (5 * (2 ** i))) <= 0.6):
	    global_list.append('Penny')
	elif ((n / (5 * (2 ** i))) <= 0.8):
	    global_list.append('Rajesh')
	else:
	    global_list.append('Howard')
	return global_list