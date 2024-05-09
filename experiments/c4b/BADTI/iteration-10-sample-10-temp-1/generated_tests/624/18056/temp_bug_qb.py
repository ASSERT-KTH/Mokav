def original_func(*args):
	global_list = []
	
	(t, s, x) = (int(z) for z in args[0].split())
	x -= t
	if ((x >= 0) and ((x % s) in [0, 1])):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list