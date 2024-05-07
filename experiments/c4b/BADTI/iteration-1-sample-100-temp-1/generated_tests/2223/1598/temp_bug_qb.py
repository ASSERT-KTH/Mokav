def original_func(*args):
	global_list = []
	
	n = args[0]
	if (((int(n) % 2) == 1) or (int(n) >= 2)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list