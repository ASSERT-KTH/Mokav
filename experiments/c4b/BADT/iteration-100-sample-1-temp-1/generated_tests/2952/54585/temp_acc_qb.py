def patched_func(*args):
	global_list = []
	
	(n, k) = args[0].split(' ')
	if (((int(n) // int(k)) % 2) == 0):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list