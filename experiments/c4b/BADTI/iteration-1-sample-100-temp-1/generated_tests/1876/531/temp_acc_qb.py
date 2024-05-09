def patched_func(*args):
	global_list = []
	
	'input\n3\n'
	n = int(args[0])
	if (n < 3):
	    global_list.append((- 1))
	else:
	    global_list.append(((((10 ** (n - 1)) // 210) + 1) * 210))
	return global_list