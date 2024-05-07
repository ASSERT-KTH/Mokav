def patched_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	l = (a // k)
	p = (b // k)
	if (l == 0):
	    if ((b % k) == 0):
	        if ((l + p) != 0):
	            global_list.append((l + p))
	        else:
	            global_list.append('-1')
	    else:
	        global_list.append('-1')
	elif (p == 0):
	    if ((a % k) == 0):
	        if ((l + p) != 0):
	            global_list.append((l + p))
	        else:
	            global_list.append('-1')
	    else:
	        global_list.append('-1')
	else:
	    global_list.append((l + p))
	return global_list