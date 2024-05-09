def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	x = ((3 * n) - k)
	if (x <= 0):
	    global_list.append('0')
	else:
	    global_list.append(x)
	return global_list