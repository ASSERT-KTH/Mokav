def original_func(*args):
	global_list = []
	
	(n, k) = args[0].split(' ')
	result = (int(n) / int(k))
	if ((int(result) % 2) == 0):
	    global_list.append('NO')
	else:
	    global_list.append('Yes')
	return global_list