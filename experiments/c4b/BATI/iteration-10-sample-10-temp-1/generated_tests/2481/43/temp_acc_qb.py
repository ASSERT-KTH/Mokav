def patched_func(*args):
	global_list = []
	
	from math import floor
	n = int(args[0])
	c = 1
	while ((c * 5) < n):
	    n -= (c * 5)
	    c *= 2
	exp = floor(((n - 1) / c))
	if (exp == 0):
	    global_list.append('Sheldon')
	if (exp == 1):
	    global_list.append('Leonard')
	if (exp == 2):
	    global_list.append('Penny')
	if (exp == 3):
	    global_list.append('Rajesh')
	if (exp == 4):
	    global_list.append('Howard')
	return global_list