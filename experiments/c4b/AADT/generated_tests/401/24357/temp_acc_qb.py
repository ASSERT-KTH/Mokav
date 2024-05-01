def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	if (a <= 12):
	    global_list.append((1 << a))
	else:
	    global_list.append((8092 << (a - 13)))
	return global_list