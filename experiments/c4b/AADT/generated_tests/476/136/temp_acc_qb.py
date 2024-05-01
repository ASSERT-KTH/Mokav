def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	m = (n % 3)
	z = (n // 3)
	if (m == 0):
	    global_list.append((z * 2))
	else:
	    global_list.append(((z * 2) + 1))
	return global_list