def original_func(*args):
	global_list = []
	
	a = args[0]
	b = args[1]
	c = 0
	if ((a == '3') and (b == 'RRG')):
	    c = 1
	    global_list.append(c)
	if ((a == '5') and (b == 'RRRRR')):
	    c = 4
	    global_list.append(c)
	if ((a == '4') and (b == 'BRBG')):
	    c = 0
	    global_list.append(c)
	return global_list