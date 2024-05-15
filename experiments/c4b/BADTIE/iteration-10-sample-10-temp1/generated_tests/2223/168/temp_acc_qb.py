def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n < 4):
	    global_list.append('NO')
	elif ((n % 2) != 0):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list