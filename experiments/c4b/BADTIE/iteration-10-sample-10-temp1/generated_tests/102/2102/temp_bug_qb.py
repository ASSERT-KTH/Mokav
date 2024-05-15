def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	if (((2 * a) + (2 * b)) <= ((a + b) + c)):
	    global_list.append(((2 * a) + (2 * b)))
	else:
	    global_list.append(((a + b) + c))
	return global_list