def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if ((a != 0) or (b != 0)):
	    if (abs((a - b)) <= 1):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list