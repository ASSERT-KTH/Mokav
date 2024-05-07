def original_func(*args):
	global_list = []
	
	(k, l) = (int(args[0]), int(args[1]))
	x = 0
	while (k < l):
	    k *= k
	    x += 1
	if (k == l):
	    global_list.append('YES')
	    global_list.append(x)
	else:
	    global_list.append('NO')
	return global_list