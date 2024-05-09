def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	x = 0
	if (a < 0):
	    exit(0)
	if (a < 13):
	    x = (2 ** a)
	    global_list.append(x)
	else:
	    x = (8092 * (2 ** (a - 13)))
	    global_list.append(x)
	return global_list