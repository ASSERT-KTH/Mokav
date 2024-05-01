def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list