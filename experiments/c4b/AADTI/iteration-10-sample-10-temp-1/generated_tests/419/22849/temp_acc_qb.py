def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	if ((((a + b) % n) % n) == 0):
	    global_list.append(n)
	else:
	    global_list.append((((a + b) % n) % n))
	return global_list