def patched_func(*args):
	global_list = []
	
	a = args[0]
	(l, r) = a.split(' ')
	if (int(l) == int(r)):
	    global_list.append(l)
	else:
	    global_list.append('2')
	return global_list