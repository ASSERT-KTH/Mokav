def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	y = 1
	if (x >= 13):
	    y = 8092
	    x -= 13
	global_list.append((y << x))
	return global_list