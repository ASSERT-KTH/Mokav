def patched_func(*args):
	global_list = []
	
	(t, s, x) = [int(x) for x in args[0].split()]
	if ((((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)) and (x >= (t + s))) or (x == t)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list