def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	for i in range(2, (n + 1)):
	    s += (str(i) + ' ')
	s += '1'
	global_list.append(s)
	return global_list