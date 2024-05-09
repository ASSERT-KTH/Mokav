def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if ((3 * a) <= b):
	    global_list.append(0)
	else:
	    global_list.append(((3 * a) - b))
	return global_list