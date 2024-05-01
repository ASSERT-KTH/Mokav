def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	c = 0
	while (x > 0):
	    d = (x % 8)
	    c += (d == 1)
	    x = (x // 8)
	global_list.append(c)
	return global_list