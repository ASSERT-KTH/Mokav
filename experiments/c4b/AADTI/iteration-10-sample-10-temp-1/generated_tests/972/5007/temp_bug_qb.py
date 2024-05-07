def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if ((a - b) in {1, 0, (- 1)}):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list