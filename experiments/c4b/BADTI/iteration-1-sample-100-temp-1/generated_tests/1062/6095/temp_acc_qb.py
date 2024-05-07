def patched_func(*args):
	global_list = []
	
	x = [int(y) for y in args[0]]
	i = 0
	q = 0
	while (i < len(x)):
	    if ((x[i] == 7) or (x[i] == 4)):
	        q += 1
	    i += 1
	if ((q == 4) or (q == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list