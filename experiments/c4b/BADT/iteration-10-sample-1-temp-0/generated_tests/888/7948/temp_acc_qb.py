def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	count = 0
	while ((a > 0) and (b > 0) and (c > 0)):
	    a -= 1
	    b -= 2
	    c -= 4
	    if ((a >= 0) and (b >= 0) and (c >= 0)):
	        count += 7
	global_list.append(count)
	return global_list