def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ''
	while (((n - 3) >= 0) and ((n - 3) != 1)):
	    a += '7'
	    n -= 3
	while (n > 0):
	    n -= 2
	    a += '1'
	global_list.append(a)
	return global_list