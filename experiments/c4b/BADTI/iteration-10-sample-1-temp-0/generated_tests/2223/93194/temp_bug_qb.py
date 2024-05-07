def original_func(*args):
	global_list = []
	
	if ((int(args[0]) % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list