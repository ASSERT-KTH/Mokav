def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	x = 0
	for j in range(2, n):
	    x = (x + ((n - j) * j))
	global_list.append((((x + n) - 1) + n))
	return global_list