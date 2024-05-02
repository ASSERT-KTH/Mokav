def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if (abs((a - b)) > 1):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list