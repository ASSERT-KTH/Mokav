def patched_func(*args):
	global_list = []
	
	'input\n12\n'
	n = int(args[0])
	if ((n % 5) == 0):
	    global_list.append((n // 5))
	else:
	    global_list.append(((n // 5) + 1))
	return global_list