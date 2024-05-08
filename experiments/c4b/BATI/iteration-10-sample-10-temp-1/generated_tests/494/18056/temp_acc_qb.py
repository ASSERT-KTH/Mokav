def patched_func(*args):
	global_list = []
	
	s = ''
	for i in range(1000):
	    s += str(i)
	n = int(args[0])
	global_list.append(s[n])
	return global_list