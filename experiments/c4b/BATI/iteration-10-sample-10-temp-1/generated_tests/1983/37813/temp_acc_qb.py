def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 2):
	    global_list.append(3)
	else:
	    global_list.append((((n ** 3) + (5 * n)) // 6))
	return global_list