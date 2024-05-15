def patched_func(*args):
	global_list = []
	
	w = int(args[0])
	if (w is 2):
	    global_list.append('NO')
	elif ((w % 2) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list