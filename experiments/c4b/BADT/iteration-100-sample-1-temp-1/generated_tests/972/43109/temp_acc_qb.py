def patched_func(*args):
	global_list = []
	
	(a, b) = [int(x) for x in args[0].split()]
	if ((abs((a - b)) not in [0, 1]) or ((a == 0) and (b == 0))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list