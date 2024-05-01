def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	c = 1
	while (((l / k) != 1) and ((l - k) > 0) and (l != 1)):
	    l /= k
	    c += 1
	if ((l / k) == 1):
	    global_list.append('YES')
	    global_list.append((c - 1))
	else:
	    global_list.append('NO')
	return global_list