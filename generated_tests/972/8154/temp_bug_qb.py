def original_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split())
	if (abs((x - y)) > 1):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list