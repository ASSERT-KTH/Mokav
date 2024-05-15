def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if (n == m):
	    global_list.append('YES')
	elif (((n + 1) == m) or ((n - 1) == m)):
	    global_list.append('YES')
	elif ((n == 0) and (m == 0)):
	    global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list