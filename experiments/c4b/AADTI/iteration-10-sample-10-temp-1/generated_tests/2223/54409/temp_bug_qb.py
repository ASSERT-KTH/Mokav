def original_func(*args):
	global_list = []
	
	weight = int(args[0])
	if ((weight % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('No')
	return global_list