def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	if ((n % 2) == 0):
	    s += ((n // 2) * '1')
	else:
	    s += '7'
	    s += (((n - 3) // 2) * '1')
	global_list.append(int(s))
	return global_list