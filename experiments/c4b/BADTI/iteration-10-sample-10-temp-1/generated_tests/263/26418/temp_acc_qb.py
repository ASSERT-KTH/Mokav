def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	tot = 0
	for i in range(1, (n + 1)):
	    tot += (2 ** i)
	global_list.append(tot)
	return global_list