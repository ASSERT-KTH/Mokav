def original_func(*args):
	global_list = []
	
	s = args[0]
	if ((len(s) == 7) or (len(s) == 4)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list