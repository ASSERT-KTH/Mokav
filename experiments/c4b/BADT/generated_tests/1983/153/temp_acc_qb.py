def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	l = 0
	for i in range(1, n):
	    l += (i * (n - i))
	global_list.append((l + n))
	return global_list