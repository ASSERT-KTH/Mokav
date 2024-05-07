def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if (abs((a - b)) <= 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list