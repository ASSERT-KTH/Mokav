def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	n -= a
	if (n > (b + 1)):
	    global_list.append((b + 1))
	else:
	    global_list.append(n)
	return global_list