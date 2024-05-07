def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = a
	for i in range(a):
	    if (((d * 2) <= b) and ((d * 4) <= c)):
	        f = (d * 2)
	        e = (d * 4)
	        global_list.append(((d + f) + e))
	        break
	    d = (a - 1)
	if (((b < 2) and (c < 4)) or (b < 2) or (c < 4)):
	    global_list.append(0)
	return global_list