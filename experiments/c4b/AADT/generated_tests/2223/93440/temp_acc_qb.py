def patched_func(*args):
	global_list = []
	
	w = int(args[0])
	if (((w % 2) == 0) and (w > 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list