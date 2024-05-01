def original_func(*args):
	global_list = []
	
	num = set(list(args[0]))
	if (num == {'4', '7'}):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list