def patched_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split(' ')))
	t = l[0]
	s = l[1]
	x = l[2]
	if (x == t):
	    global_list.append('YES')
	elif (((((x - t) % s) == 0) and ((x - t) > 0)) or (((((x - t) - 1) % s) == 0) and (((x - t) - 1) > 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list