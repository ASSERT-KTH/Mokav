def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	if ((a % 2) == 0):
	    if (a == 2):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list