def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n > 5) and ((n % 5) != 0)):
	    global_list.append(int(((n / 5) + 1)))
	elif (n <= 5):
	    global_list.append('1')
	else:
	    global_list.append(int((n / 5)))
	return global_list