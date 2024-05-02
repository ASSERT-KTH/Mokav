def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if (n > m):
	    a = (n - m)
	else:
	    a = (m - n)
	if (a > 1):
	    global_list.append('NO')
	elif (a == 0):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list