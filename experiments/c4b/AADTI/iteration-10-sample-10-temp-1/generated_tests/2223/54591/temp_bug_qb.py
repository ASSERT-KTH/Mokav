def original_func(*args):
	global_list = []
	
	t = int(args[0])
	if ((t % 2) is 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list