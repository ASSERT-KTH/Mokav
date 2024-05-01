def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = 'aabc'
	s = ''
	for i in range(n):
	    s += a[(i % 4)]
	global_list.append(s)
	return global_list