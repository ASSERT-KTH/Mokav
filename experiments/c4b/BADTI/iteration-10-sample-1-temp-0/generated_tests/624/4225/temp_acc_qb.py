def patched_func(*args):
	global_list = []
	
	(t, s, x) = map(int, args[0].split())
	if ((((x % s) == (t % s)) and (t <= x)) or (((x % s) == ((t + 1) % s)) and ((t + 1) < x))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list