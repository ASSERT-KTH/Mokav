def patched_func(*args):
	global_list = []
	
	m = int(args[0])
	if ((m % 2) | (m < 3)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list