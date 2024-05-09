def patched_func(*args):
	global_list = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if ((a + b) >= n):
	    if ((n - a) >= 0):
	        global_list.append((n - a))
	    else:
	        global_list.append(0)
	else:
	    global_list.append((b + 1))
	return global_list