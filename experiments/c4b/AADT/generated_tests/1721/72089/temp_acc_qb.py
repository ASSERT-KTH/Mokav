def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	for i in range(1, n):
	    s += (str(i) + ' ')
	s = ((str(n) + ' ') + s)
	global_list.append(s)
	return global_list