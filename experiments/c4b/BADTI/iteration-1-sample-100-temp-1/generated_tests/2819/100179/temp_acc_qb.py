def patched_func(*args):
	global_list = []
	
	(a, b) = args[0].split()
	if (a == b):
	    global_list.append(a)
	else:
	    global_list.append(2)
	return global_list