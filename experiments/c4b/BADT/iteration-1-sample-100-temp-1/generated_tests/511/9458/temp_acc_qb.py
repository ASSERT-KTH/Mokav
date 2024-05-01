def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	if (c == 0):
	    (global_list.append('NO') if (a != b) else global_list.append('YES'))
	else:
	    (global_list.append('YES') if ((((b - a) // c) >= 0) and (((b - a) % c) == 0)) else global_list.append('NO'))
	return global_list