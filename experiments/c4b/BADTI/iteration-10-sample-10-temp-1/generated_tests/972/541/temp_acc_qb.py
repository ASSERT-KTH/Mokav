def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if ((abs((a - b)) <= 1) and (not ((b == 0) and (a == 0)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list