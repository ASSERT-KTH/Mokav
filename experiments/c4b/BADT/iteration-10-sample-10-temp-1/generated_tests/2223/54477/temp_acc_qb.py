def patched_func(*args):
	global_list = []
	
	a = args[0]
	a = int(a)
	if (((a % 2) == 0) and (a != 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list