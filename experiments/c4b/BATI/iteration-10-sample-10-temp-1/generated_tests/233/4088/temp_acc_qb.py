def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	if (a <= (b - c)):
	    global_list.append((n // a))
	elif (n < b):
	    global_list.append((n // a))
	else:
	    global_list.append((((n - c) // (b - c)) + ((((n - c) % (b - c)) + c) // a)))
	return global_list