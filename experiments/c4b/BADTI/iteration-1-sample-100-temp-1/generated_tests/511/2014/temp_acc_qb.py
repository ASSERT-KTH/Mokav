def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	if (c == 0):
	    if (a == b):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif ((((b - a) % c) == 0) and ((((b - a) // c) + 1) > 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list