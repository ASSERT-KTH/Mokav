def original_func(*args):
	global_list = []
	
	mass = eval(args[0])
	if ((mass % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list