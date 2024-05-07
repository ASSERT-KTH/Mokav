def patched_func(*args):
	global_list = []
	
	s = ''
	for i in range(1, 1001):
	    s += str(i)
	n = int(args[0])
	global_list.append(s[(n - 1)])
	return global_list