def patched_func(*args):
	global_list = []
	
	(a, b) = (int(args[0]), int(args[1]))
	n = 0
	temp = a
	while (a < b):
	    a *= temp
	    n += 1
	if (a == b):
	    global_list.append('YES')
	    global_list.append(n)
	else:
	    global_list.append('NO')
	return global_list