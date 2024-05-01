def original_func(*args):
	global_list = []
	
	(t, s, x) = list(map(int, args[0].split()))
	if (x < t):
	    global_list.append('NO')
	else:
	    x -= t
	    if (((x % s) == 0) or ((x % s) == 1)):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	return global_list