def patched_func(*args):
	global_list = []
	
	(t, s, x) = map(int, args[0].split())
	if (x < t):
	    global_list.append('NO')
	elif ((((x - t) % s) == 0) or ((((x - 1) - t) % s) == 0)):
	    if (x == (t + 1)):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list