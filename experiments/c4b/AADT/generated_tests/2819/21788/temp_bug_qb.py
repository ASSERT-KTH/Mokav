def original_func(*args):
	global_list = []
	
	(l, r) = map(int, args[0].split(' '))
	if (((l - r) % 2) == 0):
	    global_list.append(2)
	else:
	    global_list.append(3)
	return global_list