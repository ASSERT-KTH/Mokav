def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if (((max(n, m) - min(n, m)) in {0, 1}) and (n != 0) and (m != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list