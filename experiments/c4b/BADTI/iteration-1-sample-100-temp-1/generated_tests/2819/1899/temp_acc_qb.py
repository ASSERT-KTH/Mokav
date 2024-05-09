def patched_func(*args):
	global_list = []
	
	(a, b) = [int(i) for i in args[0].split()]
	if (a == b):
	    global_list.append(a)
	else:
	    global_list.append(2)
	return global_list