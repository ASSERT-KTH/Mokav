def patched_func(*args):
	global_list = []
	
	(k, l) = (int(args[0]), int(args[1]))
	(x, t) = (0, k)
	while (t < l):
	    t *= k
	    x += 1
	if (t == l):
	    global_list.append('YES')
	    global_list.append(x)
	else:
	    global_list.append('NO')
	return global_list