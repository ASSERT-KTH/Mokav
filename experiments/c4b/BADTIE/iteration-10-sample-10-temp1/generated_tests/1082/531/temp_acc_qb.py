def patched_func(*args):
	global_list = []
	
	'input\n3\n8\n'
	(k, l) = (int(args[0]), int(args[1]))
	for x in range(1, 100):
	    if ((k ** x) == l):
	        global_list.append('YES')
	        global_list.append((x - 1))
	        break
	else:
	    global_list.append('NO')
	return global_list