def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	r = (max(n, m) - 1)
	g = (6 - r)
	if ((6 % g) == 0):
	    global_list.append((('1' + '/') + str((6 // g))))
	else:
	    global_list.append(((str(g) + '/') + '6'))
	return global_list