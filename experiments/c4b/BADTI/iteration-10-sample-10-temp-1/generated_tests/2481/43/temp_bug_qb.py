def original_func(*args):
	global_list = []
	
	n = int(args[0])
	c = 1
	while ((c * 5) < n):
	    n -= (c * 5)
	    global_list.append('n ', n)
	    c *= 2
	    global_list.append('C ', c)
	if (((n - 1) / c) == 0):
	    global_list.append('Sheldon')
	if (((n - 1) / c) == 1):
	    global_list.append('Leonard')
	if (((n - 1) / c) == 2):
	    global_list.append('Penny')
	if (((n - 1) / c) == 3):
	    global_list.append('Rajesh')
	if (((n - 1) / c) == 4):
	    global_list.append('Howard')
	return global_list