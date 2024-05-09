def original_func(*args):
	global_list = []
	
	(t, s, x) = map(int, args[0].split())
	c = 0
	if (((x - t) < 0) or (((s - t) > x) and ((x - t) != 0))):
	    c = 1
	if (((((x - t) % s) == 0) and (c == 0)) or (((((x - t) - 1) % s) == 0) and (c == 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list