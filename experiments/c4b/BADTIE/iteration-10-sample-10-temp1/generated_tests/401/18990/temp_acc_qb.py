def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a < 13):
	    global_list.append((2 ** a))
	else:
	    start = 8092
	    for _ in range((a - 13)):
	        start *= 2
	    global_list.append(start)
	return global_list