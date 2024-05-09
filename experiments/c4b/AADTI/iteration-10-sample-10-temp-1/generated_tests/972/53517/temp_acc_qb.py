def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if ((a == b) and (a == 0)):
	    global_list.append('NO')
	else:
	    global_list.append(('YES' if (abs((a - b)) <= 1) else 'NO'))
	return global_list