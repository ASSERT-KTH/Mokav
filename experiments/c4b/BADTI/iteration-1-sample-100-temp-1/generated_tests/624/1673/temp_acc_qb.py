def patched_func(*args):
	global_list = []
	
	(t, s, x) = map(int, args[0].split())
	if (x >= t):
	    if ((t + s) <= x):
	        y1 = ((x - t) / s)
	        y2 = (((x - t) - 1) / s)
	        if (int(y1) == y1):
	            global_list.append('YES')
	        elif (int(y2) == y2):
	            global_list.append('YES')
	        else:
	            global_list.append('NO')
	    elif (x == t):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list