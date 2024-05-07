def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n <= 10) or (n >= 22)):
	    global_list.append('0')
	elif ((n <= 19) or (n == 21)):
	    global_list.append('4')
	else:
	    global_list.append('15')
	return global_list