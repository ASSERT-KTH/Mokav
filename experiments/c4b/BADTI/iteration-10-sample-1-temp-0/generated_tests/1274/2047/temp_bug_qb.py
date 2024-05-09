def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	i = 0
	x = 0
	if ((k == 1) or (l == 1) or (m == 1) or (n == 1)):
	    x = d
	else:
	    while (i <= (d - 1)):
	        if ((i % k) == 0):
	            x += 1
	        elif ((i % l) == 0):
	            x += 1
	        elif ((i % m) == 0):
	            x += 1
	        elif ((i % n) == 0):
	            x += 1
	        i += 1
	global_list.append(x)
	return global_list