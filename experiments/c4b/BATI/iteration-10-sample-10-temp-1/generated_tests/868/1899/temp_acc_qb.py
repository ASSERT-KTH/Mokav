def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = (n % 4)
	if (n == 0):
	    global_list.append(1)
	elif (ans == 1):
	    global_list.append(8)
	elif (ans == 2):
	    global_list.append(4)
	elif (ans == 3):
	    global_list.append(2)
	else:
	    global_list.append(6)
	return global_list