def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n <= 10):
	    global_list.append('0')
	elif ((n >= 11) and (n <= 19)):
	    global_list.append('4')
	elif (n == 20):
	    global_list.append('15')
	elif (n == 21):
	    global_list.append('4')
	else:
	    global_list.append('0')
	return global_list