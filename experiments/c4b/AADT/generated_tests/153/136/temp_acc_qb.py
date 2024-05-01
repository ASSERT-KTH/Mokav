def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	t = 0
	z = ((n // 2) - 1)
	if ((n % 2) == 1):
	    global_list.append(0)
	else:
	    global_list.append((z // 2))
	return global_list