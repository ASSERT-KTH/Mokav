def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ''
	if ((n % 2) and (n >= 3)):
	    n -= 3
	    a += '7'
	while (n > 0):
	    n -= 2
	    a += '1'
	global_list.append(a)
	return global_list