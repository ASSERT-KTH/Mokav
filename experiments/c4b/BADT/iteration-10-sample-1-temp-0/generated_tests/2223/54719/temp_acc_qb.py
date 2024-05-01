def patched_func(*args):
	global_list = []
	
	weight = int(args[0])
	if (((weight % 2) == 0) and (weight > 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list