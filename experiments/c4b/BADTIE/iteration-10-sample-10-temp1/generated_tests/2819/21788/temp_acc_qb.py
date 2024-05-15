def patched_func(*args):
	global_list = []
	
	(l, r) = map(int, args[0].split(' '))
	if (l == r):
	    global_list.append(l)
	else:
	    global_list.append(2)
	return global_list