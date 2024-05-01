def patched_func(*args):
	global_list = []
	
	w = 0
	w = int(args[0])
	res = (w % 2)
	if ((res != 0) or (w <= 2)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list