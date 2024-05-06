def patched_func(*args):
	global_list = []
	
	(x, y) = args[0].split()
	x = int(x)
	y = int(y)
	if (((x - y) > 1) or ((x - y) < (- 1)) or ((x == 0) and (y == 0))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list