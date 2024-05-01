def original_func(*args):
	global_list = []
	
	a = args[0]
	l = len(a)
	if (l != 1):
	    b = (10 * (l - 1))
	    global_list.append((b - int(a[1:])))
	else:
	    global_list.append(1)
	return global_list