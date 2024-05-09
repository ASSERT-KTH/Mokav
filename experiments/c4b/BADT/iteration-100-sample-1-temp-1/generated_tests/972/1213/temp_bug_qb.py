def original_func(*args):
	global_list = []
	
	(a, b) = args[0].split()
	(a, b) = (int(a), int(b))
	if (abs((a - b)) < 2):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list